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


