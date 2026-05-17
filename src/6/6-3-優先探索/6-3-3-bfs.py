from collections import deque

# データの受け取り
def data_input():
    return int(input())

# 七五三数を数える
def count_753_numbers(limit):
    q = deque()
    q.append((0, False, False, False))

    count = 0

    while q:
        num, use3, use5, use7 = q.popleft()

        if num > limit:
            continue

        if use3 and use5 and use7:
            count += 1

        q.append((num * 10 + 3, True, use5, use7))
        q.append((num * 10 + 5, use3, True, use7))
        q.append((num * 10 + 7, use3, use5, True))

    return count


# 結果の表示
def print_result(result):
    print(result)

# メイン処理
def main():
    n = data_input()
    result = count_753_numbers(n)
    print_result(result)

if __name__ == "__main__":
    main()