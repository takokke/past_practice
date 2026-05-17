import time

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

# 単方向リスト
# 先頭ポインタと、末尾ポインタは存在する。
class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value): # 末尾に追加の場合
        new_node = Node(value)
        if not self.head: # 連結リストのデータが空のとき
            self.head = new_node
            self.tail = new_node
            return
        prev_node = self.tail
        self.tail = new_node # 末尾ポインタを更新
        prev_node.next = new_node

N = 1000000
linked_list = LinkedList()
for i in range(N):
    linked_list.append(i+1)

# 末尾に要素を追加する
start = time.perf_counter()
linked_list.append(1)
end = time.perf_counter()

print(round((end-start)*1000, 10), "m秒")