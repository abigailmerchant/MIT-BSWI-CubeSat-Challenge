from picamera2 import Picamera2
import os
import subprocess
from datetime import datetime

# Initialize the camera
camera = Picamera2()

# Configure the resolution
camera_config = camera.create_still_configuration(main={"size": (1280, 720)})
camera.configure(camera_config)

# Start the camera
camera.start()

# Path to the local GitHub repository
repo_path = "/home/pi/MIT-BSWI-CubeSat-Challenge"
testing_folder = os.path.join(repo_path, "testing")

# Ensure the "testing" folder exists
os.makedirs(testing_folder, exist_ok=True)

# Generate a unique filename using the current timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # Format: YYYYMMDD_HHMMSS
filename = f"image_{timestamp}.jpg"
image_path = os.path.join(testing_folder, filename)

# Capture an image and save it to the "testing" folder
camera.capture_file(image_path)

# Stop the camera
camera.stop()

# Change to the repository directory
os.chdir(repo_path)

# Add, commit, and push the image to GitHub
subprocess.run(["git", "add", f"testing/{filename}"], check=True)
subprocess.run(["git", "commit", "-m", f"Add {filename} to testing folder"], check=True)
subprocess.run(["git", "push", "origin", "main"], check=True)

print(f"Image saved as {filename} and pushed to your GitHub repository!")
