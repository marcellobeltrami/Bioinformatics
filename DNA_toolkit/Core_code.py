DNA_sequence = (input("Enter DNA sequence: "))

#Calculates GC content in a sequence
def GC_calculator (DNA_sequence):

    genetic_code_raw = DNA_sequence
    genetic_code1 = genetic_code_raw.upper()
    genetic_code = genetic_code1.replace(" ","")

    # Base count
    bases_dict = {"A":0, "T":0, "G":0, "C":0} 

    bases_dict["A"] = genetic_code.count("A")
    bases_dict["T"] = genetic_code.count("T")
    bases_dict["G"] = genetic_code.count("G")
    bases_dict["C"] = genetic_code.count("C")
    # Base calculation and addition to output dictionary
    output_dict = {"A":0, "T":0, "G":0, "C":0, "G+C":0}
    
    output_dict["A"] = float((bases_dict["A"] / len(genetic_code)))
    output_dict["T"] = float(bases_dict["T"] / len(genetic_code))
    output_dict["G"] = float(bases_dict["G"]/ len(genetic_code))
    output_dict["C"] = float(bases_dict["C"]/ len(genetic_code))
    output_dict["G+C"] = output_dict["G"] + output_dict["C"]

    # Outputs a G_C value (not multiplied by 100)

    return (output_dict["G+C"])


#Converts DNA sequence into RNA sequence

def mRNA(DNA):
    sequence = DNA
   

    split_sequence = list(sequence)  # input is split in single bases

    count = len(split_sequence)
    index_count = 0

    print_list = []  # paired bases are stored here

    while index_count < count:  # this loops matches and stores matched bases in an empty list
        position = split_sequence[index_count]
        if position == "A":
            print_list.append("U")
        elif position == "C":
            print_list.append("G")
        elif position == "G":
            print_list.append("C")
        elif position == "T":
            print_list.append("A")
        else:
            print_list.append("NO")

        index_count += 1  # th th

    return ("".join(print_list))

#Converts DNA sequence into aminoacid sequence

def aminoacids (DNA):
    sequence = DNA.upper()
    codon_list = ["ATT", "ATC", "ATA", "CGT", "CGC", "CGA", "CGG", "AGA", "AGG", "AAA", "AAG", "GAT", "GAC"
        , "GAA", "GAG", "CAT", "CAC", "AAT", "AAC", "CAA", "CAG"
        , "TGG", "TAT", "TAC", "TCT", "TCC", "TCA", "TCG", "AGT", "AGC", "ACT", "ACC",
                  "ACA", "ACG", "CCT", "CCC", "CCA", "CCG", "GGT", "GGC", "GGA", "GGG"
        , "TAA", "TAG", "TGA", "GCT", "GCC", "GCA", "GCG", "ATG", "TGT", "TGC", "TTT",
                  "TTC", "GTT", "GTC", "GTA", "GTG", "CTT", "CTC", "CTA", "CTG", "TTA", "ACG"
        , "TTG"]

    aa_list = ["I", "I", "I", "R", "R", "R", "R", "R", "R", "K", "K", "D", "D", "E", "E", "H", "H", "N", "N", "Q", "Q",
               "W", "Y", "Y", "S", "S", "S", "S", "S", "S", "T", "T", "T", "T", "P", "P", "P", "P", "G", "G", "G", "G",
               "*", "*", "*", "A", "A",
               "A", "A", "M", "C", "C", "F", "F", "V", "V", "V", "V", "L", "L", "L", "L", "L"
        , "L", "L"]

    #Splits string in codons
    codon_sequence = [sequence[i:i+3] for i in range(0, len(sequence), 3)]

    aminoacids = []

    for i in codon_sequence:
        in_list = codon_list.index(i)
        aminoacids.append(aa_list[in_list])

    return ("".join(aminoacids))

#Determines complimentary DNA sequence

def seq_comp (sequence_raw):
    sequence = sequence_raw.upper()
    split_sequence = list(sequence)  # input is split in single bases

    count = len(split_sequence)
    index_count = 0

    print_list = [] #paired bases are stored here

    while index_count < count: #this loops matches and stores matched bases in an empty list
        position = split_sequence[index_count]
        if position == "A":
            print_list.append("T")
        elif position == "C":
            print_list.append("G")
        elif position == "G":
            print_list.append("C")
        elif position == "T":
            print_list.append("A")
        else:
            print_list.append("NO")

        index_count += 1 

    return "".join(print_list)

#Calling functions
print(GC_calculator(DNA_sequence))
print("mRNA sequence:", mRNA(DNA_sequence))
print ("Aminoacid sequence",aminoacids(DNA_sequence))
print ("Complimentary sequence:", seq_comp(DNA_sequence))
