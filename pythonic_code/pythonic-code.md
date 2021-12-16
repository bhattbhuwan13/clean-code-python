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



# Properties, attributes, and different types of methods for objects

- In python all properties and functions of an object are public
- There is no strict enforcement, but there are some conventions. An attribute that starts with an underscore is meant to be private to that object, and it is expected that no external agent calls it. 

## Underscores in python

- All attributes with a leading underscore can be accessed by the object.
- Attributes with leading double underscores are stored differently. They follow the naming convention `_class-name__attr-name`.

```python
class Connector:
  def __init__(self, source):
    self.source = source
    self.__timeout = 60
   
  def connect(self):
    print("Connecting")
    
conn = Connector('postgres')
print(conn._Connector__timeout) #prints 60
```



## Properties

- Setter and Getter methods in python can be encapsulated usign properties
- Properties can also help us with data validation
- Example, geographical coordinates can represent each location with two values however, those values need to be within a certain range.

```python
class Coordinate:
    def __init__(self, lat: float, long: float):
        self._latitude = self._longitude = None
        self.latitude = lat
        self.longitude = long

    @property
    def latitude(self) -> float:
        return self._latitude

    @latitude.setter
    def latitude(self, lat_value: float) -> None:
        if lat_value not in range(-90, 90+l):
            raise ValueError(f"{lat_value} is an invalid value for latitude")
        self._latitude = lat_value
```

- Properties are a good way to achieve command and query separation. The command and query separation principle states that a method of an object should either answer to something or do something, but not both.
- The `@property` decorator is the query that will answer to something, and `@<property_name>.setter` is the command that will do something.

