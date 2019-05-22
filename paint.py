from tkinter import *
# by Canvas I can't save image, so i use PIL
import PIL
from PIL import Image, ImageDraw
from nafile import letter



def save():
    filename = 'test/image.png'
    image1.save(filename)
    w = Label(root, text=letter(), height= 5)
    w.pack()


def paint(event):
    x1, y1 = (event.x), (event.y)
    x2, y2 = (event.x + 1), (event.y + 1)
    cv.create_oval((x1, y1, x2, y2), fill='black', width=10)
    #  --- PIL
    draw.line((x1, y1, x2, y2), fill='black', width=10)


root = Tk()

cv = Canvas(root, width=640, height=480, bg='white')
# --- PIL
image1 = PIL.Image.new('RGBA', (640, 480),  (0, 0, 0, 0))
draw = ImageDraw.Draw(image1)
# ----
cv.bind('<B1-Motion>', paint)
cv.pack(expand=YES, fill=BOTH)

btn_save = Button(text="save", command=save)
btn_save.pack()

root.mainloop()