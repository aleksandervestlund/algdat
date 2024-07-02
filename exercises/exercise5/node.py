from __future__ import annotations

from dataclasses import dataclass, field
from io import StringIO


@dataclass(slots=True)
class Node:
    children: dict = field(default_factory=dict)
    count: int = 0

    def __str__(self) -> str:
        representation = StringIO()
        representation.write(f"┃ count: {self.count}\n")
        r = 0

        for symbol, node in self.children.items():
            r += 1

            if r == 1:
                representation.write("┃\n")

            if r != 1:
                representation.write("┃\n")

            if r != len(self.children):
                representation.write(f"┣━━━┓ {symbol}\n")
                representation.write(
                    "\n┃   " + str(node).replace("\n", "\n┃   ")
                )
            else:
                representation.write(f"┗━━━┓ {symbol}\n")
                representation.write(
                    "\n    " + str(node).replace("\n", "\n    ")
                )

        return representation.getvalue()

    @classmethod
    def from_string(cls, s: str) -> Node:
        node = Node()
        ind = 0
        ind = s.index("count") + len("count: ")
        ind2 = s.index(",", ind)
        node.count = int(s[ind:ind2])
        ind = s.index("{", ind) + 1

        while ind != len(s) - 2:
            ind = s.index("'", ind) + 1
            c = s[ind]
            ind = s.index("{", ind)
            ind2 = ind + 1
            count = 1

            while count:
                if s[ind2] == "{":
                    count += 1
                elif s[ind2] == "}":
                    count -= 1

                ind2 += 1

            node.children[c] = Node.from_string(s[ind:ind2])
            ind = ind2

        return node
