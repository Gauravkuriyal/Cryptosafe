# Cryptosafe - Secure Data Encryption and Storage

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)

## Introduction

Cryptosafe is a secure platform built using Django, where users can store their data in encrypted form. Users provide their email for authentication, after which their data is encrypted and a unique key is provided to the user after encryption. The key is essential for decrypting and retrieving the data, and Cryptosafe ensures that even the system administrators cannot recover the original data if the key is lost. In case of unauthorized access, the data is locked, and the user is notified via provided email.

## Features

- *Data Encryption*: Users' data is encrypted using multiple cryptographic algorithms.
- *Unique Decryption Key*: Each encrypted data entry is associated with a unique key required to retrieve or delete the data.
- *Email Authentication*: Users authenticate via email before data encryption.
- *Secure Data Storage*: The original data and decryption key are never stored in the database.
- *Unauthorized Access Protection*: If unauthorized access is detected, data is locked, and a notification email is sent.
- *Different Ciphers for Similar Data*: Even if two entries have the same content, they generate different cipher forms for enhanced security.

## Technologies Used

- *Backend*: Django (Python)
- *Frontend*: HTML, CSS, JavaScript
- *Database*: SQLite
- *Cryptography*: Multiple cryptographic algorithms for enhanced security like Vigenere Cipher, Caesar Cipher and Rail Fence Cipher.

## Installation

1. *Clone the repository:*

2. *Navigate to project directory*

    ```bash
   cd Cryptosafe
3. *Install dependencies*

    ```bash
   pip install -r requirements.txt
4. *Set up mail service*

   In settings.py in Cryptosafe provide your email id and email host password through which you would want to send the mails for authentication service (OTP) and alert mails to user.
   <br>
    In <b>settings.py </b> fill your email and password at the specified position:
    <br>
    ```bash
    EMAIL_HOST_USER = "Enter your mail here"
    EMAIL_HOST_PASSWORD = "Enter your mail's app password here"
5. *Apply migrations*

    ```bash
   python manage.py makemigrations
   python manage.py migrate
6. *Run the server*

    ```bash
   python manage.py runserver
7. *Open the app browser*

   Go to : http://127.0.0.1:8000/

## Usage

1. Go to Store page and select whether you would like to upload a text file or type your data manually.

2. On selecting the desired option it's corresponding fields will appear. Fill out the fields with your data with your email-id in the required field.

3. An OTP will be sent to the provided email. On entering of the correct OTP the Unique key will be provided to you (keep it safe and secure).

4. Use the key to retrieve or delete the data as per the requirement at their respective pages.