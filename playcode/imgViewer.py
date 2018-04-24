from tkinter import Tk, ttk, PhotoImage
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from os import getcwd

class imageViewer:
    def __init__(self, root):
        self.window = root
        self.img = ttk.Label(self.window, text='Select a img to begin...')
        self.img.pack() 
        self.indexLabel = ttk.Label(self.window, text='0 of 0')
        self.indexLabel.pack()
        self.browseBtn = ttk.Button(self.window, text='Browse', command=self._browse)
        self.prevBtn = ttk.Button(self.window, text='<', command=self._prev)
        self.prevBtn.pack()
        self.nextBtn = ttk.Button(self.window, text='>', command=self._next)
        self.nextBtn.pack()
        self.browseBtn.pack()
        self.imgList = []
        self.currIndex = 0


        self.window.mainloop()

    def _browse(self):
        print("browsing")
        path = askopenfilename(title='Select a new image',
                initialdir=getcwd(),
                filetypes=(("Images", "*.png"),
                        ("Images", "*.jpg"),
                        ("Images", "*.jpeg"),
                        ("Images", "*.gif"),
                        ('All Files', "*.*"),
                        ))
        image = Image.open(path)
        tkimage = ImageTk.PhotoImage(image)
        self._newImage(tkimage)

    def _newImage(self, image):
        self.img.config(image=image)
        self.imgList.append(image)
        length = len(self.imgList)
        self.indexLabel.config(text = str(length) + ' of ' + str(length))
        self.currIndex = length - 1
    
    def _prev(self):
        if self.currIndex - 1 < 0:
            return
        self.currIndex -= 1
        self.img.config(image=self.imgList[self.currIndex])
        self.indexLabel.config(text = str(self.currIndex + 1) + ' of ' + str(len(self.imgList)))
        
    def _next(self):
        if self.currIndex + 1 >= len(self.imgList):
            return
        self.currIndex += 1
        self.img.config(image=self.imgList[self.currIndex])
        self.indexLabel.config(text = str(self.currIndex + 1) + ' of ' + str(len(self.imgList)))

root = Tk()
imgViewer = imageViewer(root)
