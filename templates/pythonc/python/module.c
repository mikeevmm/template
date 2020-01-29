#include "include/module.h"

// Initialization function of the module.
// Here we initialize not only the module, but also import the NumPy
// functions (via `import_array()`), and instantiate the internal error
// module exception type, `ModuleError`.
PyMODINIT_FUNC PyInit_module() {
  PyObject *mod;

  mod = PyModule_Create(&module);
  if (mod == NULL) return NULL;

  import_array();
  if (PyErr_Occurred()) {
    return NULL;
  }

  ModuleError = PyErr_NewException("module.error", NULL, NULL);
  Py_XINCREF(ModuleError);
  if (PyModule_AddObject(mod, "error", ModuleError) < 0) {
    Py_XDECREF(ModuleError);
    Py_CLEAR(ModuleError);
    Py_DECREF(mod);
    return NULL;
  }

  return mod;
}
