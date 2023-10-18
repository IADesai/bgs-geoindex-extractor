# bgs-geoindex-scanner

Downloads selected files when a text file is uploaded containing the files to be downloaded

## Set-up and installation instructions

1. Create venv `python3 -m venv venv`
2. Activate venv `source .\venv\bin\activate`
3. Install Requirements `pip install -r requirements.txt`

## Development Instructions

- Place the .txt file you wish to download from in the File folder, making sure its the only file in the folder.
- Run `python3 main.py`
- The downloaded files will be stored in the Downloads folder. Make sure you delete the text file from the File folder before running again :)
