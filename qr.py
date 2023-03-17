import argparse
import numpy as np
from pyzbar.pyzbar import decode
import cv2
import tomllib
import local_db

parser = argparse.ArgumentParser(description='qr code scanner to text file')
parser.add_argument('-v', '--verbose', action='store_true')
args = parser.parse_args()


def main():
    with open('config.toml', 'rb') as f:
        config = tomllib.load(f)
    cap = cv2.VideoCapture(config['camera_id'])
    data_submitted = []
    scout_db = local_db.ScoutDB(config['database_file'])
    while True:
        ret, frame = cap.read()
        gray_img = cv2.cvtColor(frame, 0)
        barcode = decode(gray_img)
        for obj in barcode:
            points = obj.polygon
            (x, y, w, h) = obj.rect
            pts = np.array(points, np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(frame, [pts], True, (0, 255, 0), 3)
            barcode_data = obj.data.decode('utf-8')
            barcode_type = obj.type
            barcode_string = barcode_type + ': ' + barcode_data
            cv2.putText(
                frame, barcode_string, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 135, 0), 2
            )
            if args.verbose:
                print(barcode_string)
            if barcode_data not in data_submitted:
                data_submitted.append(barcode_data)
                scout_db.add_match_from_qr_str(barcode_data)
                print('Data submitted: ' + barcode_data)

        cv2.imshow('QR SCANNER', frame)
        code = cv2.waitKey(10)
        if code == ord('q'):
            break


if __name__ == '__main__':
    main()
