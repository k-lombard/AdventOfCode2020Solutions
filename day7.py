def file_input():
    file = open("bags.txt")

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
            
  


def sort(adict, newlist, newdict):
    templist = []
    if(len(newlist) == 0):
        return newdict
    for item in newlist:
        for key in adict:
            if item in adict[key]:
                if item not in newdict:
                    newdict[item] = [key]
                    templist.append(key)
                else:
                    newdict[item] += [key]
                    templist.append(key)
    return sort(adict, templist, newdict)




class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)



# def build_tree(root, adict):
#     if root.data in adict:
#         for a_str in adict[root.data]:
#             temp = Node(a_str)
#             root.children.append(temp)
#         for child in root.children:
#             build_tree(child, adict)


def build_tree(root, adict, templist):
    for key in adict:
        if root.data in adict[key]:
            print(adict[key])
            temp = Node(key)
            root.children.append(temp)
    
    for node in root.children:
        templist.append(node.data)
        build_tree(node, adict, templist)


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



    


#print(sort(bag_map(file_input()), ["shinygold"], {}))

root = Node("shinygold")
count = {}
#build_tree(root, sort(bag_map(file_input()), ["shinygold"], {}))
templist = []
build_tree(root, bag_map(file_input()), templist)
dfs(root, None)
print(count[root])

print(count_list(templist))
#





