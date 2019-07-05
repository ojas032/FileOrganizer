from tkinter import filedialog
import tkinter as tk
import fsort

window=tk.Tk()
content = tk.StringVar()
def file(): 
    window.filename =  filedialog.askdirectory()
    print (window.filename)
    set_Text=window.filename
    content.set(set_Text)
    fsort.organise(set_Text)
    return

window.geometry("400x180") 
window.configure(background='black')
label=tk.Label(window,text="FileSort",fg="mediumseagreen",bg="black",padx="100")
label.config(font=("Courier", 30))
label.grid(row=0,column=0,columnspan=3)

label=tk.Label(window,text="Enter the path of the folder",bg="black",fg="white",pady="5",padx="-100")
label.config(font=("Arial", 12))
label.grid(row=1,column=0)


e1=tk.Entry(width=30 ,textvariable=content)
e1.grid(row=2,column=0)

#b1=tk.Button(window,text="Sort",bg="mediumseagreen",fg="white",)
b1 = tk.Button(window, command=file)
img = tk.PhotoImage(file="Capture.png") # make sure to add "/" not "\"
b1.config(image=img)
b1.grid(row=2,column=1)

window.mainloop()


