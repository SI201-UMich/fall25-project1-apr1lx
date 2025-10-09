### SI 201 Project 1
### Name: April Xiao 
### Email: aprilx@umich.edu
### uniqname: apr1lx
### student ID: 0934 9568
### I worked alone, I used AI to help me debug and to help me form an organized structure to my code
import csv 
import math 
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, 'penguins.csv')


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
        species_averages = {}
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
                species_averages[sex] = average_mass

        if species_averages:
            result[species] = species_averages

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
        writer.writerow([])

    # average flipper and bill length
        writer.writerow(['Average Flipper Length and Bill Length by Species'])
        writer.writerow(['Species', 'Average Flipper Length (mm)', 'Average Bill Length (mm)'])
        for species in correlation_result:
            writer.writerow([species, f"{correlation_result[species][0]:.2f}", f"{correlation_result[species][1]:.2f}"])



# main function to run all calculations and write to csv
if __name__ == "__main__":
    try:
        data = read_penguin_data(csv_path)
        average_body_mass_by_species_and_sex(data)
        correlation_result = correlation_flipper_bill_length(data)
        output_path = os.path.join(BASE_DIR, 'penguin_analysis_results.csv')
        write_results_to_csv(data, output_path)
        print(f"Results written to: {output_path}")
    except FileNotFoundError:
        print(f"penguins.csv not found at:", csv_path)






# test cases
import unittest

class TestPenguinDataFunctions(unittest.TestCase):

    def setUp(self):
        self.sample = [
            {"species": "Adelie", "sex": "male",   "body_mass_g": "4000",
             "flipper_length_mm": "190", "bill_length_mm": "38.5"},
            {"species": "Adelie", "sex": "female", "body_mass_g": "3500",
             "flipper_length_mm": "186", "bill_length_mm": "36.8"},
            {"species": "Gentoo", "sex": "male",   "body_mass_g": "5485",
             "flipper_length_mm": "217", "bill_length_mm": "47.5"},
            {"species": "Gentoo", "sex": "female", "body_mass_g": "4680",
             "flipper_length_mm": "215", "bill_length_mm": "46.8"},
            {"species": "Chinstrap", "sex": "male","body_mass_g": "3940",
             "flipper_length_mm": "196", "bill_length_mm": "48.8"},
            {"species": "Chinstrap", "sex": "female","body_mass_g": "3527",
             "flipper_length_mm": "195", "bill_length_mm": "48.5"},
            # edge rows to be skipped/ignored
            {"species": "Gentoo", "sex": "female", "body_mass_g": "NA",
             "flipper_length_mm": "NA", "bill_length_mm": ""},
            {"species": "", "sex": "female", "body_mass_g": "3900",
             "flipper_length_mm": "200", "bill_length_mm": "40"},
        ]

    #tests for average body mass by species and sex 
    def test_average_body_mass_by_species_and_sex_1(self):
        """General: Adelie averages computed correctly"""
        avg = average_body_mass_by_species_and_sex(self.sample)
        self.assertAlmostEqual(avg["Adelie"]["male"], 4000.0, places=2)
        self.assertAlmostEqual(avg["Adelie"]["female"], 3500.0, places=2)

    def test_average_body_mass_by_species_and_sex_2(self):
        """General: Gentoo averages computed correctly (ignore NA row)"""
        avg = average_body_mass_by_species_and_sex(self.sample)
        self.assertAlmostEqual(avg["Gentoo"]["male"], 5485.0, places=2)
        self.assertAlmostEqual(avg["Gentoo"]["female"], 4680.0, places=2)

    def test_average_body_mass_by_species_and_sex_3(self):
        """Edge: 'NA' sex key should not be included"""
        avg = average_body_mass_by_species_and_sex(self.sample)
        self.assertNotIn("NA", avg.get("Adelie", {}))

    def test_average_body_mass_by_species_and_sex_4(self):
        """Edge: all invalid rows produce empty dict"""
        data = [{"species": "Adelie", "sex": "male", "body_mass_g": "NA"}]
        self.assertEqual(average_body_mass_by_species_and_sex(data), {}) 

    #tests for correlation between flipper length and bill length  
    def test_correlation_flipper_bill_length_1(self):
        """General: returns tuple (avg_flipper, avg_bill) per species"""
        res = correlation_flipper_bill_length(self.sample)
        self.assertIn("Adelie", res)
        self.assertEqual(len(res["Adelie"]), 2)

    def test_correlation_flipper_bill_length_2(self):
        """General: Adelie averages are the mean of the two valid rows"""
        res = correlation_flipper_bill_length(self.sample)
        # Adelie: flipper (190,186) -> 188.0 ; bill (38.5,36.8) -> 37.65
        self.assertAlmostEqual(res["Adelie"][0], 188.0, places=2)
        self.assertAlmostEqual(res["Adelie"][1], 37.65, places=2)

    def test_correlation_flipper_bill_length_3(self):
        """Edge: NA/blanks ignored; Gentoo averages > sensible thresholds"""
        res = correlation_flipper_bill_length(self.sample)
        self.assertGreater(res["Gentoo"][0], 200.0)  # flipper
        self.assertGreater(res["Gentoo"][1], 40.0)   # bill

    def test_correlation_flipper_bill_length_4(self):
        """Edge: species with only invalid numeric values is excluded"""
        bad = [{"species": "Adelie", "flipper_length_mm": "", "bill_length_mm": ""}]
        res = correlation_flipper_bill_length(bad)
        self.assertNotIn("Adelie", res)

    #test for filer by species
    def test_filter_by_species_1(self):
        """General: returns only Adelie rows"""
        rows = filter_by_species(self.sample, "Adelie")
        self.assertTrue(all(r["species"] == "Adelie" for r in rows))
        self.assertGreaterEqual(len(rows), 2)

    def test_filter_by_species_2(self):
        """General: returns only Gentoo rows"""
        rows = filter_by_species(self.sample, "Gentoo")
        self.assertTrue(all(r["species"] == "Gentoo" for r in rows))

    def test_filter_by_species_3(self):
        """Edge: nonexistent species returns empty list"""
        self.assertEqual(filter_by_species(self.sample, "Nonexistent"), [])

    def test_filter_by_species_4(self):
        """Edge: blank species filter should not match normal species"""
        rows = filter_by_species(self.sample, "")
        self.assertTrue(all(r["species"] == "" for r in rows))

    #test for write results to csv
    def test_write_results_to_csv_general(self):
        """General: file is created in BASE_DIR and has both section headers"""
        out_path = os.path.join(BASE_DIR, "tmp_results.csv")
        try:
            write_results_to_csv(self.sample, out_path)
            self.assertTrue(os.path.exists(out_path))
            with open(out_path, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertIn("Average Body Mass by Species and Sex", content)
            self.assertIn("Average Flipper Length and Bill Length by Species", content)
        finally:
            if os.path.exists(out_path):
                os.remove(out_path)

    def test_write_results_to_csv_empty_input(self):
        """Edge: empty input still creates file with headers"""
        out_path = os.path.join(BASE_DIR, "tmp_results_empty.csv")
        try:
            write_results_to_csv([], out_path)
            self.assertTrue(os.path.exists(out_path))
            with open(out_path, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertIn("Average Body Mass by Species and Sex", content)
            self.assertIn("Average Flipper Length and Bill Length by Species", content)
        finally:
            if os.path.exists(out_path):
                os.remove(out_path)


if __name__ == "__main__":
    unittest.main()