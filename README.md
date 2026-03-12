👥 Smart Crowd Counter Dashboard

A Computer Vision project that detects and counts people in an image using YOLOv8 Object Detection and visualizes the result through a Streamlit Dashboard.

This system allows users to upload an image and automatically detect how many people are present.

📌 Project Overview
The project uses a pretrained YOLOv8 model to detect the person class in an image.
Each detected person is counted and the result is displayed on a web dashboard built with Streamlit.

Workflow
Upload Image
     ↓
YOLOv8 Detection Model
     ↓
Detect "person" objects
     ↓
Count detected people
     ↓
Display result on dashboard

🚀 Features
✔ Upload an image through the dashboard
✔ Detect people using YOLOv8
✔ Count total number of people
✔ Display results in a simple UI
✔ Lightweight and fast detection

🛠 Technologies Used
Technology	Purpose
Python	Programming language
YOLOv8 (Ultralytics)	Object detection
OpenCV	Image processing
Streamlit	Web dashboard
Pillow (PIL)	Image loading

📂 Project Structure
crowd-counter-dashboard
│
├── app.py              # Streamlit dashboard interface
├── detector.py         # YOLO detection logic
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation

⚙️ Installation
Step 1 — Clone the repository
git clone https://github.com/KiranLonkar73/CV_Practical.git
Step 2 — Move into the project folder
cd CV_Practical
Step 3 — Create a virtual environment (recommended)
python -m venv venv

Activate the environment

Windows

venv\Scripts\activate

pip install streamlit ultralytics opencv-python pillow
▶ Running the Project

Run the Streamlit dashboard using:

python -m streamlit run app.py

After running this command, Streamlit will start a local server.

Open the following URL in your browser:

http://localhost:8501
📷 Using the Application

Open the Streamlit dashboard.

Upload an image containing people.

The system will detect people using YOLOv8.

The dashboard will display the total number of people detected.
