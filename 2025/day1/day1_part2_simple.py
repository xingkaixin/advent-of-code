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

    # 计算新位置
    if d == "R":
        pos = (pos + step) % 100
    else:
        pos = (pos - step) % 100

    # 计算经过0的次数
    # 在旋转过程中，每100步就会经过0一次
    zero_passes = step // 100

    # 检查是否跨越了0点（从start_pos到pos的过程中）
    if d == "R":
        # 向右旋转，如果最终位置小于起始位置，说明跨越了0
        if pos <= start_pos:
            zero_passes += 1
    else:
        # 向左旋转，如果最终位置大于等于起始位置，说明跨越了0
        if pos >= start_pos:
            zero_passes += 1

    # 检查是否停在0上
    if pos == 0:
        total_zero_count += 1

    # 加上旋转过程中经过0的次数
    total_zero_count += zero_passes

    if i < 15:  # 只显示前15步
        print(
            f"第{i + 1:4d}步: {line:6s} 从{start_pos:3d}到{pos:3d}, 经过0: {zero_passes}次,停在0: {1 if pos == 0 else 0}次, 累计: {total_zero_count}"
        )

print(f"\n最终密码: {total_zero_count}")
