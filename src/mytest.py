my_list = [10,1,0 , 11 , 12]

def make_con():
    output = []
    for x in range(10):
        output.append([])
    return output


def get_digit(mylist, dig):
    output = []
    for x in mylist:
        output.append((x//10**dig) % 10)
    return output


def redix_sort(mylist):
    digit = 0
    while True:
        flag = 0
        con = make_con()
        dig = get_digit(mylist, digit)
        counter = 0
        for x in dig:
            if x > 0:
                flag =1
            con[x].append(mylist[counter])
            counter += 1
        counter = 0
        for x in range(10):
            for y in range(len(con[x])):
                mylist[counter] = con[x][y]
                counter += 1
        if flag == 0:
            return mylist
        digit += 1
