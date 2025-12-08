# 测试算法：按照题目例子
pos = 50
total_zero_count = 0

# 题目中的例子序列
test_instructions = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]

for i, line in enumerate(test_instructions):
    d = line[0]  # 'L' 或 'R'
    step = int(line[1:])  # 旋转距离
    start_pos = pos

    # 计算经过0的次数
    zero_passes = 0

    if d == "L":
        # 向左旋转：从start_pos开始，每一步减少1
        current = start_pos
        for j in range(step):
            current = (current - 1) % 100
            if current == 0:
                zero_passes += 1
        pos = current
    else:
        # 向右旋转：从start_pos开始，每一步增加1
        current = start_pos
        for j in range(step):
            current = (current + 1) % 100
            if current == 0:
                zero_passes += 1
        pos = current

    total_zero_count += zero_passes

    print(f"第{i+1:4d}步: {line:6s} 从{start_pos:3d}到{pos:3d}, 经过0: {zero_passes}次, 累计: {total_zero_count}")

print(f"\n测试密码: {total_zero_count}")
print("期望密码: 6")