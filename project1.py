### Name: April Xiao 
### Email: aprilx@umich.edu
### uniqname: apr1lx
### Course: Fall 2025 - SI 201
import csv 
import math 
csv_path = 'penguins.csv'

def read_penguin_data(csv_file):
    data = []
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    #print(data)
    return data

def filter_by_species(data, species):
    filtered = []
    for row in data:
        if row.get("species") == species:
            filtered.append(row)
    return filtered

### calculation #1: Average Body Mass by Species and Sex
def average_body_mass_by_species_and_sex(data):
    species_list = []
    sex_list = []
    for row in data:
        species = row.get("species")
        sex = row.get("sex")
        if species not in species_list:
            species_list.append(species)
        if sex not in sex_list:
            sex_list.append(sex)

    #print(species_list)
    ##print(sex_list)
    

    result = {}
    for species in species_list:
        result[species] = {}
        for sex in sex_list:
            total_mass = 0
            count = 0
            for row in data:
                if row.get("species") == species and row.get("sex") == sex:
                    body_mass = row.get("body_mass_g")
                    if body_mass and body_mass not in ('', 'NA', 'na', None):
                        try:
                            total_mass += float(body_mass)
                            count += 1
                        except:
                            pass
            if count > 0:
                average_mass = total_mass / count
                result[species][sex] = average_mass
    print(result)
    return result

### calculation #2: correlation between flipper_length_mm and bill_length_mm
def correlation_flipper_bill_length(data):
    # getting unique species
    species_list = []
    for row in data:
        species = row.get("species")
        if species not in species_list and species != "":
            species_list.append(species)

# calculating averages for each species
    result = {}
    for species in species_list:
        total_flipper_length = 0
        total_bill_length = 0
        count = 0

        for row in data:
            if row.get("species") == species:
                flipper_length = row.get("flipper_length_mm")
                bill_length = row.get("bill_length_mm")

            #skipping empty values 
                if flipper_length and bill_length and flipper_length not in ('', 'NA', 'na', None) and bill_length not in ('', 'NA', 'na', None):
                    try:
                        total_flipper_length += float(flipper_length)
                        total_bill_length += float(bill_length)
                        count += 1
                    except:
                        pass
        if count > 0:
            avg_flipper_length = total_flipper_length / count
            avg_bill_length = total_bill_length / count
            result[species] = (avg_flipper_length, avg_bill_length)

    #printing results, more readable 
        print("Average Flipper Length and Bill Length by Species:")
        for species in result:
            print(f"{species}: Flipper Length = {result[species][0]:.2f} mm, Bill Length = {result[species][1]:.2f} mm")
        return result









data = read_penguin_data(csv_path)
average_body_mass_by_species_and_sex(data)
correlation_result = correlation_flipper_bill_length(data)

