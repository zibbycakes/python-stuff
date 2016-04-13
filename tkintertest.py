import Tkinter as tkinter

window = tkinter.Tk()

#window.title("Super cool window")
window.geometry("300x300")

#create a label
label = tkinter.Label(window, text="Label")
#create a text entry
entry = tkinter.Entry(window)
#create a button
button = tkinter.Button(window, text="Button")

#set the window's background color to the hexcode '#cb2027'
window.configure(background="#cb2027")

#now let's recreate the label so that it's background matches the window bg
label = tkinter.Label(window, text="Label", bg="#cb2027");

#now let's recreate the button with fg and bg colors!
button = tkinter.Button(window, text="Button", bg="#595959", fg="#cb2027")

#you can also add images but I don't have any right now so...
#can only use gifs or pgm/ppm images, unless using Python Imaging Library
#photo = tkinter.PhotoImage(file="title.gif")
#w = tkinter.Label(window,image=photo)
#w.pack()

#let's pack the widgets into the window in the order we want them to appear
label.pack()
entry.pack()
button.pack()

window.mainloop()
