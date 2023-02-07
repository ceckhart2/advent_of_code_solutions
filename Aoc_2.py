with open('sample.txt') as f:
    instructions = [line.split() for line in f.readlines()]
aim = 0
depth = 0
horizontal = 0
for instruction in instructions:
    elev = int(instruction[1])
    if instruction[0] == 'up':
        aim -= elev
    elif instruction[0] == 'down':
        aim += elev
    elif instruction[0] == 'forward':
        horizontal += elev
        depth += (elev * aim)
    else:
        horizontal -= elev

print(horizontal * depth)
