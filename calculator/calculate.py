class Calculate:
    def __init__(self, equalition):
        self.equalition = equalition
        self.values = []
        self.signs = []
        # Calculate.parse_equaliton(self.equalition)

    def parse_equaliton(self):
        tmp = ""
        # eq_len = len(self.equalition)
        for index in range(len(self.equalition)):
            if self.equalition[index].isdigit():
                tmp += self.equalition[index]
            elif self.equalition[index] == "+" or self.equalition[index] == "-" or \
                    self.equalition[index] == "*" or self.equalition[index] == "/":
                self.signs.append(self.equalition[index])
                self.values.append(float(tmp))
                tmp = ""

            if index >= len(self.equalition) - 1:
                self.values.append(float(tmp))

    def count(self):
        i = 0
        while i < len(self.signs):
            current_sign = self.signs[i]
            if current_sign == "*":
                i = self.carry_out_multiplication(i)
                i += 1
                continue
            elif current_sign == "/":
                i = self.carry_out_division(i)
                i += 1
                continue
            i += 1
        i = 0
        while i < len(self.signs):
            current_sign = self.signs[i]
            if current_sign == "+":
                i = self.carry_out_add(i)
                i += 1
                continue
            elif current_sign == "-":
                i = self.carry_out_subtract(i)
                i += 1
                continue
            i += 1
        return self.values[0]

    def carry_out_add(self, index):
        self.values[index] = self.values[index] + self.values[index + 1]
        self.values.pop(index + 1)
        self.signs.pop(index)
        index -= 1
        return index

    def carry_out_subtract(self, index):
        self.values[index] = self.values[index] - self.values[index + 1]
        self.values.pop(index + 1)
        self.signs.pop(index)
        index -= 1
        return index

    def carry_out_division(self, index):
        try:
            self.values[index] = self.values[index] / self.values[index + 1]
            self.values.pop(index + 1)
            self.signs.pop(index)
            index -= 1
            return index
        except ZeroDivisionError:
            print("Cannot divide by 0 ! ")
            exit(0)

    def carry_out_multiplication(self, index):
        self.values[index] = self.values[index] * self.values[index + 1]
        self.values.pop(index + 1)
        self.signs.pop(index)
        index -= 1
        return index
