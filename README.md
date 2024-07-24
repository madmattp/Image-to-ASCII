# img_to_ascii.py
  Converts any image into ASCII.

## Usage
```usage: img_to_ascii.py [-h] [-v] -r <res> -i <img> [-o <name>] [-c]```

Example: ```python3 img_to_ascii.py -v -i image.png -r 300x300 -c -o art.txt```

## Options
  - -h, --help
    - Show a help message.
  - -v, --verbose
    - Run in "verbose" mode.
  - -r <res>, --resolution [ res ]
    - Specifies the resolution of the output (default: 100x100).
  - -i <img>, --image [ img ]
    - Specifies the image to be used as input.
  - -o <name>, --output [ name ]
    - Specifies the name of the file that will be used as an output (default: output.txt).
  - -c, --clipboard
    - Automatically copies image to the clipboard.
