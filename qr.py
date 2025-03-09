import qrcode

url = "https://forms.gle/ddMRf7o4aN1GZnyw9"

qr = qrcode.make(url)

qr.save("Member_Satisfaction_Survey_Form.png")