from enum import Enum


class Status(Enum):
    VISITED = "black"
    UNVISITED = "white"
    VISITING = "gray"
