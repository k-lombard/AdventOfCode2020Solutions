
def file_input():
    file = open("passwords.txt")

    password_lines = []
    for line in file:
        password_lines.append(line.strip())
    return password_lines




def sol1(password_lines):
    valid = 0
    for line in password_lines:
        dict1 = {}
        lower = 0
        upper = 0
        temp = line.split()
        letter1 = temp[1][0]
        if (temp[0][1] == "-"):
            lower = int(temp[0][0])
            upper = int(temp[0][2:])
        else:
            lower = int(temp[0][0:2])
            upper = int(temp[0][3:])
        
        
        for letter in temp[2]:
            if letter not in dict1:
                dict1[letter] = 1
            else:
                dict1[letter] = dict1[letter] + 1
        print(dict1)
        if letter1 not in dict1:
            continue
        if (dict1[letter1] >= lower) and (dict1[letter1] <= upper):
            valid += 1
            continue
        else:
            continue
    return valid



def sol2(password_lines):
    valid = 0
    for line in password_lines:
        dict1 = {}
        lower = 0
        upper = 0
        temp = line.split()
        letter1 = temp[1][0]
        if (temp[0][1] == "-"):
            lower = int(temp[0][0])
            upper = int(temp[0][2:])
        else:
            lower = int(temp[0][0:2])
            upper = int(temp[0][3:])
        
        lower = lower - 1;
        upper = upper - 1;

        if temp[2][lower] == letter1 and temp[2][upper] != letter1:
            valid += 1
            continue
        
        if temp[2][lower] != letter1 and temp[2][upper] == letter1:
            valid +=1
            continue
        
    return valid
        
    #     for letter in temp[2]:
    #         if letter not in dict1:
    #             dict1[letter] = 1
    #         else:
    #             dict1[letter] = dict1[letter] + 1
    #     print(dict1)
    #     if letter1 not in dict1:
    #         continue
    #     if (dict1[letter1] >= lower) and (dict1[letter1] <= upper):
    #         valid += 1
    #         continue
    #     else:
    #         continue
    # return valid

print(sol2(file_input()))



        

    

    

        