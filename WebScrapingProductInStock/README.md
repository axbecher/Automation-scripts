## Table of Contents

1. Product Availability Checker
2. Terms used in the table
   - Availability
   - Product name
   - URL
   - Timestamp
3. How does it work
   - Connection to server
   - Accessing URLs
   - Emailing results
4. For the program to work correctly
5. Requirements
6. Configuration
7. Usage
8. How does it work?
9. Support
10. License

# Product Availability Checker
A python script for web scraping to check if a product exists on a website and create a HTML table with 4 columns: Availability, Product Name, URL, and Timestamp.

# Terms used in the table:
- **Availability:** If the product from the urls.txt is in stock or not;
- **Product name:** Extracted from the URL;
- **URL:** Extracted from urls.txt;
- **Timestamp:** The moment when the check was performed;

# How does it work:

- Using your email and password, the program connects to the selected server in order to send emails to the recipient;
- In the "to" field (recipient), you need to add either your own email or the email where you want to receive the output;
- After running the program, if everything goes according to plan (**see below**);
- The program will access each link mentioned in the urls.txt file;
- After accessing each link, you should receive an HTML table via email to the recipient mentioned in the "to" field, containing the columns availability, product name, url, and timestamp;

# For the program to work correctly:
- Ensure that you have all the requirements.txt installed. ( pip install -r requirements.txt )
- Make sure that you have selected the correct server in credentials.py by adding your email and password.
- Make sure you have internet connection when running the program.

# Requirements

Python 3.6 or later
Required packages listed in requirements.txt
To install the required packages, run the following command in your terminal:

```sh
pip install -r requirements.txt
```
# Configuration

The script requires user to add email credentials in credentials.py file.

- email
- password
- recipient email
- server preference

# Usage
To run the script, use the following command in your terminal:
```sh
python main.py
```

# How does it work?
- The script will generate a HTML table with 4 columns: Availability, Product Name, URL, and Timestamp.


# Support
For any questions or support, please contact me via https://axbecher.com/contact/

# License
This project is licensed under the MIT License.
