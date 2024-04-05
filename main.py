from PIL import Image
import sys
import qrcode
import os



def generateQR(url: str, save_location: str, filename: str):
    qr = qrcode.make(url)
    qr.save(save_location + filename)

def run():
    """ main program execution """

    url = "https://github.com/mjl62"
    save_location = os.path.abspath(".") + "/qr_code/"
    filename = "qrcode.png"

    for arg in sys.argv:
        if arg == "--url":
            url = sys.argv[sys.argv.index(arg) + 1]
        if arg == "--save-dir":
            save_location = sys.argv[sys.argv.index(arg) + 1]
        if arg == "--filename":
            filename = sys.argv[sys.argv.index(arg) + 1]
    generateQR(url=url, save_location=save_location, filename=filename)


if __name__ == "__main__":
    run()