import numpy as np

with open('sample.txt') as f:
    lines = np.array([list(line) for line in f.read().split()])

# PART 1:
def gamma_epsilon(arr):
    gamma = ''
    epsilon = ''
    for j in range(len(arr[0])):
        if sum([int(arr[i][j]) for i in range(len(arr))]) > len(arr) // 2:
            gamma += '1'
            epsilon +='0'
        elif sum([int(arr[i][j]) for i in range(len(arr))]) == len(arr) / 2:
            gamma += '1'
            epsilon += '1'
        else:
            epsilon += '1'
            gamma += '0'
    return [gamma, epsilon]

#print(int(gamma_epsilon(lines)[0],2) * int(gamma_epsilon(lines)[1], 2))



def calc_ratings(arr, j):
    new_arr_O2 = []
    new_arr_CO2 = []

    common = gamma_epsilon(arr[:, j])[0]
    least_common = gamma_epsilon(arr[:, j])[1]

    for i in range(len(arr)):
        if arr[i,j] == common:
            new_arr_O2.append(arr[i])
        else:
            new_arr_CO2.append(arr[i])
    return [np.array(new_arr_O2), np.array(new_arr_CO2)]



def calc_scrubers(arr):
    linesO2 = arr
    linesCO2 = arr

    j = 0
    while len(linesO2) > 1:
        linesO2 = calc_ratings(linesO2, j)[0]
        j += 1

    j = 0
    while len(linesCO2) > 1:
        linesCO2 = calc_ratings(linesCO2, j)[1]
        j += 1

    return int(''.join(linesO2[0].astype(str)),2) * int(''.join(linesCO2[0].astype(str)),2)


print(calc_scrubers(lines))





