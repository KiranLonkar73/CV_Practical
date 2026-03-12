from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def count_people(image_path):

    results = model(image_path)

    count = 0

    for r in results:
        for box in r.boxes:

            class_id = int(box.cls[0])
            confidence = float(box.conf[0])

            # Only count if confidence is strong
            if model.names[class_id] == "person" and confidence > 0.5:
                count += 1

    return count