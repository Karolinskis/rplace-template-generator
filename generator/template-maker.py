from PIL import Image
from os import listdir
from os.path import isfile, join

# Script created by Karolinskis
# r/place template maker
# 2022-04-02

# Global constants
# r/place canvas size
TEMPLATES_DIR = "templates"
RESULT_DIR = "result.png"
PLACE_X = 2000*3
PLACE_Y = 1000*3


# Creates a new transparent canvas
def NewCanvas(dest_src):
    base = Image.new('RGBA', (PLACE_X, PLACE_Y))
    base.save(dest_src, "PNG")
    return base

# Finds all file names of templates in *templates_src*
def ReadTemplates(templates_dir):
    images = []
    images = [f for f in listdir(templates_dir) if isfile(join(templates_dir, f))]
    return images


# Draws template on existing canvas
def DrawTemplate(base_src, addition, start_x, start_y) :
    base = Image.new('RGBA', (PLACE_X, PLACE_Y))  
        
    #base = Image.open(base_src)

    add = Image.open(addition,'r')
    add_val = list(add.getdata())
    add_width, add_height = add.size

    i = 0
    for y in range(add_height):
        for x in range(add_width):
            base.putpixel((start_x + x*3,start_y + y*3), (add_val[i]))
            i = i+1

    base.save("result.png")
    return base

# Main
print("Canvas to add to:")
print("Leave empty to create a new canvas")
base_src = input()


print("Directory to read templates from \n Default: /templates")
templates_dir = input()

if (templates_dir == "" or templates_dir == " ") :
    templates_dir = TEMPLATES_DIR


print("Reading...")

if(templates_dir == " " or templates_dir == "") :
    templates_dir = TEMPLATES_DIR

templates_dirs = ReadTemplates(templates_dir)
    
print("Completed!" + "\nFound " + str(len(templates_dirs)) + " templates")


for template_dir_i in templates_dirs:
    print("Populating canvas...")
    xy = template_dir_i.split('-')
    x_src = int(xy[0])
    y_src = int(xy[1].split('.')[0])
    full_templates_dir = templates_dir + "/" + template_dir_i
    template = DrawTemplate(RESULT_DIR, full_templates_dir, x_src*3+1, y_src*3+1)

template.show()
