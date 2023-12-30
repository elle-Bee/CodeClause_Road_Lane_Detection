# Road Lane Detection

This repository contains a Python script for detecting and displaying lanes in a video using OpenCV.

![Lane Detection Example](ss.png)

## Requirements
- Docker Desktop

## Usage
1. Clone the repository.
2. Jump to the repository by using following command
```bash
cd Road-Lane-Detection-System
```
3. Maintain a single video in the repository with the name **'test.mp4'** ,which is the default. If you opt to use an alternative video for testing, kindly remove the initial default video and rename your video to `test.mp4`
4. #### Prerequisites:
Before building the Docker image, install the basic framework for a GUI environment, specifically 'X11' (assuming users are using Ubuntu).
```bash
apt-get install x11-xserver-utils
```
To display a GUI-based application in Docker, Allow X server connection:
```bash
xhost +local:*
```
You will get message "non-network local connections being added to access control list".

5. #### Verify Docker Status:
To ensure a seamless Docker experience, it's essential to check the status of the Docker service on your system.To verify whether the Docker service is currently active or inactive, you can use the following steps:
* Check Docker Service Status:
```bash
systemctl status docker
```
if it's inactive, you'll need to take corrective action.

* To activate the Docker service, use the following command:
```bash
sudo systemctl start docker
```
6. #### Build:
Now, let's build the Docker image named 'lane_detection_app' using the docker build command:
```bash
sudo docker build -t lane_detection_app .
```
7. #### Run:
Write the following command to run a Docker container named 'lane_detection'
```bash
sudo docker run -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix/ --name lane_detection lane_detection_app
```
:tada: Yeah,You will be able to see the video playing on the display.

8. #### Closing Notes:
After the completion of testing,make sure to disallow the X server connection:
```bash
xhost -local:*
```
You will get message "non-network local connections being removed from access control list".

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
