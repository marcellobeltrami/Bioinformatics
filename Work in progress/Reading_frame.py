# Coding open reading frame found in RNA and convert it into aminoacid 
#Input DNA is taken
def frame_reader(DNA_seq): 
    n = 3
    start_nuc = 0 
    last_nuc = 2
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
            print ("Checked")
def aminoacids (DNA):
    sequence = DNA.upper()
    Seq_len = len(sequence)

    codon_list = ["ATT", "ATC", "ATA", "CGT", "CGC", "CGA", "CGG", "AGA", "AGG", "AAA", "AAG", "GAT", "GAC"
        , "GAA", "GAG", "CAT", "CAC", "AAT", "AAC", "CAA", "CAG"
        , "TGG", "TAT", "TAC", "TCT", "TCC", "TCA", "TCG", "AGT", "AGC", "ACT", "ACC",
                  "ACA", "ACG", "CCT", "CCC", "CCA", "CCG", "GGT", "GGC", "GGA", "GGG"
        , "TAA", "TAG", "TGA", "GCT", "GCC", "GCA", "GCG", "ATG", "TGT", "TGC", "TTT",
                  "TTC", "GTT", "GTC", "GTA", "GTG", "CTT", "CTC", "CTA", "CTG", "TTA", "ACG"
        , "TTG", ""]

    aa_list = ["I", "I", "I", "R", "R", "R", "R", "R", "R", "K", "K", "D", "D", "E", "E", "H", "H", "N", "N", "Q", "Q",
               "W", "Y", "Y", "S", "S", "S", "S", "S", "S", "T", "T", "T", "T", "P", "P", "P", "P", "G", "G", "G", "G",
               "*", "*", "*", "A", "A",
               "A", "A", "M", "C", "C", "F", "F", "V", "V", "V", "V", "L", "L", "L", "L", "L"
        , "L"]

    index = 0
    index_1 = 3

    codon_sequence = []

    print_aa_list = []

    while index < Seq_len:
        Subs = slice(index, index_1)
        xy = sequence[Subs]
        codon_sequence.append(xy)
        index += 3
        index_1 += 3

    count = len(codon_sequence)
    index_count = 0

    while index_count < count:
        position = codon_sequence[index_count]
        in_list = codon_list.index(position)
        aminoacid = print_aa_list.append(aa_list[in_list])

        index_count += 1

    return (print_aa_list)
results = open("ORF_output.txt","w")

#Open input and output files
results = open("ORF_output.txt","w")
seq_filename = input("File path:")
file_open  = open(seq_filename, "r")
print("Computing....")

# Lines in a file put in list and merged together
DNA_seq_lis_raw = file_open.readlines()
DNA_seq_lis = []
for line in DNA_seq_lis_raw: 
    DNA_seq_lis.append(line.strip()) 
DNA_sequence = "".join(DNA_seq_lis)
Nucleotide_list = list(DNA_sequence)
Index_2 = 1
Index_3 = 2
ORF = frame_reader(DNA_sequence)

#Functions are called
print ("Your reading frame is: ", ORF ,file=results)

print ("Aminoacid sequence is: ", "".join(aminoacids(ORF)), file=results)
print("Done!")
