import tkinter as tk #helps create GUI
from tkinter import filedialog, Text 
import os #allows us to run apps

root = tk.Tk() #the root is the body (whole app structure)
apps = []

if os.path.isfile("save.txt"): #if file was previously opened, will give back the file in terminal when GUI is opened again
    with open("save.txt", "r") as f:
        tempApps = f.read()
        tempApps = tempApps.split(",")
        apps = tempApps
        apps = [x for x in tempApps if x.strip()] #strips out all empty spaces for when you do not select a file


def addApp():
    for widget in frame.winfo_children(): #gives access to everything that is in the frame
        widget.destroy() #removes the previous things pushed on the frame after every use of button

    filename = filedialog.askopenfilename(initialdir="/", title="Select File", #this gives the command to the openfile button
                                        filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app) #runs the apps selected in openFile

#creating canvas
canvas = tk.Canvas(root, height = 700, width = 700, bg = "#263D42") #applies a canvas to the root
canvas.pack() #attaches the canvas to the root

#adding frame
frame = tk.Frame(root, bg="white")
frame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1) #relx and rely centre the frame

#adding buttons
openFile = tk.Button(root, text = "Open File", padx = 10, pady = 5, fg="white", bg="#263D42", command=addApp) #can attach to root or frame
openFile.pack()
runApps = tk.Button(root, text = "Run Apps", padx = 10, pady = 5, fg="white", bg="#263D42", command=runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack() #keeps the apps in the GUI after opening and closing

root.mainloop() #runs the GUI

with open("save.txt", "w") as f: #when we close the GUI, it saves it as a text file to remember what was previously selected
    for app in apps:
        f.write(app + ",")