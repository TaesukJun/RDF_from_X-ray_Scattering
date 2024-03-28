from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import pygame
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
                                               NavigationToolbar2Tk) 


#####################################################################
#####################################################################

import numpy as np
import pandas as pd
import fnmatch
import os
import torch
from torchvision.io import read_image
from sklearn.model_selection import train_test_split
import pydicom
from pydicom.data import get_testdata_file
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "arial"
import statistics
import datetime

import imageio.v3 as iio
import ipympl
import skimage as ski
#import plotly.graph_objects as go

import scipy
from scipy import signal
from scipy.optimize import curve_fit
from scipy.signal import find_peaks, peak_prominences
from lmfit.models import LorentzianModel, QuadraticModel, LinearModel, VoigtModel, GaussianModel
#Download lmfit

from pptx import Presentation
from pptx.util import Cm, Inches, Pt


def find(pattern, path):
    global result
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

def add_peak1(prefix, center, amplitude=0.002, sigma=0.0075):
    peak = GaussianModel(prefix=prefix)
    pars = peak.make_params()
    pars[prefix + 'center'].set(center, max=center*(1+PeakVariance), min=center*(1-PeakVariance))
    pars[prefix + 'amplitude'].set(amplitude, min=0)
    pars[prefix + 'sigma'].set(sigma, max=setsigma, min=0)
    return peak, pars


#####################################################################
#####################################################################

root = Tk()
root.title("DCM Image Analysis")
root.iconbitmap(r'Icons\analyst.ico')
root.geometry("1200x600")

pygame.mixer.init()

###################################################################
###################################################################


def soundplay():
    pygame.mixer.music.load(r"Sounds\Nice.mp3")
    pygame.mixer.music.play(loops=0)

def soundstop():
    pygame.mixer.music.pause()

def clicked(value):
    global myLabel
    myLabel.destroy()
    myLabel = Label(frame_Result_01, text = value)
    myLabel.pack()

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

def Dir_Open_03():
    global file_directory
    e_03.delete(0, END)
    file_directory = filedialog.askdirectory(
        initialdir= r'C:\Users\taesu\Desktop', title ="Select A File Directory",
        )
    e_03.insert(0, file_directory)    

def Sample_plot(): 
    fig = Figure(figsize = (4, 4), dpi = 100) 

    y = [i**2 for i in range(101)] 

    plot1 = fig.add_subplot(111) 
  
    plot1.plot(y) 
  
    canvas = FigureCanvasTkAgg(fig, frame_Result_01)   
    canvas.draw() 
  
    # placing the canvas on the Tkinter window 
    canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar 
    toolbar = NavigationToolbar2Tk(canvas, frame_Result_01) 
    toolbar.update() 
  
    # placing the toolbar on the Tkinter window 
    canvas.get_tk_widget().pack()

def Sample_plot_02():
    global frame_Result_02
    frame_Result_02.destroy()
    frame_Result_02 = LabelFrame(root, text="Preiview Result")
    frame_Result_02.grid(row=2,column=2,rowspan=len(Option_Set)-1)
    
    fig = Figure(figsize = (4, 4), 
                 dpi = 100) 

    y = [i**2 for i in range(101)] 

    plot1 = fig.add_subplot(111) 
  
    plot1.plot(y) 
        
    canvas = FigureCanvasTkAgg(fig, frame_Result_02)   
    canvas.draw() 
  
    # placing the canvas on the Tkinter window 
    canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar 
    toolbar = NavigationToolbar2Tk(canvas, frame_Result_02) 
    toolbar.update() 
  
    # placing the toolbar on the Tkinter window 
    canvas.get_tk_widget().pack()

def Sample_plot_03():
    global frame_Result_02
    global e_17, e_18, e_01
    global e_13, e_14, e_15, e_16
    global e_11, e_12
    global Option_Var_11
    
    frame_Result_02.destroy()
    frame_Result_02 = LabelFrame(root, text="Preiview Result")
    frame_Result_02.grid(row=2,column=2,rowspan=len(Option_Set)-1)
    

    FileDir = e_01.get()
    FileDir = FileDir.replace(os.sep,"/")
    FileDir = FileDir + "/"
    FileDir = FileDir.replace('\\','/')
    
    FileIndex = round( int(e_17.get())/2 + int(e_18.get())/2)
        
    FileIndex2 = ("%04d" %(FileIndex))

    SelectData = "*_"+FileIndex2+"*"

    OtherwayData = find(SelectData, FileDir)
    
    UpImgBound = int(e_11.get())
    DownImgBound = int(e_12.get())
    
    dcm_img = pydicom.dcmread(OtherwayData[0], force=True)
    img_array = dcm_img.pixel_array

    Filt_On = Option_Var_11.get()
    if Filt_On =='On':
        np.place(img_array, img_array > UpImgBound, 0)
        np.place(img_array, img_array < DownImgBound, 0)


    fig, ax = plt.subplots(figsize = (5.5, 5.5))
    im = plt.imshow(img_array)
    fig.colorbar(im, fraction=0.045)
    
    if Filt_On =='On':
        plt.clim(DownImgBound,UpImgBound)
        
    else:
        plt.clim(3000,6000)
            
    
    
    
    
    
    
    
    
    
    plt.show()
    
    ImgFocusH = (int(e_13.get()), int(e_14.get()))
    ImgFocusW = (int(e_15.get()), int(e_16.get()))
    
    Red_Box_x = [
        int(e_15.get()),int(e_15.get()),int(e_16.get()),int(e_16.get()),int(e_15.get())
       ]
    Red_Box_y = [
        int(e_14.get()),int(e_13.get()),int(e_13.get()),int(e_14.get()),int(e_14.get())
        ]
    
    
    
    
    ax.plot(Red_Box_x,Red_Box_y,'r', linewidth=2)
    
    canvas = FigureCanvasTkAgg(fig, frame_Result_02)   
    canvas.draw() 
  
    # placing the canvas on the Tkinter window 
    canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar 
    toolbar = NavigationToolbar2Tk(canvas, frame_Result_02) 
    toolbar.update() 
  
    # placing the toolbar on the Tkinter window 
    canvas.get_tk_widget().pack()


###################################################################
###################################################################
###################################################################

def Clicked_Analyze():
    global e_01, e_02, e_03
    global e_11, e_12, e_13, e_14, e_15, e_16, e_17, e_18, e_19
    global Option_Var_01, Option_Var_02, Option_Var_03
    global Option_Var_04, Option_Var_05, Option_Var_06
    global Option_Var_11
    global FileNumStart, FileNumEnd, IntervalFile
    global FileDir, SelectData, OtherwayData
    global find
    global PeakVariance, setsigma
    global e_101, e_102
    
    afont = {'fontname':"Arial"}
    super_top = Toplevel()
    super_top.title("Analysis data")
    super_top.iconbitmap(r'Icons\ruby.ico')
    super_top.geometry("800x700")
    
    #Create Main Frame
    Scroll_main_01 = Frame(super_top)
    Scroll_main_01.pack(fill=BOTH, expand = 1)

    #Create Canvas
    Scroll_my_canvas = Canvas(Scroll_main_01)
    Scroll_my_canvas.pack(side=TOP,fill=BOTH,expand=1)

    #Add ScrollBar to Canvas
    my_scrollbar_h = ttk.Scrollbar(Scroll_main_01,orient=HORIZONTAL, command=Scroll_my_canvas.xview)
    my_scrollbar_h.pack(side=BOTTOM, fill=X)

    #Configure Canvas
    Scroll_my_canvas.configure(xscrollcommand=my_scrollbar_h.set)
    Scroll_my_canvas.bind('<Configure>',lambda e: Scroll_my_canvas.configure(scrollregion = Scroll_my_canvas.bbox("all")))


    #Create Another Frame INSIDE Canvas
    top = Frame(Scroll_my_canvas)

    #Add New Frame to Window In Canvas
    Scroll_my_canvas.create_window((0,0), window=top, anchor='nw')
    
    
    
    
    
    
    top_pos_x = 0
    
    Button(top,text="Close\nWindow",pady=20,bg="yellow", command=super_top.destroy
           ).grid(row = 0, rowspan=3, column = top_pos_x)
    top_pos_x = top_pos_x+1
    
    FileDir = e_01.get()
    FileDir = FileDir.replace(os.sep,"/")
    FileDir = FileDir + "/"
    FileDir = FileDir.replace('\\','/')

    e = datetime.datetime.now()

    Img_Save_Path = e_02.get()
    Date_Index = "/%s%02d%02d%02d%02d%02d" % (e.year, e.month, e.day, e.hour, e.minute, e.second)
    os.mkdir(Img_Save_Path + Date_Index + "_img")
    Img_Save_Path = Img_Save_Path + Date_Index + "_img"
    Img_Save_Path = Img_Save_Path + "/"
    Img_Save_Path = Img_Save_Path.replace('\\','/')

    PlotFig_Save_Path = e_03.get()
    os.mkdir(PlotFig_Save_Path + Date_Index + "_plot")
    PlotFig_Save_Path = PlotFig_Save_Path + Date_Index + "_plot"
    PlotFig_Save_Path = PlotFig_Save_Path + "/"
    PlotFig_Save_Path = PlotFig_Save_Path.replace('\\','/')
    
    print(PlotFig_Save_Path)
    
    Filt_On = Option_Var_11.get()

    UpImgBound = int(e_11.get())
    DownImgBound = int(e_12.get())

    ##############################################################
    ########## Image Focuse ##########
    ##############################################################

    ImgFocusH = (int(e_13.get()), int(e_14.get()))
    ImgFocusW = (int(e_15.get()), int(e_16.get()))

    ##############################################################
    ########## Image Result & Save Option ##########
    ##############################################################

    ## Caution: If you set yes on Show Option, there will be long results

    ImageResultShow = Option_Var_01.get()

    Image_BW_ResultShow = Option_Var_02.get()
    # Images will be saved as Black & White images ####
    
    ImgFigSave = Option_Var_03.get()

    Hist_Fig_Save = Option_Var_04.get()
    
    Hist_Peak_Mark = Option_Var_05.get()
    
    pptSave = Option_Var_06.get()
    
    Filt_On = Option_Var_11.get()

    ##############################################################
    FileNumStart, FileNumEnd, IntervalFile = (int(e_17.get()), int(e_18.get()), int(e_19.get()))
    ##############################################################
    
    Num = 1
    
    for FileIndex in range(FileNumStart,FileNumEnd+1,IntervalFile):
        print("\n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n\n")
        
        FileIndex2 = ("%04d" %(FileIndex))
        print(FileIndex2)
        SelectData = "*_"+FileIndex2+"*"
        print(SelectData)
        OtherwayData = find(SelectData, FileDir)
        print(OtherwayData[0])
        #data = np.loadtxt("%s" %(OtherwayData[0]), comments = '%',delimiter=",")
        #print(data)
        
        ###################################################################
        
        dcm_img = pydicom.dcmread(OtherwayData[0], force=True)
        img_array = dcm_img.pixel_array
        print(img_array)

        if ImageResultShow == 'On':
            fig, ax = plt.subplots()
            im = plt.imshow(img_array)
            fig.colorbar(im)
            plt.clim(3000,6000)

            plt.show()

        ##################################################################
        if Filt_On =='On':
            np.place(img_array, img_array > UpImgBound, 0)
            np.place(img_array, img_array < DownImgBound, 0)

        if ImageResultShow == 'On':
            fig, ax = plt.subplots()
            im = plt.imshow(img_array)
            fig.colorbar(im)
            #plt.clim(3000,6000)
            plt.show()

        ##################################################################
        
        img_array_selection = img_array[ImgFocusH[0]:ImgFocusH[1], ImgFocusW[0]:ImgFocusW[1]]

        if ImageResultShow == 'On':
            Label(top, text = "%02d" %(FileIndex)).grid(row=0,column=top_pos_x)
            fig, ax = plt.subplots()
            im = plt.imshow(img_array_selection)
            fig.colorbar(im)
            plt.clim(3000,6000)
            plt.show()

            canvas = FigureCanvasTkAgg(fig, top)    
            canvas.draw()
            canvas.get_tk_widget().grid(row=1,column=top_pos_x)
            
            toolbarFrame = LabelFrame(top, text = 'toolbar')
            toolbarFrame.grid(row=2,column=top_pos_x)
            toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
            toolbar.update()
            top_pos_x = top_pos_x + 1
        ##################################################################  
        
        img_array_bw = ski.util.img_as_float(img_array_selection)
        
        if Image_BW_ResultShow == 'On':
            #fig = Figure(figsize = (4, 4), dpi = 100) 
            Label(top, text = "%02d" %(FileIndex)).grid(row=0,column=top_pos_x)
            fig, ax = plt.subplots()
            im = plt.imshow(img_array_bw, cmap ="gray")
            fig.colorbar(im)
            plt.clim(0.02,0.09)
            
            canvas = FigureCanvasTkAgg(fig, top)    
            canvas.draw()
            canvas.get_tk_widget().grid(row=1,column=top_pos_x)
            top_pos_x = top_pos_x + 1

            if ImgFigSave == 'On':
                e = datetime.datetime.now()
                fig.savefig(Img_Save_Path + "%s_bw_Index%04d_%s%02d%02d%02d%02d%02d.png"
                            % (FileIndex2, Num, e.year, e.month, e.day,e.hour, e.minute, e.second))
        
        Temp_img = img_array_selection
        Temp_img[Temp_img>0] = 1
        Temp_img[Temp_img<0] = 0
        
        Count = np.sum(Temp_img)
        print("Visuable Area : ",Count)
        
        ##################################################################
        if Filt_On =='On':
            xscalerange = [0.048 , 0.065]
        else:
            xscalerange = [0.04 , 0.07]           
            
        histogram, bin_edges = np.histogram(img_array_bw, bins=256, range=(xscalerange[0], xscalerange[1]))
        #histogram[0]=0
        #histogram = histogram / max(histogram)

        histogram = signal.savgol_filter(histogram,23,3)  

        x = bin_edges[0:-1]
        y = histogram
        y[y<0] = 0
        
        
        #print(histogram)
        if Image_BW_ResultShow == 'On':

            #plt.xlim([xscalerange[0], xscalerange[1]]) 
            Label(top, text = "%02d" %(FileIndex)).grid(row=0,column=top_pos_x)
            fig, ax = plt.subplots()

            plt.title("Grayscale Histogram Sections")
            plt.xlabel("grayscale value")
            plt.ylabel("pixel count")
            plt.xlim([xscalerange[0], xscalerange[1]])  # <- named arguments do not work here
        
            plot = plt.plot(x, y)  # <- or here

            canvas = FigureCanvasTkAgg(fig, top)    
            canvas.draw()
            canvas.get_tk_widget().grid(row=1,column=top_pos_x)


            
            str_num = 0
            str1 = ""
            Label(top,text="xy data").grid(row=3, column=top_pos_x)
            for i in x:
                str1 = str1 + "\n" + str(x[str_num]) + "\t" + str(y[str_num])
                str_num = str_num + 1
            
            xyInfoText  = Entry(top, width=15, borderwidth = 2)
            xyInfoText.grid(row=4, rowspan=1000, column=top_pos_x)
            xyInfoText.insert(0, "%s" %(str1))
            # xyInfoText = Label(top)
            # xyInfoText.grid(row=3,rowspan=1, column=top_pos_x)
            # xyInfoText.insert(0, "%s" %(str1))
            # Label(top, text = "%s" %(str1)).grid(row=2,rowspan=5000, column=top_pos_x)






            
            top_pos_x = top_pos_x + 1
            
            
            
            if ImgFigSave == 'On':
                e = datetime.datetime.now()
                fig.savefig(PlotFig_Save_Path + "%s_bw_Index%04d_%s%02d%02d%02d%02d%02d.png"
                            % (FileIndex2, Num, e.year, e.month, e.day,e.hour, e.minute, e.second))

        if FileIndex == FileNumStart:
            hist_data = [x,y]
            #hist_data = np.transpose(hist_data)
            
        else:
            hist_data = np.append(hist_data,[y], axis=0)

        Num = Num + 1
        
    #######################################################################

    total_hist_num = np.shape(hist_data)
        
    avg_hist_data = np.average(hist_data[1:total_hist_num[0],:], axis=0)

    hist_data = np.append(hist_data,[avg_hist_data], axis=0)

    hist_data = np.transpose(hist_data)
    #print(hist_data)

    if Hist_Fig_Save == 'yes':
        name = 'Avg_Histogram'
        e = datetime.datetime.now()
        ExportFileName = ("%s%02d%02d_%s_data_%02d%02d%02d.csv" % (e.year, e.month, e.day, name, e.hour, e.minute, e.second))
        pd.DataFrame(hist_data).to_csv(PlotFig_Save_Path + ExportFileName, index = False)

    print("\n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n")
        
    
    fig, ax = plt.subplots()

    plt.title("Grayscale Histogram")
    plt.xlabel("grayscale value")
    plt.ylabel("pixel count")
    plt.xlim([xscalerange[0], xscalerange[1]])  # <- named arguments do not work here
    #plt.ylim([0.00, 1.0])
          
    x = hist_data[:,0]
    y = hist_data[:,total_hist_num[0]]
        
    plot_G_Hist = plt.plot(x, y)  # <- or here
    
    
    canvas = FigureCanvasTkAgg(fig, top)    
    canvas.draw()
    canvas.get_tk_widget().grid(row=1,column=top_pos_x)
    
    toolbarFrame = LabelFrame(top, text = 'toolbar')
    toolbarFrame.grid(row=2,column=top_pos_x)
    toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
    toolbar.update()

    str_num = 0
    str1 = ""
    Label(top,text="xy data").grid(row=3, column=top_pos_x)
    for i in x:
        str1 = str1 + "\n" + str(x[str_num]) + "\t" + str(y[str_num])
        str_num = str_num + 1
    
    xyInfoText  = Entry(top, width=15, borderwidth = 2)
    xyInfoText.grid(row=4, rowspan=1000, column=top_pos_x)
    xyInfoText.insert(0, "%s" %(str1))    


    top_pos_x = top_pos_x + 1
    
    
    fitGmin = 0.04
    fitGmax = 0.07
    PeakHeightAllowFactor = 25
    PeakBroadnessAllowFactor = 1


            
    fitrange = [i for i, value in enumerate(x) if (value > fitGmin) * (value < fitGmax)]

    x2 = x[fitrange]
    y2 = y[fitrange]
    y2 = y2[~np.isnan(y2)]

    peaks, properties = find_peaks(y2, prominence = PeakHeightAllowFactor, width = PeakBroadnessAllowFactor)
    prominences = peak_prominences(y2, peaks)[0]

    roughfitq = x2[peaks]

    #plt.plot(x2[peaks], y2[peaks], "rx",markersize = 10, markeredgewidth = 3)

    plt.show()

    MaxNumPeaksUse = 3

    model = LinearModel(prefix='bkg_')
    params = model.make_params(a=0, b=0)
        
    rough_peak_positions = roughfitq[0:MaxNumPeaksUse]


    PeakVariance = float(e_101.get())
    setsigma = float(e_102.get())

    for i, cen in enumerate(rough_peak_positions):
        peak, pars = add_peak1('lz%d_' % (i+1), cen)
        model = model + peak
        params.update(pars)

    init = model.eval(params, x=x)
    result = model.fit(y, params, x=x)

    comps = result.eval_components()
    
    peakdata02 = []
    peakdata01 = []
    
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
            
            
    n = 1
    peakfit_x = []    
            
            
    for name, par in result.params.items():
        if 'center' in name:
            if n == 1:
                peakfit_x = par.value
                #print("  %s: value = %f" % (name, par.value))
                Label(top,text="  %s: value = %f" % (name, par.value)).grid(row=1+2*n,column=top_pos_x)
                n = n + 1
            else:
                #print("  %s: value = %f" % (name, par.value))
                Label(top,text="  %s: value = %f" % (name, par.value)).grid(row=1+2*n,column=top_pos_x)
                peakfit_x = np.append(peakfit_x, par.value)
                n = n + 1
            
    
    
    n = 1
    amp = []
    for name, par in result.params.items():
        if 'amplitude' in name:
            if n == 1:
                amp = par.value
                #print("  %s: value = %f" % (name, par.value))
                Label(top,text="  %s: value = %f" % (name, par.value)).grid(row=2+2*n,column=top_pos_x)
                n = n + 1
            else:
                #print("  %s: value = %f" % (name, par.value))
                Label(top,text="  %s: value = %f" % (name, par.value)).grid(row=2+2*n,column=top_pos_x)
                amp = np.append(amp, par.value)
                n = n + 1

            
    fig, ax = plt.subplots()

    plt.plot(x, y, label='data')
    plt.plot(x, result.best_fit, label='best fit')
    for name, comp in comps.items():
        #plt.semilogy(xdat, comp, '--', label=name)
        plt.plot(x, comp, '--', label=name)
    plt.legend(loc='upper right')

    plt.plot(x2[peaks], y2[peaks], "rx",markersize = 10, markeredgewidth = 3)
    #plt.show()

    canvas = FigureCanvasTkAgg(fig, top)    
    canvas.draw()
    canvas.get_tk_widget().grid(row=1,column=top_pos_x)
    
    toolbarFrame = LabelFrame(top, text = 'toolbar')
    toolbarFrame.grid(row=2,column=top_pos_x)
    toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
    toolbar.update()
    top_pos_x = top_pos_x + 1            
            
            
    
    
    
    
    
            
###################################################################
###################################################################
###################################################################

OnOff_MODES = [
    ("On","On"),
    ("Off","Off"),
    ]

Option_Set = [
    
    ( "ImageResultShow" ), ( "Image_BW\nHistShow" ), ( "ImgFigSave" ), 
    ( "Hist_Fig_Save" ), ( "Hist_Peak_Mark" ),
    ( "pptSave" )
    
    ]


Option_Var_01 = StringVar()
Option_Var_01.set("Off")
Option_Var_02 = StringVar()
Option_Var_02.set("Off")
Option_Var_03 = StringVar()
Option_Var_03.set("Off")
Option_Var_04 = StringVar()
Option_Var_04.set("Off")
Option_Var_05 = StringVar()
Option_Var_05.set("Off")
Option_Var_06 = StringVar()
Option_Var_06.set("Off")

Option_Var_11 = StringVar()
Option_Var_11.set("Off")

Frame_gap_x = 18
Frame_gap_y = 2

#####################################################################
#####################################################################

Label(root, text = "Options",).grid(row=0, column=0)

n = 0
frame_01 = LabelFrame(root, text = Option_Set[n], padx= Frame_gap_x, pady=Frame_gap_y)
frame_01.grid(row=n+1,column=0,padx=20,pady=Frame_gap_y)
for text, mod in OnOff_MODES:
    Radiobutton(frame_01, text=text, variable=Option_Var_01 , value = mod ).pack(anchor=CENTER)
n = n + 1

frame_01 = LabelFrame(root, text = Option_Set[n], padx= Frame_gap_x, pady=Frame_gap_y)
frame_01.grid(row=n+1,column=0,padx=20,pady=Frame_gap_y)
for text, mod in OnOff_MODES:
    Radiobutton(frame_01, text=text, variable=Option_Var_02 , value = mod ).pack(anchor=CENTER)
n = n + 1

frame_01 = LabelFrame(root, text = Option_Set[n], padx= Frame_gap_x, pady=Frame_gap_y)
frame_01.grid(row=n+1,column=0,padx=20,pady=Frame_gap_y)
for text, mod in OnOff_MODES:
    Radiobutton(frame_01, text=text, variable=Option_Var_03 , value = mod ).pack(anchor=CENTER)
n = n + 1

frame_01 = LabelFrame(root, text = Option_Set[n], padx= Frame_gap_x, pady=Frame_gap_y)
frame_01.grid(row=n+1,column=0,padx=20,pady=Frame_gap_y)
for text, mod in OnOff_MODES:
    Radiobutton(frame_01, text=text, variable=Option_Var_04 , value = mod ).pack(anchor=CENTER)
n = n + 1

frame_01 = LabelFrame(root, text = Option_Set[n], padx= Frame_gap_x, pady=Frame_gap_y)
frame_01.grid(row=n+1,column=0,padx=20,pady=Frame_gap_y)
for text, mod in OnOff_MODES:
    Radiobutton(frame_01, text=text, variable=Option_Var_05 , value = mod ).pack(anchor=CENTER)
n = n + 1

frame_01 = LabelFrame(root, text = Option_Set[n], padx= Frame_gap_x, pady=Frame_gap_y)
frame_01.grid(row=n+1,column=0,padx=20,pady=Frame_gap_y)
for text, mod in OnOff_MODES:
    Radiobutton(frame_01, text=text, variable=Option_Var_06 , value = mod ).pack(anchor=CENTER)
n = n + 1

#####################################################################
#####################################################################

frame_11 = LabelFrame(root, text="File Directory Setting", padx= 30, pady=5)
frame_11.grid(row=3, rowspan= 3, column=1,padx=20,pady=5)

myButton = Button(frame_11, text="Data Directory", 
                  bg = "green", fg = "black", 
                  padx= 20, pady=2,
                  command=Dir_Open_01)
myButton.pack()
e_01 = Entry(frame_11, width = 50, borderwidth = 3)
e_01.pack(pady=(0,10))
e_01.insert(0,r"C:\Users\taesu\OneDrive - purdue.edu\Tjun_231114_PEG_additive\PEG_additive\CT_20231114_104928\Sample_1_20231114_104928")

myButton = Button(frame_11, text="Image Save Directory", 
                  bg = "green", fg = "black", 
                  padx= 20, pady=2,
                  command=Dir_Open_02)
myButton.pack()
e_02 = Entry(frame_11, width = 50, borderwidth = 3)
e_02.pack(pady=(0,10))
e_02.insert(0,r"C:\JunDrive\Mouse_data\Fig_data")

myButton = Button(frame_11, text="Histogram Plot Save Directory", 
                  bg = "green", fg = "black", 
                  padx= 20, pady=2,
                  command=Dir_Open_03)
myButton.pack()
e_03 = Entry(frame_11, width = 50, borderwidth = 3)
e_03.pack(pady=(0,10))
e_03.insert(0,r"C:\JunDrive\Mouse_data\Histogram_Plot_data")





################### Section 2 / Parameters ##################################################
#####################################################################


frame_12 = LabelFrame(root, text="Image Analysis Setting", padx= 30, pady=5)
frame_12.grid(row=0, rowspan= 3, column=1,padx=20,pady=5)


Label(frame_12, text = "Filter On/Off", bg = "#90EE90",
      borderwidth = 3
      ).grid(row=0,column=4)
n = 1
for text, mod in OnOff_MODES:
    Radiobutton(frame_12, text=text, variable=Option_Var_11 , value = mod 
                ).grid(row=n, column=4)
    n = n + 1

Label(frame_12, text = "Fit Parameter",bg = "#90EE90").grid(row=3,column=4)

Label(frame_12, text = "Variance" ).grid(row=4,column=4)

e_101 = Entry(frame_12, width = 6, borderwidth = 3,
             bg = "#10EE90"
             )
e_101.grid(row=5,column=4)
e_101.insert(0,"0.05")

Label(frame_12, text = "Sigma").grid(row=6,column=4)

e_102 = Entry(frame_12, width = 6, borderwidth = 3,
             bg = "#10EE90"
             )
e_102.grid(row=7,column=4)
e_102.insert(0,"0.003")


Label(frame_12, text = "Intensity Filter (Higher Num in red)"
      ).grid(row=0,column=0,columnspan=3)

Label(frame_12, text = "Upper Int. Bound ="
      ).grid(row=1,column=0)
e_11 = Entry(frame_12, width = 12, borderwidth = 3,
             bg = "#F05650"
      )
e_11.grid(row=1,column=1,columnspan=2)
e_11.insert(0,"3700")

Label(frame_12, text = "Lower Int. Bound ="
      ).grid(row=2,column=0)
e_12 = Entry(frame_12, width = 12, borderwidth = 3,
             bg = "light blue"
      )
e_12.grid(row=2,column=1,columnspan=2)
e_12.insert(0,"3240")

Label(frame_12, text = "Area of Interest (FOV)"
      ).grid(row=3,column=0,columnspan=3, pady=(10,0))

Label(frame_12, text = "Vertical From/To(pixel) = "
      ).grid(row=4,column=0)
e_13 = Entry(frame_12, width = 6, borderwidth = 3,
             bg = "light blue"
      )
e_13.grid(row=4,column=1)
e_13.insert(0,"200")
e_14 = Entry(frame_12, width = 6, borderwidth = 3,
             bg = "#F05650"
      )
e_14.grid(row=4,column=2)
e_14.insert(0,"400")

Label(frame_12, text = "Horizontal From/To(pixel) = "
      ).grid(row=5,column=0)
e_15 = Entry(frame_12, width = 6, borderwidth = 3,
             bg = "light blue" 
      )
e_15.grid(row=5,column=1)
e_15.insert(0,"140")
e_16 = Entry(frame_12, width = 6, borderwidth = 3,
             bg = "#F05650"
      )
e_16.grid(row=5,column=2)
e_16.insert(0,"365")


Label(frame_12, text = "File Analysis Index Number"
      ).grid(row=6,column=0,columnspan=4, pady=(10,0))
Label(frame_12, text = "Start/End/Bin ="
      ).grid(row=7,column=0)


e_17 = Entry(frame_12, width = 7, borderwidth = 3,
             bg = "light blue" 
      )
e_17.grid(row=7,column=1)
e_17.insert(0,"280")

e_18 = Entry(frame_12, width = 7, borderwidth = 3,
             bg = "#F05650"
      )
e_18.grid(row=7,column=2)
e_18.insert(0,"330")

e_19 = Entry(frame_12, width = 4, borderwidth = 3,
             bg = "#CF9FFF"
      )
e_19.grid(row=7,column=3)
e_19.insert(0,"15")






#####################################################################
#####################################################################



frame_Result_01 = LabelFrame(root, text="Analysis")
frame_Result_01.grid(row=0,column=2,rowspan=2, padx=20,pady=20)


my_button = Button(frame_Result_01, text="Preview", font = ("Times new roman",12),
       padx = 20, pady = 5,
       command=Sample_plot_03
                   ).grid(row=0,column=0)

my_button = Button(frame_Result_01, text="Analyze", font = ("Times new roman",12),
       padx = 20, pady = 5,
       command=Clicked_Analyze
                   ).grid(row=0,column=2)

my_button = Button(frame_Result_01, text="Test", font = ("Times new roman",12),
       padx = 20, pady = 5,
       command=Sample_plot_02
                   ).grid(row=0,column=3)

#####################################################################
#####################################################################

frame_Result_02 = LabelFrame(root, text="Preiview result")
frame_Result_02.grid(row=2,column=2,rowspan=len(Option_Set)-1)

fig = Figure(figsize = (4, 4), dpi = 100) 
  
canvas = FigureCanvasTkAgg(fig, frame_Result_02)   
canvas.draw() 
  
# placing the canvas on the Tkinter window 
canvas.get_tk_widget().pack()
  
# creating the Matplotlib toolbar 
toolbar = NavigationToolbar2Tk(canvas, frame_Result_02) 
toolbar.update() 
  
# placing the toolbar on the Tkinter window 
canvas.get_tk_widget().pack()

#####################################################################
#####################################################################




Dialog_Index_Row = 0
Dialog_Index_Col = 3


my_button = Button(root, text="Nice", bg = '#ABCD00', font = ("Times new roman",12),
       padx = 20, pady = 5,
       command=soundplay
                   ).grid(
                       row=Dialog_Index_Row+0, column=Dialog_Index_Col+0, 
                       padx = 10, pady = 5
                       )

my_button = Button(root, text="Exit", bg ="yellow", font = ("Times new roman",12),
       padx = 20, pady = 5, command=root.destroy
                   ).grid(
                       row=Dialog_Index_Row+1, column=Dialog_Index_Col+0, 
                       padx = 10, pady = 5
                       )







"""
stop_button = Button(
    root, text="Stop", font = ("Times new roman",32),
    padx = 20, pady = 20,
    command=soundstop
    
    ).pack(padx = 20, pady = 20)
"""





mainloop()