#ifndef MODULE_H_
#define MODULE_H_

#define PY_SSIZE_T_CLEAN
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION

#include <Python.h>
#include <numpy/arrayobject.h>

static PyObject *ModuleError;

PyMODINIT_FUNC PyInit_module(void);

static PyMethodDef mod_methods[] = {{NULL, NULL, 0, NULL}};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT, "cmodule",
    "Python C extension module template project.", -1, mod_methods};

#endif  // MODULE_H_
