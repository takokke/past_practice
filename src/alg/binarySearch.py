def binary_search(A, key):
    left = 0
    right = len(A) - 1
    
    # 配列の要素数が偶数の場合、最後centerが１つ反対方向に動く。
    # そこで一致するため、 =にしたほうが良い。
    while left <= right:
        center = int((left+right) / 2)
        if A[center] == key:
            return True
        elif A[center] > key:
            right = center - 1
        elif A[center] < key:
            left = center + 1
    return False

def main():
    import random
    A = [random.randint(0, 100) for i in range(100)]
    A.sort()
    key = 99

    key_exists = binary_search(A, key)
    if key_exists:
        print("success!")
    else:
        print("not exists...")

if __name__ == "__main__":
    main()
