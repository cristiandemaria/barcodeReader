# Barcode Reader

An implementation of a barcode scanner in screenshots (Reading the copyboard area).

# Getting Started

`pip install -r requirements.txt`

# Building to standalone

`pyinstaller --onefile --add-binary "./leitorbarcode/Lib/site-packages/pyzbar/libiconv.dll;." --add-binary "./leitorbarcode/Lib/site-packages/pyzbar/libzbar-64.dll;." .\readerbarcode.py`

# How to use

Execute the executable (build the standalone first), then take a screenshot of whatever barcode you want to scan and check the output.

Keys:
 - p) exits the app
 - WIN + S) takes a screenshot