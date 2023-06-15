

# >>> aaabca
# <<< a: 4, b: 1, c: 1


# s = 'bbbbcca'
# for sym in s:
#     count = 0
#     for sub_sym in s:
#         if sym == sub_sym:
#             count+=1
#
#     print(sym, count)

# O(N) = N*N = 2 * 2,

# s = 'abc'
# for sym in set(s):
#     count = 0
#     for sub_sym in s:
#         if sym == sub_sym:
#             count+=1
#
#     print(sym, count)

# O(N) = M * N, где M - кол-во уникальных символов

#{key: value}

s = 'abccccd'
syms_counter = {}
for sym in s:
    syms_counter[sym] = syms_counter.get(sym, 0) + 1

print(syms_counter)

