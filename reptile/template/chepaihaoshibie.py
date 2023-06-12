import cv2
import pytesseract

# 加载图片
img = cv2.imread('static/IMAGES/R.png')
if img is None:
    print('Image not loaded')

# 对图片进行处理
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)

# 对图片进行边缘检测
edges = cv2.Canny(blur, 100, 200)

# 查找图片中的轮廓
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 遍历所有轮廓，寻找可能是车牌的轮廓
for cnt in contours:
    area = cv2.contourArea(cnt)
    x, y, w, h = cv2.boundingRect(cnt)
    aspect_ratio = w / h
    if area > 2000 and aspect_ratio > 4:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        plate = img[y:y+h, x:x+w]
        text = pytesseract.image_to_string(plate)
        print("License Plate:", text)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
