#6-1

def SSN(numbers):
    n_lst = (numbers.split('-'))
    result = (n_lst[0] + '*******')
    return result

print(SSN(940503-123456))