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


num = 5
if num in arr_sequential_simple:
    print(f"O numero {num} foi encontrado no array.")
else:
    print(f"O numero {num} nao foi encontrado no array.")

arr_sequential_simple.sort(reverse=True)
print("Array ordenado em ordem decrescente:")
print(arr_sequential_simple)



arr_even = [i for i in range(20) if i % 2 == 0]
print("Array de numeros pares de 0 a 19:")
print(arr_even)

arr_squared = [i**2 for i in range(10)]
print("Array de quadrados de 0 a 9:")
print(arr_squared)

arr_cubed = [i**3 for i in range(10)]
print("Array de cubos de 0 a 9:")
print(arr_cubed)

x = 5
if x in arr_sequential_simple:
    arr_sequential_simple.remove(x)
    print(f"O numero {x} foi removido do array.")
else:
    arr_sequential_simple.append(x)
    print(f"O numero {x} foi adicionado ao array.")

print("Array final:")
print(arr_sequential_simple)

arr_slice = [i for i in range(20)]
print(arr_slice[5:15:2])

a = [1, 2, 3]
a.extend([4, 5, 6])
print("Array apos extend:")
print(a)

arr_copy = arr_sequential_simple.copy()
print("Copia do array sequencial:")
print(arr_copy)


b = [7, 8, 9]
c = ["a", "b", "c"]
zipped = list(zip(a, b, c))
print("Array zipado:")
print(zipped)

nums = [10, 3, 6, 2, 8, 4]
print("pares?:",any(n % 2 == 0 for n in nums))
print("todos > 0?:",all(n > 0 for n in nums))   

print("Array original nums:")

print(max(nums))
print(min(nums))
print(sum(nums))
print(nums)
print(sorted(nums))


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matriz:")
flat = [num for row in matrix for num in row]
print(flat)

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("Matriz transposta:")
print(transposed)   