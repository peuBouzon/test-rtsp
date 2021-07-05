import cv2 as cv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '--input', type=str, help="RTSP uri connection string", required=True)
args = parser.parse_args()

capturer = cv.VideoCapture(args.input)
if not capturer.isOpened():
    raise Exception(f'Failed to open {args.input}')

print("PRESS 'Q' TO STOP")
while True:
    ret, frame = capturer.read()
    if not ret:
        raise Exception(f'No return from camera: {args.input}')
    cv.namedWindow('camera', cv.WINDOW_NORMAL)
    cv.imshow('camera', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
