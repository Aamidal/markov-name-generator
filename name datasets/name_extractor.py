#name_extractor.py
import os
import csv

"""To pull names from the worldcities.csv, insert a list of ISO 2 codes in quotes
separated by a comma"""
countries = ['UZ', 'QA', 'ZW']
filename = ' '.join(countries) #Names file after the countries input.


# specifiying file path
script_dir = os.path.dirname(__file__)
rel_path = "libs\worldcities.csv"
save_path = f'libs\{filename}.txt'
abs_read_path = os.path.join(script_dir, rel_path)
abs_save_path = os.path.join(script_dir, save_path)



def read_file(filename, iso):
    """Open and read CSV. Check lines for specified ISO-2 code
    and add city names on those lines to a list."""
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] in iso:
                places.append(row[1])

def save_list(data):
    """Save created list to .txt"""
    with open(abs_save_path, 'w') as f:
        for place in data:
            f.write(place +"\n")


# main code block
places = []
read_file(abs_read_path, countries)
print(places)
print(len(places), 'names in list.')
save_list(places)


