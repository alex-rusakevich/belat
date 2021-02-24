import tkinter as tk
from tkinter import scrolledtext as st

class Belat_GUI:
    def __init__(self, version):
        # Standards
        self.transl_opts = ["1"]
        # File type (txt, epub, etc.)
        self.file_types = ["txt"]

        self.window = tk.Tk()
        self.window.title("belat")
        self.window.geometry("400x250")
        self.window.resizable(width=False, height=False)

        # Standards panel
        self.transl_opts_var = tk.StringVar(self.window)
        self.transl_opts_var.set(self.transl_opts[0])
        self.transl_list = tk.OptionMenu(self.window, self.transl_opts_var,
            *self.transl_opts)
        self.transl_list.config(width=35)
        self.transl_list.grid(row=1, column=1)

        # Text panel
        self.file_types_var = tk.StringVar(self.window)
        self.file_types_var.set(self.file_types[0])
        self.fl_types_list = tk.OptionMenu(self.window, self.file_types_var,
            *self.file_types)
        self.fl_types_list.config(width=35)
        self.fl_types_list.grid(row=2, column=1)

        # Start button
        self.start_button = tk.Button(self.window, text="Start!")
        self.start_button.config(width=19)
        self.start_button.grid(row=1, column=2, rowspan=2, sticky="nesw")

        # File in
        self.file_in_path = tk.StringVar()
        self.file_in_path_entry = tk.Entry(textvariable=self.file_in_path)
        self.file_in_path_entry.config(width=41)
        self.file_in_path_entry.grid(row=3, column=1)
        self.open_button = tk.Button(self.window, text="Open...")
        self.open_button.config(width=19)
        self.open_button.grid(row=3, column=2, sticky="nesw")

        # File out
        self.file_out_path = tk.StringVar()
        self.file_out_path_entry = tk.Entry(textvariable=self.file_out_path)
        self.file_out_path_entry.config(width=41)
        self.file_out_path_entry.grid(row=4, column=1)
        self.save_button = tk.Button(self.window, text="Save...")
        self.save_button.config(width=19)
        self.save_button.grid(row=4, column=2, sticky="nesw")

        # Status panel
        self.log_entry = st.ScrolledText()
        self.log_entry.config(width=47, height=8, state="disabled")
        self.log_entry.place(x=2, y=115)

        self.log("Hello! Belat's version is "+version+"\n")

    def log(self, txt=""):
        self.log_entry.config(state="normal")
        self.log_entry.insert(tk.END, txt)
        self.log_entry.config(state="disabled")
        
        if txt == "":
            return self.log_entry.get(1.0, tk.END)

    def start(self):
        self.window.mainloop()
