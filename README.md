**📧 Email Validator Project**

**📌 Description**

In today's digital world, invalid email addresses cause failed deliveries, poor user experience, and data quality issues in applications. Whether it's a registration form, a mailing list, or a contact system, validating email input is a critical step.
This project aims to solve this real-life problem by using Python's regex-based pattern matching to validate, extract details from, and format email addresses. It provides clean error handling and a modular structure for easy integration into any Python application.

**🎯 Objectives**

1.To validate email address formats in real-time

2.To alert users when an email is empty or incorrectly formatted

3.To extract the username and domain from a valid email

4.To support email formatting (uppercase/lowercase)

5.To improve data quality and input reliability in applications


**🚀 Features**

✅ Email Format Validation

⚠️ Custom Exception Handling (InvalidEmailError)

🔍 Username & Domain Extraction

🔡 Email Formatting (Uppercase / Lowercase)

🐍 Modular Python Design

💻 Clean Console Output


**⚙️ How It Works**

1.User provides an email address as input

2.The system checks if the email is empty or missing

3.A regex pattern validates the email format

4.If invalid, a custom InvalidEmailError is raised with the reason

5.If valid, username and domain are extracted and the email is formatted as needed


**🛠️ Technologies Used**

🐍 Python – Core language used for validation logic and processing

🔤 Regex (re module) – Used for pattern matching and email format validation

⚠️ Custom Exceptions – InvalidEmailError for meaningful error messages

📦 Modular Architecture – Separate files for validator, exceptions, and main runner

💻 GitHub – Used for project hosting and version control

**💻 Code**

Run the program:

python main.py

**📜 License**

Licensed under the MIT License.
