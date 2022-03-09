import pyqrcode
import png

def qr_code():
    s = "Sample Qr Code Reader"
    d = pyqrcode.create(s)
    d.png("my_img.png",scale=6)
    print("code executed")

if __name__ == "__main__":
    qr_code()