#define PY_SSIZE_T_CLEAN
#include <python3.8/Python.h>
#include <eigen3/Eigen/Dense>

#include "include/maybe.hh"

static PyMethodDef methods[] = {
  /* {"method_name", method, METH_VARARGS | METH_KEYWORDS, "description" }*/
  {NULL, NULL, 0, NULL}};

static struct PyModuleDef module = {PyModuleDef_HEAD_INIT, "cextension",
                                    NULL,  // Documentation
                                    -1, methods};

/** This method must have this name **/
PyMODINIT_FUNC PyInit_cextension(void) {
  return PyModule_Create(&module);
}
