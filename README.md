# CodeClause_Road_Lane_Detection

This repository contains a Python script for detecting and displaying lanes in a video using OpenCV.

![Lane Detection Example](ss.png)

## Requirements
- Python 3.x
- OpenCV (`cv2`) library
- NumPy library

## Usage
1. Clone the repository or download the `lane_detection.py` script.
2. Make sure you have Python 3.x installed on your system along with the required libraries.
3. Place the video file you want to analyze in the same directory as the script and update the `cap_path` variable with the correct video filename.
4. Run the script using the following command:
```shell
   python lane_detection.py
```

## Main Code
The main code initializes the video capture object using the provided video file path. It creates a named window "Lane Detector" and adds two trackbars for adjusting the Canny edge detection thresholds. The script then proceeds to process each frame of the video:

1. It reads a frame from the video.
2. Applies Canny edge detection to the frame using the `canny` function.
3. Masks the region of interest in the frame using the `roi` function.
4. Detects lines in the masked frame using the Hough Line Transform (`cv.HoughLinesP`).
5. Draws the detected lines on a new image using the `displayLines` function.
6. Combines the original color frame and the lines image using `cv.addWeighted`.
7. Displays the resulting frame in the "Lane Detector" window.
8. The script continues processing frames until the user presses the 'q' key, at which point it terminates the video capture and closes the window.

Feel free to modify the threshold values and the region of interest (`roi_vertices`) to better suit your specific use case. Happy lane detection!
