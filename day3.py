def file_input():
    file = open("trees.txt")

    tree_lines = []
    for line in file:
        tree_lines.append(line.strip())
    return tree_lines

def sol1(tree_lines):
    trees = 0
    index = 0
    for line in tree_lines:
        index = index % len(line)
        if line[index] == "#":
            trees += 1
        index = index + 3     
    return trees



def sol2(tree_lines):
    trees = 0
    index = 0
    for line in tree_lines:
        index = index % len(line)
        if line[index] == "#":
            trees += 1
        index = index + 1
    return trees

def sol3(tree_lines):
    trees = 0
    index = 0
    for line in tree_lines:
        index = index % len(line)
        if line[index] == "#":
            trees += 1
        index = index + 5
    return trees



def sol4(tree_lines):
    trees = 0
    index = 0
    for line in tree_lines:
        index = index % len(line)
        if line[index] == "#":
            trees += 1
        index = index + 7
    return trees



def sol5(tree_lines):
    trees = 0
    index = 0
    count = 0
    for line in tree_lines:
        if (count % 2 != 0):
            count += 1
            continue
        index = index % len(line)
        if line[index] == "#":
            trees += 1
        index = index + 1
        count += 1
    return trees

#part 1
print(sol1(file_input()))
#part 2
print(sol1(file_input()) * sol2(file_input()) * sol3(file_input()) * sol4(file_input()) * sol5(file_input()))