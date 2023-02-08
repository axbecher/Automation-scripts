import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def get_page_html(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    page = requests.get(url, headers=headers)
    #print(page.status_code)
    return page.content

def check_item_in_stock(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    out_of_stock_divs = soup.findAll("div", {"class": "flex items-center text-green text-13px leading-tight -tracking-0.39 undefined"})
    #print(out_of_stock_divs)
    return len(out_of_stock_divs) != 0

#def check_inventory_onlyExist():
    with open("urls.txt", "r") as file:
        urls = file.readlines()
        new_entry_line = "__New entry line in file__\n"
        entries = []
        for url in urls:
            url = url.strip()  # remove the newline character
            product_name = url.split('/')[-4]
            page_html = get_page_html(url)
            if check_item_in_stock(page_html):
                # Get current timestamp
                current_timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
                # Add the data to the list of entries
                entries.append(current_timestamp + " - " + product_name + " - EXIST - " + url)
        # Write the entries to the file
        with open("logger.txt", "r+") as f:
            content = f.read()
            f.seek(0, 0)
            if entries:
                f.write(new_entry_line + "\n".join(entries) + "\n" + content)
            else:
                f.write(content)

def check_inventoryBothExists():
    with open("urls.txt", "r") as file:
        urls = file.readlines()
        entries = []
        for url in urls:
            url = url.strip()
            product_name = url.split('/')[-4]
            page_html = get_page_html(url)
            current_timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
            if check_item_in_stock(page_html):
                entries.append(["Exists", product_name, url, current_timestamp])
            else:
                entries.append(["Not Exists", product_name, url, current_timestamp])
        df = pd.DataFrame(entries, columns=["Availability", "Product Name", "URL", "Timestamp"])
        return df

def send_email(df):
    import credentials
    # Define email details
    email_user = credentials.email_user
    email_password = credentials.email_password
    to = credentials.to
    subject = 'Inventory Report'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = to
    msg['Subject'] = subject
    body = 'Inventory Report'
    msg.attach(MIMEText(body, 'plain'))

    # Convert the dataframe to html and attach it as an html file
    df.to_html("logger.html", index=False)
    filename = "logger.html"
    attachment = open(filename, "rb")
    part = MIMEBase('application', "octet-stream")
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)

    # Send the email
    server_credential = credentials.server
    server = smtplib.SMTP(server_credential, 587) #editServer
    server.starttls()
    server.login(email_user, email_password)
    text = msg.as_string()
    server.sendmail(email_user, to, text)
    server.quit()

if __name__ == '__main__':
    df = check_inventoryBothExists()
    send_email(df)
    print('Finish')