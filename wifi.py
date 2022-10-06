# Script to generate a WiFi QR Code in png
# pip install wifi_qrcode_generator

import wifi_qrcode_generator as wifi

# Generate WiFi QR Code
qrcode = wifi.generate_qrcode("WiFi Name", False, "WPA", "Password")

# Save QR Code
qrcode.save("WiFi.png")