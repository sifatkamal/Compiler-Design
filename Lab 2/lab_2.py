upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z']

lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

others = ['.', ',', ';', ')', '(', '{', '}', '[', ']']

test = []

n = int(input('Provide the value of n: '))


# Email

def state_0(listt):
    
    value = listt[0]

    index = 0

    if value in upper or value in lower:

        # index+=1

        state_1(listt[index], index)


    elif value in numbers or value == '.' or value == '@':

        index += 1

        state_6(listt[index], index)


def state_1(value, index):
    
    if value in upper or value in lower or value in numbers or value == '.':

        index += 1

        state_1(listt[index], index)

    elif value == '@':

        index += 1

        state_2(listt[index], index)


def state_2(value, index):

    if value in upper or value in lower or value == '.':

        index += 1

        try:

            state_2(listt[index], index)

        except:

            count = i + 1

            print('Email', end=', ')

            print(count)


    elif value in numbers or value == '@' or value in others:

        index += 1

        state_6(listt[index], index)

def state_6(value, index):
    
    while index < len(listt):
        index += 1

        continue

    print('ERROR')


# URL


def url_state_1(listt):
    
    value = listt[0]

    index = 0

    if value == 'w':

        index += 1

        url_state_2(listt[index], index)

    else:

        index += 1

        url_state_7(listt[index], index)


def url_state_2(value, index):
    
    if value == 'w':

        index += 1

        url_state_3(listt[index], index)

    else:

        index += 1

        url_state_7(listt[index], index)


def url_state_3(value, index):
    
    if listt[index] == 'w':

        index += 1

        url_state_4(listt[index], index)

    else:

        index += 1

        url_state_7(listt[index], index)


def url_state_4(value, index):
    
    if listt[index] == '.':

        index += 1

        url_state_5(listt[index], index)

    else:

        index += 1

        url_state_7(listt[index], index)


def url_state_5(value, index):
    
    if listt[index] == '.':

        index += 1

        url_state_6(listt[index], index)

    elif listt[index] == others:

        index += 1

        url_state_6(listt[index], index)

    elif listt[index] in upper or listt[index] in lower or listt[index] in numbers:

        index += 1

        url_state_5(listt[index], index)


def url_state_6(value, index):
    
    if listt[index] in upper or listt[index] in lower:

        try:

            url_state_6(listt[index], index)

        except:

            print('web', end=', ')

            count = i + 1

            print(count)


def url_state_7(value, index):
    
    while index < len(listt):
    
        index += 1

        continue

    print('ERROR')


# Main Code

for i in range(n):

    stringg = input()

    listt = list(stringg)

    if '@' in listt:

        state_0(listt)

    else:

        url_state_1(listt)