"""
This is the abstract base class for the Stack datastructure.
"""

import abc


class BaseStack:
    def __init__(self) -> None:
        pass

    # @property
    # @abc.abstractmethod
    # def items(self):
    #     raise NotImplementedError

    @abc.abstractmethod
    def is_empty(self):
        raise NotImplementedError(
            "All subclasses should implement an 'is_empty' method!")

    @abc.abstractmethod
    def push(self, _):
        raise NotImplementedError(
            "All subclasses should implement an 'push' method!")

    @abc.abstractmethod
    def pop(self):
        raise NotImplementedError(
            "All subclasses should implement an 'pop' method!")
