from tkinter import *
from tkinter.ttk import *
from time import strftime

# Create the main window
root = Tk()

# Set the title of the window
root.title("Clock tutorial by Broth")


def time():
    # Format the current time as a string
    string = strftime("%H:%M:%S %p")

    # Update the text of the label with the new time string
    Label.config(text=string)

    # Schedule the time function to be called again after 1 second
    Label.after(1000, time)


# Create a label to display the time
Label = Label(root, font=("ds-digital", 80),
              background="black", foreground="cyan")

# Add the label to the window and position it in the center
Label.pack(anchor='center')

# Start the clock
time()

# Enter the main event loop
mainloop()
