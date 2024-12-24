from picamera2 import Picamera2
import os
import subprocess

# Initialize the camera
camera = Picamera2()

# Configure the resolution
camera_config = camera.create_still_configuration(main={"size": (1280, 720)})
camera.configure(camera_config)

# Start the camera
camera.start()

# Path to the local clone of your repository
repo_path = "https://github.com/abigailmerchant/MIT-BSWI-CubeSat-Challenge/edit/main/Testing/"
testing_folder = os.path.join(repo_path, "testing")

# Ensure the "testing" folder exists
os.makedirs(testing_folder, exist_ok=True)

# Capture an image and save it to the "testing" folder
image_path = os.path.join(testing_folder, "testresolution.jpg")
camera.capture_file(image_path)

# Stop the camera
camera.stop()

# Change to the repository directory
os.chdir(repo_path)

# Add, commit, and push the image to GitHub
subprocess.run(["git", "add", "testing/testresolution.jpg"], check=True)
subprocess.run(["git", "commit", "-m", "Add captured image to testing folder"], check=True)
subprocess.run(["git", "push", "origin", "main"], check=True)

print(f"Image saved and pushed to {image_path} in your GitHub repository!")
