# Hello mr boneville i dont know if you are reading the code but yes i wrote this
# I decided instead of making a mediocre Pixel Art I would do this :)

print("hello world")

from PIL import Image
import pyperclip

im = Image.open("image.jpg")
pixels = im.load()

def main():
    binaryImage = ''

    for y in range(im.size[1]):
        for x in range(im.size[0]):
            #add to string the binary values
            binaryImage += toBinary(pixels[x,y][0])
            binaryImage += toBinary(pixels[x,y][1])
            binaryImage += toBinary(pixels[x,y][2])

    print(im.size)
    pyperclip.copy(binaryImage)

def toBinary(decimal):
    value = bin(decimal)[2:]
    if len(value) < 8:
        annex = (8-len(value))*'0'
        value = annex + value

    return value


if __name__ == '__main__':
    main()

