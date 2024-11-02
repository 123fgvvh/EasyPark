# EasyPark – Real-Time Parking Slot Detection System

**EasyPark** is a computer vision-based application for detecting available and occupied parking slots in real-time from video feeds. Built using **OpenCV**, **NumPy**, and **cvzone**, this project processes video inputs, identifies parking slot occupancy based on pixel analysis, and displays real-time availability with color-coded indicators.

## Features

- **Real-time Monitoring**: Updates slot occupancy every 10 milliseconds for responsive tracking.
- **Manual Slot Configuration**: User-defined slot positions for flexibility with different parking layouts.
- **Clear Visual Indicators**: Color-coded overlays for easy distinction between occupied (red) and available (green) slots.
- **Accurate Occupancy Detection**: Achieves approximately 90% accuracy in controlled conditions using pixel-based thresholding techniques.

![EasyPark Demo](CarParkingProject.gif)


## Table of Contents

- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Customization](#customization)
- [License](#license)

## Getting Started

### Prerequisites

- Python 3.6+
- OpenCV
- cvzone
- NumPy

Ensure you have a video file of a parking lot or a live feed for testing.

### Installation

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/123fgvvh/EasyPark.git]
   cd EasyPark
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download or use an existing video feed**:
   - Place your video file (e.g., `carPark.mp4`) in the project directory.

## Usage

1. **Set up slot positions manually**:
   - Run `ParkingSpacePicker.py` to define the top-left corner coordinates of each slot manually on the `carParkImg.png` image.
   - The positions are saved in `CarParkPos`, which will be used by `main.py`.

2. **Run the project**:
   ```bash
   python main.py
   ```

3. **View real-time slot updates**:
   - The program will display the parking lot video feed (`carPark.mp4`) with slot status updated in real time.
   - Occupied slots are shown in red, and available slots in green.

## Project Structure

```plaintext
easypark/
├── .venv/                          # Virtual environment directory
├── carPark.mp4                     # Sample video feed for testing
├── carParkImg.png                  # Image file for picking slot positions
├── CarParkPos                      # Pickle file to save manually initialized slot positions
├── main.py                         # Main script to run the parking detection system
├── ParkingSpacePicker.py           # Script for manually setting up slot positions
└── requirements.txt                # List of required packages
```

## Customization

- **Adjust Slot Dimensions**:
  - Update `width` and `height` values in `main.py` to fit the parking slots in your specific video feed.

- **Set Slot Positions**:
  - Use `ParkingSpacePicker.py` to manually configure each slot position on `carParkImg.png`. This will save the coordinates in `CarParkPos`.

- **Thresholding Sensitivity**:
  - Adjust the pixel count threshold in `main.py` (e.g., set to 900) to fine-tune the detection sensitivity for different lighting conditions.
