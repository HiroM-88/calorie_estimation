from ultralytics import YOLO

# load model
model = YOLO("yolov8n.pt")

# Run detection
results = model("images/test_image.jpg")

# Threshold
CONF_THRESHOLD = 0.5

# Store detected items
detected_items = []

for result in results:
    names = result.names

    for box in results




