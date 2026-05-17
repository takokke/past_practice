def dfs(i, A, E, visited, key):
    for j in E[i]:
        if visited[j]: continue
        print(j)
        dfs(j, A, E, visited, key)
    visited[i] = True # 呼び出し元に戻る
    if A[i] == key:
        print("探索成功! ", key)

def main():
    # 頂点の情報
    A = [
        'PCA株式会社', 
        '開発部', 
        '営業部',
        '開発統括部',
        '営業統括部',
        '第1開発G', 
        '第2開発G', 
        '第3開発G',
        '業務プロセスデザイン部',
        '関東営業部',
        '中部営業部',
        ]

    # 辺情報
    E = [
        [1, 2], # PCA株式会社
        [3], # 開発部
        [4], # 営業部
        [5, 6, 7, 8], # 開発統括部
        [8, 9, 10], # 営業統括部
        [], # 第1開発G
        [], # 第2開発G
        [], # 第3開発G
        [], # 業務プロセスデザイン部
        [], # 関東営業部
        [] # 中部営業部
    ]

    visited = [False] * len(A)

    s = 0

    dfs(s, A, E, visited, '第1開発G')


if __name__ == "__main__":
    main()