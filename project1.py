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

        if species not in species_list and species != "":
            species_list.append(species)
        if sex not in sex_list and sex not in ('', 'NA', 'na', None):
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

# writing results into a csv
def write_results_to_csv(data, filename):
    average_body_mass = average_body_mass_by_species_and_sex(data)
    correlation_result = correlation_flipper_bill_length(data)

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

    #average body mass
        writer.writerow(['Average Body Mass by Species and Sex'])
        writer.writerow(['Species', 'Sex', 'Average Body Mass (g)'])
        for species in average_body_mass:
            for sex in average_body_mass[species]:
                writer.writerow([species, sex, average_body_mass[species][sex]])

    #empty row between two sections, figure out later

    # average flipper and bill length
        writer.writerow(['Average Flipper Length and Bill Length by Species'])
        writer.writerow(['Species', 'Average Flipper Length (mm)', 'Average Bill Length (mm)'])
        for species in correlation_result:
            writer.writerow([species, f"{correlation_result[species][0]:.2f}", f"{correlation_result[species][1]:.2f}"])




# main function to run all calculations and write to csv
data = read_penguin_data(csv_path)
average_body_mass_by_species_and_sex(data)
correlation_result = correlation_flipper_bill_length(data)
write_results_to_csv(data, 'penguin_analysis_results.csv')
print("Results written to penguin_analysis_results.csv")

# test cases
test_data = [
    {"species": "Adelie", "sex": "male", "body_mass_g": "4000", "flipper_length_mm": "190", "bill_length_mm": "38.5"},
    {"species": "Adelie", "sex": "female", "body_mass_g": "3500", "flipper_length_mm": "186", "bill_length_mm": "36.8"},
    {"species": "Gentoo", "sex": "male", "body_mass_g": "5485", "flipper_length_mm": "217", "bill_length_mm": "47.5"},
    {"species": "Gentoo", "sex": "female", "body_mass_g": "4680", "flipper_length_mm": "215", "bill_length_mm": "46.8"},
    {"species": "Chinstrap", "sex": "male", "body_mass_g": "3940", "flipper_length_mm": "196", "bill_length_mm": "48.8"},
    {"species": "Chinstrap", "sex": "female", "body_mass_g": "3527", "flipper_length_mm": "195", "bill_length_mm": "48.5"},
   
    # edge cases:
    {"species": "Adelie", "sex": "NA", "body_mass_g": "NA", "flipper_length_mm": "", "bill_length_mm": ""},
    {"species": "", "sex": "female", "body_mass_g": "3900", "flipper_length_mm": "200", "bill_length_mm": "40"},
]

print("\n---Test Cases---")

#test for read_penguin_data()
print("read_penguin_data() - not tested since its using file input")

#test for filter_by_species()
print('filter_by_species() general case:', filter_by_species(test_data, "Adelie"))
print('filter_by_species() edge case (no match):', filter_by_species(test_data, "Nonexistent"))

#test for average_body_mass_by_species_and_sex()
print('average_body_mass_by_species_and_sex() general case:', average_body_mass_by_species_and_sex(test_data))
print('average_body_mass_by_species_and_sex() edge case (no match):', average_body_mass_by_species_and_sex(test_data))

#test for correlation_flipper_bill_length()
print('correlation_flipper_bill_length() general case:', correlation_flipper_bill_length(test_data))
print('correlation_flipper_bill_length() edge case (no match):', correlation_flipper_bill_length(test_data))

#test for write_results_to_csv()
print('write_results_to_csv() general case (check output file):')
write_results_to_csv(test_data, 'test_output.csv')
print('test_output.csv file created successfully.')
