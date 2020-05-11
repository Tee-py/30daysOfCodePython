

def closest_power(num1,num2):
    if type(num1)!=int or type(num2)!=int or num1<0 or num2<0:
        return 'Invalid args..args should be positive integers'
    elif num2<num1:
        return 'Second argument shpould be higher or equal to the first arg'
    else:
        test_nums = [num1**i for i in range(num2) if num1**i<=num2]
        return test_nums.index(test_nums[-1])

print(closest_power(3,26))


