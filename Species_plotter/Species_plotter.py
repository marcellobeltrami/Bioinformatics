# REFERENCES
# https://note.nkmk.me/en/python-list-clear-pop-remove-del/ [Accessed: 01/03/2022 ]
# https://realpython.com/python-sets/ [Accessed: 06/03/2022]

import math
# Calculates distance given two sets of coordinates
def CalculateDistance(Lat1, Lon1, Lat2, Lon2):
    Lat1 = float(Lat1)
    Lon1 = float(Lon1)
    Lat2 = float(Lat2)
    Lon2 = float(Lon2)
    nDLat = (Lat1 - Lat2) * 0.017453293
    nDLon = (Lon1 - Lon2) * 0.017453293
    Lat1 = Lat1 * 0.017453293
    Lat2 = Lat2 * 0.017453293
    nA = (math.sin(nDLat / 2) ** 2) + math.cos(Lat1) * math.cos(Lat2) * (math.sin(nDLon / 2) ** 2)
    nC = 2 * math.atan2(math.sqrt(nA), math.sqrt(1 - nA))
    nD = 6372.797 * nC
    return nD

# LineToList takes a string and converts it to a list breaking it on the tabs (\t).New lines are removed.
def LineToList(Str):
    Str = Str.rstrip()
    return Str.split("\t")

# Converts name, longitude and latitude to single elements in a list
def SeparedList (file_list):
    separed_list = []
    for line in file_list: # loops over file list removing \t for each element in file_list.
        ln_to_list = LineToList(line)
        separed_list.append(ln_to_list)
    return separed_list

# Calculates distance between a given point and the animals´coordinates
def DistancesList(list_len, sep_list, lat0, long0):
    pos_counter = 0
    dist_list = []
    # This loop accesses long and lat in list and calculates distance from a input to animal in list
    while pos_counter < list_len:
        lat2 = sep_list[pos_counter][1]
        long2 = sep_list[pos_counter][2]
        pos_counter += 1
        Calc_dist = CalculateDistance(lat0, long0, lat2, long2)
        dist_list.append(Calc_dist)
    return dist_list

# Returns which animals (name and coordinates) are found within the range between two coordinate points.
def DistanceSelection (list_len, sep_list, lat0, long0, distance_provided):
    pos_counter = 0
    selection_list = []
    # This loop accesses longitude and latitude in list and determines which animals are found within the distance
    # provided.
    while pos_counter < list_len:
        name = sep_list[pos_counter][0]
        lat2 = sep_list[pos_counter][1]
        long2 = sep_list[pos_counter][2]
        pos_counter += 1
        Calc_dist = CalculateDistance(lat0, long0, lat2, long2)
        if Calc_dist < distance_provided:
            selection_list.append(name)
            selection_list.append(lat2)
            selection_list.append(long2)
    return selection_list

# (Part 1 function) Returns number of animals found within a specified distance of a given location
def LocationCount(txt_file1, dist_km1, lat1, long1):
    file_open = open(txt_file1, "r")
    file_list= file_open.readlines() # Load from file to list (called file_list)
    list1 = SeparedList(file_list) # Returns list without names, only longitude and latitude.
    list1_len = len(list1)
    distance_list = DistancesList(list1_len,list1, lat1, long1) # Returns list of distances from animal and point provided
    # This loop compares the calculated distance with the distance provided as argument in function. +1 to counter
    # if animal is within distance range, pass if animal is outside distance range.
    animal_counter = 0
    for distance in distance_list:
        if distance < dist_km1:
            animal_counter += 1
        else :
            pass
    file_open.close()
    return animal_counter

# (Part 2 function) Returns a .kml document containing position of animal in distance range.
def PrintLocation (txt_file2, dist_km2, lat2, long2):
    # File is open, all lines are read, and list items are count
    file_open =  open(txt_file2, "r")
    file_list= file_open.readlines()
    list1 = SeparedList(file_list)
    list1_len = len(list1)
    kml_open = open("Output.kml", "w")
    # Selects animal in range provided based on coordinates
    selected_list = DistanceSelection(list1_len, list1, lat2, long2, dist_km2)
    # .kml structure is printed to "Output.kml" for only the animals found in selected_list by looping over the list
    # with a step of 3 for each name, latitude and longitude.
    sel_len = len(selected_list)
    print("<Document>", file = kml_open)
    index_n = 0
    index_lat = 2
    index_lon = 1
    while index_lat < sel_len:
        print("<Placemark>","\n",
              "<description>", selected_list[index_n], "</description>", "\n","<Point>",
              "\n", "<coordinates>", selected_list[index_lat] , ",", selected_list[index_lon],"</coordinates>",
              "\n", "</Point>", "\n", "</Placemark>", file = kml_open)
        index_n += 3
        index_lon += 3
        index_lat += 3
    print("</Document>", file = kml_open)
    print("Output.kml: check")
    file_open.close()
    kml_open.close()

# (Part 3 function) Returns the amount of unique species found within a specified distance from a given location.
def BiodiversityCount (txt_file3, dist_km3, lat3, long3):
    # File is open, all lines are read, list of single items is created and list items are count. Dist_selec determines
    # animals found within the distance range "dist_km3"
    file_open = open(txt_file3, "r")
    file_list= file_open.readlines()
    Sep_list = SeparedList(file_list)
    file_list_len = len(file_list)
    Dist_selec = DistanceSelection(file_list_len, Sep_list, lat3, long3, dist_km3)
    dist_list_len = len(Dist_selec)
    # Takes names of species found within distance range and adds them to a list (Names_in_list)
    Names_in_list = []
    indexBC = 0
    counter = 2
    while counter < dist_list_len:
        Names_in_list.append(Dist_selec[indexBC])
        counter += 3
        indexBC += 3
    # set() removes duplicates and list length is counted
    Names_set = set(Names_in_list)
    Unique_count = len(Names_set)
    file_open.close()
    return Unique_count

# Functions called for Part 1,2,3.
coordinates_file = input("File path containing names and coordinates:")
latitude = float(input("Input latitude value:"))
longitude = float(input("Input longitude value:"))
km_of_area = float(input("Input are size in km value:"))

print("Animal count: ", LocationCount(coordinates_file, km_of_area, latitude, longitude))
PrintLocation( coordinates_file, km_of_area, latitude, longitude)
print("Unique species: ", BiodiversityCount(coordinates_file, km_of_area, latitude, longitude))