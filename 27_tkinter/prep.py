import tkinter

window = tkinter.Tk()
window.title("My first window")
window.minsize(width=500, height=300)

# labels
my_label = tkinter.Label(text="I am a label", font=("Iosevka", 24, "bold"))

# the pack function adds the label to the screen and centers it.
# without the pack, the label isnt visible.
my_label.pack()

# assign new properties to the label
# this is possible due to kwargs
my_label["text"] = "New Text"
my_label.config(text="new text")

# buttons


def button_clicked():
    """ gets the contents of the entry field """
    print("i got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


# use the command to assign the function to the button.
# note you just write the name, without the parentheses.
button = tkinter.Button(text="click meh", command=button_clicked)
button.pack()

input = tkinter.Entry(width=10)
input.pack()


# this line always needs to be at the bottom of the program
window.mainloop()
