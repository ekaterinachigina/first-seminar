# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ¬ - Отрицание ⋁ - логическое "Или" ⋀ - логическое "И"


X = int(input())
Y = int(input())
Z = int(input())

def a(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result


if a() == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")

