
import pyqrcode

text = input("Enter the text to generate QR code:")

qr_code = pyqrcode.create(text)

qr_code.svg('B:\Python\project\qr_code.svg', scale = 8)
