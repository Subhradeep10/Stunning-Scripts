import qrcode
import qrcode.image.svg
img = qrcode.make('https://github.com/Subhradeep10/Automation-Scripts-Using-Python',
                  image_factory=qrcode.image.svg.SvgImage)
with open('qr.svg', 'wb') as qr:
    img.save(qr)
