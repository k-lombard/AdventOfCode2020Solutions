def file_input():
    file = open("passports.txt")

    passport_lines = []
    for line in file:
        passport_lines.append(line.strip())
    return passport_lines



def make_dict(passport_lines):
    count = 0
    adict = {}
    for line in passport_lines:
        if line:
            line = line.split()
        if not line:
            count += 1
            continue
        if count not in adict:
            adict[count] = line
        else:
            adict[count] = adict[count] + line
    
    newdict = {}
    
    for key in adict:
        tempdict = {}
        for item in adict[key]:
            colon = item.find(":")
            tempdict[item[0:colon]] = item[colon + 1:]
        newdict[key] = tempdict
    

    total = 0
    for key in newdict:
        if ((len(newdict[key]) == 7 and "cid" not in newdict[key]) or len(newdict[key]) == 8):
            if (int(newdict[key]['byr']) >= 1920 and int(newdict[key]['byr']) <= 2002):
                
                if (int(newdict[key]['iyr']) >= 2010 and int(newdict[key]['iyr']) <= 2020):
                    
                    if (int(newdict[key]['eyr']) >= 2020 and int(newdict[key]['eyr']) <= 2030):
                        
                        if (("cm" in newdict[key]['hgt'] and (int(newdict[key]['hgt'][0:len(newdict[key]['hgt']) - 2]) >= 150 and int(newdict[key]['hgt'][0:len(newdict[key]['hgt']) - 2]) <= 193) or ("in" in newdict[key]['hgt'] and (int(newdict[key]['hgt'][0:len(newdict[key]['hgt']) - 2]) >= 59 and int(newdict[key]['hgt'][0:len(newdict[key]['hgt']) - 2]) <= 76)))):
                             
                            if (newdict[key]['hcl'][0] == "#" and len(newdict[key]['hcl']) == 7): 
                                
                                if (newdict[key]['ecl'] == "amb" or newdict[key]['ecl'] == "blu" or newdict[key]['ecl'] == "brn" or newdict[key]['ecl'] == "gry" or newdict[key]['ecl'] == "grn" or newdict[key]['ecl'] == "hzl" or newdict[key]['ecl'] == "oth"):
                                    if (len(newdict[key]['pid']) == 9):
                                        total += 1
    return total



    
    
        
    


print(make_dict(file_input()))