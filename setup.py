from os import listdir
from os.path import isfile, join
from path import Path
import numpy as np
import cv2
import json
# Dataset path
target_path = Path('target_train/')
annotation_images_path = Path('dataset/ade20k/annotations/training/').abspath()
dataset = [ f for f in listdir(annotation_images_path) if isfile(join(annotation_images_path,f))]
images = np.empty(len(dataset), dtype = object)
count = 1
# Iterate all Training Images
for n in range(0, len(dataset)):
    # Read image
    images[n] = cv2.imread(join(annotation_images_path,dataset[n]),-1)
 
    # Convert it to array
    array = np.asarray(images[n],dtype=np.int8)

    # Conditions when the value equal less than 1, change it to 255. 
    # If it is >= 1, increment it by -1
    arr = np.where(array < 1, 255, array -1)

    if count < 10:
        cv2.imwrite(target_path +'ADE_val_0000000'+ str(count) + ".png", arr)
    elif count < 100 and count > 9:
        cv2.imwrite(target_path +'ADE_val_000000'+ str(count) + ".png", arr)
    elif count < 1000 and count > 99:
        cv2.imwrite(target_path +'ADE_val_00000'+ str(count) + ".png", arr)
    elif count < 10000 and count > 999:
        cv2.imwrite(target_path +'ADE_val_0000'+ str(count) + ".png", arr)
    else:
        cv2.imwrite(target_path +'ADE_val_000'+ str(count) + ".png", arr)
    print(str(count) + ".png is printed")
    count += 1
    print(count)
  



                
