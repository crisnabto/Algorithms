# Complexidade 0(n log n) metodo QuickSort:


def quicksort(list):
    # print(f"lista = {list}")
    if len(list) <= 1:
        return list
    else:
        ref = list[0]  # primeiro elemento para referencia
        # [p, e, d, r, a]
        left = []
        right = []
        for i in range(1, len(list)):  # inicia comparacao pelo segundo
            if list[i] < ref:
                left.append(list[i])  # 1.[e, d, a]  2.[d, a] 3.[a]
            else:
                right.append(list[i])  # 1.[r]  2.[]
        return quicksort(left) + [ref] + quicksort(right)  # [e, d, a], p, [r]


def is_anagram(first_string, second_string):
    if first_string == '' and second_string == '':
        return ('', '', False)

    letters1 = quicksort(list(first_string.lower()))  # ['a', 'm', 'o', 'r']
    letters2 = quicksort(list(second_string.lower()))  # ['r', 'o', 'm', 'a']

    if letters1 == letters2:
        return ''.join(letters1), ''.join(letters2), True
    else:
        return ''.join(letters1), ''.join(letters2), False


# Complexidade O(n^2) duas complexidade lineares aninhadas:


# def is_anagram(first_string, second_string):  # (amor, roma)
#     letters1 = list(first_string.lower())  # ['a', 'm', 'o', 'r']
#     letters2 = list(second_string.lower())
#     len_letters = len(letters1)  # 4
#     len_letters2 = len(letters2)

#     if first_string == '' and second_string == '':
#         return ('', '', False)

#     for a in range(len_letters):  # (0, 3) -> 0, 1 e 2
#         for b in range(len_letters - a - 1):  # (0, 2)  -> 0 e 1
#             if letters1[b] > letters1[b + 1]:
#                 letters1[b], letters1[b + 1] = letters1[b + 1], letters1[b]

#     for a in range(len_letters2):  # (0, 3) -> 0, 1 e 2
#         for b in range(len_letters2 - a - 1):  # (0, 2)  -> 0 e 1
#             if letters2[b] > letters2[b + 1]:
#                 letters2[b], letters2[b + 1] = letters2[b + 1], letters2[b]
#     tupla = ("".join(letters1).lower(), "".join(letters2).lower())

#     if letters1 == letters2:
#         return tupla[0], tupla[1], True
#     else:
#         return tupla[0], tupla[1], False
