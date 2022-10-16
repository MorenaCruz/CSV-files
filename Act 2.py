'''Using the CSV file of flowers again, fill in the gaps of the contents_of_file function to process the data without turning it into a dictionary. '''

import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename) as f:
    # Read the rows of the file
    rows = csv.reader(f)
    # Process each row
    for row in rows:
      Name,Color,Type = row
      # Format the return string for data rows only
      if Name!="name":
        return_string += "a {} {} is {}\n".format(Color,Name,Type)
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))
