# Sequences in Python

- A sequence in python implements both the `__getitem__` and `__len__` method and hence can be iterated over.
  - Examples: list, tuple, and string

When building your own custom sequence, keep the following things in mind:

- When indexing by a range, the result should be an instance of the same type of the class.
- In the range provided by `slice`, respect the semantics that python uses, excluding the element at the end.



# Context Manager

There are situations when we want to run some code that has preconditions and postconditions, meaning we want to run things before and after a certain main action. Context managers are a great tool to use in such situations.

Example: In situation when we open files, we want to make sure that they are closed after processing.

- ``` python
  with open(filename, mode) as f:
    some_processing_here(f)
  ```

- Here, the `with` statement enters the context manager and `open` function implements the context manager protocol. 

- Context managers implement two functions: `__enter__`, and `__exit__`. On the first line of context manager, the `with` statement calls the first method the return value of which is passed to the variable that follows `as`. After the last statement on the block is executed, the context will be exited and python will call the `__exit__` method of the original context manager. The `__exit__` method is still called even if there is an error or exception inside the context manager. 

# Implementing Context Managers

- Most common way: Write a class that implements both the `__enter__` and `__exit__` methods.
- `contextlib` module contains a lot of helper functions and objects to either implement context managers or use ones already provided.

### Using the `contextlibe.contextmanager` decorator and a `generator` function.

``` python
import contextlib
@contextlib.contextmanager
def db_handler():
  try:
    stop_db()
  	yield 
  finally:
    start_db()
    
with db_handler():
  db_backup()
```

- Upon applying the `contextlib.contextmanager` decorator, everything before the `yield` keyword becomes the part of the `__enter__` method, the yielded value will function as the value returned as a part of the `__enter__` method. In the generator function, every line that comes after the `yield` statement becomes the part of `__exit__` method.

### Using the `contextlib.ContextDecorator`

- Upon inheriting from the `contextlib.ContextDecorator` , the resultant class works as a context manager if it implements the required magic methods.

```python
class dbhandler_decorator(contextlib.ContextDecorator):
  def __enter__(self):
    stop_database()
    return self
  def __exit__(self, ext_type, ex_value, ex_traceback):
    start_database()
    
@dbhandler_decorator()
def offline_backup():
  run("pg_dump database")
```

Since, the decorator is implemented as a class, we cannot interact with the underlying object, however, if we want access to the underlying object, we can use it as:

```python
def offline_backup():
  with dbhandler_decorator() as handler:
    pass
```

The `contextlib` library provies with the `supress` module which is a utility to supress desired exception.

```python
import contextlib
with contextlib.supress(DataConversionException):
  do_something_here()
  pass
```

