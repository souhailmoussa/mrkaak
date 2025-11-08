import qrcode
img = qrcode.make("https://mrkaak.netlify.app")
img.save("mrkaak-qr.png")