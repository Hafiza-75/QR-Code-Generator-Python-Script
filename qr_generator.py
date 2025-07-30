import qrcode
from PIL import Image

def generate_qr_code(data, filename="my_qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    img.show()
    print(f"✅ QR Code saved as '{filename}' and opened successfully.")

if __name__ == "__main__":
    user_data = input("🔗 Enter text or URL to encode into a QR code: ")
    file_name = input("💾 Enter filename to save (with .png extension): ").strip()

    if not file_name:
        file_name = "my_qrcode.png"
    elif not file_name.endswith(".png"):
        file_name += ".png"

    generate_qr_code(user_data, file_name)
