import qrcode
qr=qrcode.QRCode(    # define the structure and size of that Qrcode structure.
    version=2,
    box_size=10,
    border=6
)
print("Welcome to QR code generator\n\n")
choice='y'
while(choice.lower()=="y"):
    data=input("Enter the website/link for which you want to make QR code : ")
    name = input("Enter the name you want to save the QR code : ")
    qr.add_data(data)
    qr.make(fit=True )
    img=qr.make_image(fill="black",back_color="white")
    img.save(name+'.png')        
    choice = input("Want to continue (y) or (n) : ")

print("Thank you for using our service ")

    
