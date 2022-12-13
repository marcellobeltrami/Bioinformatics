from Bio import SeqIO

#Deals with files inputted 
sequence_filename1 = input("fasta1 file path:")
sequence_filename2 = input("fasta2 file path:")

print("Computing sequence 1....")
record1 = SeqIO.read(sequence_filename1, "fasta")
print("Done!")
print("Computing sequence 2....")
record2 = SeqIO.read(sequence_filename2, "fasta")
print("Done!")
sequence1 = list(record1)
sequence2 = list(record2)

counter = 0 
tot_nuc = len(sequence1)
print("Comparing sequences...")


#Calculates ANI
index_value = 0
for i in sequence1: 
    if i == sequence2[index_value]: 
        counter += 1
    else: 
        pass
    index_value += 1

ANI = (counter/tot_nuc)*100

print ("Your sequence identity value is: ", ANI, "%")

input_choice = input("Do you wanna continue (Y/N):")
