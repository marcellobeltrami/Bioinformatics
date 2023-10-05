def Bases_count(DNA): 
    bases = {"A":0, "T":0, "G":0, "C":0} 

    bases["A"] = DNA.count("A")
    bases["T"] = DNA.count("T")
    bases["G"] = DNA.count("G")
    bases["C"] = DNA.count("C")
    return bases


def Base_perc(sequence):
    genetic_code_raw = sequence
    genetic_code = list(genetic_code_raw.upper())

    # Base countpython
    bases_dict = Bases_count(sequence)

    output_dict = {"A":0, "T":0, "G":0, "C":0, "G+C":0}
    # Base calculation and addition to output dictionary
    output_dict["A"] = float((bases_dict["A"] / Total)
    output_dict["T"] = float(bases_dict["T"] / Total)
    output_dict["G"] = float(bases_dict["G"]/ Total)
    output_dict["C"] = float((bases_dict["C"]/ Total)
    output_dict["G+C"] = output_dict["G"] + output_dict["C"]

    

    # Outputs a dictionary with values for each base. 
    #print("A: " + A + " %")
    #print("C: " + C + " %")
    #print("T: " + T + " %")
    #print("G: " + G + " %")

    return percentage_dict


    
