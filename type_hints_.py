from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, NamedTuple, TypedDict, Union, TypeVar


class Point(NamedTuple):
    x: int
    y: int


bob: Student


@dataclass
class Student:
    name: str
    age: int
    position: Point
    friends: List[Student]


student = Student(
    **{  # ignore: arg-type
        "name": "Marcy",
        "age": 25,
        "position": Point(1, 2),
        "friends": [
            Student(
                **{
                    "name": "Jared",
                    "age": 25,
                    "position": Point(1, 2),
                    "friends": [],
                }
            )
        ],
    }
)

# other_student = Student(name="Jared", age=23)
print(student)

TStudentArgsDictKeys = Union[str, int, Point, List[Student]]
TStudentArgsDict = Dict[str, TStudentArgsDictKeys]

# TAddableEntity = Union[int, float, str, list, tuple]

TAddableEntity = TypeVar["TAddableEntity"]


def make_list_of_addable_entity(
    a: TAddableEntity, b: TAddableEntity
) -> List[TAddableEntity]:
    return [a, b]

print("test2")
