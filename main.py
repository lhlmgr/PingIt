import os
import time
from time import strftime
import re
import csv
import collections

from collections import OrderedDict

import matplotlib.pyplot as plt

def plot_day():
   files = list_files("~/Documents/pingit")

   results = {}   
   days = collections.defaultdict(dict)

   for file in files:
      f = open(file, 'r')
      creation_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(os.path.getmtime(file)))
      creation_day = time.strftime("%d.%m.%Y", time.localtime(os.path.getmtime(file)))

      pings = []      

      for line in f:
         l = f.readline()
         m = re.search('(?<=time=)\d+[\.\d]*', l)

         if(m != None):
            pings.append(float(m.group(0)))
         
      results[creation_time] = pings

      days[creation_day][creation_time] = pings

   results = OrderedDict(sorted(results.items(), key=lambda t: t[0]))

   #with open('mycsvfile.csv', 'w') as f:  # Just use 'w' mode in 3.x
   #   w = csv.DictWriter(f, results.keys())
   #   w.writeheader()
   #   w.writerow(results)  

   days = OrderedDict(sorted(days.items(), key=lambda t: t[0]))
   for res in days.keys():
      pingPerDay = days[res]
      pingPerDay = OrderedDict(sorted(pingPerDay.items(), key=lambda t: t[0]))
      fig = plt.figure()
      fig.set_size_inches(20,12)

      ax = fig.add_subplot(111) 

      data = []
      keys = []
      for resKey in pingPerDay.keys():
         keys.append(resKey)
         data.append(pingPerDay[resKey])

      xtickNames = plt.setp(ax, xticklabels=keys)
      plt.setp(xtickNames, rotation=90, fontsize=8)
      ax.set_title(res)
      ax.boxplot(data)
      #plt.show()

      plt.savefig(res+".svg", dpi=500,bbox_inches='tight')


def main():
   files = list_files("~/Documents/pingit")

   results = {}   

   for file in files:
      f = open(file, 'r')
      creation_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(os.path.getmtime(file)))
      creation_day = time.strftime("%d.%m.%Y", time.localtime(os.path.getmtime(file)))
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
   plot_day()  
   #main()
