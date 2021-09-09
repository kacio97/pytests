signs = []
values = []


def calculate_from_file(filename):
    equalitions = __read_data_from_file(filename)
    print(equalitions)
    results = []
    if len(equalitions):
        for equalition in equalitions:
            results.append(__calculate(equalition))
            signs.clear()
            values.clear()
        print(results)
        return results
    else:
        return 0


def __read_data_from_file(filename):
    equalition_list = []
    if ".txt" in filename:
        with open(filename) as f:
            for line in f:
                for eq in line.split():
                    equalition_list.append(eq.rstrip('\n'))
                    # print(eq, end='')
    else:
        return equalition_list
    return equalition_list


def __calculate(equalition):
    # =================================================
    #         PARSING                                 #
    # =================================================
    tmp = ""
    for index in range(len(equalition)):
        if equalition[index].isdigit():
            tmp += equalition[index]
        elif equalition[index] == "+" or equalition[index] == "-" or \
                equalition[index] == "*" or equalition[index] == "/":
            signs.append(equalition[index])
            values.append(float(tmp))
            tmp = ""
        if index >= len(equalition) - 1:
            values.append(float(tmp))
    # =================================================
    #         COUNTING                                #
    # =================================================
    i = 0
    while i < len(signs):
        current_sign = signs[i]
        current_res = values[i]
        if current_sign == "*":
            i = __carry_out_multiplication(i)
            i += 1
            continue
        elif current_sign == "/":
            i = __carry_out_division(i)
            i += 1
            continue
        i += 1
    i = 0
    while i < len(signs):
        current_sign = signs[i]
        current_res = values[i]
        if current_sign == "+":
            i = __carry_out_add(i)
            i += 1
            continue
        elif current_sign == "-":
            i = __carry_out_subtract(i)
            i += 1
            continue
        i += 1
    return values[0]


def __carry_out_add(index):
    values[index] = values[index] + values[index + 1]
    values.pop(index + 1)
    signs.pop(index)
    index -= 1
    return index


def __carry_out_subtract(index):
    values[index] = values[index] - values[index + 1]
    values.pop(index + 1)
    signs.pop(index)
    index -= 1
    return index


def __carry_out_division(index):
    try:
        values[index] = values[index] / values[index + 1]
        values.pop(index + 1)
        signs.pop(index)
        index -= 1
        return index
    except ZeroDivisionError:
        print("Cannot divide by 0 ! ")
        exit(0)


def __carry_out_multiplication(index):
    values[index] = values[index] * values[index + 1]
    values.pop(index + 1)
    signs.pop(index)
    index -= 1
    return index
