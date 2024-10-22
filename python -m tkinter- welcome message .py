
# Importing the tkinter module
import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()

# Set the window title
root.title("Welcome")

# Set the window size
root.geometry("400x250")

# Function to display the welcome message
def show_welcome_message():
    messagebox.showinfo("Welcome", "Welcome to My GitHub (Chiman-Badri)")

# Create a button that will trigger the welcome message
welcome_button = tk.Button(root, text="Click Me for Welcome Message", command=show_welcome_message)

# Place the button in the window
welcome_button.pack(pady=20)

# Run the application
root.mainloop()
