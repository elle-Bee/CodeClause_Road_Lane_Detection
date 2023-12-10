import cv2 as cv
import numpy as np


def displayLines(img, lines):
    line_image = np.zeros_like(img)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 7)
    return line_image


def canny(img):
    thresh1 = cv.getTrackbarPos("Threshold 1", "Lane Detector")
    thresh2 = cv.getTrackbarPos("Threshold 2", "Lane Detector")
    gray_img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    blurred_img = cv.GaussianBlur(gray_img, (5, 5), 0)
    canny_img = cv.Canny(blurred_img, thresh1, thresh2)
    return canny_img


def trackbar_click(x):
    print(x)


def roi(img, vertices):
    region = np.zeros_like(img)
    cv.fillPoly(region, [vertices], 255)
    final_masked = cv.bitwise_and(img, region)
    return final_masked


cap_path = "test.mp4"
cap = cv.VideoCapture(cap_path)

cv.namedWindow("Lane Detector")
cv.createTrackbar("Threshold 1", "Lane Detector", 0, 255, trackbar_click)
cv.createTrackbar("Threshold 2", "Lane Detector", 0, 255, trackbar_click)
cv.setTrackbarPos("Threshold 1", "Lane Detector", 50)
cv.setTrackbarPos("Threshold 2", "Lane Detector", 150)

height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
roi_vertices = np.array(
    [[(0, height), (width / 2, height / 3), (width, height)]], dtype=np.int32
)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame_canny = canny(frame)
    frame_roi = roi(frame_canny, roi_vertices)
    lane = cv.HoughLinesP(
        frame_roi, 2, np.pi / 180, 100, np.array([]), minLineLength=40, maxLineGap=5
    )
    lines_frame = displayLines(frame, lane)
    combo_frame = cv.addWeighted(frame, 0.5, lines_frame, 1, 1)
    cv.imshow("Lane Detector", combo_frame)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
