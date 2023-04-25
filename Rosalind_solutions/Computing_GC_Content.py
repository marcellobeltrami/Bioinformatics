from Bio import SeqIO


def GC_comparator(fasta_file):
    Fasta_sequences = []

    for record in SeqIO.parse(fasta_file, "fasta"):
        Fasta_sequences.append(record.id)
        Fasta_sequences.append(record.seq)

    index_id = 0
    index_seq = 1

    GC_list = []
    highest_value = 0

    while index_seq < len(Fasta_sequences): 
        GC_list.append(Fasta_sequences[index_id])
    
        nucleotides = list(Fasta_sequences[index_seq])
        GC_counter = 0
        for base in nucleotides: 
            if base == "C":
                GC_counter += 1
            if base == "G": 
                GC_counter += 1
            
        GC_percentage = (GC_counter/len(nucleotides))*100
        
        if GC_percentage > highest_value: 
            highest_value = GC_percentage

        GC_list.append(GC_percentage)

        index_id += 2
        index_seq += 2

    highest_index = GC_list.index(highest_value)

    highest_ID = GC_list[(highest_index-1)]

    #prints to console highest GC content value
    print (highest_ID, highest_value)

GC_comparator(#insert file name
    )