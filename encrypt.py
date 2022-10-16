from cProfile import label
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Encryption/Decryption")
root.geometry("300x250")
l1 = Label(root, text = "Encryption and Decryption", font = "Helvetica 14 bold", foreground = "blue")
l1.pack()

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
encrypt_label = Label(root, text = "Enter key")     
b1 = Button(root, text="Encrypt",relief = RAISED, command = encrypt_image)
b1.place(x=90, y=20)

entry1 = Text(root, height=1, width=10)
entry1.place(x=70, y=70)
root.mainloop()