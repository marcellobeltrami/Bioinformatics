#Calculate total mass of protein sequence in Da
def total_mass(aa_sequence):

    amino_acids = ["A","C","D","E","F","G","H",
                "I","K","L","M","N","P","Q",
                "R","S","T","V","W","Y"]

    aa_mass_Da = [71.03711,103.00919,115.02694,129.04259,
                147.06841,57.02146,137.05891,113.08406,
                128.09496,113.08406,131.04049,114.04293,
                97.05276,128.05858,156.10111,87.03203,
                101.04768,99.06841,186.07931,163.06333] 
    
    seq_list = list(aa_sequence)

    tot_mass = 0
    for i in seq_list: 
        ndx = amino_acids.index(i)

        tot_mass += aa_mass_Da[ndx]
    
    
    return round(tot_mass,3)

        

#Call function 
sequence = input("Amino acid sequence:")
print(total_mass(sequence))
