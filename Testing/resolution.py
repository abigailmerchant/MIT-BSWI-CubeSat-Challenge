from picamera2 import Picamera2

# Initialize the camera
camera = Picamera2()

# Configure the resolution
camera_config = camera.create_still_configuration(main={"size": (1280, 720)})
camera.configure(camera_config)
 
# Start the camera
camera.start()

# Capture an image
camera.capture_file("testresolution.jpg")

# Stop the camera
camera.stop()
