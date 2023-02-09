import tkinter as tk

class UrlForm:
    def __init__(self, master):
        self.master = master
        self.master.title("Save URLs")

        self.urls_text = tk.Text(self.master, height=10, width=50)
        self.urls_text.pack()

        self.load_button = tk.Button(self.master, text="Load URLs", command=self.load_urls)
        self.load_button.pack()

        self.save_button = tk.Button(self.master, text="Save URLs", command=self.save_urls)
        self.save_button.pack()

        self.clear_button = tk.Button(self.master, text="Clear", command=self.clear_text)
        self.clear_button.pack()

        self.quit_button = tk.Button(self.master, text="Quit", command=self.master.quit)
        self.quit_button.pack()

        self.label_text = tk.StringVar()
        self.label = tk.Label(self.master, textvariable=self.label_text)
        self.label.pack()

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