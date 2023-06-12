import cv2
import tkinter as tk
from PIL import Image, ImageTk
import json

# 使用OpenCV自带的人脸检测和眼睛检测模型
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# 打开摄像头
cap = cv2.VideoCapture(0)

# 创建Tkinter窗口
window = tk.Tk()
canvas = tk.Canvas(window, width = 640, height = 480)
canvas.pack()

# 创建一个字典来存储识别结果
result = {"faces": [], "eyes": []}

# 定义一个标志变量来标识是否已经开始了关闭窗口的计时
close_timer_started = False

def update_image():
    global close_timer_started

    # 从摄像头读取图像
    ret, frame = cap.read()

    if not ret:
        return

    # 将图像转换为灰度图，因为人脸检测需要灰度图
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 进行人脸检测
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # 如果检测到了人脸，并且还没有开始关闭窗口的计时，那么开始计时
    if len(faces) > 0 and not close_timer_started:
        window.after(3000, window.destroy)
        close_timer_started = True

    # 在图像上绘制出检测到的人脸
    for i, (x, y, w, h) in enumerate(faces):
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # 在人脸区域进行眼睛检测
        face_gray = gray[y:y+h, x:x+w]
        face_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(face_gray)

        # 在图像上绘制出检测到的眼睛
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(face_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 255), 2)

        # 将检测结果存储到字典中
        result["faces"].append({"face_id": i, "position": [int(x), int(y), int(w), int(h)]})
        result["eyes"].extend([{"face_id": i, "position": [int(ex), int(ey), int(ew), int(eh)]} for ex, ey, ew, eh in eyes])

    # 将OpenCV的图像转换为Tkinter兼容的图像
    cv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv_image)
    photo = ImageTk.PhotoImage(image=img)

    # 在画布上显示图像
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    canvas.image = photo

    # 每33毫秒更新一次图像
    window.after(33, update_image)

# 开始更新图像
update_image()

# 开始Tkinter的主循环
window.mainloop()

# 关闭摄像头
cap.release()

# 将结果转换为JSON字符串并打印出来
result_json = json.dumps(result)
print(result_json)
