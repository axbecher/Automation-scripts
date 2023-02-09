import tkinter as tk

class UrlForm:
    def __init__(self, master):
        self.master = master
        self.master.title("Save URLs")
        self.dark_mode = False


        self.mode_button = tk.Button(self.master, text="Dark/Light mode", command=self.switch_mode, height=2, width=15, bg="#645CBB", relief="flat", bd=0, activebackground="#BFACE2", activeforeground="#03001C", fg="white")
        self.mode_button.config(highlightbackground="#645CBB", highlightcolor="#645CBB", highlightthickness=1)
        self.mode_button.pack(pady=5)

        self.urls_text = tk.Text(self.master, height=30, width=150)
        self.urls_text.pack()

        self.load_button = tk.Button(self.master, text="Load URLs", command=self.load_urls, height=2, width=15, bg="#645CBB", relief="flat", bd=0, activebackground="#BFACE2", activeforeground="#03001C", fg="white")
        self.load_button.config(highlightbackground="#645CBB", highlightcolor="#645CBB", highlightthickness=1)
        self.load_button.pack(pady=5)

        self.save_button = tk.Button(self.master, text="Save URLs", command=self.save_urls, height=2, width=15, bg="#645CBB", relief="flat", bd=0, activebackground="#BFACE2", activeforeground="#03001C", fg="white")
        self.save_button.config(highlightbackground="#645CBB", highlightcolor="#645CBB", highlightthickness=1)
        self.save_button.pack(pady=5)

        self.clear_button = tk.Button(self.master, text="Clear", command=self.clear_text, height=2, width=15, bg="#645CBB", relief="flat", bd=0, activebackground="#BFACE2", activeforeground="#03001C", fg="white")
        self.clear_button.config(highlightbackground="#645CBB", highlightcolor="#645CBB", highlightthickness=1)
        self.clear_button.pack(pady=5)

        self.quit_button = tk.Button(self.master, text="Quit", command=self.master.quit, height=2, width=15, bg="#645CBB", relief="flat", bd=0, activebackground="#BFACE2", activeforeground="#03001C", fg="white")
        self.quit_button.config(highlightbackground="#645CBB", highlightcolor="#645CBB", highlightthickness=1)
        self.quit_button.pack(pady=5)

        self.label_text = tk.StringVar()
        self.label = tk.Label(self.master, textvariable=self.label_text)
        self.label.pack()
        
    def switch_mode(self):
        if self.dark_mode:
            self.master.config(bg="#FFFFFF")
            self.urls_text.config(bg="#FFFFFF", fg="#000000")
            self.load_button.config(bg="#645CBB", fg="white", activebackground="#BFACE2", activeforeground="#03001C")
            self.save_button.config(bg="#645CBB", fg="white", activebackground="#BFACE2", activeforeground="#03001C")
            self.clear_button.config(bg="#645CBB", fg="white", activebackground="#BFACE2", activeforeground="#03001C")
            self.quit_button.config(bg="#645CBB", fg="white", activebackground="#BFACE2", activeforeground="#03001C")
            self.label.config(fg="#000000")
            self.dark_mode = False
        else:
            self.master.config(bg="#000000")
            self.urls_text.config(bg="#000000", fg="#FFFFFF")
            self.load_button.config(bg="#BFACE2", fg="#03001C", activebackground="#645CBB", activeforeground="white")
            self.save_button.config(bg="#BFACE2", fg="#03001C", activebackground="#645CBB", activeforeground="white")
            self.clear_button.config(bg="#BFACE2", fg="#03001C", activebackground="#645CBB", activeforeground="white")
            self.quit_button.config(bg="#BFACE2", fg="#03001C", activebackground="#645CBB", activeforeground="white")
            self.label.config(fg="#FFFFFF")
            self.dark_mode = True

    def switch_mode(self):
        if self.dark_mode:
            self.master.configure(bg='black')
            self.urls_text.configure(bg='black', fg='white')
            self.mode_button.configure(bg='#645CBB', fg='white')
            self.dark_mode = False
        else:
            self.master.configure(bg='white')
            self.urls_text.configure(bg='white', fg='black')
            self.mode_button.configure(bg='#645CBB', fg='black')
            self.dark_mode = True

    def load_urls(self):
        try:
            with open("urls.txt", "r") as f:
                content = f.read()
                self.urls_text.delete("1.0", tk.END)
                self.urls_text.insert("1.0", content)
                self.label_text.set("URLs loaded successfully")
        except FileNotFoundError:
            self.urls_text.delete("1.0", tk.END)
            self.label_text.set("No URLs to load")

    def save_urls(self):
        try:
            with open("urls.txt", "w") as f:
                content = self.urls_text.get("1.0", tk.END)
                f.write(content)
            self.urls_text.delete("1.0", tk.END)
            self.label_text.set("URLs saved successfully")
        except:
            self.urls_text.delete("1.0", tk.END)
            self.label_text.set("Error saving URLs")

    def clear_text(self):
        self.urls_text.delete("1.0", tk.END)
        self.label_text.set("")

root = tk.Tk()
url_form = UrlForm(root)
root.mainloop()