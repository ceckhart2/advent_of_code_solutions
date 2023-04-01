monkey_dict = {}

with open('advent_1') as f:
    instructions = f.read().split('\n\n')
    monkey_split = [instruction.split('\n') for instruction in instructions]
    items = [info[1][18:].replace(' ', '').split(',') for info in monkey_split]
    operations = [info[2].strip()[21:] for info in monkey_split]
    tests = [info[3].strip()[6:] for info in monkey_split]
    true = [info[4].strip()[25:] for info in monkey_split]
    false = [info[5].strip()[26:] for info in monkey_split]


    for i in range(len(monkey_split)):
        monkey_dict[i] = []
        monkey_dict[i].append(items[i])
        monkey_dict[i].append(operations[i])
        monkey_dict[i].append(tests[i])
        monkey_dict[i].append(true[i])
        monkey_dict[i].append(false[i])
        monkey_dict[i].append(0)
    divisor = 1
    for i in range(len(monkey_split)):
        divisor *= int(monkey_dict[i][2][13:])
    print(divisor)

def calc(operator, num1, num2):

    if operator == '+':
        return (num1 + num2)
    elif operator == '*':
        return (num1 * num2)


for i in range(10000):
    for j in range(len(monkey_dict)):

        while monkey_dict[j][0]:
            item = monkey_dict[j][0][0]

            operator = monkey_dict[j][1][:1]
            num2 = monkey_dict[j][1][2:]
            divisor = int(monkey_dict[j][2][13:])
            tf = False

            if 'old' in num2:
                num2 = int(item)

            fear = calc(operator, int(item), int(num2))
            monkey_dict[j][5] += 1

            tf = True if fear % divisor == 0 else False

            sendto = int(monkey_dict[j][3]) if tf else int(monkey_dict[j][4])
            monkey_dict[sendto][0].append(fear % 9699690)
            del(monkey_dict[j][0][0])
    print(i)

most_actives = []
for key in monkey_dict.keys():
    most_actives.append(monkey_dict[key][5])

sorted = sorted(most_actives, reverse=True)
print(sorted[0] * sorted[1])


