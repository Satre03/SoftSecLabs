import re
"""
MOCK calculator implementation.

Purpose: unblock the sub-group building the API and its tests while the
real calculator implementation is still being developed on another branch.
This is a stand-in that satisfies the same interface (a `calc` method
taking a string and returning a string) -- swap it out once the real
implementation is merged.

WARNING -- do not use this pattern for anything beyond this lab exercise:
this calls eval() directly on its input with NO sanitisation whatsoever.
That means any Python expression -- not just arithmetic -- will be
executed, including code with side effects. This is intentionally unsafe
and is meant only as a temporary stub while you build against a stable
interface.
"""


class Calculator:
    def calc(self, expression: str) -> str:
        if not re.fullmatch(r"[0-9+\-*/(). ]+", expression):
            raise ValueError("Invalid expression")


if __name__ == "__main__":
    calc = Calculator()
    print(calc.calc("2 + 3"))       # -> "5"
    print(calc.calc("(2 + 3) * 4")) # -> "20"
