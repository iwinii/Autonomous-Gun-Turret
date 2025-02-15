import SSDMobileNetModule as mnSSDm
import cv2

def main():
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    myModel = mnSSDm.mnSSD("ssd-mobilenet-v2", 0.5)
    while True:
        success, img = cap.read()
        objects = myModel.detect(img, True)

        cv2.imshow("Image", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()
