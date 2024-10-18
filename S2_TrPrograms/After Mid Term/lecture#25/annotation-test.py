def foo(a:"int", b:"float"=15.0) -> "a+b":
    sum=a+b
    return sum

print(foo(10,10.5))
print(foo.__annotations__)
