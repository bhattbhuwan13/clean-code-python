# MyPy

- If you sprinkle your code with type annotations, mypy can type check your code and find common bugs

# Function signatures to enable type checking

If a function does not explicitly return a value, give it a return type of `None`.

``` python
def p() -> None:
    print('hello')

a = p()  # Error: "p" does not return a value
# If you don't return None the function will be dynamically typed
def f():
    1 + 'x'  # No static type error (dynamically typed)

def g() -> None:
    1 + 'x'  # Type check error (statically typed)
```

For arguments with default value, provide the default value after the annotation.

``` python
def greeting(name: str, excited: bool = False) -> str:
    message = 'Hello, {}'.format(name)
    if excited:
        message += '!!!'
    return message
```

`*args` and `**kwargs` can also be annotated by providing the respective annotation

``` python
def stars(*args: int, **kwargs: float) -> None:
    # 'args' has type 'Tuple[int, ...]' (a tuple of ints)
    # 'kwargs' has type 'Dict[str, float]' (a dict of strs to floats)
    for arg in args:
        print(arg)
    for key, value in kwargs:
        print(key, value)
```

# Additional types and typing module

- To indicate that the function accepts a list of string, (for python 3.9 and later)

  ``` python
  def greet_all(names: list[str]) -> None:
  ```

  The `list` type is an example of something called a *generic type*: it can accept one or more *type parameters*.

  For python 3.8 or earlier, import the `List` type from the `typing` module.

  ``` python
  from typing import List  # Python 3.8 and earlier
  
  def greet_all(names: List[str]) -> None:
    pass
  ```

- Many of these complex static types can be found in `typing` module.

- To indicate that the function accepts list, set, tuple or any custom iterable, use `collections.abc.Iterable` (or `typing.Iterable` for python 3.8 or earlier)

  ``` python
  from collections.abc import Iterable  # or "from typing import Iterable"
  
  def greet_all(names: Iterable[str]) -> None:
    pass
  ```

- For a function that can accept *either* ints or strings, but no other types, use `Union`

  ``` python
  from typing import Union
  
  def normalize_id(user_id: Union[int, str]) -> str:
    pass
  ```

- For a function that accepts only string or None, use `Union[str, None]` or `Optional[None]`.

  ``` python
  from typing import Optional
  
  def greeting(name: Optional[str]) -> str:
    pass
  
  from typing import Union
  
  def greeting(name: Union[str, None]) -> str:
    pass
  ```

# Local type inference

- After adding type hints to a function, mypy will automatically type check that function’s body. While doing so, mypy will try and *infer* as many details as possible.

- If mypy cannot infer type of a variable, it will warn you.

  ``` python
  my_global_dict = {}  # Error: Need type annotation for "my_global_dict"
  ```

- If you know `my_global_dict` is a dict of int to floats, you can annotate it accordingly

  ``` python
  # If you're using Python 3.9+
  my_global_dict: dict[int, float] = {}
  
  # If you're using Python 3.6+
  my_global_dict: Dict[int, float] = {}
  ```

# Library Stubs and typeshed

- `mypy` uses library **stubs** to check code interacting with library modules, including the python stanadard library.
- A library stub defines public interface of the library, including classes, variables and functions, and their types.
- Stubs in the [typeshed](https://github.com/python/typeshed) projects are included in mypy. For reference, you can view an example stub for the `auth` module in the `requests` library [here](https://github.com/python/typeshed/blob/master/stubs/requests/requests/auth.pyi)

# Configuring MyPy

- Use command line argument to specify the strictness of `mypy`
- Passing the option `--disallow-untyped-defs` to mypy doesn't allow statically typed function
- Passing the option `--strict` enables many(not all) of the strictness options including `--disallow-untyped-defs`

# References
1. [Official mypy documentation](https://mypy.readthedocs.io/en/stable/getting_started.html)

