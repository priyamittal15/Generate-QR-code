import qrcode
qr=qrcode.QRCode(    # define the structure and size of that Qrcode structure.
    version=2,
    box_size=10,
    border=6
)
data="www.linkedin.com/in/priya-mittal-83560619b"
qr.add_data(data)
qr.make(fit=True )
img=qr.make_image(fill="black",back_color="white")
img.save("Qrcode_linkdin.png")        
    
