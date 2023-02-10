import tkinter as tk

def save_credentials():
    email_user = emailU.get()
    email_password = emailP.get()
    option_selected = server.get()
    to = recipient.get()

    with open("credentials.py", "w") as f:
        f.write(f"# User email: \n")
        f.write(f"email_user = '{email_user}'\n")
        f.write(f"# User password: \n")
        f.write(f"email_password = '{email_password}'\n")
        f.write(f"# Server for Office, details -> https://domar.com/pages/smtp_pop3_server \n")
        f.write(f"server = '{option_selected}'\n")
        f.write(f"# Who will receive this email / output / html / table ? \n")
        f.write(f"to = '{to}'\n")
        f.write(f"# Created using saveCredentials.py \n")

    root.destroy()

def switch_mode():
    global mode
    if mode == "dark":
        mode = "light"
        switch_button.configure(text="Switch to Dark Mode", font=font)
        root.configure(bg="white")
        emailULabel.configure(bg="white", fg="black")
        emailPLabel.configure(bg="white", fg="black")
        serverLabel.configure(bg="white", fg="black")
        recipientLabel.configure(bg="white", fg="black")
        saveButton.configure(bg="white", fg="black", font=font)
    else:
        mode = "dark"
        switch_button.configure(text="Switch to Light Mode", font=font)
        root.configure(bg="black")
        emailULabel.configure(bg="black", fg="white")
        emailPLabel.configure(bg="black", fg="white")
        serverLabel.configure(bg="black", fg="white")
        recipientLabel.configure(bg="black", fg="white")
        saveButton.configure(bg="black", fg="white")

mode = "light"

root = tk.Tk()
root.geometry("500x450")
root.title("Save Credentials")

switch_button = tk.Button(root, text="Switch to Dark Mode", command=switch_mode, font=("Helvetica", 16), padx=10, pady=10)
switch_button.pack()

font = ("TkDefaultFont", 14)

emailULabel = tk.Label(root, text="Email User", font=font)
emailULabel.pack()
emailU = tk.Entry(root, width=40, font=font)
emailU.pack()

emailPLabel = tk.Label(root, text="Email Password", font=font)
emailPLabel.pack()
emailP = tk.Entry(root, show="*", width=40, font=font)
emailP.pack()

serverLabel = tk.Label(root, text="Server", font=font)
serverLabel.pack()
server = tk.StringVar(root)

options = [("Office 365 - smtp.office365.com", "smtp.office365.com"),
           ("Gmail - smtp.gmail.com", "smtp.gmail.com"),
           ("Yahoo - smtp.mail.yahoo.com", "smtp.mail.yahoo.com"),
           ("Outlook.com - smtp-mail.outlook.com", "smtp-mail.outlook.com")]

server.set(options[0][1])

serverOption = tk.OptionMenu(root, server, *[item[0] for item in options])
serverOption.config(width=40)
serverOption.pack()

recipientLabel = tk.Label(root, text="Who will receive this email / output / html / table ?", font=font)
recipientLabel.pack()
recipient = tk.Entry(root,width=40, font=font)
recipient.pack()

saveButton = tk.Button(root, text="Save", command=save_credentials, font=font)
saveButton.pack()

root.mainloop()