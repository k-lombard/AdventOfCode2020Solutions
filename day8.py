def file_input():
    file = open("boot.txt")

    boot = []
    for line in file:
        boot.append(line.strip())
    return boot


def sol1(boot):
    acc = 0
    i = 0
    newlist=[]
    while i < len(boot):
        if i not in newlist:
            if "nop" in boot[i]:
                newlist.append(i)
                i += 1
                continue
            if "acc" in boot[i]:
                acc += int(boot[i][4:])
                newlist.append(i)
                i += 1
                continue
            if "jmp" in boot[i]:
                num = int(boot[i][4:])
                newlist.append(i)
                i += num
                continue
                
        else:
            return acc


def locations(boot):
    loc_dict = {}
    count = 0
    for line in boot:
        if "nop" in line or "jmp" in line:
            loc_dict[count] = line
            count +=1
        else:
            count += 1

    return loc_dict




# def sol2(boot):
#     acc = 0
#     i = 0
#     newlist=[]
#     templist = []
#     while i < len(boot):
#         print(templist)
#         templist.append(boot[i])
#         if "nop" in boot[i]:
#             newlist.append(i)
#             i += 1
#             continue
#         if "acc" in boot[i]:
#             acc += int(boot[i][4:])
#             newlist.append(i)
#             i += 1
#             continue
#         if "jmp" in boot[i]:
#             num = int(boot[i][4:])
#             newlist.append(i)
#             i += num
#             continue
                
        
        
#     return acc



def bruteforce(boot, loc_dict):
    for key in loc_dict:
        
        acc = 0
        i = 0
        newlist=[]
        while i < len(boot):
            if i not in newlist:
                if i == key:
                    print(boot)
                    if "jmp" in boot[i]:
                        newlist.append(i)
                        i += 1
                        continue
                    if "nop" in boot[i]:
                        num = int(boot[i][4:])
                        newlist.append(i)
                        i += num
                        continue
                else:
                    if "nop" in boot[i]:
                        newlist.append(i)
                        i += 1
                        continue
                    if "acc" in boot[i]:
                        acc += int(boot[i][4:])
                        newlist.append(i)
                        i += 1
                        continue
                    if "jmp" in boot[i]:
                        num = int(boot[i][4:])
                        newlist.append(i)
                        i += num
                        continue
            else:
                break
            
    return acc
                    



        


# < 1867


print(bruteforce(file_input(), locations(file_input())))

