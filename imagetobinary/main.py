# Hello mr boneville i dont know if you are reading the code but yes i wrote this me kingston du
# I decided instead of making a mediocre dime image Pixel Art I would do this :)


print("hello world")

from PIL import Image
import pyperclip
from sys import argv

imageName = ''

def main():
    im = Image.open(imageName)
    pixels = im.load()
    binaryImage = ''

    for y in range(im.size[1]):
        for x in range(im.size[0]):

            #add to string the binary values
            binaryImage += toBinary(pixels[x,y][0])
            binaryImage += toBinary(pixels[x,y][1])
            binaryImage += toBinary(pixels[x,y][2])

            if(argv[2]=='-bw' and not pixels[x,y][0]==pixels[x,y][1]==pixels[x,y][2]):
                raise Exception("Not a black and white image")

    #black and white option
    if argv[2] == '-bw':
        # image is all 00000000 or 111111111 turn it to just 1
        binaryImage = binaryImage[0:len(binaryImage)-1:24]

    print(im.size)
    pyperclip.copy(binaryImage)

#convert decimal to binary, and make it have 8 digits
def toBinary(decimal):
    value = bin(decimal)[2:]
    if len(value) < 8:
        annex = (8-len(value))*'0'
        value = annex + value

    return value


if __name__ == '__main__':
    imageName = argv[1]
    if len(argv) < 3:
        argv.append("-c")
    main()

