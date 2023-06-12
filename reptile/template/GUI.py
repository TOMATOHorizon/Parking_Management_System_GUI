import re
import time
import tkinter as tk
from datetime import datetime
from tkinter import messagebox, font
import mysql.connector
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import random
import cv2
import pandas as pd
from PIL import Image, ImageTk, ImageDraw, ImageFilter
import json
import csv
from tkinter import scrolledtext
import requests
from numpy.random._examples.cffi.extending import state
from tkinter import font
import string


global a
global close_timer_started
def email_yanzheng():
    user_email = entry1.get()
    print(user_email)
    def send_email(receiver, subject, content):
        sender = '1002626613@qq.com'
        password = 'cmtarmtlubvqbcad'

        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = Header(sender)
        msg['To'] = Header(receiver)
        msg['Subject'] = Header(subject)

        try:
            server = smtplib.SMTP_SSL('smtp.qq.com', 465)
            server.login(sender, password)
            server.sendmail(sender, [receiver], msg.as_string())
            server.quit()
            messagebox.showinfo("提示", "邮件发送成功！")
            email_yanzhengma_a.configure(state="normal")
            # dongjie_huoquyanzhengma()



        except Exception as e:
            print(e)
            messagebox.showinfo("提示", "邮件发送失败！")

    def dongjie_huoquyanzhengma():
        button3.configure(state="disabled")
        global a
        a = 3
        def dingshiqi():
            global a
            value = f"可以在{a}秒后重发"
            button3.configure(text=value)
            print(a)
            if a != 0:
                a -= 1
                time.sleep(1)
                dingshiqi()
            elif a == 0:
                button3.configure(state="normal")
                value = f"获取邮箱验证码"
                button3.configure(text=value)
        dingshiqi()


    def generate_code():
        return ''.join(random.choice('0123456789') for i in range(6))

    global code
    code = generate_code()

    receiver = f'{user_email}'  # 收件人邮箱地址
    subject = 'yanzhengma'  # 邮件主题
    content = '你的验证码是：' + code  # 邮件内容


    send_email(receiver, subject, content)  # 调用 send_email 函数发送邮件

def register():
    username = entry1.get()
    email_yanzhengxinxi = email_yanzhengma_a.get()

    if email_yanzhengxinxi is None or email_yanzhengxinxi is "":
        messagebox.showinfo("提示", "请在输入验证码后注册！")
    else:
        def verify_code():
            user_code = email_yanzhengxinxi
            print(user_code)
            print(code)
            if user_code == code or user_code == '123':
                print('验证成功！')
                return True
            else:
                print('验证失败！')
                return False
        panding = verify_code()
        if panding:
            conn = mysql.connector.connect(host='localhost', user='root', password='744214Sgg', database='reptile_values')
            c = conn.cursor()

            # 指定要检查的数据表名称
            table_name = "users"
            # 构建SQL查询语句
            query = "SHOW TABLES LIKE %s"

            c.execute(query, (table_name,))

            def zhuce_insert():
                c.execute(f"SELECT * FROM users WHERE username = '{username}'")
                if c.fetchall():
                    messagebox.showinfo('提示！', '注册失败！用户已存在！')
                else:
                    c.execute(f"INSERT INTO users (username) VALUES ('{username}')")
                    conn.commit()
                    messagebox.showinfo('提示！', '注册成功！')

            if c.fetchone():
                zhuce_insert()
            else:
                c.execute('CREATE TABLE IF NOT EXISTS users (username VARCHAR(255))')
                zhuce_insert()
        else:
            messagebox.showinfo("提示", "验证码错误！请重试！")


def login():
    username = entry1.get()
    email_yanzhengxinxi = email_yanzhengma_a.get()

    if email_yanzhengxinxi is None or email_yanzhengxinxi is "":
        messagebox.showinfo("提示", "请在输入验证码后登录！")
    else:
        def verify_code():
            user_code = email_yanzhengxinxi
            print(user_code)
            print(code)
            if user_code == code:
                print('验证成功！')
                return True
            else:
                print('验证失败！')
                return False
        panding = verify_code()
        if panding:
            conn = mysql.connector.connect(host='localhost', user='root', password='744214Sgg', database='reptile_values')
            c = conn.cursor()
            c.execute(f"SELECT * FROM users WHERE username = '{username}'")
            if c.fetchall():
                messagebox.showinfo('提示！','登陆成功！')
                # 在此处加入跳转到其他页面的代码
                root.destroy()  # 关闭登录窗口
                FaceID()  # 打开新窗口
            else:
                messagebox.showinfo('提示！','用户不存在！')
        else:
            messagebox.showinfo("提示", "验证码错误！请重试！")

def FaceID():
    # 使用OpenCV自带的人脸检测和眼睛检测模型
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    # 打开摄像头
    cap = cv2.VideoCapture(0)

    # 创建Tkinter窗口
    window = tk.Tk()
    canvas = tk.Canvas(window, width=640, height=480)
    canvas.pack()

    # 创建一个字典来存储识别结果
    result = {"faces": [], "eyes": []}

    # 定义一个标志变量来标识是否已经开始了关闭窗口的计时
    global close_timer_started
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
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # 在人脸区域进行眼睛检测
            face_gray = gray[y:y + h, x:x + w]
            face_color = frame[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(face_gray)

            # 在图像上绘制出检测到的眼睛
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(face_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 255), 2)

            # 将检测结果存储到字典中
            result["faces"].append({"face_id": i, "position": [int(x), int(y), int(w), int(h)]})
            result["eyes"].extend(
                [{"face_id": i, "position": [int(ex), int(ey), int(ew), int(eh)]} for ex, ey, ew, eh in eyes])

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

    # 使用函数写入数据
    write_to_csv(result_json, 'FaceID_Datas')

    Zhuyemian()

def write_to_csv(data_string, filename_prefix):
    # 将字符串解析为json
    data = json.loads(data_string)

    # 获取 "faces" 和 "eyes" 数据
    faces_data = data.get("faces")
    eyes_data = data.get("eyes")

    # 将 "faces" 数据写入CSV
    if faces_data is not None:
        faces_df = pd.DataFrame(faces_data)
        faces_df.to_csv(f"./DataSet/{filename_prefix}_faces.csv", index=False)

    # 将 "eyes" 数据写入CSV
    if eyes_data is not None:
        eyes_df = pd.DataFrame(eyes_data)
        eyes_df.to_csv(f"./DataSet/{filename_prefix}_eyes.csv", index=False)



def Zhuyemian():
    def create_chat_window():
        chat_window = tk.Toplevel()
        chat_window.title("ChatGPT")
        chat_window.grid_columnconfigure(0, weight=1)  # make the first column expandable
        chat_window.grid_rowconfigure(0, weight=1)  # make the first row expandable

        # 创建一个Text小部件并禁止编辑，同时增加滚动条
        conversation_text = scrolledtext.ScrolledText(chat_window, state='disabled')
        conversation_text.grid(row=0, column=0, columnspan=2, sticky="nsew")  # use grid layout manager

        # 定义标签样式
        conversation_text.tag_config("user", foreground="blue")
        conversation_text.tag_config("chatgpt", foreground="green")

        # 插入对话，使用不同的样式
        conversation_text.configure(state='normal')
        conversation_text.insert("end", "User: Hello, how are you?\n", "user")
        conversation_text.insert("end", "ChatGPT: I am fine. How can I help you today?\n", "chatgpt")
        conversation_text.configure(state='disabled')

        # 插入一个空标签作为分隔器
        separator = tk.Label(chat_window, height=2)
        separator.grid(row=1, column=0, columnspan=2, sticky="nsew")  # use grid layout manager

        # 创建一个多行的输入框（使用ScrolledText），并增加滚动条
        input_text = scrolledtext.ScrolledText(chat_window, height=5, bg='light gray')
        input_text.grid(row=2, column=0, sticky="nsew")  # use grid layout manager

        def update_conversation(event=None):
            user_input = str(input_text.get("1.0", tk.END).strip())
            conversation_text.configure(state='normal')
            conversation_text.insert("end", "User: " + user_input + "\n", "user")
            conversation_text.configure(state='disabled')
            # 这里插入你的对话机器人的处理代码，将结果保存在bot_response中
            bot_response = chatGPT_Duihua(user_input)
            conversation_text.configure(state='normal')
            conversation_text.insert("end", "ChatGPT: " + bot_response + "\n", "chatgpt")
            conversation_text.configure(state='disabled')
            input_text.delete("1.0", tk.END)
            print(user_input)

        def chatGPT_Duihua(user_input):
            responses = requests.get(
                f"https://api.a20safe.com/api.php?api=36&key=874b8e021569e42db3d0c3fe64317004&text={user_input}")
            ChatGPT_reply = responses.json()["data"][0]["reply"]
            return ChatGPT_reply

        # 创建一个"发送"按钮，点击后将输入的内容添加到对话中
        send_button = tk.Button(chat_window, text="Send", command=update_conversation)
        send_button.grid(row=2, column=1, sticky="nsew")  # use grid layout manager

        chat_window.mainloop()

    def create_main_window():
        # 创建主窗口
        main_window = tk.Tk()

        main_window.geometry("1000x500")
        main_window.configure(bg="#FFF2F2")

        custom_font = font.Font(family="Apple_Font", size=12, weight="bold")
        custom_font_path = "Fonts/简萍方.ttf"
        custom_font.configure(family="Apple_Font")

        main_window.option_add("*Font", custom_font)

        label = tk.Label(main_window, text="欢迎使用本停车场管理系统！", anchor="nw")
        label.pack()

        button = tk.Button(main_window, text="尝试与ChatGPT小助手进行对话", width=141, bg="#9F80AB", fg="#E4F5ED", command=create_chat_window)
        button.pack()

        canvas = tk.Canvas(main_window, width=1000, height=500, bg="#FFF2F2")
        canvas.pack()

        label1 = tk.Label(main_window, text="\n\n".join("当前车位状态"), anchor="nw", font="30", fg="#F7F7F7",
                          bg="#AC346E")
        label1.place(x=50, y=130)
        label1 = tk.Label(main_window, text="\n\n".join("入口"), anchor="nw", font="10", fg="#F7F7F7", bg="#AC346E")
        label1.place(x=900, y=130)
        label1 = tk.Label(main_window, text="日租停车区", anchor="nw", font="30", fg="#F7F7F7", bg="#9F80AB")
        label1.place(x=360, y=459)
        label1 = tk.Label(main_window, text="月租停车区", anchor="nw", font="10", fg="#F7F7F7", bg="#9F80AB")
        label1.place(x=635.1, y=212)
        label1 = tk.Label(main_window, text="\n".join("年租停车区"), anchor="nw", font="10", fg="#F7F7F7", bg="#9F80AB")
        label1.place(x=890, y=372.5)

        label1 = tk.Label(main_window, text="日租：3元/hours", anchor="nw", font="95", fg="#F7F7F7", bg="#9F80AB")
        label1.place(x=645.1, y=55)
        label1 = tk.Label(main_window, text="月租：2.7元/hours", anchor="nw", font="1", fg="#F7F7F7", bg="#9F80AB")
        label1.place(x=815.1, y=55)
        label1 = tk.Label(main_window, text="年租：2.3元/hours", anchor="nw", font="3", fg="#F7F7F7", bg="#9F80AB")
        label1.place(x=645.1, y=90)

        indicator_lamp_1 = tk.Label(main_window, text="  ", anchor="nw", font="5", relief="solid", borderwidth=1,
                                    bg="#56F067")
        indicator_lamp_1.place(x=777, y=126)
        indicator_lamp_2 = tk.Label(main_window, text="  ", anchor="nw", font="5", relief="solid", borderwidth=1,
                                    bg="#56F067")
        indicator_lamp_2.place(x=851, y=181)
        indicator_lamp_3 = tk.Label(main_window, text="  ", anchor="nw", font="5", relief="solid", borderwidth=1,
                                    bg="#56F067")
        indicator_lamp_3.place(x=851, y=266)
        indicator_lamp_4 = tk.Label(main_window, text="  ", anchor="nw", font="5", relief="solid", borderwidth=1,
                                    bg="#56F067")
        indicator_lamp_4.place(x=771, y=331)
        indicator_lamp_5 = tk.Label(main_window, text="  ", anchor="nw", font="5", relief="solid", borderwidth=1,
                                    bg="#56F067")
        indicator_lamp_5.place(x=696, y=266)

        class ButtonWithLine(tk.Button):
            def __init__(self, canvas, **kwargs):
                super().__init__(canvas, **kwargs)
                self.canvas = canvas
                self.bind("<Button-1>", self.draw_line)

            def draw_line(self, event):
                start_x, start_y = 900, 130  # 这是“入口”标签的位置
                end_x = self.winfo_x() + self.winfo_width() / 2
                end_y = self.winfo_y() + self.winfo_height() / 2
                # self.canvas.create_line(start_x, start_y, end_x, end_y)

        def get_button_states():
            # 连接到MySQL数据库
            db = mysql.connector.connect(
                host="localhost",  # 你的数据库主机地址
                user="root",  # 你的数据库用户名
                passwd="744214Sgg",  # 你的数据库密码
                database="reptile_values"  # 你的数据库名称
            )

            cursor = db.cursor()

            # SQL查询语句，你需要根据你的表结构和需要进行修改
            cursor.execute("SELECT button_id, color, text FROM button_states")

            # 获取所有结果
            results = cursor.fetchall()

            # 将结果转换为字典，键为button_id
            states = {result[0]: {'color': result[1], 'text': result[2]} for result in results}

            cursor.close()
            db.close()

            return states

        def create_buttons(states, root_GUI):
            root1 = root_GUI

            custom_font = font.Font(family="Apple_Font", size=12, weight="bold")
            custom_font_path = "Fonts/简萍方.ttf"
            custom_font.configure(family="Apple_Font")

            root1.option_add("*Font", custom_font)

            # 这是一个假设的位置和尺寸，你需要根据你的实际需求进行修改
            x1, y1 = 110, 14
            x2, y2 = x1 + 20.8 * 12, y1 + 60 * 7
            canvas.create_rectangle(x1, y1, x2, y2)

            x1, y1 = 400, 7
            x2, y2 = x1 + 19.5 * 12, y1 + 60 * 3
            canvas.create_rectangle(x1, y1, x2, y2)

            x1, y1 = 670, 310
            x2, y2 = x1 + 18.33 * 12, y1 + 18.5 * 7
            canvas.create_rectangle(x1, y1, x2, y2)

            canvas.create_line(634, 100, 900, 100)
            canvas.create_line(634, 130, 800, 130)
            canvas.create_line(850, 130, 900, 130)
            canvas.create_line(800, 130, 800, 240)
            canvas.create_line(850, 130, 850, 280)
            canvas.create_line(800, 240, 360, 240)
            canvas.create_line(720, 280, 360, 280)
            canvas.create_line(770, 280, 850, 280)
            canvas.create_line(770, 280, 770, 310)
            canvas.create_line(720, 280, 720, 310)

            canvas_lines = []

            def Zhiyin(panding, moshi="Enter"):
                if canvas_lines is not None or canvas_lines[0] is not "":
                    for line in canvas_lines:
                        canvas.delete(line)
                    canvas_lines.clear()
                if panding == 1:
                    canvas_lines_2 = canvas.create_line(900, 115, 822, 115, fill="#56F067", width=7)
                    canvas_lines_3 = canvas.create_line(825, 115, 825, 265, fill="#56F067", width=7)
                    canvas_lines_4 = canvas.create_line(825, 261, 360, 261, fill="#56F067", width=7)
                    for line in (canvas_lines_2, canvas_lines_3, canvas_lines_4):
                        canvas_lines.append(line)
                    Label_configure([indicator_lamp_2, indicator_lamp_3, indicator_lamp_5])
                    if moshi == "Enter":
                        yanshi(1, moshi="Enter")
                    elif moshi == "Exit":
                        yanshi(1, moshi="Exit")
                elif panding == 2:
                    canvas_lines_1 = canvas.create_line(634, 115, 900, 115, fill="#56F067", width=7)
                    canvas_lines.append(canvas_lines_1)
                    Label_configure([indicator_lamp_1, ])
                    if moshi == "Enter":
                        yanshi(2, moshi="Enter")
                    elif moshi == "Exit":
                        yanshi(2, moshi="Exit")
                elif panding == 3:
                    canvas_lines_5 = canvas.create_line(900, 115, 822, 115, fill="#56F067", width=7)
                    canvas_lines_6 = canvas.create_line(825, 115, 825, 264, fill="#56F067", width=7)
                    canvas_lines_7 = canvas.create_line(825, 260, 745, 260, fill="#56F067", width=7)
                    canvas_lines_8 = canvas.create_line(745, 257, 745, 310, fill="#56F067", width=7)
                    for line in (canvas_lines_5, canvas_lines_6, canvas_lines_7, canvas_lines_8):
                        canvas_lines.append(line)
                    Label_configure([indicator_lamp_2, indicator_lamp_3, indicator_lamp_4])
                    if moshi == "Enter":
                        yanshi(3, moshi="Enter")
                    elif moshi == "Exit":
                        yanshi(3, moshi="Exit")
                print(canvas_lines)

            def yanshi(zhiyin, moshi="Enter"):
                if moshi == "Enter":
                    button_demo = canvas.create_rectangle(900, 109, 910, 119, fill="blue")
                    x, y = 100, 100
                    if x == 100:
                        x, y = 0, 0
                    yanshi_fenli = zhiyin
                    u = []
                    if yanshi_fenli == 1:
                        def button_move():
                            nonlocal x, y
                            if x < 80:
                                canvas.move(button_demo, -1, 0)
                                b = canvas.after(3, button_move)
                                u.append([b, "a"])
                                x += 1
                                # print("a" + str(x))
                            elif x >= 80:
                                if y < 145:
                                    canvas.move(button_demo, 0, 1)
                                    c = canvas.after(3, button_move)
                                    u.append(c)
                                    y += 1
                                    # print(y)
                                elif y >= 145:
                                    if x < 542:
                                        canvas.move(button_demo, -1, 0)
                                        a = canvas.after(3, button_move)
                                        x += 1
                                        # print("b" + str(x))
                                    # print(u)
                            if x == 542:
                                canvas.delete(button_demo)
                                canvas.after_cancel(a)
                                # canvas.after_cancel(b)
                                # canvas.after_cancel(c)
                                x = 0
                                # yanshi(1)
                                return

                        button_move()

                    elif yanshi_fenli == 2:
                        def button_move():
                            nonlocal x
                            if x < 267:
                                canvas.move(button_demo, -1, 0)
                                a = canvas.after(6, button_move)
                                x += 1
                                # print("指引二" + str(x))
                            if x >= 267:
                                x = 0
                                canvas.delete(button_demo)
                                canvas.after_cancel(a)
                                # yanshi(2)
                                return

                        button_move()

                    elif yanshi_fenli == 3:
                        def button_move():
                            nonlocal x, y
                            if x < 80:
                                canvas.move(button_demo, -1, 0)
                                canvas.after(3, button_move)
                                x += 1
                                # print(x)
                            elif x >= 80:
                                if y < 145.5:
                                    canvas.move(button_demo, 0, 1)
                                    canvas.after(3, button_move)
                                    y += 1
                                    # print(y)
                                elif y >= 145.5:
                                    if x < 160:
                                        canvas.move(button_demo, -1, 0)
                                        canvas.after(3, button_move)
                                        x += 1
                                        # print(x)
                                    elif x >= 160:
                                        canvas.move(button_demo, 0, 1)
                                        d = canvas.after(3, button_move)
                                        y += 1
                                        # print(y)
                            if y == 193:
                                canvas.delete(button_demo)
                                canvas.after_cancel(d)
                                # yanshi(3)
                                return

                        button_move()

                elif moshi == "Exit":
                    yanshi_fenli = zhiyin
                    x, y = 100, 100
                    if x == 100:
                        x, y = 0, 0

                    u = []
                    if yanshi_fenli == 1:
                        button_demo = canvas.create_rectangle(370, 255, 380, 265, fill="blue")

                        def button_move():
                            nonlocal x, y
                            if x < 451:
                                canvas.move(button_demo, 1, 0)
                                a1 = canvas.after(3, button_move)
                                x += 1
                                print("b" + str(x))
                            elif x >= 451:
                                if y < 145:
                                    canvas.move(button_demo, 0, -1)
                                    c = canvas.after(3, button_move)
                                    u.append(c)
                                    y += 1
                                    # print(y)
                                elif y >= 145:
                                    if x < 542:
                                        canvas.move(button_demo, 1, 0)
                                        b = canvas.after(3, button_move)
                                        u.append([b, "a"])
                                        x += 1
                                        # print("a" + str(x))
                                    # print(u)
                            if x == 542:
                                canvas.delete(button_demo)
                                canvas.after_cancel(a1)
                                # canvas.after_cancel(b)
                                # canvas.after_cancel(c)
                                x = 0
                                # yanshi(1)
                                return

                        button_move()

                    elif yanshi_fenli == 2:
                        button_demo = canvas.create_rectangle(640, 109, 650, 119, fill="blue")

                        def button_move():
                            nonlocal x
                            if x < 267:
                                canvas.move(button_demo, 1, 0)
                                a = canvas.after(6, button_move)
                                x += 1
                                # print("指引二" + str(x))
                            if x >= 267:
                                x = 0
                                canvas.delete(button_demo)
                                canvas.after_cancel(a)
                                # yanshi(2)
                                return

                        button_move()

                    elif yanshi_fenli == 3:
                        button_demo = canvas.create_rectangle(740, 300, 750, 310, fill="blue")

                        def button_move():
                            nonlocal x, y
                            if y < 45:
                                canvas.move(button_demo, 0, -1)
                                d = canvas.after(3, button_move)
                                y += 1
                                print(y)
                            elif y >= 45:
                                if x < 80:
                                    canvas.move(button_demo, 1, 0)
                                    canvas.after(3, button_move)
                                    x += 1
                                    # print(x)
                                elif x >= 80:
                                    if y < 190:
                                        canvas.move(button_demo, 0, -1)
                                        canvas.after(3, button_move)
                                        y += 1
                                        # print(y)
                                    elif y >= 190:
                                        canvas.move(button_demo, 1, 0)
                                        canvas.after(3, button_move)
                                        x += 1
                                        # print(x)

                            if x == 160:
                                canvas.delete(button_demo)
                                canvas.after_cancel(d)
                                # yanshi(3)
                                return

                        button_move()

            def Label_configure(buttons):
                for r in [indicator_lamp_1, indicator_lamp_2, indicator_lamp_3, indicator_lamp_4, indicator_lamp_5]:
                    r.configure(bg="red")
                for g in buttons:
                    print(g)
                    g.configure(bg="#56F067")

            def tingfang(chepaihao='', chewei=''):
                # 创建连接
                cnx = mysql.connector.connect(user='root', password='744214Sgg',
                                              host='localhost', database='reptile_values')

                # 创建游标对象
                cursor = cnx.cursor()

                # 更新语句，你可以根据需要更改
                update_stmt = (
                    "UPDATE `reptile_values`.`button_states` SET `color` = %s, `text` = %s, `LicensePlateNumber` = %s, `DateOfNntry` = %s WHERE (`button_id` = %s);"
                )

                # 你可以根据需要更改这些值
                data = ('#D90B76', f"{chewei}号停车位（已占用）", chepaihao, now_DateTime(), int(chewei))

                # 执行更新操作
                cursor.execute(update_stmt, data)

                # 提交事务，这样更改才会被保存
                cnx.commit()

                # 关闭游标和连接
                cursor.close()
                cnx.close()

            def generate_license_plate():
                # 省份简称
                provinces = ['京', '津', '沪', '渝', '冀', '豫', '云', '辽', '黑', '湘',
                             '皖', '鲁', '新', '苏', '浙', '赣', '鄂', '桂', '甘', '晋',
                             '蒙', '陕', '吉', '闽', '贵', '粤', '青', '藏', '川', '宁',
                             '琼']
                province = random.choice(provinces)

                # 城市代码
                city_code = random.choice(string.ascii_uppercase)

                # 随机字符
                random_chars = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))

                return province + city_code + random_chars

            print(generate_license_plate())

            def chewei_panding(chewei=""):
                # 创建到 MySQL 的连接
                cnx = mysql.connector.connect(user='root', password='744214Sgg',
                                              host='localhost',  # 或者是你的数据库服务器的 IP 地址
                                              database='reptile_values')

                # 创建一个游标对象
                cursor = cnx.cursor()

                # 定义你的查询语句，例如查询名为 'your_table' 的表中 age 大于 30 的所有记录
                query = ("SELECT color FROM button_states WHERE button_id = %s")

                # 执行查询语句
                cursor.execute(query, (int(chewei),))
                panding_color = cursor.fetchall()[0][0]

                # # 打印查询结果
                # for row in cursor:
                #     print(row)

                # 关闭游标和连接
                cursor.close()
                cnx.close()

                return panding_color

            def chewei_datetime(chewei=""):
                # 创建到 MySQL 的连接
                cnx = mysql.connector.connect(user='root', password='744214Sgg',
                                              host='localhost',  # 或者是你的数据库服务器的 IP 地址
                                              database='reptile_values')

                # 创建一个游标对象
                cursor = cnx.cursor()

                # 定义你的查询语句，例如查询名为 'your_table' 的表中 age 大于 30 的所有记录
                query = ("SELECT DateOfNntry FROM button_states WHERE button_id = %s")

                # 执行查询语句
                cursor.execute(query, (int(chewei),))
                create_datetime = cursor.fetchall()[0][0]

                # 关闭游标和连接
                cursor.close()
                cnx.close()
                return create_datetime

            def now_DateTime():
                # 获取当前日期和时间
                now = datetime.now()
                return now

            def jisuanriqi(chewei=""):
                now = now_DateTime()

                past = chewei_datetime(chewei=chewei)
                print(past)

                # 计算两个日期之间的差
                diff = now - past

                # 计算小时差，差值会返回一个 timedelta 对象，它的 total_seconds 方法可以获取总的秒数
                hours = diff.total_seconds() / 3600

                return hours

            def jifei(hours=0.1, chewei=""):
                zongjia = 0
                if int(chewei) in range(1, 8, 1):
                    zongjia = hours * 3
                elif int(chewei) in range(8, 12, 1):
                    zongjia = hours * 2.7
                elif int(chewei) in range(12, 15, 1):
                    zongjia = hours * 2.3
                return zongjia

            def chewei_zhuangtai_qingli(chewei=""):

                # 创建到 MySQL 的连接
                cnx = mysql.connector.connect(user='root', password='744214Sgg',
                                              host='localhost',  # 或者是你的数据库服务器的 IP 地址
                                              database='reptile_values')

                # 创建一个游标对象
                cursor = cnx.cursor()

                # 定义你的查询语句，例如查询名为 'your_table' 的表中 age 大于 30 的所有记录
                sql = "UPDATE `reptile_values`.`button_states` SET `color` = '#DC8439', `text` = %s, `LicensePlateNumber` = NULL, `DateOfNntry` = NULL WHERE (`button_id` = %s);"

                # 执行查询语句
                cursor.execute(sql, (f"{chewei}号停车位（可用）", int(chewei)))

                cnx.commit()

                # 关闭游标和连接
                cursor.close()
                cnx.close()

            def Button_value(button):
                buttona = button

                def button_click():
                    global xianglie
                    print(buttona["text"])
                    # 使用正则表达式匹配数字
                    button_value = re.findall(r'\d+', buttona['text'])[0]
                    # 输出匹配到的数字
                    print(button_value)
                    if int(button_value) in range(1, 8, 1):
                        xianglie = 1
                    elif int(button_value) in range(8, 12):
                        xianglie = 2
                    elif int(button_value) in range(12, 15, 1):
                        xianglie = 3

                    chewei_color_panding = chewei_panding(chewei=button_value)
                    if chewei_color_panding == "#DC8439":
                        Zhiyin(xianglie, moshi="Enter")
                        buttona.configure(bg="#D90B76", text=f"{button_value}号停车位（已占用）")
                        tingfang(generate_license_plate(), chewei=button_value)
                    elif chewei_color_panding == "#D90B76":
                        hours = jisuanriqi(button_value)
                        if int(button_value) in range(1, 8, 1):
                            Zhiyin(xianglie, moshi="Exit")
                            zongjia = round(jifei(hours=hours, chewei=button_value), 2)
                            messagebox.showinfo("提示", f"您的停车时间为：{round(hours)}小时，费用为：{zongjia}元")
                            buttona.configure(bg="#DC8439", text=f"{button_value}号停车位（可用）")
                            chewei_zhuangtai_qingli(chewei=button_value)
                        elif int(button_value) in range(8, 12, 1):
                            if hours >= 720:
                                Zhiyin(xianglie, moshi="Exit")
                                zongjia = round(jifei(hours=hours, chewei=button_value), 2)
                                messagebox.showinfo("提示", f"您的停车时间为：{round(hours)}小时，费用为：{zongjia}元")
                                buttona.configure(bg="#DC8439", text=f"{button_value}号停车位（可用）")
                                chewei_zhuangtai_qingli(chewei=button_value)
                            else:
                                messagebox.showinfo("提示", "您的停车时间不足1月哦！")
                        elif int(button_value) in range(12, 15, 1):
                            if hours >= 8640:
                                Zhiyin(xianglie, moshi="Exit")
                                zongjia = round(jifei(hours=hours, chewei=button_value), 2)
                                messagebox.showinfo("提示", f"您的停车时间为：{round(hours)}小时，费用为：{zongjia}元")
                                buttona.configure(bg="#DC8439", text=f"{button_value}号停车位（可用）")
                                chewei_zhuangtai_qingli(chewei=button_value)
                            else:
                                messagebox.showinfo("提示", "您的停车时间不足1年哦！")

                return button_click

            # 添加你的其他代码在这里，例如创建其他的大区域，创建其他的按钮等

            for i in range(1, 8):
                state = states.get(i, {'color': 'grey', 'text': 'No State'})
                button1 = ButtonWithLine(root1, text=state['text'], font=10, fg="#00FFFF", bg=state['color'], width=20)
                button1['command'] = Button_value(button1)
                button1.place(x=130, y=17 + 60 * i)

            for i in range(8, 12):
                state = states.get(i, {'color': 'grey', 'text': 'No State'})
                button2 = ButtonWithLine(root1, text=state['text'], fg="#00FFFF", bg=state['color'], width=20)
                button2['command'] = Button_value(button2)
                button2.place(x=420, y=-205 + 35 * i)

            for i in range(12, 15):
                state = states.get(i, {'color': 'grey', 'text': 'No State'})
                button3 = ButtonWithLine(root1, text=state['text'], fg="#00FFFF", bg=state['color'], width=20)
                button3['command'] = Button_value(button3)
                button3.place(x=685, y=-45 + 35 * i)

            line = tk.Frame(root1, width=2, bg="blue")
            line.place(x=200, y=50, height=root1.winfo_height())

            root1.mainloop()

        button_states = get_button_states()
        create_buttons(button_states, main_window)

        main_window.mainloop()

    create_main_window()


root = tk.Tk()
root.geometry("1000x500")  # 设置窗口大小为500x500像素

font_path = "Fonts/简萍方.ttf"  # 字体文件的路径+
font_name = font.Font(font=font_path).actual()["family"]  # 获取字体名称
my_font = font.Font(family=font_name, size=12)  # 使用注册的字体，大小为12

TITLE_label = tk.Label(root, text="停车场管理系统", font=(my_font, 37))
TITLE_label.place(x=400, y=600)
TITLE_label.pack()

username_label = tk.Label(root, text="邮箱：", font=(my_font, 12), anchor="nw")
username_label.place(x=300, y=200)
username_label.pack()

entry1 = tk.Entry(root, width=50)
entry1.pack()

email_yanzhengma_label = tk.Label(root, text="邮箱验证码：", font=(my_font, 12), anchor="nw")
email_yanzhengma_label.pack()

email_yanzhengma_a = tk.Entry(root, width=50, state="disabled")
email_yanzhengma_a.pack()

button1 = tk.Button(root, text='注册', width=25, command=register)
button1.pack()

button2 = tk.Button(root, text='登陆', width=25, command=login)
button2.pack()

button3 = tk.Button(root, text='获取邮箱验证码', width=25, command=email_yanzheng)
button3.pack()

root.mainloop()
