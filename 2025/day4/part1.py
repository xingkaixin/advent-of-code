def solve():
    with open("2025/day4/input.txt", "r") as f:
        grid = [list(line.strip()) for line in f if line.strip()]

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    accessible_count = 0

    # 遍历每个位置
    for i in range(rows):
        for j in range(cols):
            # 如果当前位置是纸卷
            if grid[i][j] == "@":
                # 检查8个相邻位置
                adjacent_rolls = 0

                # 检查周围的8个方向：上、下、左、右、四个对角线
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        # 跳过当前位置
                        if di == 0 and dj == 0:
                            continue

                        ni, nj = i + di, j + dj
                        # 检查边界
                        if 0 <= ni < rows and 0 <= nj < cols:
                            if grid[ni][nj] == "@":
                                adjacent_rolls += 1

                # 如果相邻纸卷少于4个，则叉车可以访问
                if adjacent_rolls < 4:
                    accessible_count += 1

    print(f"可以被叉车访问的纸卷数量: {accessible_count}")
    return accessible_count

if __name__ == "__main__":
    solve()
