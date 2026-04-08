from ultralytics import YOLO

# Load pretrained YOLO model
model = YOLO("yolov8n.pt")

# Run detection on an image
results = model("images/test_image.jpg", save=True)


print("Detection Finished")