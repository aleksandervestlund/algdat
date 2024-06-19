from enum import Enum


class Status(Enum):
    UNVISITED = "white"
    VISITING = "gray"
    VISITED = "black"
