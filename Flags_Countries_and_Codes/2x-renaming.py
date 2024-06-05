### Renaming Script for iOS asset images @2x 
### Instructions:
    ## 1. Create local folder with the name "2x"
    ## 2. Create destination folder with the name "final_2x"
    ## 3. Load all images into the "2x" folder
    ## 4. Run the script and delete "2x" folder since all images are renamed and moved to "final_2x"
    ## 5. Have fun!
import os

counter = 0

## Loop through all files in the path folder
for file in os.listdir(path="2x"):
    # Increment counter to check number of processed files
    counter += 1

    # Save current file name and path
    source = f"2x/{file}"

    # Add destination path and name edit
    name = f"final_2x/{file[:-4]}@2x.png"

    # Rename and move the files
    os.rename(source, name)

    # Print worked on files to confirm
    print(f"Renamed and moved {source} to {name}.")

# Print number of files processed
print(f"\nFinal count {counter}\n")