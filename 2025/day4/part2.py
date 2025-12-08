def solve():
    with open("2025/day4/input.txt", "r") as f:
        grid = [list(line.strip()) for line in f if line.strip()]

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    total_removed = 0
    iterations = 0

    # 创建可访问性检查的辅助函数
    def is_accessible(grid, i, j):
        """检查位置(i,j)的纸卷是否可访问"""
        if grid[i][j] != "@":
            return False

        adjacent_rolls = 0
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue

                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols:
                    if grid[ni][nj] == "@":
                        adjacent_rolls += 1

        return adjacent_rolls < 4

    # 迭代移除过程
    while True:
        # 找出所有当前可访问的纸卷
        to_remove = []
        for i in range(rows):
            for j in range(cols):
                if is_accessible(grid, i, j):
                    to_remove.append((i, j))

        # 如果没有可访问的纸卷，退出循环
        if not to_remove:
            break

        # 移除所有可访问的纸卷
        removed_count = len(to_remove)
        total_removed += removed_count
        iterations += 1

        print(f"第 {iterations} 次迭代：移除 {removed_count} 个纸卷")

        for i, j in to_remove:
            grid[i][j] = "."  # 用"."标记为已移除

    print(f"\n总共移除的纸卷数量: {total_removed}")
    print(f"迭代次数: {iterations}")

    return total_removed

if __name__ == "__main__":
    solve()
