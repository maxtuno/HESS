///////////////////////////////////////////////////////////////////////////////
//        Copyright (c) 2012-2020 Oscar Riveros. all rights reserved.        //
//                        oscar.riveros@peqnp.science                        //
//                                                                           //
//   without any restriction, Oscar Riveros reserved rights, patents and     //
//  commercialization of this knowledge or derived directly from this work.  //
///////////////////////////////////////////////////////////////////////////////

#include "libhess.h"

static PyMethodDef module_methods[] = {{"sequence", (PyCFunction) sequence, METH_VARARGS, ""},
                                       {"binary", (PyCFunction) binary, METH_VARARGS, ""},
                                       {NULL, NULL, 0, NULL}};


#if PY_MAJOR_VERSION < 3

PyMODINIT_FUNC initlibhess() {
    Py_InitModule3("libhess", module_methods, "");
}

#else
static struct PyModuleDef libhess = {PyModuleDef_HEAD_INIT, "libhess",
                                   ""
                                   "libhess AI Technology."
                                   "",
                                   -1, module_methods};

    PyMODINIT_FUNC PyInit_libhess() {
        return PyModule_Create(&libhess);
    }
#endif