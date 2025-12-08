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

    if i < 10:  # 只显示前10步
        print(
            f"第{i + 1:4d}步: {line:6s} 从{start_pos:3d}到{pos:3d}, 经过0: {zero_passes}次, 累计: {total_zero_count}"
        )

print(f"\n最终密码: {total_zero_count}")
