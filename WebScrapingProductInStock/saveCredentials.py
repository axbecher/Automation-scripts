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

root = tk.Tk()
root.geometry("350x300")
root.title("Save Credentials")

emailULabel = tk.Label(root, text="Email User")
emailULabel.pack()
emailU = tk.Entry(root, width=40)
emailU.pack()

emailPLabel = tk.Label(root, text="Email Password")
emailPLabel.pack()
emailP = tk.Entry(root, show="*", width=40)
emailP.pack()

serverLabel = tk.Label(root, text="Server")
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

recipientLabel = tk.Label(root, text="Who will receive this email / output / html / table ?")
recipientLabel.pack()
recipient = tk.Entry(root,width=40)
recipient.pack()

saveButton = tk.Button(root, text="Save", command=save_credentials)
saveButton.pack()

root.mainloop()