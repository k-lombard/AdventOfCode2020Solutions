def file_input():
    file = open("answers.txt")

    answers = []
    for line in file:
        answers.append(line.strip())
    return answers



def make_dict(answers):
    adict = {}
    count = 0
    for line in answers:
        if len(line) == 0:
            count += 1
            continue
        else:
            if count not in adict:
                adict[count] = [line]
            else:
                adict[count] = adict[count] + [line]
    return adict


def sol1(adict):
    total = 0
    for key in adict:
        answer_dict = {}
        for item in adict[key]:
            for letter in item:
                if letter not in answer_dict:
                    answer_dict[letter] = 1
                else:
                    continue
        for letter in answer_dict:
            total += 1
    
    return total
        



#part 1
print(sol1(make_dict(file_input())))