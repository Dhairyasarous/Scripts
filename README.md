# scripts
Collection of scripts I have written over the years
## delete-unedited-raws.py
### Purpose
This script deletes RAW files that are not chosen to be edited, however keep the ones which are edited incase future changes need to be made to them.
### How it works
The script achieves this by deleting raw files which do not have corresponding metadata file (e.g. .xmp) that the editing software such as Lightroom creates.
### Disclaimers
* Run AFTER editing pictures and ONLY IF the editing software creates a metadata file in the same location.
* Tested only on Python3.6
