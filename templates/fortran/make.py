import subprocess as sp
import os
from glob import glob

from sane import *

FCC = "gfortran"
EXE = "main"
SRC_DIR = "src"
OBJ_DIR = "obj"
COMPILE_FLAGS = ""

os.makedirs(SRC_DIR, exist_ok=True)
os.makedirs(OBJ_DIR, exist_ok=True)

def make_source_recipe(source_file):
    base_file = os.path.basename(source_file)
    base_name = base_file[:base_file.rfind('.')]

    @recipe(name=source_file,
            hooks=["source_compile"],
            file_deps=[source_file],
            target_files=[f"{OBJ_DIR}/{base_name}.o"])
    def compile():
        sp.run(f"{FCC} {COMPILE_FLAGS} -c {source_file} -o {OBJ_DIR}/{base_name}.o", shell=True)

for source_file in glob(f"{SRC_DIR}/*.f90"):
    make_source_recipe(source_file)

@recipe(hook_deps=["source_compile"],
        info="Links the compiled objects into an executable.")
def link():
    obj_files = glob(f"{OBJ_DIR}/*.o")
    sp.run(f"{FCC} {' '.join(obj_files)} -o {EXE}", shell=True)  

@recipe(recipe_deps=["link"],
        info="Runs the linked executable.")
def run_main():
    sp.run(f"./{EXE}")

sane_run(run_main)
