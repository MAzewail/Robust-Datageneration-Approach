## Automated Light Intensity Image Acquisition System

This repository contains the Python script and instructions for an automated image acquisition system used for training a deep learning model for light intensity estimation.

###  Project Description

This project automates the capture of images at various light intensities to be used as training data for a deep learning model. The system utilizes:

* **Python script:** Controls image capture, interacts with Arduino, and organizes captured data.
* **Connected camera:** Captures images at specified intervals.
* **Arduino board:** Controls supplemental lighting via PWM signal based on 5 intensity levels.
* **Servo motor (optional):** Rotates an object in front of the camera (controlled by Arduino).

###  Features

* **Automated image capture:** Captures images at various light intensities.
* **Arduino integration:** Controls lighting levels using PWM signals.
* **Data organization:** Saves images with filenames reflecting intensity level.
* **Scalability:** Adjustable number of images per intensity level.

###  Requirements

* Python 3 (tested with Python 3.x)
* OpenCV library (`pip install opencv-python`)
* Serial library (`pip install pyserial`)
* Pandas library (optional, for data organization)
* Arduino Uno or compatible board (if using servo motor)
* Camera connected to your computer

###  Setup Instructions

1. **Install libraries:**
    - Open a terminal or command prompt.
    - Run the following commands to install required libraries:
      ```bash
      pip install opencv-python pyserial
      ```
2. **Connect the camera:** Connect your camera to your computer.
3. **Connect Arduino (optional):** 
    - If using a servo motor, connect the Arduino board to your computer and upload a program to control the servo based on received data.
4. **Modify script (optional):**
    - Open the script `image_acquisition.py` in a text editor.
    - Update the following values if necessary:
        - `ser = serial.Serial('COM10', 9600)`: Change the COM port if your Arduino is connected to a different port.
        - `cam_loc = 5`: Modify this value to adjust the number of images captured for each light intensity level (currently set to capture 5 images per level).
        - `NUM_IMGS = 200`: Adjust this value to change the total number of images captured (currently set to capture 200 images in total).
    
###  How to Use

1. **Run the script:**
    - Open a terminal or command prompt and navigate to the directory containing the script (`image_acquisition.py`).
    - Run the script using the following command:
      ```bash
      python image_acquisition.py
      ```

2. **Process captured data:**
    - The script will create a folder named `Reinf_learning/Final/` with subfolders for each light intensity level (`level0`, `level1`, etc.).
    - Each subfolder will contain captured images named according to the light intensity level and image number (e.g., `sample_image201-3.jpg`).
    - Use the captured images to train your deep learning model for light intensity estimation.

###  Additional Notes

* This script provides a basic framework for image acquisition. You can modify it further based on your specific needs.
* Ensure your Arduino program receives and interprets the light intensity level data sent by the script.
* Consider using a library like NumPy for more advanced image processing after capture.

###  Contributing

We welcome contributions to this project! Please feel free to submit pull requests with improvements or additional features.

###  License

This project is licensed under the MIT License. See the `LICENSE` file for details.
