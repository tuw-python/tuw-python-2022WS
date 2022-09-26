from typing import Any, Union, Optional, Sequence


def foo(value: float) -> None:
    print(value, value + 1)


def bar(value: int) -> int:
    foo(value)
    return 0


def happy_birthday(name: str, age: Union[int, str]) -> str:
    return f"Happy {age}th birthday, {name}"


def print_all(elements: Sequence, prefix: Optional[str] = None) -> None:
    for e in elements:
        if prefix:
            print(f"{prefix}: {e}")
        else:
            print(e)


def call_happy(name: str, age: Union[list, int, str]) -> None:
    print(happy_birthday(name, age))


def main():
    # bar(42)
    call_happy("John", [1, 2, 3])
    # print_all([1, "abc", "def"])


if __name__ == '__main__':
    main()
