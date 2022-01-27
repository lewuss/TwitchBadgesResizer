from PIL import Image
from os import listdir, getcwd
from os.path import isfile, join
mypath = getcwd()
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
images = [image for image in onlyfiles if image[-1]=="g"]

for file in images:
    image = Image.open(file)
    new_image = image.resize((112, 112))
    new_image.save(f'112_{file}')
    new_image = image.resize((56, 56))
    new_image.save(f'56_{file}')
    new_image = image.resize((28, 28))
    new_image.save(f'28_{file}')

