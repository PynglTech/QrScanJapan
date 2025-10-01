import qrcode

# 1. This is the correct direct link to your image.
image_url = "https://i.ibb.co/v6pc8kFZ/image1.jpg"

# 2. Configure and create the QR code object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# 3. Add the image URL data to the QR code
qr.add_data(image_url)
qr.make(fit=True)

# 4. Create the image from the QR code object
img = qr.make_image(fill_color="black", back_color="white")

# 5. Save the final QR code image.
img.save("13. Terracotta Vase.png")

print("Successfully generated the final QR code!")
print("File saved as: final_image_qr.png")