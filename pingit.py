import os
import time
from time import strftime
import re
import csv
from collections import OrderedDict

import matplotlib.pyplot as plt

def main():
   files = list_files("~/Documents/pingit")

   results = {}   

   for file in files:
      f = open(file, 'r')
      creation_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(os.path.getmtime(file)))
      pings = []      

      for line in f:
         l = f.readline()
         m = re.search('(?<=time=)\d+[\.\d]*', l)

         if(m != None):
            pings.append(float(m.group(0)))
         
      results[creation_time] = pings

   results = OrderedDict(sorted(results.items(), key=lambda t: t[0]))

   #with open('mycsvfile.csv', 'w') as f:  # Just use 'w' mode in 3.x
   #   w = csv.DictWriter(f, results.keys())
   #   w.writeheader()
   #   w.writerow(results)  

   fig = plt.figure()
   ax = fig.add_subplot(111) 

   data = []
   keys = []
   for res in results.keys():
      keys.append(res)
      data.append(results[res])

   xtickNames = plt.setp(ax, xticklabels=keys)
   plt.setp(xtickNames, rotation=90, fontsize=6)
   
   ax.boxplot(data)
   plt.show()      

def list_files(path):
    # returns a list of names (with extension, without full path) of all files 
    # in folder path
    files = []
    for name in os.listdir(path):
        if os.path.isfile(os.path.join(path, name)):
            files.append(os.path.join(path, name))

    return files 

if __name__ == "__main__":
     main()
