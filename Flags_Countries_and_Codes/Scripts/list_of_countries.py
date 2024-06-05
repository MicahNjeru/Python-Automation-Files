### List of countries Script for JSON file 
### Instructions:
    ## 1. Create file with the name "countries_list.json"
    ## 2. Run the script and 
    ## 3. Have fun!
import json

list_of_countries = []
## Import/Open the JSON file to memory
with open("countries.json", "r") as file:
    json_obj = json.load(file)

for key in json_obj:
    list_of_countries.append(json_obj[key])

with open("countries_list.json", "w") as output:
    json.dump(list_of_countries, output)
