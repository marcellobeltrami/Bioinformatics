#This script requires Biopython dependecy installed to work
import re
from Bio import SeqIO

# define the sequence of the plasmid
plasmid_path = input(r"Copy and paste path to .fasta file with multiple sequences in it:")
plasmid_sequences = SeqIO.parse(plasmid_path,'fasta')
print(plasmid_sequences)

# define the recognition site for the restriction enzymes in a list. Make sure each site sequence is on a new line.
def sites_list(file_path):
    recognition_site = open(file_path, "r")
    sites_list = recognition_site.readlines()
    processed_list = []
    for site in sites_list:  
        processed_list.append(site.strip("/n"))
    return processed_list

cutting_sites = sites_list(input(r"Copy and paste path to .txt file with all restriction sites in a list:"))
# use a regular expression to find all occurrences of the recognition site in the sequence
for file in plasmid_sequences:
        for recognition_site in  cutting_sites: 
            matches = re.finditer(recognition_site, plasmid_sequences)
            print ("chekc")

    # print the start and end indices of each match
        for match in matches:
            start = match.start()
            end = match.end()
            print(f"Found match at nucleotides: {start}-{end}")


