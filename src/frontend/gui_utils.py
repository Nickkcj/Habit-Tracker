from tkinter import messagebox

def show_error_message():
    messagebox.showerror(title="Error", message="Something wrong happened. Try again.")

def show_success_message():
    messagebox.showinfo(title="Success", message="Operation was successful.")

