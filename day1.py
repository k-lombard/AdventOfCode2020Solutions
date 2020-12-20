def file_input():
    file = open("input.txt")

    numbers = []

    for line in file:
        numbers.append(line.strip())

    return numbers


def sol1(numbers):
    answer = []
    for i in numbers:
        for j in numbers:
            for k in numbers:   
                if (int(i) + int(j) + int(k)) == 2020:
                    answer.append(int(i)*int(j)*int(k))
    return answer[0]

#part 2
print(sol1(file_input()))


