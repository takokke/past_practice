N, Q = map(int, input().split())
# ユーザーの関係を隣接行列で表す
# 縦軸がフォローする人、横軸がフォローされる人
users = [[False for _ in range(N)] for _ in range(N)]

def show_table():
    for i in range(N):
        row = ""
        for j in range(N):
            if users[i][j]:
                row = row + "Y"
            else:
                row = row + "N"
        print(row)

for _ in range(Q):
    query = list(map(int, input().split()))
    type = query[0]

    if type == 1: # フォロー
        a = query[1]
        b = query[2]
        a -= 1
        b -= 1
        users[a][b] = True

    elif type == 2: # フォロー全返し
        a = query[1]
        a -= 1
        for i in range(N):
            if users[i][a]: # aをフォローしている場合
                users[a][i] = True

    elif type == 3: #フォロー
        a = query[1]
        a -= 1
        x_follow_users = [] # ユーザx達がフォローしているユーザを入れる配列
        for i in range(N):
            if users[a][i]:
                for j in range(N):
                    if users[i][j] and j != a:
                        x_follow_users.append(j)
        
        for user in x_follow_users:
            users[a][user] = True

show_table()