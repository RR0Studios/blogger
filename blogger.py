import os

class blogger:
    def __init__():
        code = open("index.html", "w")
        code.write("")
        code.close()
    
    def title(text = "", style = "default"):
        if text == "":
            print("blogger: No text provided")
            raise SyntaxError("No text provided")
        
        orig_style = style

        style = open("Styles/" + style + ".txt", "r")
        code  = open("index.html", "a")
        
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
        if os.stat("Styles/" + orig_style + ".txt") != 0:
            code.write("\n")            
    
        code.write('<h1 style = "color: ' + str(color) + '; font-family: ' + str(font) + '; font-size: ' + str(size) + 'px;">' + text + '</h1>')

        code.close()
        style.close()

    def heading(text = "", style = "default", level = 1):
        if text == "":
            print("blogger: No text provided")
            raise SyntaxError("No text provided")
        
        orig_style = style

        style = open("Styles/" + style + ".txt", "r")
        code  = open("index.html", "a")
        
        counter = 0
        left = -1

        for line in style:
            counter += 1
            left -= 1

            if "HEADING" + str(level) in line:
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

        if os.stat("Styles/" + orig_style + ".txt") != 0:
            code.write("\n")

        if level > 0 and level <= 6:
            code.write('<h' + str(level) + ' style = "color: ' + str(color) + '; font-family: ' + str(font) + '; font-size: ' + str(size) + 'px;">' + text + '</h' + str(level) + '>')

        elif level > 0:
            raise SyntaxError("Invalid heading number (Provide between 1 and 6)")

        else:
            code.write('/n <p style = "color: ' + str(color) + '; font-family: ' + str(font) + '; font-size: ' + str(size) + 'px;">' + text + '</p>')

        code.close()
        style.close()