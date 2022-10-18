fdata = open('input_1.txt')

fdata = fdata.read()

data = fdata.split('\n')

index = 0

listt = []

for i in data:
    
    value = data[index].split(" ")

    listt.append(value)

    index+=1

print(listt)