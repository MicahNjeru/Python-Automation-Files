### Import json module for parsing JSON files
### Import os module for renaming image files
### Import re (regex) module for parsing various file names
### Import csv module for parsing csv data
import json, os


## Import/Open the JSON file to memory
with open("countries.json", "r") as file:
    json_obj = json.load(file)

## Invert the Country name and ISO-2 code
## Assign the long form counrty name to 'key'
## Assign the short ISO-2 name to the 'value'
working_dict = {}
for key, value in json_obj.items():
    working_dict[key] = value

## Print key:value pairs to check on dictionary format
# for key, value in working_dict.items():
#     print(f"Key => {key}, Value => {value}")

### Regex working portion

# examples = ["gb-wls", "sx", "ke", "09",""]
# pattern = re.compile(r"[a-z]+[-]*[a-z]*")
# newlist = list(filter(pattern.match, examples))
# print(newlist)

### End of Regex portion

### Create temporary list of dictionary keys to use to match 

keys_list = []
for key in working_dict:
    keys_list.append(f"{key.lower()}.png")

### End of temporary list creation

## Print string slices to check where '.png' ends in order to use in the renaming function
# for key in keys_list:
#     print(key[:-4])


### Start of renaming function
def rename_and_move_files():
    number_of_files = 0
    # Loop through the dictionary with keys as counter
    for key in working_dict:
        # Loop through the temporary list
        for x in keys_list:
            # Loop through all files in the path 
            for file in os.listdir(path="input_images"):
                # Check if the names (minus extension) in the list are similar to names in the dict AND
                # Check if the names (plus extension) in the list are similar to file names in the folder
                if x[:-4] == key.lower() and x == file:
                    # Name the source files' folder and file name to work on
                    source = f"input_images/{file}"

                    # Assign the file name wanted to a variable and the folder to move it to
                    name = f"output_images/{working_dict[key]}.png"

                    # Print the process about to run to check if it picked correct values
                    print(f"Renaming => {file} to => {name}")

                    # Use the os.rename() function to rename the files 
                    # Provide the source path and destination path + name to change it to
                    os.rename(source, name)

                    # Incremenet the local counter to get result of how many files were edited and moved. 
                    number_of_files += 1

                    # Print the edited results to check if all files were renamed and moved to the right directory. 
                    print(f"Renamed => {file} to => {working_dict[key]}.png")

    # Print the total number of files that were edited 
    print(f"Files found and ready for processing => {number_of_files}")

    ### End of renaming function

## Run the function to execute the task
rename_and_move_files()