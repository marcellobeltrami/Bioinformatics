def fibonacci_rabbits(n, k): 
    fibonacci_list = [1]

    months_total = n 
    months_elapsed = 0 
    f1 = 0

    while months_elapsed <= months_total: 
        rabbits_total = fibonacci_list[f1] + k
        fibonacci_list.append(rabbits_total)
        
        months_elapsed += 1
        f1 += 1 

    return max(fibonacci_list)
    
print("Total rabbits are:", fibonacci_rabbits(5,3))
    