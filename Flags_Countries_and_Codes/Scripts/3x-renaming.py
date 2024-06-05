### Renaming Script for iOS asset images @3x 
### Instructions:
    ## 1. Create local folder with the name "3x"
    ## 2. Create destination folder with the name "final_3x"
    ## 3. Load all images into the "3x" folder
    ## 4. Run the script and delete "3x" folder since all images are renamed and moved to "final_3x"
    ## 5. Have fun!
import os

counter = 0

## Loop through all files in the path folder
for file in os.listdir(path="3x"):
    # Increment counter to check number of processed files
    counter += 1

    # Save current file name and path
    source = f"3x/{file}"

    # Add destination path and name edit
    name = f"final_3x/{file[:-4]}@3x.png"

    # Rename and move the files
    os.rename(source, name)
    
    # Print worked on files to confirm
    print(f"Renamed and moved {source} to {name}.")

# Print number of files processed
print(f"\nFinal count {counter}\n")