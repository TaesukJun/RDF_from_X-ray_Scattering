#%%




#################################
############# Setups ############
#################################


import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
import os, fnmatch
import datetime

plt.rcParams["font.family"] = "arial"
plt.rcParams.update({'font.size': 13})


from scipy.signal import find_peaks, peak_prominences
import matplotlib.pyplot as plt
import numpy as np
from lmfit.models import LorentzianModel, QuadraticModel, LinearModel, VoigtModel

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import pygame
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
                                               NavigationToolbar2Tk) 


def add_peak1(prefix, center, amplitude=0.002, sigma=0.0075):
    global PeakVariance, setsigma
    peak = VoigtModel(prefix=prefix)
    pars = peak.make_params()
    pars[prefix + 'center'].set(center, max=center*(1+PeakVariance), min=center*(1-PeakVariance))
    pars[prefix + 'amplitude'].set(amplitude, min=0)
    pars[prefix + 'sigma'].set(sigma, max=setsigma, min=0)
    return peak, pars

def cm_to_inch(value):
    return value/2.54

def find(pattern, path):
    global name
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result






# Parameter









#################################################################################

def Clicked_Analyze():
    global Option_Var_01, e_01, e_17, e_18, e_19, e_15, e_16,e_101,e_102,e_103,e_104
    global PeakVariance, frame_Result_02, setsigma, peakdata, name
    # Parameter
    Beamline = Option_Var_01.get()
    FileDir = e_01.get()
    FileDir = FileDir.replace(os.sep,"/")
    FileDir = FileDir + "/"
    FileDir = FileDir.replace('\\','/')


    whereistemp_section = int(e_03.get())

    FileNumStart, FileNumEnd, IntervalFile = (int(e_17.get()), int(e_18.get()), int(e_19.get())) 
    qmin, qmax = float(e_15.get()), float(e_16.get())

    
    PeakVariance = float(e_101.get())
    #처음 피팅된 값에서 피팅허용할 범위 ex) 0.1 이면 초기 피팅된 값 10% 이내로만 움직일 수 있음.
    setsigma = float(e_102.get())
    # 픽의 최소 넓이 정하는 것

    ## Allowance 픽 발견 민감도 낮으면 많은 픽들을 발견함
    PeakHeightAllow = float(e_103.get()) # The higher number allows the sharper peaks
    PeakBroadnessAllow = float(e_104.get())  # The higher number allows the narrower peaks




    fitqmin, fitqmax = qmin, qmax
    fitqmin2,fitqmax2 = fitqmin, fitqmax
    NumofData = int((FileNumEnd - FileNumStart + 1)/IntervalFile)
    dataCollection = [[]]
    fig = plt.figure(figsize=(cm_to_inch(17),cm_to_inch(13)))
    ax = fig.add_subplot(111)
    peakdata = []

    n = 1
                    


    for FileIndex in range(FileNumStart,FileNumEnd+1,IntervalFile):

        if Beamline =='9A':
            FileIndex2 = ("%04d" %(FileIndex))
        else:
            FileIndex2 = ("%05d" %(FileIndex))
        
        print(FileIndex2)
        SelectData = "*_"+FileIndex2+"*"
        OtherwayData = find(SelectData, FileDir)
        print(OtherwayData)
        data = np.loadtxt("%s" %(OtherwayData[0]), dtype=np.str_, comments = '%',delimiter=",")
        data_size = np.shape(data)[0]
        data_temp = np.zeros((data_size,2))
        for i in range(data_size):
            data_temp[i,0] = data[i].split()[0]
            data_temp[i,1] = data[i].split()[1]
        data = data_temp
        if n == 1:
            dataCollection = data[:,0]
            dataCollection = np.reshape(dataCollection,(dataCollection.size,1))
        AddData = np.reshape(data[:,1],(data[:,1].size, 1))   
        dataCollection = np.hstack((dataCollection,AddData))
        x = data[:,0]
        y = dataCollection[:,n]

        
        plot = plt.plot(x, y, 'k')



        
        fitrange = [i for i, value in enumerate(x) if (value > qmin) * (value < qmax)]
        y3 = y[fitrange]
        y3 = y3[~np.isnan(y3)]
        fitrange2 = [i for i, value in enumerate(y3) if (value > 0)]
        y3 = y3[fitrange2]
        PeakHeightAllowFactor = (np.max(y3) - np.mean(np.power(y3, 0.5)) ** 2) / 500 * PeakHeightAllow
        #print(PeakHeightAllowFactor)
        PeakBroadnessAllowFactor = (qmax - qmin) / 50 * PeakBroadnessAllow
        #print(PeakBroadnessAllowFactor)
        ## Data fitting
        fitrange = [i for i, value in enumerate(x) if (value > fitqmin) * (value < fitqmax)]
        x2 = x[fitrange]
        y2 = y[fitrange]

        peaks, properties = find_peaks(y2, prominence = PeakHeightAllowFactor, width = PeakBroadnessAllowFactor)
        prominences = peak_prominences(y2, peaks)[0]
        plt.plot(x2[peaks], y2[peaks], "rx",markersize = 10, markeredgewidth = 3)
        roughfitq = x2[peaks]
        

        #MaxNumPeaksUse = len(x2[peaks])
        MaxNumPeaksUse = 2
        
        xdat = dataCollection[:,0]
        #xx = dataCollection[:,0]
        ydat = dataCollection[:,n]

        fitrange = [i for i, value in enumerate(xdat) if (value > fitqmin2) * (value < fitqmax2)]
        xdat = xdat[fitrange]
        ydat = ydat[fitrange]

        model = LinearModel(prefix='bkg_')
        params = model.make_params(a=0, b=0)
        
        rough_peak_positions = roughfitq[0:MaxNumPeaksUse]
        
        for i, cen in enumerate(rough_peak_positions):
            peak, pars = add_peak1('lz%d_' % (i+1), cen)
            model = model + peak
            params.update(pars)

        init = model.eval(params, x=xdat)
        result = model.fit(ydat, params, x=xdat)

        comps = result.eval_components()

        peakdata02 = []
        peakdata01 = []
        
        k3 = OtherwayData[0].split('_')
        k4 = k3[whereistemp_section-1]
        peakdata01 = k4[:-1]
        
        
        for name, par in result.params.items():
            if 'center' in name:
                peakdata02 = np.array([name, par.value])
                peakdata01 = np.hstack((peakdata01,peakdata02))
        for name, par in result.params.items():
            if 'height' in name:
                peakdata02 = np.array([name, par.value])
                peakdata01 = np.hstack((peakdata01,peakdata02))
                
        for name, par in result.params.items():
            if 'fwhm' in name:
                peakdata02 = np.array([name, par.value])
                peakdata01 = np.hstack((peakdata01,peakdata02))
        
        for name, par in result.params.items():
            if 'amplitude' in name:
                peakdata02 = np.array([name, par.value])
                peakdata01 = np.hstack((peakdata01,peakdata02))
                

        
        if n == 1:
            peakdata = peakdata01
        else:
            peakdata = np.vstack((peakdata,peakdata01))
            
            
        n = n + 1    
    plt.xlabel("$\it{q}$ (A$^\mathrm{-1}$)", fontsize = 14)
    plt.ylabel("$\it{I}$ (a.u)", fontsize = 15)

    frame_Result_02.destroy()
    frame_Result_02 = LabelFrame(root, text="Result")
    frame_Result_02.grid(row=1,column=2,rowspan=4)

    canvas = FigureCanvasTkAgg(fig, frame_Result_02)   
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, frame_Result_02)
    toolbar.update()
    canvas.get_tk_widget().pack()

    # plt.xlabel("$\it{q}$ (A$^\mathrm{-1}$)", fontsize = 16)
    # plt.ylabel("$\it{I}$ (a.u)", fontsize = 17)


###################################################################################






def Dir_Open_01():
    global file_directory
    e_01.delete(0, END)
    file_directory = filedialog.askdirectory(
        initialdir= r'C:\Users\taesu\Desktop', title ="Select A File Directory",
        )
    e_01.insert(0, file_directory)



def Dir_Open_02():
    global file_directory
    e_02.delete(0, END)
    file_directory = filedialog.askdirectory(
        initialdir= r'C:\Users\taesu\Desktop', title ="Select A File Directory",
        )
    e_02.insert(0, file_directory)

def TestWhereTis():
    global WhereT_Result
    global e_13
    ThisT= e_13.get()
    ThisT = ThisT.split('_')
    ThisT_text = ""
    n=1
    for i in ThisT:
        ThisT_text = ThisT_text + "\n" + "%s  - " %(n) + i
        n=n+1
    WhereT_Result.destroy()
    WhereT_Result = Label(frame_13, text= ThisT_text).pack()

def saveClicked():
    global e_02, peakdata
    Save_Path = e_02.get()
    e = datetime.datetime.now()
    ExportFileName = ("%s%02d%02d_%s_data_%02d%02d%02d.csv" % (e.year, e.month, e.day, name, e.hour, e.minute, e.second))
    Save_Path = Save_Path + "/" + ExportFileName
    Save_Path = Save_Path.replace('\\','/')
    print(Save_Path)
    pd.DataFrame(peakdata).to_csv(Save_Path)


root = Tk()
root.title("Analysis")
root.geometry("1300x800")




OnOff_MODES = [
    ("9A","9A"),
    ("4C","4C"),
    ]

Option_Var_01 = StringVar()
Option_Var_01.set("9A")


Label(root, text = "Options",).grid(row=0, column=0)


frame_01 = LabelFrame(root, text = "Beamline")
frame_01.grid(row=1,column=0,padx=20,pady=20)

Radiobutton(frame_01, text='9A', variable=Option_Var_01 , value = "9A" ).pack(anchor=CENTER)
Radiobutton(frame_01, text='4C', variable=Option_Var_01 , value = "4C" ).pack(anchor=CENTER)

frame_11 = LabelFrame(root, text="File Directory Setting", padx= 30, pady=5)
frame_11.grid(row=2, column=0,padx=20,pady=5)

myButton = Button(frame_11, text="Data Directory", 
                  bg = "green", fg = "black", 
                  padx= 20, pady=2,
                  command=Dir_Open_01)
myButton.pack()

e_01 = Entry(frame_11, width = 30, borderwidth = 3)
e_01.pack(pady=(0,10))
e_01.insert(0,r"C:\Users\taesu\OneDrive - purdue.edu\Tjun_231114_PEG_additive\PEG_additive\CT_20231114_104928\Sample_1_20231114_104928")


myButton = Button(frame_11, text="Save Directory", 
                  bg = "light blue", fg = "black", 
                  padx= 20, pady=2,
                  command=Dir_Open_02)
myButton.pack()
e_02 = Entry(frame_11, width = 30, borderwidth = 3)
e_02.pack(pady=(0,10))
e_02.insert(0,r"C:\JunDrive\Mouse_data\Fig_data")

frame_03 = LabelFrame(root, text = "Where is temperature section", bg='lightyellow')
frame_03.grid(row=3, column=0,padx=10,pady=10)

Label(frame_03, text = "Section splited by [_]:",).pack()


e_03 = Entry(frame_03, width = 10, borderwidth = 3)
e_03.pack(pady=(0,10))
e_03.insert(0,6)

frame_13 = LabelFrame(root, text = "Test where is temperature section\nsection# / file text", bg='lightyellow')
frame_13.grid(row=0,column=1,rowspan=4, padx=10,pady=10)

Label(frame_13, text = "Put your data name",).pack()

e_13 = Entry(frame_13, width = 30, borderwidth = 3)
e_13.pack(pady=(0,10))
e_13.insert(0,"HS-0_2m_11keV_WAXS_PPMA_030c_att0_5sec_0334.dat_bsub")

myButton = Button(frame_13, text="Test", 
                  bg = "gray", fg = "black", 
                  padx= 20, pady=2,
                  command=TestWhereTis)
myButton.pack()

WhereT_Result = Label(frame_13, text= "here")
WhereT_Result.pack()

frame_12 = LabelFrame(root, text="Analysis Setting", padx= 30, pady=5)
frame_12.grid(row=4,column=0,padx=20,pady=5)


Label(frame_12, text = "q range for fitting"
      ).grid(row=0,column=0,columnspan=4, pady=(10,0))
Label(frame_12, text = "qMin/qMax =", anchor="e", width=18,
      ).grid(row=1,column=0)

e_15 = Entry(frame_12, width = 7, borderwidth = 3,
             bg = "light blue" 
      )
e_15.grid(row=1,column=1)
e_15.insert(0,"0.5")

e_16 = Entry(frame_12, width = 7, borderwidth = 3,
             bg = "#F05650"
      )
e_16.grid(row=1,column=2)
e_16.insert(0,"2.4")

Label(frame_12, text = "File Analysis Index Number"
      ).grid(row=2,column=0,columnspan=4, pady=(10,0))
Label(frame_12, text = "Start/End/Interval ="
      ).grid(row=3,column=0)


e_17 = Entry(frame_12, width = 7, borderwidth = 3,
             bg = "light blue" 
      )
e_17.grid(row=3,column=1)
e_17.insert(0,"270")

e_18 = Entry(frame_12, width = 7, borderwidth = 3,
             bg = "#F05650"
      )
e_18.grid(row=3,column=2)
e_18.insert(0,"271")

e_19 = Entry(frame_12, width = 4, borderwidth = 3,
             bg = "#CF9FFF"
      )
e_19.grid(row=3,column=3)
e_19.insert(0,"1")

Label(frame_12, text = "Fit Parameter").grid(row=4,column=0, columnspan =4)

Label(frame_12, text = "Variance =" ,anchor="e", width=18).grid(row=5,column=0)

e_101 = Entry(frame_12, width = 6, borderwidth = 3,
             bg = "#10EE90"
             )
e_101.grid(row=5,column=1)
e_101.insert(0,"0.1")

Label(frame_12, text = "Sigma =",anchor="e", width=18).grid(row=6,column=0)

e_102 = Entry(frame_12, width = 6, borderwidth = 3,
             bg = "#10EE90"
             )
e_102.grid(row=6,column=1)
e_102.insert(0,"0.1")


Label(frame_12, text = "PeakHeightAllow =" ,anchor="e", width=18).grid(row=7,column=0)

e_103 = Entry(frame_12, width = 6, borderwidth = 3,
             bg = "#10EE90"
             )
e_103.grid(row=7,column=1)
e_103.insert(0,"10")

Label(frame_12, text = "PeakBroadnessAllow =", anchor='e',  width=18).grid(row=8,column=0)

e_104 = Entry(frame_12, width = 6, borderwidth = 3,
             bg = "#10EE90"
             )
e_104.grid(row=8,column=1)
e_104.insert(0,"10")







frame_Result_01 = LabelFrame(root, text="Analysis")
frame_Result_01.grid(row=4,column=1,rowspan=2, padx=20,pady=20)



my_button = Button(frame_Result_01, text="Analyze", font = ("Times new roman",12),
       padx = 20, pady = 5,bg="green",
       command=Clicked_Analyze
                   ).grid(row=0,column=1)
my_button = Button(frame_Result_01, text="Save", font = ("Times new roman",12),
       padx = 20, pady = 5, bg='light blue',
       command=saveClicked
                   ).grid(row=0,column=2)



frame_Result_02 = LabelFrame(root, text="Result")

frame_Result_02.grid(row=1,column=2,rowspan=3)
Label(frame_Result_02, text = "result here").pack()


mainloop()


#################################################################################



# %%
