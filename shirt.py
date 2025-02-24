import sys
import string
from PIL import Image
import PIL

def main():
    ''' main function '''
    check_arguments()
    image = input_image(sys.argv[1])
    shirt = get_shirt()
    image = PIL.ImageOps.fit(image, shirt.size)
    Image.Image.paste(image, shirt,shirt)
    image = image.save(sys.argv[2])

def get_shirt():
    ''' returns shirt img '''
    try:
        img = Image.open("shirt.png")
    except FileNotFoundError:
        print("shirt.png not found")
        sys.exit(1)
    return img

def input_image(arg):
    ''' returns inputted image '''
    try:
        image = Image.open(arg)
    except FileNotFoundError:
        print("File cannot be found")
        sys.exit(1)
    return image

def check_extensions(arg1, arg2):
    ''' checks extensions of arguments'''
    extensions = ('.jpg', '.jpeg', '.png')
    try:
        if not arg1.lower().endswith(extensions):
            raise ValueError("invalid input")
        if not arg2.lower().endswith(extensions):
            raise ValueError("invalid output")
        ''' check if extensions match '''
        for ext in extensions:
            if ext in arg1:
                if ext not in arg2:
                    raise ValueError("Input and output have different extensions")
    except ValueError as ex:
        print(ex)
        sys.exit(1)

def check_arguments():
    ''' check if arguments are correct '''
    try:
        if len(sys.argv) != 3:
            raise Exception
    except Exception:
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        else:
            sys.exit("Too few command-line arguments")
    check_extensions(sys.argv[1], sys.argv[2])
if __name__ == "__main__":
    main()
