import re

def file_input():
    file = open("bags.txt")

    bags = []
    for line in file:
        bags.append(line.strip())
    return bags



def file_input3():
    file = open("bagception.txt")

    bags = []
    for line in file:
        bags.append(line.strip())
    return bags



def bag_map(bags):
    adict = {}
    for line in bags:
        right_colors = []
        first = line.find("bags")
        left_color = line[0:first-1]
        left_color = left_color.replace(" ", "")
        contain_index = line.find("contain")
        temp = line[contain_index+10:]
        result = ''.join([i for i in temp if not i.isdigit()])
        result = result.replace(" ", "")
        result = result.replace(".", "")
        result = result.replace("bags", "")
        result = result.replace("bag", "")
        right_colors = result.split(",")
        count1 = 0
        for item in right_colors:
            right_colors[count1] = item.replace("bags", "")
            count1 += 1
        adict[left_color] = right_colors
    for key in adict:
        for item in adict[key]:
            item = item.replace(".", "")
            
    return adict


def bag_map_nums(bags):
    adict = {}
    for line in bags:
        right_colors = []
        first = line.find("bags")
        left_color = line[0:first-1]
        left_color = left_color.replace(" ", "")
        contain_index = line.find("contain")
        result = line[contain_index+8:]
        result = result.replace(" ", "")
        result = result.replace(".", "")
        result = result.replace("bags", "")
        result = result.replace("bag", "")
        right_colors = result.split(",")
        count1 = 0
        for item in right_colors:
            right_colors[count1] = item.replace("bags", "")
            count1 += 1
        adict[left_color] = right_colors
    for key in adict:
        for item in adict[key]:
            item = item.replace(".", "")
            
    return adict



class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []
    

    def add_child(self, obj):
        self.children.append(obj)


class Node2(object):
    def __init__(self, data, amount):
        self.data = data
        self.children = []
        self.amount = amount

    def add_child(self, obj):
        self.children.append(obj)




def build_tree(root, adict, templist):
    for key in adict:
        if root.data in adict[key]:
            
            temp = Node(key)
            root.children.append(temp)
    
    for node in root.children:
        templist.append(node.data)
        build_tree(node, adict, templist)


def build_tree2(root, adict, templist):
    for item in adict[root.data]:
        if item != "noother":
            if item[0] in "1234567890":
                 temp = Node2(item[1:], int(item[0]))
            else:
                 temp = Node2(item, 1) 
            root.children.append(temp)

            
        
    for node in root.children:
        templist.append(node)
        build_tree2(node, adict, templist)


def dfs2(root, prev):
    count2[root] = root.amount
    for child in root.children:
        if child == prev:
            continue
        dfs(child, root)
        count2[root] += root.amount + root.amount*child.amount
    


def dfs(root, prev):
    count[root] = 1
    
    for child in root.children:
        if child == prev:
            continue
        dfs(child, root)
        count[root] += count[child]
        
        


def count_list(templist):
    newlist = []
 
    for item in templist:
        if item not in newlist:
            newlist.append(item)
    
    return len(newlist)




def count_bags(root2):
    num = 0
    bag = root2.children
    for child in bag:
        num += child.amount + child.amount*count_bags(child)
    return num



#part 1
root = Node("shinygold")
count = {}
count2 = {}
templist = []
build_tree(root, bag_map(file_input()), templist)
dfs(root, None)
print(count_list(templist))



#part 2
templist2 = []
root2 = Node2("shinygold", 1)

build_tree2(root2, bag_map_nums(file_input()), templist2)

count2 = {}

dfs2(root2, None)

total = 0
alist = []


print(count_bags(root2))









