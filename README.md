# 📱 Phone Number Info Tool

A simple Python GUI application that helps users retrieve detailed information about a phone number — including its region, carrier, and time zone — using the `phonenumbers` library.

## ✨ Features
* Easy-to-use GUI built with Tkinter
* Parses and validates international phone numbers
* Displays:

  * City or region
  * Country/region code
  * Carrier/service provider
  * Time zones

## 🚀 Getting Started

### Prerequisites

Ensure Python is installed (preferably 3.7 or above).

Install required packages:

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python gui.py
```

## 🛠️ Project Structure

```
📁 Phone_Number_Info
│
├── gui.py             # Main GUI application
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

## 🧰 Dependencies

From `requirements.txt`:

* **phonenumbers**: For number parsing and metadata lookup
* **tkinter**: Built-in Python library for GUI (usually pre-installed)

> ⚠️ If you're using a Linux environment, you might need to install Tkinter separately:

```bash
sudo apt-get install python3-tk
```

## 📸 Example Input

**Input:** `+14155552671`
**Output:**

```
City/Region: California
Region Code: US
Carrier: AT&T
Timezones: America/Los_Angeles
```

## 📌 Notes

* Use international format (e.g., `+91`, `+1`, etc.).
* Application handles invalid phone numbers gracefully.

## 👌 Contributing

Feel free to fork the repository, improve the UI or functionality, and submit a pull request!
