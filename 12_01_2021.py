with open('sample.txt') as f:
    lines = f.read().split()
    lines = [int(line) for line in lines]

# Part 1
# count = sum([1 for i in range(1, len(lines)) if lines[i] > lines[i-1]] )

# Part 2
three_sums = [sum(lines[i: i + 3]) for i in range(len(lines) - 2)]
count = sum(1 for i in range(1, len(three_sums)) if three_sums[i] > three_sums[i - 1])

print(count)
