import qrcode 
import image 

qr = qrcode.QRCode(
    version = 15,
    box_size =10,
    border = 5
)

data = " money transfer this side"
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "red", back_colour = "blue")
img.save("test.png")