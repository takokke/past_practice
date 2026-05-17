
def convert_index(x, y):
    return x + 201, y + 201

def main():
    N, X, Y = map(int, input().split())
    
    visited = []
    
    for i in range(403):
        visited.append([-1]*403)
        
    for i in range(N):
        x, y = map(int, input().split())
        j, i = convert_index(x, y)
        visited[i][j] = -2
        
    sx, sy = convert_index(0, 0)
    gx, gy = convert_index(X, Y)
    
    from collections import deque
    
    q = deque()
    
    q.append([sx, sy])
    visited[sy][sx] = 0
    
    while q:
        x, y = q.popleft()
        for x2, y2 in [[x+1,y+1], [x,y+1], [x-1,y+1], [x+1,y], [x-1,y], [x,y-1]]:
            if not (0 <= x2 < 403 and 0 <= y2 < 403): # 範囲外の場合
                continue
        
            # 壁の場合
            if visited[y2][x2] == -2:
                continue
            
            if visited[y2][x2] == -1:
                q.append([x2, y2])
                visited[y2][x2] = visited[y][x] + 1
                
    print(visited[gy][gx])

if __name__ == "__main__":
    main()