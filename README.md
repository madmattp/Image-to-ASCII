# img_to_ascii.py

usage: img_to_ascii.py [-h] [-v] [-r <res>] [-i <img>] [-o <name>] [-c]

img_to_ascii.py, Converts an image to ASCII.

options:
  -h, --help            show this help message and exit
  -v, --verbose         Executes in "verbose" mode
  -r <res>, --resolution <res>
                        Specifies the resolution of the output (default: 100x100)
  -i <img>, --image <img>
                        Specifies the image to be used as input.
  -o <name>, --output <name>
                        Specifies the name of the file that will be used as output (default: output.txt)
  -c, --clipboard       Automatically copies image to the clipboard

Ex: python3 img_to_ascii.py -v -i image.png -r 300x300 -c -o art.txt
