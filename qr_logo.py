import qrcode
from PIL import Image
import qrcode.constants

url = "https://forms.gle/ddMRf7o4aN1GZnyw9"

qr = qrcode.QRCode(
    version=5, # controls the size of a qr
    error_correction=qrcode.constants.ERROR_CORRECT_H, # High error correction (allows, adding logo)
    box_size=15, 
    border=4
)
qr.add_data(url)
qr.make(fit=True)

# Create the QR code image
qr_img = qr.make_image(fill="black", 
                       back_color="white").convert("RGB")

# Open and resize logo
logo = Image.open("logo.jpg")
logo_size = (qr_img.size[0]//5,
             qr_img.size[1]//5)

logo = logo.resize(logo_size,
                   Image.LANCZOS)

if logo.mode != "RGBA":
    logo = logo.convert("RGBA")

mask = logo.split()[3]

# Calculate the position to paste the logo at the center
qr_width, qr_height = qr_img.size
logo_width, logo_height = logo.size
logo_position = ((qr_width - logo_width) // 2, 
                 (qr_height-logo_height) // 2)

# Paste the logo onto the QR code
qr_img.paste(logo, logo_position, mask=logo)

#save the QR code with logo
qr_img.save("qr_with_logo.png")

print("QR code with logo generated successfully!")