import qrcode
import os

# Define the name of the file containing the URLs
urls_file = 'urls.txt'

# Define a folder to save the QR codes
output_folder = 'qr_codes'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# --- QR Code Customization ---
# You can change the size and border of the QR codes here
box_size = 10
border = 4
# -----------------------------

print(f"Reading URLs from {urls_file}...")

try:
    # Open the file and read each line
    with open(urls_file, 'r') as file:
        # 'enumerate' gives us a counter (i) starting from 1
        for i, line in enumerate(file, 1):
            # Remove any leading/trailing whitespace from the URL
            url = line.strip()
            
            # Skip empty lines
            if not url:
                continue

            # Create a QR code object
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=box_size,
                border=border,
            )
            
            # Add the URL data to the QR code
            qr.add_data(url)
            qr.make(fit=True)
            
            # Create an image from the QR code object with colors
            img = qr.make_image(fill_color="black", back_color="white")
            
            # Define the filename for the QR code image
            filename = f"qr_code_{i}.png"
            filepath = os.path.join(output_folder, filename)
            
            # Save the image file
            img.save(filepath)
            
            print(f"({i}/23) Successfully created {filename} for URL: {url}")

    print(f"\nAll QR codes have been generated and saved in the '{output_folder}' folder.")

except FileNotFoundError:
    print(f"Error: The file '{urls_file}' was not found. Please create it and add your URLs.")
except Exception as e:
    print(f"An error occurred: {e}")