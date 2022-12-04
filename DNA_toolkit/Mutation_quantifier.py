
#Determines mutation in 2 DNA strings of same length 

DNA_1 = list("ACTACGTAGAACCACCACAACA")
DNA_2 = list("ACCGCGCTTAATCGGCCCAGGC")

tracker = 0
H_value = 0

for i in DNA_1: 
    if i != DNA_2[tracker]: 
        H_value += 1 

    else: 
        pass
    tracker += 1

print(H_value)