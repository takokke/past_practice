# https://atcoder.jp/contests/past202004-open/tasks/past202004_d
S = input()

def is_match(T, S): #TがSに含まれるならTrue、それ以外はFalse
    for i in range(0, len(S)-len(T)+1):
        ok = True
        for j in range(0, len(T)):
            if T[j] != S[i+j] and T[j] != '.':
                ok = False

        if ok:
            return True
    return False

chars = "abcdefghijklmnopqrstuvwxyz."

count = 0

# Tが1文字の場合
for c1 in chars:
    T = c1
    if is_match(T, S):
        count+=1

# Tが2文字の場合
for c1 in chars:
    for c2 in chars:
        T = c1 + c2
        if is_match(T, S):
            count+=1

# Tが3文字の場合
for c1 in chars:
    for c2 in chars:
        for c3 in chars:
            T = c1 + c2 + c3
            if is_match(T, S):
                count+=1

print(count)