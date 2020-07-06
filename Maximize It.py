from itertools import product

K, M = map(int, input().strip().split(' '))

lists = []
for _ in range(K):
    lists.append(map(lambda x: x ** 2, map(int, input().strip().split(" ")[1:])))

print (max(map(lambda x: x % M, map(sum, product(*lists)))))
