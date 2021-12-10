from collections.abc import Sequence

class Items(Sequence):

    def __init__(self, *values) -> None:
        self._values = list(values) 
    def __len__(self) -> int:
        return len(self._values)
    def __getitem__(self, item) -> Items:
        return self._values.__getitem__(item)

class ItemsNew(Sequence):
    def __init__(self, *values) -> None:
        self._values = list(values) 
    def __len__(self) -> int:
        return len(self._values)
    def __getitem__(self, item) -> ItemsNew:
        return self._values[item]

a = Items(1,2,3,4)
print(a[1], a[1:3])
b = ItemsNew(1,2,3,4)
print(b[1], b[1:3])

