import csv, os

# The two variables 'source_csv' & 'target_csv' will be used -
# to assign the source of our data and the end value target

source_csv = "List of country codes by alpha-2, alpha-3 code (ISO 3166).csv"
target_csv = "List of countries.csv"


def read_file(input_filename):
    """ Function for reading a csv file and returning a list of rows """

    with open(input_filename, "r") as csv_file:
        csv_object = csv.reader(csv_file)
        final_rows = []
        for rows in csv_object:
            final_rows.append(rows)

        return final_rows

sample = read_file(source_csv)

### Run these 3 lines to check on the data and how it's organized/disorganized. ###
# for samples in sample:
#     print(samples)
# print(sample[244])
# print(len(sample[0]))


def remove_empty_elements():
    """ 
    This function is used to remove all empty elements in the rows of the sample list.
    You can modify it to take a nested list of elements 
    That is, a list within a list that has elements e.g.: [["1", "2"], ["1", "2"]]
    """

    index = 0 
    row_counter = 0
    # Start of while loop
    while row_counter <= len(sample):
        row = sample[row_counter]
        print("\n")
        print(f"Processing row = {row_counter}")
        row_len = len(row) - 1
        while index <= row_len:
            print(f"Index count' {index} ' row count ' {row_counter} '")
            if index > (len(row) - 1):
                break
            else:
                if row[index] == "" and index < (len(row)):
                    print("Empty")
                    removed = row.pop(index)
                    print(f"Removing '{removed}', proceeding to next element in row")
                    # index += 1
                else:
                    print("Not empty")
                    index += 1
        row_counter += 1
        index = 0
        if row_counter >= len(sample):
            break
    # End of while loop


# Run the above function to see output on your terminal
remove_empty_elements()
# Take note of row 246 & 247, notice something? 
# Since all values were removed the row entry is an empty list
# This will mess up with the final result, so we remove the empty list entries


def clean_up():
    """ This function removes all empty lists within the larger list"""
    # Clean up the elements and remove all empty lists
    final_list = []
    print(final_list)
    index_test = 0
    for samples in sample:
        if len(sample[index_test]) != 0:
            final_list.append(sample[index_test])
            print(f"Appended => {sample[index_test]} \t to 'final_list' from\t index => {index_test}")
        index_test += 1 

    print("\n")
    # End of cleanup

    ### (OPTIONAL) Uncomment the following set of code to see the end result (OPTIONAL) ###
    # print("\n")
    # row_number = 0
    # for item in final_list:
    #     print(f"{item} index number => {row_number}")
    #     row_number += 1
    # print(f"\nLength of final list is => {len(final_list)}\n")
    
    return final_list


# Run the clean-up function to see your work!
final_data = clean_up()

for entry in final_data:
    print(entry)
print("\n")

# Better right?
# We'll use the 'final_data' variable in the final function
# Now, let's finish up and save our very clean data!

### Also, try answering this question: ###
# What is this data about? Can you say what the data is saving?


def write_rows(output_filename):
    with open(output_filename, "w", encoding="UTF8", newline="") as csv_file:
        writer_object = csv.writer(csv_file)
        for row in final_data:
            writer_object.writerow(row)
        

# Let's save our work on disc by running the function
write_rows(target_csv)

# Test the end result by importing it using the `read_file()` function
test = read_file("List of countries.csv")
for row in test:
    print(row)
print("\n")

### AND THAT'S IT FOR OUR PROJECT! Want to see something cool? 
# Uncomment the print statement and the for loop below this comment!

# print("\U0001F50A\U0001F50A\U0001F50A\t TESTING CLEAN DATA 1-2, 1-2!!!\t \U0001F50A\U0001F50A\U0001F50A")
# for number in range(0,9):
#     print("\U0001F918 \U0001F60E \U0001F919 \U0001F60E ", end="")
# print("\n")


# Don't worry about the emojis if they aren't working on your PC
# We'll figure that out later and maybe even create a game out of it 🤷🏾‍♂️
# Are you excited now???

### All credits to the GRIT team - authored by Micah Njeru 11th May 2023. ###