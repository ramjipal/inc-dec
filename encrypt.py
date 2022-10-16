from cProfile import label
from tkinter import *
from tkinter import filedialog
def on_entry(button):
     button.bind('<Enter>', func = lambda e: button.config(background = "green", foreground = "white"))
def on_leave(button):
     button.bind('<Leave>', func = lambda e: button.config(background = "SystemButtonFace", foreground= "black"))
     
root = Tk()
root.title("Encryption/Decryption")
root.geometry("350x300")
root.config(bg="#494D5F")
l1 = Label(root, text = "Encryption and Decryption", font = "Helvetica 14 bold underline", foreground = "light blue",bg="#494D5F")
l1.pack(pady = 15)

def encrypt_image():
     file1= filedialog.askopenfile(mode='r', filetype=[('jpg file', '*.jpg')])
     if file1 is not None:
          print(file1)
          # entry1 = Tk.Entry(root)
          file_name = file1.name
          # print(file_name)
          key = entry1.get (1.0, END)
          print(file_name, key)
          fi = open(file_name, "rb")
          image = fi.read()
          fi.close()
          image = bytearray(image)
          for index,values in enumerate(image):
               image[index] = values^int(key)
          fi1 = open(file_name, 'wb')
          fi1.write(image)
          fi1.close() 
encrypt_label = Label(root, text = "Enter key:", font = "Helvetica 12 bold",fg= "white", bg="#494D5F")  
encrypt_label.place(x = 20, y = 80)   
entry1 = Text(root, height=1.4, width=21, font = "Helvetica 12 bold")
entry1.place(x=110, y=80)
b1 = Button(root, text="Encrypt",relief = RAISED, command = encrypt_image, width = 10, height = 2, font = "Helvetica 9 bold")
b1.place(x=115, y=120)
on_entry(b1)
on_leave(b1)

b2 = Button(root, text="Decrypt",relief = RAISED, command = encrypt_image, width = 10, height = 2, font = "Helvetica 9 bold")
b2.place(x=215, y=120)
on_entry(b2)
on_leave(b2)

root.mainloop()