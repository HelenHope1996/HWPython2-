# 2.3[14]: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), 
# не превосходящие числа N.
# Примеры/Тесты:
# 10 ->
# 1
# 2
# 4
# 8



N = int(input("Введите число N:"))
k = 0
P = 2
for i in range(N):
    if k != 1:
        P = P ** i
        if P <= N:
            print(P, end=' ')
            P = 2
        else:
            k = 1
    else:
        i = N
