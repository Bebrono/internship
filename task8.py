#Написать функцию с аннотациями типов для аргументов и возвращаемого
#значения.

def Hello(name: str) -> str:
    return f"Hello, {name}"

gg: str = input()

print(Hello(gg))