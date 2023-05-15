# Python Automation Files

__The repo contains a list of python files used to automate random and tedious process involved with data obtained from various sources.__
 
- Images in the output_images repo were obtained from [hampusborgos/country-flags](https://github.com/hampusborgos/country-flags) repo.
- Country/economic regions pdf file was obtain from (IBAN's list of country codes Alpha-2 & Alpha-3 website)[https://www.iban.com/country-codes]
- The PDF was then converted to a csv file using a (free online tool)[https://www.zamzar.com/convert/pdf-to-csv/]
- The csv file with the list of countries was parsed and cleaned, clean data was saved to the (List of countries.csv)[https://github.com/MicahNjeru/Python-Automation-Files/blob/main/List%20of%20countries.csv] file.
- Countries JSON data file from (hampusborgos/country-flags/countries.json)[https://github.com/hampusborgos/country-flags/blob/main/countries.json] was used to access country names and compare with IBAN's list
- The countries.json file was used to rename all images from (hampusborgos/country-flags/png1000px)[https://github.com/hampusborgos/country-flags/tree/main/png1000px] to the full country's name
-  Finally, all images that were copied to the input_images folder from (hampusborgos/country-flags/png1000px)[https://github.com/hampusborgos/country-flags/tree/main/png1000px] were renamed to the corresponding countrie's full name obtained from (hampusborgos/country-flags/countries.json)[https://github.com/hampusborgos/country-flags/blob/main/countries.json] in order to match the names and number of images

## Key takeaway points

1. Using Python did help work on the images faster than would have been doing it manually. 
2. The number of countries from the IBAN list of countries did differ from the repo where images were obtained from, this is something to look into further. 
3. Python's `rename()` function, does not copy and past files after renaming but instead moves the files after having renamed them. This means the `remove()` function can be used to move files from source folder to destination. 

##  Lessons learned from this project
1. Data pre-processing is a very important step when working with structured/unstructured data. 
2. Take time to think of the process from start to finish, I tried using regex for one reason or another thinking it would help fill in the gaps but I ended up wasting time. Lesson learned!
3. Solving problems using programming languages is definitely something I love doing!!!
