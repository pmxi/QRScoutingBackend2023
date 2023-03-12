import argparse
import numpy as np
from pyzbar.pyzbar import decode
import cv2


parser = argparse.ArgumentParser(description="qr code scanner to text file")
parser.add_argument("-f", "--file", type=str, default="scouting.txt",
                    help="file to output qr code scans to, relative or absolute")
parser.add_argument("-v", "--verbose", action="store_true")
parser.add_argument("-d", "--remove-duplicate", action="store_true")
args = parser.parse_args()


def decoder(image):
    gray_img = cv2.cvtColor(image, 0)
    barcode = decode(gray_img)

    for obj in barcode:
        points = obj.polygon
        (x, y, w, h) = obj.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)
        barcode_data = obj.data.decode("utf-8")
        v.add(barcode_data)
        barcode_type = obj.type
        string = str(barcode_data) + " | Type " + str(barcode_type)
        cv2.putText(
            frame, string, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2
        )
        if args.verbose:
            print("QR: " + barcode_data + " | Type: " + barcode_type)


def save(values):
    with open(args.file, "a") as scouting_file:
        if len(v) != 0:
            for i in v:
                scouting_file.write(i + "\n")
            print("SAVED! ( ͡° ͜ʖ ͡°)\n")
        else:
            print("SAVED NOTHING! ¯\\_(ツ)_/¯\n")


if __name__ == "__main__":
    if not args.remove_duplicate:
        cap = cv2.VideoCapture(0)
        v = set()
        while True:
            ret, frame = cap.read()
            decoder(frame)
            cv2.imshow("QR SCANNER", frame)
            code = cv2.waitKey(10)
            if code == ord("s"):
                print("Saving! (O.o)\n         /||\\\n         / \\")
                save(v)
                v.clear()
            elif code == ord("p"):
                for i in v:
                    print(i)
            elif code == ord("q"):
                break

    elif args.remove_duplicate:
        with open(args.file, "r+") as scouting_file:
            values = set(scouting_file.readlines())
            scouting_file.seek(0)
            for v in values:
                scouting_file.write(v)
            scouting_file.truncate()
        print("duplicates removed from scouting file: {args.files}")
