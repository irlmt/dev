def foo(mark: int) -> str:
    assert 0 <= mark <= 100, "Incorrect input value, mark must be between 0 and 100"
    assert isinstance(mark, int), f"Incorrect input value, {mark} of type {type(mark)}"
    if 90 <= mark <= 100:
        return "A"
    elif 80 <= mark <= 89:
        return "B"
    elif 70 <= mark <= 79:
        return "C"
    elif 60 <= mark <= 69:
        return "D"
    else:
        return "F"


try:
    a = int(input())
except ValueError as e:
    print("Incorrect input value")
else:
    print(foo(a))
