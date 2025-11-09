import random

class Foo:
    def __init__(self, num:int):
        self.num:int = num
    def __str__(self):
        return f"{self.num}"
    def __repr__(self):
        return str(self)

arr_simple:list[int] = []
arr_obj:list[Foo] = []


arr_filled_simple:list[int] = [0, 1, 2, 3, 4, 5]
arr_filled_obj:list[Foo] = [Foo(i+10) for i in range(6)]

print(len(arr_filled_simple))
print(len(arr_filled_obj))

arr_simple.append(6)
arr_filled_obj.append(Foo(20))

print("Apos append:")
print(arr_filled_obj)
print(arr_filled_simple)

arr_filled_simple.pop()
arr_filled_obj.pop()

print("Apos pop:")
print(arr_filled_obj)
print(arr_filled_simple)

arr_filled_simple.insert(0, -1)
arr_filled_obj.insert(0, Foo(5))

print("Apos insert:")
print(arr_filled_obj)
print(arr_filled_simple)


arr_filled_simple.remove(3)
arr_filled_obj.remove(arr_filled_obj[3])
print("Apos remove:")
print(arr_filled_obj)
print(arr_filled_simple)

arr_random_simple:list[int] = [random.randint(0, 100) for _ in range(5)]

print("Array randomica:")
print(arr_random_simple)

arr_sequential_simple:list[int] = list(range(10))
print("Array sequencial:")
print(arr_sequential_simple)

print("Acessando elementos:")
print("index 3:", arr_sequential_simple[3])
print("index -1:", arr_sequential_simple[-1])

print("Array como string(join by -):")
print("-".join(map(str, arr_sequential_simple)))


num = int(input("Digite um numero para buscar no array: "))
if num in arr_sequential_simple:
    print(f"O numero {num} foi encontrado no array.")
else:
    print(f"O numero {num} nao foi encontrado no array.")

arr_sequential_simple.sort(reverse=True)
print("Array ordenado em ordem decrescente:")
print(arr_sequential_simple)

arr_sequential_simple.clear()
print("Array apos clear:")
print(arr_sequential_simple)
