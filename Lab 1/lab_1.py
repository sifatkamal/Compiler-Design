fdata = open('lab_1.txt')

fdata= fdata.read()

data = fdata.split('\n')

keyword = ['int', 'float', 'if', 'else', 'double', 'for', 'while', 'except', 'in', 'is', 'from','not', 'or', 'elif','as', 'True', 'False', 'and', 'def','break','pass' ]

math_operator = ['+', '-', '/', '%', '*','=']

logical_operator =['>', '<', '<=','>=','!=','==' ]

others = [',', ';', ')','(','{','}','[',']']

numbers = ['1','2','3','4','5','6','7','8','9','0']

listt = []

index = 0

key = []

idd = []

math = []

logic = []

num = []

symbol = []


for i in data:
    
    value = data[index].split(" ")
    
    for j in value:
            
        if j in keyword or j in math_operator or j in logical_operator or j in others or j in numbers:
            
            listt.append(j)
            
        else:
            
            listt_2 = list(j)
        
            for k in listt_2:
            
                listt.append(k)
                                  
    index+=1
    
count = 0
    
for j in listt:
    
    if j in keyword:
        
        key.append(j)
        
    elif j in numbers:
        
        if listt[count+1] == ".":
            
            listt.pop(count+1)
            
            add_1 = listt.pop(count+1)
                        
            add = j + "." + add_1
            
            num.append(add)
            
        else:    
        
            num.append(j)
        
    elif j in math_operator:
        
        math.append(j)
    
    elif j in logical_operator:
        
        logic.append(j)

    elif j in others:

        symbol.append(j)
        
    elif type(j) == type(float):
        
        num.append(j)
        
    else:
        
        idd.append(j)
        
    count+=1 
        
print("Keywords:", end = " ")        
        
for i in key:
    
    if i == key[-1]:
        
        print(i)
        
    else:    
    
        print(i, end = ", ")

print()

print("Identifiers:", end = " ")

duplicate_1 = []

[duplicate_1.append(x) for x in idd if x not in duplicate_1] 

duplicate_1.remove("\t")
    
for i in duplicate_1:
        
    if i == duplicate_1[-1]:
        
        print(i)
        
    else:    
    
        print(i, end = ", ")

print()

print("Math Operators:", end = " ")


duplicate_2 = []

[duplicate_2.append(x) for x in math if x not in duplicate_2]

duplicate_2.sort()

for i in duplicate_2:
    
    if i == duplicate_2[-1]:
        
        print(i)
        
    else:    
    
        print(i, end = ", ")

print()

print("Logical Operators:", end = " ")

for i in logic:
    
    print(i, end = " ")

print()

print("Numerical Values:", end = " ")

for i in num:
        
    if i == num[-1]:
        
        print(i)
        
    else:
        
        print(i, end = ", ")

print()

print("Others:", end = " ")

duplicate = []

[duplicate.append(x) for x in symbol if x not in duplicate]  

for i in duplicate:

    print(i, end = "")