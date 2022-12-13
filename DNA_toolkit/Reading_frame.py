#Takes input sequence
sequence_raw = input("DNA sequence:")
sequence = sequence_raw.upper()
print("Computing....")

# Determine open reading frame found in RNA and convert it into aminoacid 
#Input DNA is taken

def start_finder(DNA_seq): 
    n = 3
    start_nuc = 0 
    last_nuc = 2
    Nucleotide_list = list(DNA_seq)
    for i in Nucleotide_list: 
        if start_nuc < len(DNA_seq): 
            my_list_2 = [DNA_seq[i:i+n] for i in range(start_nuc, len(DNA_seq), n)]
            #Upon match reading frame is printed
            if my_list_2[0] == "AUG" or "ATG": 
                return  "".join(my_list_2)
                break
            
            else: 
                start_nuc += 1
                last_nuc  +=1
        else: 
            return "Checked, no starting codon found!"
#Takes a  sequence and finds the stop codon
def stop_finder(DNA_seq):
    started_sequence = start_finder(DNA_seq)
    #Determines codon sequence from started one
    codon_sequence = [started_sequence[i:i+3] for i in range(0, len(started_sequence),3)]
    ORF = []
    #Finds the stop codon 
    for i in codon_sequence: 
        if i != "TAG" or "TAA" or "TGA": 
            ORF.append(i)
        
        else:
            break

        break
    return "".join(ORF) 

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
                "stop", "stop", "stop", "A", "A",
                "A", "A", "M", "C", "C", "F", "F", "V", "V", "V", "V", "L", "L", "L", "L", "L"
        , "L", "L"]

    #Splits string in codons
    codon_sequence = [sequence[i:i+3] for i in range(0, len(sequence), 3)]

    aminoacids = []

    for i in codon_sequence:
        in_list = codon_list.index(i)
        aminoacids.append(aa_list[in_list])

    return ("".join(aminoacids))

# Lines in a file put in list and merged together
DNA_seq_lis = []
for line in sequence: 
    DNA_seq_lis.append(line.strip()) 
DNA_sequence = "".join(DNA_seq_lis)

Index_2 = 1
Index_3 = 2
ORF = stop_finder(DNA_sequence)

#Functions are called
print ("Your reading frame is: ", ORF )

print ("Aminoacid sequence is: ", "".join(aminoacids(ORF)))
print("Done!")

