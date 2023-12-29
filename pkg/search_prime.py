def check_if_prime(num):
    is_prime = False

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
        else:
            is_prime = True
            
    if is_prime:
        return True 
    return False
    

def search_prime_num(num_list):
    prime_numbers = []
    for num in num_list:
        
        num = check_if_prime(num)
        if num:
            prime_numbers.append(num)
                

    return prime_numbers



