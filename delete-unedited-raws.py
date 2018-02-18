import os
import argparse
from send2trash import send2trash


def main():
    ext_raw = ".CR2"
    ext_metadata = ".xmp"

    # Argument Parsing
    parser = argparse.ArgumentParser(description='Delete raw files which do not have corresponding metadata file ('
                                                 'e.g. .xmp). Run AFTER editing pictures and only if the editing '
                                                 'software creates a metadata file in the same location.')
    parser.add_argument("location", help="specify the directory containing the unedited raw files")
    parser.add_argument("-e1", "--extension1", help="raw extension (e.g. .CR2)")
    parser.add_argument("-e2", "--extension2", help="metadata extension (e.g. .xmp)")
    args = parser.parse_args()

    dir_location = args.location
    if not (args.extension1 is None):
        ext_raw = args.extension1
    if not (args.extension2 is None):
        ext_metadata = args.extension2

    print("\nDirectory:", dir_location)
    print("Raw Extension:", ext_raw)
    print("Metadata Extension:", ext_metadata, "\n")

    os.chdir(dir_location)

    # create a collection of edited raw files
    edited_raws = set()

    for file in os.listdir(dir_location):
        if file.endswith(ext_metadata):
            file_name = os.path.splitext(os.path.basename(file))[0] + ext_raw
            edited_raws.add(file_name)

    print("The following files are moved to trash/recycling bin:")

    # delete files not in the edited_raw collection
    files_list = os.listdir(dir_location)
    for file in files_list:
        if file.endswith(ext_raw):
            if file not in edited_raws:
                send2trash(file)
                print(file)

    print("\nDone!")

if __name__ == "__main__":
    main()
