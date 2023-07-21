from Bio import SeqIO
import re



##change file location with a variable based of user location
out_res = open("Results.txt", "w")

def basic_stats(sequence): 
    
    # Bases distribution count
    Seq_lis = list(sequence)
    a,c,t,g = 0,0,0,0

    for base in Seq_lis:
        #Check A and C 
        if base == "A" or "C": 
            if base == "A": 
                a += 1
            if base == "C": 
                c += 1
        #Check A and C 
        if base == "T" or "G": 
            if base == "T": 
                t += 1
            if base == "G": 
                g += 1

    GC_content = ((g+c)/len(sequence)) * 100  

    
    print ("A:", a, file= out_res)
    print ("G:", g, file= out_res)
    print ("T:", t, file= out_res)
    print ("C:", c, file= out_res)
    print ("GC content: ", "{:.2f}".format(GC_content), "%", file= out_res)

# DNA-> mRNA
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




    
#Translate sequence
def translate_sequence(dna_sequence, start_pos, end_pos):
    codon_table = {
        "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
        "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
        "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
        "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
        "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
        "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "TAT": "Y", "TAC": "Y", "TAA": "*", "TAG": "*",
        "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
        "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
        "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
        "TGT": "C", "TGC": "C", "TGA": "*", "TGG": "W",
        "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
        "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",
        "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"
    }

    translated_sequence = ""
    codon = ""

    for i in range(start_pos, end_pos + 1, 3):
        codon = dna_sequence[i:i + 3]
        if codon in codon_table:
            translated_sequence += codon_table[codon]
        else:
            translated_sequence += "X"  # Placeholder for unknown codons

    return translated_sequence

# Search motif in DNA seq, uses re module
def find_motif(sequence, motif):
    matches = re.finditer(motif, sequence)
    motif_positions = [match.start() + 1 for match in matches]  # Adding 1 to start positions for 1-based indexing
    return motif_positions


#input and file handling
file_name = input(r"File path with all your fasta sequences:")

print("Analysis running....")
print ("------------------------------------------")

#Call functions and use cases
for record in SeqIO.parse(file_name, "fasta"):
    print(record.id)
    Seq = record.seq

    #Determine reading frame 
    
    basic_stats(Seq)
    print ("Basic stats check")

    

    #Find open reading frames 
    pattern = r"(?<=ATG)(?:(?!TAA|TAG|TGA)...)*(?=TAA|TAG|TGA)"
    open_reading_frames = re.findall(pattern, str(Seq))
    print(open_reading_frames, file=out_res)

    print ("Reading frames check")

    print("mRNA: ", mRNA(Seq), file= out_res)
    print ("mRNA check")
    
    print("-------------------------------------------")