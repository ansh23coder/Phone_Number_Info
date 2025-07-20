import tkinter as tk
from tkinter import messagebox
import phonenumbers
from phonenumbers import geocoder, carrier, timezone


def get_number_info(number: str):
    try:
        parsed = phonenumbers.parse(number)

        if not phonenumbers.is_valid_number(parsed):
            return "Invalid phone number.", None

        location = geocoder.description_for_number(parsed, "en")
        region = geocoder.region_code_for_number(parsed)
        service_provider = carrier.name_for_number(parsed, "en") 
        timezones = timezone.time_zones_for_number(parsed)

        info = {
            "City/Region": location,
            "Region Code": region,
            "Carrier": service_provider,
            "Timezones": ", ".join(timezones)
        }
        return None, info

    except Exception as e:
        return str(e), None


def on_lookup():
    number = entry.get()
    error, info = get_number_info(number)
    if error:
        messagebox.showerror("Error", error)
    else:
        result_text.set(
            "\n".join([f"{k}: {v}" for k, v in info.items()])
        )


# Setup GUI
root = tk.Tk()
root.title("Phone Number Info Tool")
root.geometry("400x300")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill="both", expand=True)

tk.Label(frame, text="Enter Phone Number (+CountryCodeNumber):").pack(anchor="w")

entry = tk.Entry(frame, width=30)
entry.pack(pady=5)

tk.Button(frame, text="Lookup", command=on_lookup).pack(pady=10)

result_text = tk.StringVar()
result_label = tk.Label(frame, textvariable=result_text, justify="left", anchor="w")
result_label.pack(fill="both", expand=True)

root.mainloop()
