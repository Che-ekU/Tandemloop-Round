# returning dictionary with number of factors

keys = [1, 2, 3, 4, 5, 6, 7, 8, 9]

multiples = input()

req_list = (list(map(int, (multiples[1:-1].split(',')))))

print(req_list)

result_dict = dict()

for i in keys :
    num = 0
    for j in req_list :
        if j % i == 0:
            num += 1
    result_dict[i] = num

print(result_dict)