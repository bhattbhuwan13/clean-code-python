# Sequences in Python

- A sequence in python implements both the `__getitem__` and `__len__` method and hence can be iterated over.
  - Examples: list, tuple, and string

When building your own custom sequence, keep the following things in mind:

- When indexing by a range, the result should be an instance of the same type of the class.
- In the range provided by `slice`, respect the semantics that python uses, excluding the element at the end.

