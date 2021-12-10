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
