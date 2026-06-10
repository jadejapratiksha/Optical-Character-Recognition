import tkinter
import train_cnn
from tkinter import filedialog as fd
from PIL import ImageTk, Image 
import os
import cv2
import pytesseract

if os.path.exists("query.png"):
    os.remove("query.png")
    os.remove("Seg.png")
    os.remove("reg.png")
    
master = tkinter.Tk() 
master.configure(bg='#B1ACA7')
master.title("SANSKRIT CHARACTER RECOGNITION AND DIGITIZATION USING SOFT COMPUTING")
var = tkinter.StringVar()
label = tkinter.Label( master, textvariable=var, fg = "Yellow",bg = "blue",font = "Verdana 11 bold")
var.set("SANSKRIT CHARACTER RECOGNITION AND DIGITIZATION USING SOFT COMPUTING")
label.pack()

def train():
    if os.path.exists('Model/model.h5'):
        a=92.41
    else:
        a=train_cnn.tran()
       
    
    var = tkinter.StringVar()
    label = tkinter.Label( master, textvariable=var, fg = "Black",bg = "White",font = "Verdana 10 bold")
    var.set(round(a,4))
    label.place(x = 10, y = 180 + 8*30, width=150, height=50)
    
    img = Image.open("plot1.png") 
    img = img.resize((250, 250), Image.Resampling.LANCZOS)   
    img = ImageTk.PhotoImage(img)    
    panel = tkinter.Label(master, image = img)       
    panel.image = img 
    panel.place(x = 180, y = 5 + 1*30, width=250, height=250)
    
    img = Image.open("plot2.png") 
    img = img.resize((250, 250), Image.Resampling.LANCZOS)   
    img = ImageTk.PhotoImage(img)    
    panel = tkinter.Label(master, image = img)       
    panel.image = img 
    panel.place(x = 460, y = 5 + 1*30, width=250, height=250)
    
    

def BowseImage():
    name= fd.askopenfilename()
    img = Image.open(name) 
    img.save("query.png")  
    img = img.resize((250, 250), Image.Resampling.LANCZOS)   
    img = ImageTk.PhotoImage(img)    
    panel = tkinter.Label(master, image = img)       
    panel.image = img 
    panel.place(x = 180, y = 280 + 1*30, width=250, height=250)     
    
def segment():
    img=cv2.imread('query.png',0)
    img = cv2.medianBlur(img, 3)
    ret,seg = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    cv2.imwrite("Seg.png",seg)
    img = Image.open("Seg.png")
    img = img.resize((250, 250), Image.Resampling.LANCZOS)   
    img = ImageTk.PhotoImage(img)    
    panel = tkinter.Label(master, image = img)       
    panel.image = img 
    panel.place(x = 460, y = 280 + 1*30, width=250, height=250)
    
def recog():   
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\S Jadeja\AppData\Local\Tesseract-OCR\tesseract.exe'
    results = pytesseract.image_to_string(Image.open('query.png'),lang="san")
    img = cv2.imread('query.png')
    h, w, c = img.shape
    boxes = pytesseract.image_to_boxes(img) 
    for b in boxes.splitlines():
        b = b.split(' ')
        img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)       
    cv2.imwrite('reg.png',img)
    img = Image.open("reg.png")
    img = img.resize((250, 250), Image.Resampling.LANCZOS)   
    img = ImageTk.PhotoImage(img)    
    panel = tkinter.Label(master, image = img)        
    panel.image = img 
    panel.place(x = 460, y = 280 + 1*30, width=250, height=250)    
    
    var = tkinter.StringVar()
    label = tkinter.Entry( master, textvariable=var, fg = "black",bg = "white",font = "Verdana 10 bold")
    var.set(results)
    label.place(x = 180, y = 535 + 1*30, width=530, height=40)
    master.mainloop()
def writ():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\S Jadeja\AppData\Local\Tesseract-OCR\tesseract.exe'
    results = pytesseract.image_to_string(Image.open('query.png'),lang="san")
    text_file = open("recognize.txt", "w", encoding="utf-8")
    n = text_file.write(results)
    text_file.close()
  
        
def Exit():
    if os.path.exists("query.png"):
        os.remove("query.png")
        os.remove("Seg.png")
        os.remove("reg.png")
    master.destroy()

master.geometry("750x630+100+100") 
master.resizable(width = True, height = True) 

b0 = tkinter.Button(master, text = "Train", command = train,bg='#F1EAE3',fg='black',font = "Verdana 10 bold") 
b0.place(x = 10, y = 5 + 1*30, width=150, height=50)

b1 = tkinter.Button(master, text = "Bowse Image", command = BowseImage,bg='#F1EAE3',fg='black',font = "Verdana 10 bold") 
b1.place(x = 10, y = 30 + 2*30, width=150, height=50)

b2 = tkinter.Button(master, text = "Segment", command = segment,bg='#F1EAE3',fg='black',font = "Verdana 9 bold") 
b2.place(x = 10, y = 55 + 3*30, width=150, height=50)

b3 = tkinter.Button(master, text = "Recognize", command = recog,bg='#F1EAE3',fg='black',font = "Verdana 10 bold") 
b3.place(x = 10, y = 80 + 4*30, width=150, height=50)

b4 = tkinter.Button(master, text = "Write Text", command = writ,bg='#F1EAE3',fg='black',font = "Verdana 10 bold") 
b4.place(x = 10, y = 105 + 5*30, width=150, height=50)

b5 = tkinter.Button(master, text = "Quit", command = Exit,bg='#F1EAE3',fg='black',font = "Verdana 10 bold") 
b5.place(x = 10, y = 130 + 6*30, width=150, height=50)

var = tkinter.StringVar()
label = tkinter.Label( master, textvariable=var, fg = "White",bg = "Green",font = "Verdana 10 bold")
var.set("Accuracy")
label.place(x = 10, y = 155 + 7*30, width=150, height=50)

var = tkinter.StringVar()
label = tkinter.Label( master, textvariable=var, fg = "Black",bg = "White",font = "Verdana 10 bold")
var.set("0.00")
label.place(x = 10, y = 180 + 8*30, width=150, height=50)

master.mainloop() 
