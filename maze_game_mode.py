from tkinter import *
from PIL import ImageTk,Image
m=Tk()
m.geometry("700x700+330+0")
m.title("Maze Game")
image1 = Image.open('mg_front_page.jpg')
img_copy = image1.copy()
image3 = ImageTk.PhotoImage(image1)

def BB1():
  m.destroy()
  import maze_game_easy
def BB2():
  m.destroy()
  import maze_game_medium
def BB3():
  m.destroy()
  import maze_game_difficult
def Resize_image(event):
    new_width = 700
    new_height = 700
    image4 = img_copy.resize((new_width, new_height))
    image5 = ImageTk.PhotoImage(image4)
    label.config(image=image5)
    label.image = image5  # avoid garbage collection
label = Label(m, image=image3);label.pack(fill=BOTH, expand = YES);label.bind('<Configure>',Resize_image)
B1=Button(m,text="Easy",command= BB1, width=15, height = 3,bg='#b380ff',cursor="dot");B1.place(x=295,y=420)
B2=Button(m,text="Medium",command= BB2, width=15, height = 3,bg='#b380ff',cursor="dot");B2.place(x=295,y=481)
B3=Button(m,text="Difficult",command= BB2, width=15, height = 3,bg='#b380ff',cursor="dot");B3.place(x=295,y=542)
m.mainloop()
