### Name: April Xiao 
### Email: aprilx@umich.edu
### uniqname: apr1lx
### Course: Fall 2025 - SI 201
import csv 
import math 

def read_penguin_data(csv_file):
    data = []
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    print(data)
    return data
