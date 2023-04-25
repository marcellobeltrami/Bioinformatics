def Base_perc(sequence):
    genetic_code_raw = sequence
    genetic_code = list(genetic_code_raw.upper())

    # Base countpython
    A_base = int(genetic_code.count("A"))
    C_base = int(genetic_code.count("C"))
    T_base = int(genetic_code.count("T"))
    G_base = int(genetic_code.count("G"))
    Total = int(len(genetic_code))

    # Base calculation
    A = str(round((A_base / Total)*100))
    C = str(round((C_base / Total)*100))
    T = str(round((T_base / Total)*100))
    G = str(round((G_base / Total)*100))
    G_C = ((C_base / Total)*100) + ((G_base / Total)*100)
    

    # Output
    #print("A: " + A + " %")
    #print("C: " + C + " %")
    #print("T: " + T + " %")
    #print("G: " + G + " %")
    #print("G-C: " + G_C + " %")
    #print("A-T: " + A_T + " %")
    return G_C


    