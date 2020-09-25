///////////////////////////////////////////////////////////////////////////////
//        Copyright (c) 2012-2020 Oscar Riveros. all rights reserved.        //
//                        oscar.riveros@peqnp.science                        //
//                                                                           //
//   without any restriction, Oscar Riveros reserved rights, patents and     //
//  commercialization of this knowledge or derived directly from this work.  //
///////////////////////////////////////////////////////////////////////////////


#include <Python.h>
#include <stdio.h>

#ifndef HESS_HESS_H
#define HESS_HESS_H

#define MIN(a, b) ((a < b) ? a : b)
#define MAX(a, b) ((a < b) ? b : a)

void inv(int a, int b, PyObject *pList) {
    int i = MIN(a, b);
    int j = MAX(a, b);
    PyObject *aux;
    while (i < j) {
        aux = PyList_GET_ITEM(pList, i);
        PyList_SET_ITEM(pList, i, PyList_GET_ITEM(pList, j));
        PyList_SET_ITEM(pList, j, aux);
        i++;
        j--;
    }
}

void step(int i, int j, PyObject *pList) {
    int aux;
    if (PyList_GET_ITEM(pList, i) == PyList_GET_ITEM(pList, j)) {
        PyList_SET_ITEM(pList, i, PyBool_FromLong(!PyObject_IsTrue(PyList_GET_ITEM(pList, j))));
    } else {
        aux = PyObject_IsTrue(PyList_GET_ITEM(pList, i));
        PyList_SET_ITEM(pList, i, PyBool_FromLong(!PyObject_IsTrue(PyList_GET_ITEM(pList, j))));
        PyList_SET_ITEM(pList, j, PyBool_FromLong(aux));
    }
}

PyObject *sequence(PyObject *self, PyObject *args) {
    int n, done;
    double local, global, cursor = MAXFLOAT;
    size_t i, j, k;
    PyObject *pOracle;
    PyObject *pList;
    PyObject *pOpt;
    PyObject *arg_list;
    PyObject *result;

    if (!PyArg_ParseTuple(args, "iO", &n, &pOracle)) {
        return Py_None;
    }

    pList = PyList_New(n);
    pOpt = PyList_New(n);
    for (i = 0; i < n; i++) {
        PyList_SET_ITEM(pList, i, PyLong_FromSize_t(i));
        PyList_SET_ITEM(pOpt, i, PyLong_FromSize_t(i));
    }

    for (;;) {
        done = 1;
        global = MAXFLOAT;
        for (i = 0; i < n; i++) {
            for (j = 0; j < n; j++) {
                oo:
                inv(i, j, pList);
                arg_list = Py_BuildValue("(O)", pList);
                result = PyObject_CallObject(pOracle, arg_list);
                Py_DECREF(arg_list);
                local = PyFloat_AsDouble(result);
                Py_DECREF(result);
                if (local < global) {
                    global = local;
                    if (global < cursor) {
                        cursor = global;
                        for (k = 0; k < n; k++) {
                            PyList_SET_ITEM(pOpt, k, PyList_GET_ITEM(pList, k));
                        }
                        if (cursor == 0) {
                            Py_DECREF(pList);
                            return pOpt;
                        }
                        done = 0;
                    }
                } else if (local > global) {
                    goto oo;
                }
            }
        }
        if (done) {
            break;
        }
    }

    Py_DECREF(pList);

    return pOpt;
}

PyObject *binary(PyObject *self, PyObject *args) {
    int n, done;
    double local, global, cursor = MAXFLOAT;
    size_t i, j, k;
    PyObject *pOracle;
    PyObject *pList;
    PyObject *pOpt;
    PyObject *arg_list;
    PyObject *result;

    if (!PyArg_ParseTuple(args, "iO", &n, &pOracle)) {
        return Py_None;
    }

    pList = PyList_New(n);
    pOpt = PyList_New(n);
    for (i = 0; i < n; i++) {
        PyList_SET_ITEM(pList, i, PyBool_FromLong(0));
        PyList_SET_ITEM(pOpt, i, PyBool_FromLong(0));
    }

    for (;;) {
        done = 1;
        global = MAXFLOAT;
        for (i = 0; i < n; i++) {
            for (j = 0; j < n; j++) {
                oo:
                step(i, j, pList);
                arg_list = Py_BuildValue("(O)", pList);
                result = PyObject_CallObject(pOracle, arg_list);
                Py_DECREF(arg_list);
                local = PyFloat_AsDouble(result);
                Py_DECREF(result);
                if (local < global) {
                    global = local;
                    if (global < cursor) {
                        cursor = global;
                        for (k = 0; k < n; k++) {
                            PyList_SET_ITEM(pOpt, k, PyList_GET_ITEM(pList, k));
                        }
                        if (cursor == 0) {
                            Py_DECREF(pList);
                            return pOpt;
                        }
                        done = 0;
                    }
                } else if (local > global) {
                    goto oo;
                }
            }
        }
        if (done) {
            break;
        }
    }

    Py_DECREF(pList);

    return pOpt;
}

#endif //HESS_HESS_H

