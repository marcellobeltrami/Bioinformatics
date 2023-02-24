#This script requires Biopython dependecy installed to work
import re
from Bio import SeqIO

# define the sequence of the plasmid 
plasmid_path = input(r"Copy and paste path to .fasta file with multiple sequences in it:")
plasmid_sequence = SeqIO.read(plasmid_path,'fasta')
print(plasmid_sequence)

# define the recognition site for the restriction enzymes in a list. Make sure each site sequence is on a new line.
def sites_list(file_path):
    recognition_site = open(file_path, "r")
    sites_list = recognition_site.readlines()
    res = []
    for sub in sites_list:
        res.append(re.sub('\n', '', sub))
    return res

cutting_sites = sites_list(input(r"Copy and paste path to .txt file with all restriction sites in a list:"))
# use a regular expression to find all occurrences of the recognition site in the sequence
print(cutting_sites)
for re_site in cutting_sites: 
    matches = re.finditer(str(re_site), str(plasmid_sequence))
    print (matches)

# print the start and end indices of each match (BUG does not iterate)
for match in matches:
    start = match.start()
    end = match.end()
    print (start)

    print(f"Found match at nucleotides: {start}-{end}")


