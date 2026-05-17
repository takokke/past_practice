
class BinaryTree:
    def __init__(self, node, edge, visited):
        self.node = node
        self.edge = edge
        self.visited = visited

def search(i, bt: BinaryTree, key):
    print(i, "の値を探索しました")
    bt.visited[i] = True
    if bt.node[i] == key:
        print("探索成功!!", key)

def dfs(i, bt: BinaryTree, key):
    match len(bt.edge[i]):
        case 0:
            search(i, bt, key)
        case 1:
            j = bt.edge[i][0]
            if not bt.visited[j]:
                dfs(j, bt, key)
            search(i, bt, key)
        case 2:
            left = bt.edge[i][0]
            right = bt.edge[i][1]
            # 左
            if not bt.visited[left]:
                dfs(left, bt, key)
            # 自分
            search(i, bt, key)
            # 右
            if not bt.visited[right]:
                dfs(right, bt, key)

def main():
    # 通りがけは２分木のみ
    # 頂点の情報
    A = [
        'PCA株式会社', 
        '開発部', 
        '営業部',
        '開発統括部',
        '営業統括部',
        '第1開発G',
        '業務プロセスデザイン部',
        '関東営業部',
        ]

    # 辺情報
    E = [
        [1, 2], # PCA株式会社
        [3], # 開発部
        [4], # 営業部
        [5, 6], # 開発統括部
        [6,7], # 営業統括部
        [], # 第1開発G
        [], # 業務プロセスデザイン部
        [], # 関東営業部'
    ]
    
    visited = [False] * len(A)

    bt = BinaryTree(A, E, visited)

    s = 0

    dfs(s, bt,'第1開発G')


if __name__ == "__main__":
    main()