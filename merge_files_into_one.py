"""This script helps to merge txt, dcvs, JSON file data from several/all files into one"""

"""In order to use this, please place this script in the folder you have all the files in and change the extension in the line 11 if the extention is different from .txt """
#using datetime module to produce a file that has a time stamp as its name
import datetime

#make sure you have glob2 installed using pip install glob2
import glob2


filenames =glob2.glob("*.txt")

#if you want custom name please change
#datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") to a "filename"
with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")+".txt", 'w') as file:
    for filename in filenames:
        with open(filename, "r") as f:
            file.write(f.read()+"\n")
