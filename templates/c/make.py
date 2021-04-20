import os
from subprocess import run
from glob import glob

from sane import *
from sane import _Help as Help

CC = 'gcc'
EXE = 'main'
SRC_DIR = 'src'
OBJ_DIR = 'obj'
TEST_DIR = 'tests'
TEST_BUILD_DIR = os.path.join(TEST_DIR, 'build')

LIBS = []
INCLUDES = ['.'] 
COMPILE_FLAGS = '-g -O2 -Wall -lm'

# Ensure source, objects, tests directories exist
os.makedirs(SRC_DIR, exist_ok=True)
os.makedirs(OBJ_DIR, exist_ok=True)
os.makedirs(TEST_DIR, exist_ok=True)
os.makedirs(TEST_BUILD_DIR, exist_ok=True)

sources = glob(f'{SRC_DIR}/*.c')

# Define a compile recipe for each source file in SRC_DIR
def make_compile_recipe(source_file):
    basename = os.path.basename(source_file)
    obj_file = f'{OBJ_DIR}/{basename}.o'
    objects_older_than_source = (
        Help.file_condition(
            sources=[source_file],
            targets=[obj_file]))
    
    @recipe(name=source_file,
            conditions=[objects_older_than_source],
            hooks=['compile'],
            info=f'Compiles the file \'{source_file}\'')
    def compile():
        run(f'{CC} {COMPILE_FLAGS} {" ".join(f"-I{x}" for x in INCLUDES)} -c {source_file} -o {obj_file}', shell=True)

for source_file in sources:
    make_compile_recipe(source_file)
    # Why not define the recipe here directly? Because Python loops don't create
    # new scope. See stackoverflow:2295290 for more information.

# Define a linking recipe
@recipe(hook_deps=['compile'],
        info='Links the executable.')
def link():
    obj_files = glob(f'{OBJ_DIR}/*.o')
    run(f'{CC} {" ".join(obj_files)} -o {EXE} {" ".join(f"-L{x}" for x in LIBS)}', shell=True)

# Define a run recipe
@recipe(recipe_deps=[link],
        conditions=[lambda: True],
        info='Runs the compiled executable.')
def run_exe():
    run(f'./{EXE}', shell=True)

# Define recipes for each test

def make_test(test_file):
    basename = os.path.basename(test_file)
    test_build_name = os.path.join(TEST_BUILD_DIR, basename)
    print(test_build_name)
    test_file_modified = (
        Help.file_condition(
            sources=[test_file],
            targets=[test_build_name]))

    @recipe(name=f'build-{test_file}',
            conditions=[test_file_modified],
            recipe_deps=[link],
            info=f'Builds test file \'{test_file}\'')
    def build_test():
        print(f'{CC} {COMPILE_FLAGS} {" ".join(f"-I{x}" for x in INCLUDES)} '
            f'-o {test_build_name} {test_file} '
            f'{" ".join(f"-L{x}" for x in LIBS)}')
        run(f'{CC} {COMPILE_FLAGS} {" ".join(f"-I{x}" for x in INCLUDES)} '
            f'-o {test_build_name} {test_file} '
            f'{" ".join(f"-L{x}" for x in LIBS)}',
            shell=True)

    @recipe(name=f'{test_file}',
            recipe_deps=[f'build-{test_file}'],
            hooks=['test'],
            conditions=[lambda: True],
            info=f'Runs test file \'{test_file}\'')
    def run_test():
        run(test_build_name, shell=True)

for test_file in glob('tests/test_*.c'):
    make_test(test_file)

@recipe(hook_deps=['test'],
        info='Run all tests')
def test():
    pass

sane_run(run_exe)
