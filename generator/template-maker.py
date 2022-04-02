from asyncio.windows_events import NULL
from turtle import width
from PIL import Image

# Creates a new transparent canvas
def NewCanvas(destination):
    base = Image.new('RGBA', (3000, 3000))
    base.save(destination, "PNG")
    return base

# Draws template on existing canvas
def DrawTemplate(base, addition, start_x, start_y) :
    if(base == " " or base == NULL or base == ""):
        base = Image.new('RGBA', (3000, 3000)) 
    else:
        base = Image.open(base)

    add = Image.open(addition,'r')
    add_val = list(add.getdata())
    add_width, add_height = add.size

    i = 0
    for y in range(add_height):
        for x in range(add_width):
            base.putpixel((start_x + x*3,start_y + y*3), (add_val[i]))
            i = i+1

            
    base.save('result.png')
    base.show()
    return base

# coords of template
start_x = 363
start_y = 645
base = " "
addition = " "



print("1 to create on blank canvas")
print("2 to draw on existing canvas")
draw_mode = input()

if(int(draw_mode) == 1):
    base = NewCanvas("blankcanvas.png")
    base.show()

if(int(draw_mode) == 2):
    print("Start x coords of art:")
    start_x = input()
    start_x = int(start_x)

    print("Start y coords of art:")
    start_y = input()
    start_y = int(start_y)

    print(start_y)

    print("Canvas to add to:")
    print("Leave empty to create a new canvas")
    base = input()

    print("Image to add:")
    addition = input()
    addition = str(addition)

    DrawTemplate(base, addition, start_x*3+1, start_y*3+1)



