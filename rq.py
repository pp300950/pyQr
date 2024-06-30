import cv2
from pyzbar.pyzbar import decode

image_path = "qqtess.png"
image = cv2.imread(image_path)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
data = decode(gray_image)

if data:
    for qr_code in data:
        qr_data = qr_code.data.decode('utf-8')
        print(f"QR Code มีข้อมูลเป็น: {qr_data}")
else:
    print("ไม่เจอQRCodeในภาพ")
