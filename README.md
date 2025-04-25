# 📍 Phone Number Geolocator

This script uses a phone number to retrieve the **region**, **service provider**, and generate a map with a marker showing the **approximate location** of the number using `phonenumbers`, `OpenCageGeocode`, and `folium`.

> ⚠️ Note: This does **not** return the real-time or exact location of a device — only a general area based on the number's prefix/registration.

---

## 🚀 Features

- Detects the **general region** of a phone number (e.g., city or province)
- Identifies the **mobile carrier** (e.g., MTN, Vodacom)
- Uses **OpenCage Geocoder API** to convert region names into coordinates
- Generates an interactive **HTML map** with a marker on the location

---

## 🧰 Requirements

Install the required packages:

```bash
pip install folium
pip install opencage
pip install phonenumbers
```

---

## 🔑 Setup

1. Get a free API key from [OpenCage Geocoder](https://opencagedata.com/)
2. Replace the `key = "yourAPIKEY"` line in the script with your actual API key.
3. Ensure your phone number is defined in a file called `test.py` like this:

```python
# test.py
number = "+27123456789"  # Replace with the number you want to track
```

---

## ▶️ Usage

Run the script:

```bash
python your_script_name.py
```

Output:
- Region and carrier printed in the console
- A map file called `mylocation.html` saved to your project folder
- Open the file in any browser to view the result

---

## 🛑 Limitations

- Does **not** show live GPS location.
- Accuracy depends on the number's registration location, not current position.
- OpenCage may not return precise coordinates if the region is vague.

---

## 📌 Example

If `number = "+27821234567"` is from South Africa, the output might be:

```
Detected region: Gauteng
Carrier: MTN
Coordinates: -26.2708, 28.1123
Map saved as mylocation.html
```

---

## 📃 License

This project is open-source and free to use for educational or non-commercial purposes.
