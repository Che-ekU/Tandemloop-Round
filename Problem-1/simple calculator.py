# operations = ['ADD', 'SUB', 'MUL', 'DIV', 'MOD', 'EXP']
# EXP => num_1 ** num_2, performs exponentiation
# MOD => num_1 % num_2, performs Modulus
# SUB operation subtracts num_2 from num_1, and other operations too.

num_1 = float(input())
num_2 = float(input())
operation = input()

if operation.upper() == 'ADD' :
    print(round((num_1 + num_2), 3))
    
elif operation.upper() == 'SUB' :
        print(round((num_1 - num_2), 3))
    
elif operation.upper() == 'MUL' :
        print(round((num_1 * num_2), 3))
        
elif operation.upper() == 'DIV' :
    if num_2 == 0 :
        print('Cannot perform 0 division')
    else :
        print(round((num_1 / num_2), 3))
        
elif operation.upper() == 'EXP' :
        print(round((num_1 ** num_2), 3))
        
elif operation.upper() == 'MOD' :
        print(round((num_1 % num_2), 3))
        
else :
    print("Please Enter Valid Data")