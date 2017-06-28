# scripts
Collection of scripts I have written over the years
## delete-unedited-raws.py
### Purpose
Are your photographs taking too much space? Do you want to get rid of the RAW files that you haven't deemed worth of editing? Look no further! This script deletes RAW files that are not chosen to be edited, while keeping the ones which are edited incase future changes need to be made to them.
### How it works
The script achieves this by deleting raw files which do not have corresponding metadata file (e.g. .xmp) that the editing software such as Lightroom creates.
### Disclaimers
* If you provide the wrong metadata extension, it will delete all raw files in that folder... It's a feature not a bug! Don't worry accidents happen. The script simply moves the files to trash/recycling bin so you can get your precious RAWs back.
* Run AFTER editing pictures and ONLY IF the editing software creates a metadata file in the same location.
* Tested only on Python3.6
### Usage

      python3 delete-unedited-raws.py [-h] [-e1 EXTENSION1] [-e2 EXTENSION2] location
      
      positional arguments:
          location
              specify the directory containing the unedited raw files
        
      optional arguments:
          -h, --help 
              show this help message and exit
          -e1 EXTENSION1, --extension1 EXTENSION1
              raw extension (e.g. .CR2)
          -e2 EXTENSION2, --extension2 EXTENSION2
              metadata extension (e.g. .xmp)
