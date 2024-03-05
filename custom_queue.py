from __future__ import annotations
import dataclasses
import typing


@dataclasses.dataclass
class NodeItem:
    data: typing.Any
    next: NodeItem | None


class CustomQueue:
    def __init__(self):
        self.__length = 0
        self.__head = None
        self.__tail = None

    def push(self, data: typing.Any):
        if self.__head is None:
            self.__tail = NodeItem(data=data, next=None)
            self.__head = self.__tail
        else:
            new_elem = NodeItem(data=data, next=None)
            self.__tail.next = new_elem
            self.__tail = new_elem
        self.__length += 1

    def extend(self, iterable):
        for elem in iterable:
            self.push(elem)

    def pop(self):
        if self.__head is None:
            self.__tail = None
            return None
        else:
            data = self.__head.data
            self.__head = self.__head.next
            self.__length -= 1
            return data

    def __len__(self):
        return self.__length
