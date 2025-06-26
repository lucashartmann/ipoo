x = 5
y = 5

# for i in range(y):
#     for i in range(x):
#         print("[#]", end=" ")
#     print("[#]")



mapa = ((('#', [1]), (' ',[2]), ('#', [3])),
        (('#', [4]), (' ',[5]), ('#',[6])),
        (('#',[7]),(' ',[8]),('#',[9])),
        (('#',[10]),(' ', [11]),('#', [12])))

for linha in range(len(mapa)):
    for hashtag, numero in mapa[linha]:
        for elemento in hashtag:
            print(elemento, end=" ")
    print()