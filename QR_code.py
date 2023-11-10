import qrcode
qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
usuario= input("Escreva o que deseja transcrever para QR CODE: ")
qr.add_data(usuario)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("QR_CODE.png")