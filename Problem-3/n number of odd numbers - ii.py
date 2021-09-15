# generating 'n' number of odd numbers 

num = int(input())

if num % 2 == 0 :
    num = num - 1

output_list = []
for i in range(1, num * 2):
    if i % 2 != 0 :
        output_list += [str(i)]
        
print((', ').join(output_list))