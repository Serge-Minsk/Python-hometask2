
def same(a, b):
    c = list(set([i for i in a if i in b]))
    print('Otvet:', c)
    return c

k = same([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] ,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
