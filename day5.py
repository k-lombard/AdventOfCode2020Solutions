import math

def file_input():
    file = open("boarding.txt")

    boarding = []
    for line in file:
        boarding.append(line.strip())
    return boarding




def sol1(boarding):
    id_map = {}
    for line in boarding:
        id_map[line] = (recurse_first(line[0:len(line)-3], 0, 127) * 8) + recurse_second(line[7:], 0, 7)
    return id_map


def recurse_first(line, min, max):
    if (len(line) == 1):
        if line[0] == "F":
            return min
        if line[0] == "B":
            return max
    else:
        if line[0] == "F":
            max = math.floor((max-min)/2 + min)
        if line[0] == "B":
            min = math.ceil((max-min)/2 + min)
        return recurse_first(line[1:], min, max)



def recurse_second(line, min, max):
    if (len(line) == 1):
        if line[0] == "L":
            return min
        if (line[0] == "R"):
            return max
    else:
        if line[0] == "L":
            max = math.floor((max-min)/2 + min)
        if line[0] == "R":
            min = math.ceil((max-min)/2 + min)
        return recurse_second(line[1:], min, max)


def find_max(id_map):
    max = 0
    for key in id_map:
        if id_map[key] > max:
            max = id_map[key]
    
    return max


def find_seat(id_map):
    newlist = []
    for key in id_map:
        newlist.append(id_map[key])
    newlist = sorted(newlist)
    start = newlist[0]
    for i in newlist:
        if start != i:
            return start
        else:
            start += 1
    


        

#part 1
print(find_max(sol1(file_input())))
#part 2
print(find_seat(sol1(file_input())))
