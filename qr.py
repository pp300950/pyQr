import qrcode

qr = qrcode.QRCode(
    version=1,  #ขนาดของQRcode (1-40)
    error_correction=qrcode.constants.ERROR_CORRECT_L, 
    box_size=10,  #ขนาดของแต่ละช่องในQRcod
    border=4,  #อบขอQRcod
)

#ข้อมูลที่จะใส่QR
data = "https://pantip.com/topic/36243141"
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("barbecued_code.png")

print("QR code ได้ถูกสร้างและบันทึกเป็นไฟล์ barbecued_code.png")