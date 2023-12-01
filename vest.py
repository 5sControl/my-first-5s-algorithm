import datetime
import uuid
import cv2
import os
from dotenv import load_dotenv
from yolo_model_settings.ObjectDetectionModel import YOLOv8ObjDetectionModel

model = YOLOv8ObjDetectionModel(model_path='model/best_final.pt', conf_thresh=0.6,
                                iou_thresh=0.6, classes=[0, 1], img_size=640)

if os.environ.get("server_url") is None:
    load_dotenv("config/settings.env")

server_url = os.environ.get("server_url")
camera_url = os.environ.get("camera_url")
camera_ip = os.environ.get("camera_ip")
folder = os.environ.get("folder")

myColor = 0
while True:
    logg.debug("Detection started")
    img = ImageExtractor(camera_url).get_image()
    results = model(img[..., ::-1])
    print(len(results))
    if len(results) == 0:
        logg.critical('No objects')
    else:
        logg.info('Objects')
    start_track = datetime.datetime.now()
    for res in results:
        current_boxes = res.boxes
        for box in current_boxes:
            coord = [int(i) for i in box.xyxy[0].tolist()]
            x1, y1, x2, y2 = coord[0], coord[1], coord[2], coord[3]
            w, h = x2 - x1, y2 - y1

            probability = round(box.conf[0].item(), 2)

            class_name = res.names[box.cls[0].item()]

            if class_name == 'no-vest' and probability > 0.6:
                myColor = (255, 0, 0)
            elif class_name == 'vest':
                myColor = (0, 255, 0)
            else:
                myColor = (0, 0, 255)

            if myColor == (0, 0, 255):
                break
            cv2.putText(img, f'{probability, class_name}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX,
                                  0.5, myColor, 1, cv2.LINE_AA)
            cv2.rectangle(img, (x1, y1), (x2, y2), myColor, 3)

            if not os.path.exists(folder):
                os.makedirs("images", exist_ok=True)
                os.makedirs(folder, exist_ok=True)
            logg.info("Photo creating")
            name_file = uuid.uuid4()
            file_path = os.path.join(folder, f"{name_file}.jpg")
            cv2.imwrite(file_path, cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
            end_track = datetime.datetime.now()

            report.send_report(f'{folder}/{name_file}.jpg', str(start_track), str(end_track))

    cv2.imshow("Image", cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
