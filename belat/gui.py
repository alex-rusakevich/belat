import tkinter as tk
import tkinter.filedialog as tf
from tkinter import scrolledtext as st

import belat.worker as bw

class Belat_GUI:
    def __init__(self, version):
        # Standards
        self.transl_opts = ["Scheme"]
        # File type (txt, epub, etc.)
        self.file_types = ["txt", "epub", "fb2"]
        # Encodings
        self.encodings = ["utf8", "cp1251", "koi8-r"]
        # Direction
        self.direction = "Cyr-to-lat"

        self.window = tk.Tk()
        self.window.title("belat")
        self.window.geometry("477x275")
        self.window.resizable(width=False, height=False)

        # Standards panel
        self.transl_opts_var = tk.StringVar(self.window)
        self.transl_opts_var.set(self.transl_opts[0])
        self.transl_list = tk.OptionMenu(self.window, self.transl_opts_var,
            *self.transl_opts)
        self.transl_list.config(width=35)
        self.transl_list.grid(row=1, column=1)

        # File type panels
        self.file_types_var = tk.StringVar(self.window)
        self.file_types_var.set(self.file_types[0])
        self.fl_types_list = tk.OptionMenu(self.window, self.file_types_var,
            *self.file_types)
        self.fl_types_list.config(width=35)
        self.fl_types_list.grid(row=2, column=1)

        # File in
        self.file_in_path = tk.StringVar()
        self.file_in_path_entry = tk.Entry(textvariable=self.file_in_path)
        self.file_in_path_entry.config(width=41)
        self.file_in_path_entry.grid(row=3, column=1)
        self.open_button = tk.Button(self.window, text="Open...", command=self.open_file)
        self.open_button.config(width=15)
        self.open_button.grid(row=3, column=2, sticky="nesw")

        # File out
        self.file_out_path = tk.StringVar()
        self.file_out_path_entry = tk.Entry(textvariable=self.file_out_path)
        self.file_out_path_entry.config(width=41)
        self.file_out_path_entry.grid(row=4, column=1)
        self.save_button = tk.Button(self.window, text="Save...", command=self.save_file)
        self.save_button.config(width=15)
        self.save_button.grid(row=4, column=2, sticky="nesw")

        # Encodings
        # Encoding from
        self.enc_from_var = tk.StringVar(self.window)
        self.enc_from_var.set(self.encodings[0])
        self.enc_from_list = tk.OptionMenu(self.window, self.enc_from_var,
            *self.encodings)
        self.enc_from_list.config(width=10)
        self.enc_from_list.grid(row=3, column=3)
        # Encoding to
        self.enc_to_var = tk.StringVar(self.window)
        self.enc_to_var.set(self.encodings[0])
        self.enc_to_list = tk.OptionMenu(self.window, self.enc_to_var,
            *self.encodings)
        self.enc_to_list.config(width=10)
        self.enc_to_list.grid(row=4, column=3)

        # Lat to cyr or cyr to lat button
        self.dir_button = tk.Button(self.window, text=self.direction, command=self.lat_cyr)
        self.dir_button.config(width=7)
        self.dir_button.grid(row=1, column=2, rowspan=2, sticky="nesw")

        # Status panel
        self.log_entry = st.ScrolledText()
        self.log_entry.config(width=57, height=9, state="disabled")
        self.log_entry.place(x=2, y=125)

        # Start button
        self.start_button = tk.Button(self.window, text="Start!")
        self.start_button.config(width=7, command=self.start_worker)
        self.start_button.grid(row=1, column=3, rowspan=2, sticky="nesw")

        self.log("Hello! Belat's version is "+version+"\n")

    def start_worker(self):
        self.log("Starting...\n")
        worker = bw.Worker(self, self.file_in_path.get(), self.file_out_path.get(), 
            self.enc_from_var.get(), self.enc_to_var.get(), self.direction)


    def log(self, txt=""):
        self.log_entry.config(state="normal")
        self.log_entry.insert(tk.END, txt)
        self.log_entry.config(state="disabled")
        
        if txt == "":
            return self.log_entry.get(1.0, tk.END)

    def open_file(self):
        self.file_in_path.set(
            tf.askopenfilename(filetypes=[("All types", "*.*")])
        )

    def save_file(self):
        self.file_out_path.set(
            tf.asksaveasfilename(filetypes=[("All types", "*.*")])
        )

    def lat_cyr(self):
        if self.direction == "Cyr-to-lat":
            self.direction = "Lat-to-cyr"
            self.dir_button.config(text=self.direction)
        elif self.direction == "Lat-to-cyr":
            self.direction = "Cyr-to-lat"
            self.dir_button.config(text=self.direction)
        
    def start(self):
        self.log("Loading schemes...\n")
        
        self.transl_opts = []
        for i in bw.Worker.get_schemes_from_json(self.log):
            self.transl_opts.append(i.name)
            self.log("Loaded "+i.name+"\n")
        
        self.transl_opts_var = tk.StringVar(self.window)
        self.transl_opts_var.set(self.transl_opts[0])
        self.transl_list = tk.OptionMenu(self.window, self.transl_opts_var,
            *self.transl_opts)
        self.transl_list.config(width=35)
        self.transl_list.grid(row=1, column=1)

        self.log("Schemes loaded!\n")

        self.window.mainloop()
