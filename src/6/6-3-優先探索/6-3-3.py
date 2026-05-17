# データ受け取り
def data_input():
    N = int(input())
    return N

# 深さ優先探索
def count_753_numbers(limit, n, use3, use5, use7):
    import sys
    sys.setrecursionlimit(1000000)

    if n > limit: # 値が大きければ親ノードに戻る
        return 0
    cnt = 0
    if use3 and use5 and use7:
        cnt += 1

    # 末尾に値を追加する。
    cnt += count_753_numbers(limit, n*10+3, True, use5, use7)
    cnt += count_753_numbers(limit, n*10+5, use3, True, use7)
    cnt += count_753_numbers(limit, n*10+7, use3, use5, True)
    return cnt

# 結果を表示
def printResult(result):
    print(result)

# メイン処理
def main():
    N = data_input()
    cnt = count_753_numbers(N, 0, False, False, False)
    printResult(cnt)

if __name__ == "__main__":
    main()