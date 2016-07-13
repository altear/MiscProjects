#include <Python.h>
#include <math.h>

/*  wrapped cosine function */
static  PyObject* list_test(PyObject* self, PyObject* args)
{
    Py_ssize_t value;
    PyObject* answer;
    Py_ssize_t i;

    /*  parse the input, from python int to c double */
    if (!PyArg_ParseTuple(args, "n", &value))
        return NULL;
    /* if the above function returns -1, an appropriate Python exception will
     * have been set, and the function simply returns NULL
     */

    /* call cos from libm */
    answer = PyList_New(value);
    
    
    for (i=0; i<value;i++){
	    PyList_SetItem(answer, i, Py_BuildValue("n", i*i));
    }
    /*  construct the output from cos, from c double to python float */
    return answer;
}

static  PyObject* make_factorials_from_list(PyObject* self, PyObject* args)
{
    PyObject* listObj;
   
    /*  parse the input, from python int to c double */
    
    if (! PyArg_ParseTuple( args, "O!", &PyList_Type, &listObj)) return NULL;
	
    /* call cos from libm */
    //printf("Just Checking! %i", (int)value);
    
    printf("%i\n",(int)PyList_Size(listObj));
   
    //printf("%i\n", (int)size);
    /*  construct the output from cos, from c double to python float */
    return Py_BuildValue("O",listObj);
}

/*  define functions in module */
static PyMethodDef CosMethods[] =
{
     {"list_test", list_test, METH_VARARGS, "build list of fact"},
     {"list_test2", make_factorials_from_list, METH_VARARGS, "build list from list"},
     {NULL, NULL, 0, NULL}
};


static struct PyModuleDef cos_module =
{
    PyModuleDef_HEAD_INIT,
    "cos_module", /* name of module */
    "",          /* module documentation, may be NULL */
    -1,          /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
    CosMethods
};

/* module initialization */
PyMODINIT_FUNC PyInit_cos_module(void)
{
    return PyModule_Create(&cos_module);
}