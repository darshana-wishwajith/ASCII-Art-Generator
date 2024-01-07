from tqdm import tqdm  # tqdm for progress bar
from time import sleep  # time for calculate delay
from pyfiglet import figlet_format  # this for ascii texts
from termcolor import colored  # termcolor for colourize to text
from random import randint  # for select random font
import PIL.Image  # Image Librery for image to ASCII
import random

colors = ('red', 'green', 'yellow', 'blue', 'cyan', 'white' ,'magenta')
sucsess, stop = False, False


def text_to_ascii(text="demo", color="white"):
    # This colors will apllied on your text1
    colors = ('red', 'green', 'yellow', 'blue', 'cyan', 'white' ,'magenta')

    # This fonts will be apllied on your text
    fonts = ["slant", "3-d", "3x5", "5lineoblique",
             "alphabet", "banner3-D", "doh", "isometric1", "letters",
             "alligator", "dotmatrix", "bubble", "bulbhead", "digital"]

    # select one font randomly
    random.shuffle(fonts)
    random_font = randint(0, len(fonts))

    # message what you want print using ASCII
    ascii_text = figlet_format(text, font=fonts[random_font])

    # Message in colorized
    colored_ascii = colored(ascii_text, color)

    # Result
    print(colored_ascii)

    # result Print on text file
    with open("ASCII_TXT.txt", "w") as f:
        f.write(colored_ascii)


def image_to_ascii(new_width=100, color="white"):
    # List a character to decending oder of imdencity
    ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

    # Resize image to new width
    def resize_image(image, new_width=100):
        width, height = image.size
        ratio = height / width
        new_height = int(new_width * ratio)
        resized_image = image.resize((new_width, new_height))
        return (resized_image)

    # Convert to all pixels to grayscale
    def grayify(image):
        grayscale_image = image.convert("L")
        return (grayscale_image)

    # Convert all pixels to Collection of ASCII characters

    def pixels_to_ascii(image):
        pixels = image.getdata()
        characters = "".join([ASCII_CHARS[pixels // 25] for pixels in pixels])
        return (characters)

    # Main Fuction for get input path of image
    def main(new_width=100):
        # Convert image to ASCII
        new_image_data = pixels_to_ascii(grayify(resize_image(image)))

        # formating ASCII Characters
        pixels_count = len(new_image_data)
        ascii_image = "\n".join(new_image_data[i:(i + new_width)] for i in range(0, pixels_count, new_width))

        # coloring ASCII ART
        colored_ascii_art = colored(ascii_image, color)
        # print Result (ASCII ART!)
        print(colored_ascii_art)

        # Save Result to "ascii_image.txt"
        with open("ASCII_ART.txt", "w") as f:
            f.write(ascii_image)

    main()

print("*" * 50 , "ASCII ARTS 1.0" , "*" * 50)
print("")
print("Initializing Program.....")
sleep(2)
print("Initializing Completed.....")
sleep(1)
print("")
while stop == False:

    print("Select a mode")
    print("")
    print("\t 1 = Text to ASCII")
    print("\t 2 = Image to ASCII")
    print("")
    mode = input()
    if  '1' or "2" in mode :
        if mode == "1":
            while True:
                text = input("Enter your text here : ")
                print("your text is", '-', text, '-')
                print("")
                print(" Do you want to change this ?")
                print("")
                print("\t y = Yes")
                print("\t n = No")
                print("")
                y_or_n = input()
                if y_or_n == "n":
                    break
            while True :
                color = input("Enter your color here : ")
                while True:
                    if color not in colors:
                        print(color, "Color is not a valid color. The valid colors are ", colors)
                        color = input("Enter your color here : ")
                        continue
                    else:
                        print("Your color is valid !")
                        print("")
                        break
                print("your color is", '-', color, '-')
                print("Do you want to change this ?")
                print("")
                print("\t y = Yes")
                print("\t n = No")
                print("")
                y_or_n = input()
                if y_or_n == "n":
                    break

            for i in tqdm(range(100)):
                sleep(0.1)

            text_to_ascii(text, color)

        elif mode == "2":
            while sucsess == False:
                path = input("Enter your image path : \n")
                print("your path is", '-', path, '-')
                print("")
                print("Do you want to change this ?")
                print("\t y = Yes")
                print("\t n = No")
                print("")
                y_or_n = input()
                if y_or_n == "n":
                    try:
                        image = PIL.Image.open(path)
                        sucsess = True
                    except:
                        print(path, "is a not valid path for image. Enter your correct path again")
                        print("")

            while True:
                new_width = input("Enter image with what you want here : ")
                print("your image width is", '-', new_width, '-')
                print("")
                print(" Do you want to change this ?")
                print("\t y = Yes")
                print("\t n = No")
                print("")
                y_or_n = input()
                if y_or_n == "n":
                    break

            while True:
                color = input("Enter your color here : ")
                while True:
                    if color not in colors:
                        print(color, "Color is not a valid color. The valid colors are ", colors)
                        color = input("Enter your color here : ")
                        continue
                    else:
                        print("Your color is valid !")
                        break
                print("your color is", '-', color, '-')
                print("")
                print("Do you want to change this ?")
                print("\t y = Yes")
                print("\t n = No")
                print("")
                y_or_n = input()
                if y_or_n == "n":
                    break

            for i in tqdm(range(100)):
                sleep(0.1)

            image_to_ascii(new_width, color)

        print("The program is end !")
        print("")
        print("What you want to do")
        print("")
        print("\t r = reset")
        print("\t s = stop")
        status = input()

        if status == "s":
            stop = True
    else:
         print(mode,"is not a mode. enter a valid mod! ")
         print("")

k = input("Press Any Key to exit ......")