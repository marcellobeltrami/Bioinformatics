
# Function to load country, ID, sequence records from a file into a list of lists
# Input - FileName (string) of the file contrains the records
# Ouput - a list of records
# Errors are not checked for, file is expected to be in the correct format. 
def LoadRecords(FileName):

	# The list of sequence records to reutrn 
	RecordList = []

	FIn = open(FileName, "r")

	# Read file line by line, to save memory. 
	for Line in FIn:
		# Tokenize the file line on white space. 
		# Record elements cannot contain white space.
		# Elemts in order are, the country code, unique ID, sequnce		
		Tokens = Line.split()

		# Save the current record at the end of RecordList
		RecordList.append(Tokens)
	
	FIn.close()

	return RecordList


# Function to load the frist seuqnce from a data file
# Format is is the same as for LoadRecords
# Input - FileName (string) of the file contrains the records
# Ouput - the seuquence (string) 
# Errors are not checked for, one records is expected
def LoadSingleSequence(FileName):
	
	# Load All records, eventhough only the first is needed
	RecordData = LoadRecords(FileName)
	
	# only return the seqince from the first record. 
	return RecordData[0][2]

# Load all records from "Human-Covid19.txt" into a list of list, called Records
Records = LoadRecords("Human-Covid19.txt")

# Load only the Bat sequnce into a string, BatSeq
BatSeq = LoadSingleSequence("Bat-Covid19.txt")

#(1)Calculates distance between 2 inputted sequences
def SequenceDistance(Bat_sequence, Human_sequence):
	Bat_nuc = list(Bat_sequence)
	Hum_nuc = list(Human_sequence)
	Sequence_sim = 0
	index = 0
	Human_len = len(Hum_nuc)
	Bat_len = len(Bat_nuc)

	if Bat_len != Human_len: 
		print("Sequences are not aligned!")
	
	for nuc in Bat_nuc: 
		if nuc == Hum_nuc[index] and index <= Human_len: 
			Sequence_sim += 1
		index += 1 
	
	Distance_calculator = 1-(Sequence_sim/Bat_len)
	
	return Distance_calculator

#(2b) Find closest record
def FindClosestRecord(Query_seq, record_list):
	dist_record = []
	pure_distances = [] 

	#Finds calculate distances and associates them to relative records
	for sequence in record_list:
		prov_list = []
		Count_ID = sequence[0] 
		Unique_ID = sequence [1]
		distance =SequenceDistance(Query_seq,sequence[2]) 
		prov_list.append(Count_ID)
		prov_list.append(Unique_ID)
		prov_list.append(distance)
		dist_record.append(prov_list)
		pure_distances.append(distance)
	
	#Finds and returns closest record
	lowest_value = min(pure_distances)
	for closest in dist_record: 
		if lowest_value ==  closest[2]:
			return closest

#(3a)Filters countries and associated data based on 3 letter ID  
def FilterByCountry(list_records, Country_ID ): 
	filtered_list= []

	for record in list_records: 
		if record[0] == Country_ID:
			filtered_list.append(record)
	
	return filtered_list

#(3b) Determines closest related strains between two countries target
def PrintTransmitter(list_records, Origin_ID, Target_ID):
	#Filters countries
	Origin_country = FilterByCountry(list_records, Origin_ID)
	Target_country = FilterByCountry(list_records, Target_ID)

	Fused_lists = []
	distances_values = []
	index_target = 0

	#Loop creates a list of lists containig 2 sequences records (minus sequences) and calculates distance
	for Or_seq in Origin_country:
		Closest_record = list(FindClosestRecord(Or_seq[2], Target_country))
		Closest_record.append(Or_seq[0])
		Closest_record.append(Or_seq[1])
		Fused_lists.append(Closest_record)
		distances_values.append(Closest_record[2])

		print("Sequence",index_target,"compared")
		index_target += 1 

	lowest_value = min(distances_values)

	for records in Fused_lists: 
		if lowest_value == records[2]:
			print (records[3], records[4], records[0], records[1],records[2] )		


#Loops over records file and prints all distances with labels. 
PrintTransmitter(Records, "EST", "UZB")
	