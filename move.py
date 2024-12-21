#%%
#read a markdown file
import os

file=open("Self-Supervised Learning.md","r")
lines=file.readlines()
print(lines)
# %%
for line in lines:
    if line.startswith("![alt text]"):
        #find the image name and move it to a folder
        image_name=line.split("(")[1].split(")")[0]
        print(image_name)
        os.rename(image_name,"Self-Supervised Learning_source/"+image_name)
# %%
