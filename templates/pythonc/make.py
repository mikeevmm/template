import os
import subprocess as sp
from distutils.core import Extension, setup
from glob import glob

from sane import *
from sane import _log, _warn, _error, _AnsiColor

pwd = os.path.dirname(os.path.realpath(__file__))

@recipe()
def clean():
    pass

@recipe(file_deps=[*glob("src/*"), *glob("include/*")], target_files=[*glob("build/**/*")])
def build():
    main_module = Extension('cextension',
                    define_macros = [('MAJOR_VERSION', '1'),
                                     ('MINOR_VERSION', '0')],
                    include_dirs = ['/usr/local/include', f'{pwd}/include/..'],
                    libraries = [],
                    library_dirs = ['/usr/local/lib'],
                    sources = [*glob("src/*")])
    setup(name = 'CExtensions',
        version = '1.0',
        description = 'C++ routines to make PC go brr',
        author = 'John Doe',
        author_email = 'john.doe@example.com',
        long_description = '''
    C++ routines makes computer go fast
    ''',
        ext_modules = [main_module],
        script_name = 'setup.py',
        script_args = ['build'])


@recipe(recipe_deps=["build"])
def test():
    sp.call("cp build/lib.linux-x86_64-3.8/cextension.cpython-38-x86_64-linux-gnu.so tests", shell=True)
    sp.call("mv tests/cextension.cpython-38-x86_64-linux-gnu.so tests/cextension.so", shell=True)
    
    tests = glob("tests/*.py")

    failed = 0
    for test_script in tests:
        _log(f"Running {test_script}")
        test_subproc = sp.Popen(["python3", test_script])
        stdout, stderr = test_subproc.communicate()
        
        if test_subproc.returncode != 0:
            _warn(f"{test_script} failed with error code {test_subproc.returncode}\n"
            f"Standard output: \n{stdout}\n Standard error: \n{stderr}")
            failed += 1

    if failed == 0:
        print(f"{_AnsiColor.OKGREEN}All tests passed{_AnsiColor.ENDC}")
    else:
        _error(f"{failed}/{len(tests)} failed, see output above.")

sane_run(test)
