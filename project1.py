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

    print(species_list)
    print(sex_list)
    return species_list, sex_list





data = read_penguin_data(csv_path)
average_body_mass_by_species_and_sex(data)

