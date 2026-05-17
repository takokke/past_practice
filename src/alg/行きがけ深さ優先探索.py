def dfs(i, A, E, visited):
    visited[i] = True
    for j in E[i]:
        if visited[j]: continue
        dfs(j, A, E, visited)


def main():
    # 頂点の情報
    A = [
        'PCA株式会社', 
        'テクノロジー本部', 
        'AI・データソリューション本部'
        'DX統括部', 
        'ビジネスシステムテクノロジー本部', 
        '第1開発G', 
        '第2開発G', 
        '第3開発G', 
        'エージェントサービス事業部',
        ]

    # 辺情報
    E = [
        [1, 2, 8],
        [3], # 'テクノロジー本部'
        [], # 'AI・データソリューション本部'
        [4], # 'DX統括部', 
        [5, 6, 7],
        [],
        [],
        [],
        []
    ]

    visited = [False] * len(A)

    s = 0

    dfs(s, A, E, visited)


if __name__ == "__main__":
    main()