# 从test1.py提取旋转指令
instructions = []
with open("test1.py", "r") as f:
    for line in f:
        line = line.strip()
        if line.startswith("→") and ("R" in line or "L" in line):
            instruction = line.split()[1].strip('"')
            instructions.append(instruction)

pos = 50
total_zero_count = 0

for i, line in enumerate(instructions):
    d = line[0]  # 'L' 或 'R'
    step = int(line[1:])  # 旋转距离
    start_pos = pos

    if d == "R":
        # 向右旋转：每经过0点一次
        # 从start_pos开始，向右移动step步
        # 每100步经过0一次，再加上跨越0的次数
        zero_passes = step // 100
        # 检查是否跨越0点
        if start_pos < pos:
            # 从50到82，没有跨越0
            pass
        else:
            # 跨越0一次
            zero_passes += 1
    else:
        # 向左旋转：从start_pos开始，向左移动step步
        # 每100步经过0一次，再加上跨越0的次数
        zero_passes = step // 100
        # 检查是否跨越0点
        if start_pos > pos:
            # 从82到52，没有跨越0
            pass
        else:
            # 跨越0一次
            zero_passes += 1

    # 计算新位置
    if d == "R":
        pos = (pos + step) % 100
    else:
        pos = (pos - step) % 100

    # 检查是否停在0上
    if pos == 0:
        total_zero_count += 1

    # 加上旋转过程中经过0的次数
    total_zero_count += zero_passes

print(f"最终密码: {total_zero_count}")
