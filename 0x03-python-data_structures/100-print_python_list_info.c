#include <python.h>
#include <listobject.h>
#include <object.h>
#include <stdlib.h>

/**
 * print_python_list_info - prints info about a python list
 * @p: python object
 */
void print_python_list_info(PyObject *p)
{
	PyObject *list_obj;
	int i;
	long int lenght;

	if (!PyArg_ParseTuple(p, "0", &list_obj))
		return (NULL);
	if (!PyList_Check(list_obj))
		return (NULL);
	length = PyList_Size(list_obj);
	printf("[*] Size of the Python List: = %li\n", length);
	printf("[*] Allocated: %li\n", ((PyListObject *)list_obj)->allocated);
	for (i = 0; i < lenght; i++)
	{
		PyObject *item = PyList_GetItem(list_obj, i);

		printf("Element %zd: %s", i, Py_TYPE(item)->tp_name);
	}
}
