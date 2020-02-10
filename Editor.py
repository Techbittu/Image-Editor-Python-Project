import tkinter as tk
from tkinter import Tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox as ms
from PIL import Image,ImageEnhance,ImageFilter
import os
win = tk.Tk()
win.title("Is-Image Shop")
win.minsize(600,400)
# win.configure(background="black")
# win.wm_iconbitmap("icon.iso")

def menu():                                #   start menu
    pass

 
def clear():
    img_hight_Entry.delete("",tk.END)
    img_width_Entry.delete("",tk.END)
    Sharpness_Entry.delete("",tk.END)
    Color_Entry.delete("",tk.END)
    Brightness_Entry.delete("",tk.END)
    Blur_Entry.delete("",tk.END)
    Contrast_Entry.delete("",tk.END)

def show():
    img = Image.open("editedimg.jpg")
    img.show("editedimg.jpg")

def browser():                           #---------------------------Browse
    global folder_path
    filename = filedialog.askopenfilename()
    folder_path.set(filename)
    return filename

def software():
    raise ms.showinfo("Software Info","Company : asktohow \n Owner : Deepak Kumar Arya \n Domain : www.asktohow.com")

def Version():
    raise ms.showinfo("Version","Version info : 1.0001 \n Date : 6/07/2019 \n Time : 6:28 PM")


menubar = tk.Menu(win)
file_menu = tk.Menu(menubar,tearoff=0)
file_menu.add_command(label="New",command=clear)
file_menu.add_command(label="Open",command=browser)
file_menu.add_separator
file_menu.add_command(label="Save",command=show)


edit_menu = tk.Menu(menubar,tearoff=0)
edit_menu.add_command(label="Software",command=software)
edit_menu.add_command(label="Version",command=Version)
edit_menu.add_separator
menubar.add_cascade(label="File",menu=file_menu)
menubar.add_cascade(label="About",menu=edit_menu)              # end menu


main_label_frame = ttk.LabelFrame(win,text="Find Image")
main_label_frame.grid(row=0,column=0)

label_frame = ttk.LabelFrame(main_label_frame,text="Image Editing Detail")        # lable frema
label_frame.grid(row=0,column=0)

#                     -----  Image Hight

img_hight_Lable = ttk.Label(label_frame,text="Enter Hight in Pixel:")
img_hight_Lable.grid(row=2 ,column=0,padx=10,pady=10,sticky=tk.W)

img_height = tk.IntVar()

img_hight_Entry = ttk.Entry(label_frame,textvariable=img_height,width=10)
img_hight_Entry.grid(row=2,column=1,padx=10,pady=10,sticky=tk.W)

#------------------------  Image Width

img_width_Lable = ttk.Label(label_frame,text="Enter Width in Pixel:")
img_width_Lable.grid(row=2 ,column=2,padx=10,pady=10,sticky=tk.W)

img_width = tk.IntVar()

img_width_Entry = ttk.Entry(label_frame,textvariable=img_width,width=10)
img_width_Entry.grid(row=2,column=3,padx=10,pady=10,sticky=tk.E)

#-----------------------   Sharpness

Sharpness_Lable = ttk.Label(label_frame,text="Sharpness (-5 to +5):")
Sharpness_Lable.grid(row=3 ,column=0,padx=10,pady=10,sticky=tk.W)

Sharpness_var = tk.IntVar()

Sharpness_Entry = ttk.Entry(label_frame,textvariable=Sharpness_var,width=10)
Sharpness_Entry.grid(row=3,column=1,padx=10,pady=10,sticky=tk.E)

#-------------------------  Color

Color_Lable = ttk.Label(label_frame,text="Color (-5 to +5):")
Color_Lable.grid(row=4 ,column=0,padx=10,pady=10,sticky=tk.W)

Color_var = tk.IntVar()

Color_Entry = ttk.Entry(label_frame,textvariable=Color_var,width=10)
Color_Entry.grid(row=4,column=1,padx=10,pady=10,sticky=tk.E)

#---------------------- Brightness

Brightness_Lable = ttk.Label(label_frame,text="Brightness (-5 to +5):")
Brightness_Lable.grid(row=5 ,column=0,padx=10,pady=10,sticky=tk.W)

Brightness_var = tk.IntVar()

Brightness_Entry = ttk.Entry(label_frame,textvariable=Brightness_var,width=10)
Brightness_Entry.grid(row=5,column=1,padx=10,pady=10,sticky=tk.E)

#-----------------  Contrast

Contrast_Lable = ttk.Label(label_frame,text="Contrast (-5 to +5):")
Contrast_Lable.grid(row=6 ,column=0,padx=10,pady=10,sticky=tk.W)

Contrast_var = tk.IntVar()

Contrast_Entry = ttk.Entry(label_frame,textvariable=Contrast_var,width=10)
Contrast_Entry.grid(row=6,column=1,padx=10,pady=10,sticky=tk.E)

#------------------- Blur

Blur_Lable = ttk.Label(label_frame,text="Blur (-5 to +5):")
Blur_Lable.grid(row=7 ,column=0,padx=10,pady=10,sticky=tk.W)

Blur_var = tk.IntVar()

Blur_Entry = ttk.Entry(label_frame,textvariable=Blur_var,width=10)
Blur_Entry.grid(row=7,column=1,padx=10,pady=10,sticky=tk.E)


                                          


folder_path = tk.StringVar()

# file_name = (browser())

ab =  ttk.Label(main_label_frame,textvariable=folder_path)
ab.grid(row=1,column=0,padx=20,pady=20,)
button = ttk.Button(main_label_frame,text="Browse Image",command=browser)
button.grid(row=1,column=0,padx=10,pady=20,sticky=tk.W)               #--------------------Browse end


# ---------------  Ok button

def func():
    global folder_path
    filename = (browser())
    hight = img_height.get()
    width = img_width.get()
    sharpness = Sharpness_var.get()
    contrast = Contrast_var.get()
    color = Color_var.get()
    brightness = Brightness_var.get()
    blur = Blur_var.get()
    img = Image.open(f"{filename}")
    
    if hight != 0  and width != 0:
        size = (hight,width)                        # change size
        img.thumbnail(size)
        img.save("editedimg.jpg")
    if sharpness == -5<sharpness>5:
        enhancer = ImageEnhance.Sharpness(img)                   # Sharpness
        enhancer.enhance(sharpness).save("editedimg.jpg")
    if contrast == -5<contrast>5:                                #contrast
        enhancer = ImageEnhance.Contrast(img)
        enhancer.enhance(contrast).save("editedimg.jpg")
    if brightness == -5<brightness>5:                            #brightness
        enhancer = ImageEnhance.Brightness(img)
        enhancer.enhance(brightness).save("editedimg.jpg")
    if color == -5<color>5:                                      #color
        enhancer = ImageEnhance.Color(img)
        enhancer.enhance(color).save("editedimg.jpg")
    if blur == -5<blur>5:                                        #blur
        img.filter(ImageFilter.GaussianBlur(radius=blur)).save("editedimg.jpg")

    img_hight_Entry.delete("",tk.END)
    img_width_Entry.delete("",tk.END)
    Sharpness_Entry.delete("",tk.END)
    Color_Entry.delete("",tk.END)
    Brightness_Entry.delete("",tk.END)
    Blur_Entry.delete("",tk.END)
    Contrast_Entry.delete("",tk.END)

    
            


  
show_button = ttk.Button(win,text="Show",command=show)
show_button.grid(row=1,column=1)

Clear_button = ttk.Button(win,text="Clear",command=clear)
Clear_button.grid(row=1,columnspan=2)


Sub_button = ttk.Button(win,text="OK",command=func)
Sub_button.grid(row=1,column=0,padx=10,pady=10,sticky=tk.W)


win.config(menu=menubar)
win.mainloop()