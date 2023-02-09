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
        df.insert(0, "Index", range(1, 1+len(df)))
        
    def color_pink(row):
        color = 'background-color: springgreen' if row['Availability'] == 'Exists' else 'background-color: lightcoral'
        return [color] * len(row)    

    return (df.style.apply(color_pink, axis=1)
              .set_properties(**{'text-align': 'center', 'font-size': '15px'})
              .hide_index())

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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

    # Convert the dataframe to html
    
    html_table = df.to_html(index=False, classes=["dataframe"])

    # Define the body of the email with HTML
    body = f"""
    <html>
    <head>
        <style>
        body {{
            background-color: gainsboro;
        }}
        .dataframe thead th {{
            padding: 10px;
            padding-right: 15px;
            font-size: 25px;
            font-weight: bold;
            text-align: center;
        }}
        .dataframe thead th {{
            font-size: 25px;
            font-weight: bold;
            padding-right: 15px;
        }}
        .header {{
            font-size: 50px;
            text-align: center;
            background-clip: text;
            background-color: white;
            -webkit-background-clip: text;
            -webkit-text-fill-color: linear-gradient(to right, #f80759, #f5d50e, #64dd17, #0288d1, #7117ea, #ea00c9);
        }}
        .table-container {{
        margin: 20px;
        border: 1px solid black;
        padding: 15px;
        padding-right: 10px;
        color: black;
        text-align: center;
        }}
        </style>
    </head>
    <body style="background-color: gainsboro;">
            <h1 class="header" style="font-size: 50px; text-align: center; background: linear-gradient(to right, #f80759, #f5d50e, #64dd17, #0288d1, #7117ea, #ea00c9); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Products inventory check</h1>
            <div class="table-container">
                <style>
                    .dataframe thead th {{
                        padding: 10px;
                        font-size: 25px;
                        font-weight: bold;
                        text-align: center;
                    }}
                    .dataframe tbody td {{
                        background-color: {{ 'Exists' == df.at[0, 'Availability']  ? 'springgreen' : 'lightcoral' }};
                    }}
                </style>
                {html_table}
            </div>
    </body>
    </html>
    """

    msg.attach(MIMEText(body, 'html'))

    # Send the email
    server_credential = credentials.server
    server = smtplib.SMTP(server_credential, 587)
    server.starttls()
    server.login(email_user, email_password)
    text = msg.as_string()
    server.sendmail(email_user, to, text)
    server.quit()


if __name__ == '__main__':
    df = check_inventoryBothExists()
    send_email(df)
    print('Finish')
