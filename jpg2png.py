import sys, os
from PIL import Image
jpgFolder = sys.argv[1]
pngFolder = sys.argv[2]

if not os.path.exists(pngFolder):
    os.makedirs(pngFolder)
else:
    print(f'A folder named {pngFolder} already exists!')

images = os.listdir(jpgFolder)

for image in images:
    img = Image.open(f'{jpgFolder}/{image}')
    cleaned_name = os.path.splitext(image)[0]
    img.save(f'{pngFolder}/{cleaned_name}.png', 'png')

print("Done!")