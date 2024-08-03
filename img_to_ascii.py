import cv2
import pyperclip
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(
        description='img_to_ascii.py, Converts an image to ASCII.',
        epilog='Ex: python3 img_to_ascii.py -v -i image.png -r 300x300 -c -o art.txt'
    )

    parser.add_argument('-v', '--verbose', action='store_true', help='Executes in "verbose" mode')
    parser.add_argument('-r', '--resolution', metavar='<res>', required=True, default='100x100', help='Specifies the resolution of the output (default: 100x100)')
    parser.add_argument('-i', '--image', metavar='<img>', required=True, help='Specifies the image to be used as input.')
    parser.add_argument('-o', '--output', metavar='<name>', default='output.txt', help='Specifies the name of the file that will be used as output (default: output.txt)')
    parser.add_argument('-c', '--clipboard', action='store_true', help='Automatically copies image to the clipboard')

    args = parser.parse_args()
    return args

def img_to_ascii(image):
    d = '⠀.;coPO?@▓█'
    copy = ""

    rows, cols = image.shape
    for i in range(rows):
        row = ""
        for j in range(cols):
            pixel_value = image[i, j]
            pixel_value = int(pixel_value / 25.5)
            row += f"{d[pixel_value] + d[pixel_value]}"
        row += "\n"
        copy += row    
    
    return copy

if __name__ == "__main__":
    args = parse_arguments()

    x = ""
    y = ""
    is_x = True
    for char in args.resolution:
        if char == "x":
            is_x = False
        elif is_x:
            x += char
        else:
            y += char
    res = (int(x), int(y))

    image = cv2.imread(args.image, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, res)
    image = cv2.equalizeHist(image)

    output = img_to_ascii(image=image)

    if args.verbose:
        print(output)

    if args.clipboard:
        pyperclip.copy(output)
        print("[ Added image to clipboard! ]")

    try:
        with open(file=args.output, mode="w") as file:
            file.write(output)
    except FileExistsError as e:
        print(f"[{e}] File'{args.output}' already exists!")
