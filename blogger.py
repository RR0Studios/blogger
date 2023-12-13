import sys
import os

class blogger:
    def title(text = "", style = "default"):
        if text == "":
            print("blogger: No text provided")
            raise SyntaxError("No text provided")
        
        style = open("Styles/" + style + ".txt", "r")
        code  = open("code.txt", "w")
        
        counter = 0
        left = -1

        for line in style:
            counter += 1
            left -= 1

            if "TITLE" in line:
                left = 3

            if left == 2:
                size = line[6:]
                size = size.replace("\n", "")

            if left == 1:
                font = line[6:]
                font = font.replace("\n", "")
            
            if left == 0:
                color = line[7:]
                color = color.replace("\n", "")
                break

        code.write('<h1 style = "color: ' + str(color) + '; font-family: ' + str(font) + '; font-size: ' + str(size) + ' px;">' + text + '</h1>')

        code.close()
        style.close()