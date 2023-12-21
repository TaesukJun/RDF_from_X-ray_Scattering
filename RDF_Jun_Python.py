import numpy as np
import os
import fnmatch
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import datetime
import pandas as pd

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result
##########################################################################
##########################################################################

# q value need to be in unit A^-1

##########################################################################
######  File directory: Please Modify #####
##########################################################################

FileDir = r"C:\JunDrive\X-ray Data\PS52KRE-Heating"

Save_path = "C:\JunDrive\X-ray Data\Data"
Save_File_Name = "New_File_Name"

##########################################################################
##########################################################################





##########################################################################
######  Coding No Need to Modify Below  #####
##########################################################################

Save_path = Save_path + "/"
Save_path = Save_path.replace('\\','/')
FileDir = FileDir.replace(os.sep,"/")
FileDir = FileDir + "/"
FileDir = FileDir.replace('\\','/')
print('#############################################################################')
print('#############################################################################')
print('File Directory :\n%s' %(FileDir))
print('#############################################################################')
print('#############################################################################\n')
e = datetime.datetime.now()

      
r_range = np.arange(0.5, 11, 0.05)

r = np.zeros(len(r_range))
n = 0 
     
dataCollect = r_range

FileIndex2 = '_backsub-result.dat'
SelectData = "*"+FileIndex2
OtherwayData = find(SelectData, FileDir)
print(OtherwayData)
print('\n')
total_data_num = np.shape(OtherwayData)[0]

for i in range(0,np.shape(OtherwayData)[0],1):
    
    data = np.loadtxt("%s" %(OtherwayData[i]), comments = '%',delimiter=",")
    data = np.array(data)
    x = data[:,0]
    y = data[:,1]
    z = x*y
    n = 0
    r = np.zeros(len(r_range))
    
    plt.subplot(121)
    plt.plot(x,y, color=[i/total_data_num, 0.5, 1-i/total_data_num])
    plt.xlabel("Scattering data")
      
      
    for k in r_range:
        cal_y = z*np.sin(k*x)
        result = integrate.simpson(cal_y,x)
        r[n] = result
        n = n + 1
      

    dataCollect = np.vstack((dataCollect,r))
    plt.subplot(122)
    plt.plot(r_range,r,color=[i/total_data_num, 0.5, 1-i/total_data_num])
    plt.xlabel("RDF distribution")
    
      
# FileIndex in range(FileNumStart,FileNumEnd+1,IntervalFile):
dataCollect = np.transpose(dataCollect)


plt.show()


ExportFileName = ("%s%02d%02d_%s_data_%02d%02d%02d.csv" % (e.year, e.month, e.day, Save_File_Name, e.hour, e.minute, e.second))
pd.DataFrame(dataCollect).to_csv(Save_path + ExportFileName, index=False )

