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

# 创建主窗口
main_window = tk.Tk()

main_window.geometry("1000x500")
main_window.configure(bg="#FFF2F2")

custom_font = font.Font(family="Apple_Font", size=12, weight="bold")
custom_font_path = "../Fonts/简萍方.ttf"
custom_font.configure(family="Apple_Font")

main_window.option_add("*Font", custom_font)

label = tk.Label(main_window, text="欢迎使用本停车场管理系统！", anchor="nw")
label.pack()

button = tk.Button(main_window, text="尝试与ChatGPT小助手进行对话", width=141, bg="#9F80AB", fg="#E4F5ED")
button.pack()

canvas = tk.Canvas(main_window, width=1000, height=500, bg="#FFF2F2")
canvas.pack()

label1 = tk.Label(main_window, text="\n\n".join("当前车位状态"), anchor="nw", font="30", fg="#F7F7F7", bg="#AC346E")
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

indicator_lamp_1 = tk.Label(main_window, text="  ", anchor="nw", font="5", relief="solid", borderwidth=1, bg="#56F067")
indicator_lamp_1.place(x=777, y=126)
indicator_lamp_2 = tk.Label(main_window, text="  ", anchor="nw", font="5", relief="solid", borderwidth=1, bg="#56F067")
indicator_lamp_2.place(x=851, y=181)
indicator_lamp_3 = tk.Label(main_window, text="  ", anchor="nw", font="5", relief="solid", borderwidth=1, bg="#56F067")
indicator_lamp_3.place(x=851, y=266)
indicator_lamp_4 = tk.Label(main_window, text="  ", anchor="nw", font="5", relief="solid", borderwidth=1, bg="#56F067")
indicator_lamp_4.place(x=771, y=331)
indicator_lamp_5 = tk.Label(main_window, text="  ", anchor="nw", font="5", relief="solid", borderwidth=1, bg="#56F067")
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
    custom_font_path = "../Fonts/简萍方.ttf"
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
            yanshi(1, moshi="Enter")
        elif panding == 2:
            canvas_lines_1 = canvas.create_line(634, 115, 900, 115, fill="#56F067", width=7)
            canvas_lines.append(canvas_lines_1)
            Label_configure([indicator_lamp_1, ])
            yanshi(2, moshi="Enter")
        elif panding == 3:
            canvas_lines_5 = canvas.create_line(900, 115, 822, 115, fill="#56F067", width=7)
            canvas_lines_6 = canvas.create_line(825, 115, 825, 264, fill="#56F067", width=7)
            canvas_lines_7 = canvas.create_line(825, 260, 745, 260, fill="#56F067", width=7)
            canvas_lines_8 = canvas.create_line(745, 257, 745, 310, fill="#56F067", width=7)
            for line in (canvas_lines_5, canvas_lines_6, canvas_lines_7, canvas_lines_8):
                canvas_lines.append(line)
            Label_configure([indicator_lamp_2, indicator_lamp_3, indicator_lamp_4])
            yanshi(3, moshi="Enter")
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
                button_demo = canvas.create_rectangle(871, 825, 881, 835, fill="blue")
                def button_move():
                    nonlocal x, y
                    if x < 80:
                        canvas.move(button_demo, 1, 0)
                        a = canvas.after(3, button_move)
                        x += 1
                        # print("b" + str(x))
                    elif x >= 80:
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
                        canvas.after_cancel(a)
                        # canvas.after_cancel(b)
                        # canvas.after_cancel(c)
                        x = 0
                        # yanshi(1)
                        return


                button_move()

            elif yanshi_fenli == 2:
                button_demo = canvas.create_rectangle(900, 109, 910, 119, fill="blue")
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
                button_demo = canvas.create_rectangle(900, 109, 910, 119, fill="blue")
                def button_move():
                    nonlocal x, y
                    if x < 80:
                        canvas.move(button_demo, 0, 1)
                        d = canvas.after(3, button_move)
                        y += 1
                        # print(y)
                    elif x >= 80:
                        if y < 145.5:
                            canvas.move(button_demo, -1, 0)
                            canvas.after(3, button_move)
                            x += 1
                            # print(x)
                        elif y >= 145.5:
                            if x < 160:
                                canvas.move(button_demo, 0, 1)
                                canvas.after(3, button_move)
                                y += 1
                                # print(y)
                            elif x >= 160:
                                canvas.move(button_demo, -1, 0)
                                canvas.after(3, button_move)
                                x += 1
                                # print(x)

                    if y == 193:
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
            "UPDATE `reptile_values`.`button_states` SET `color` = %s, `LicensePlateNumber` = %s, `DateOfNntry` = %s WHERE (`button_id` = %s);"
        )

        # 你可以根据需要更改这些值
        data = ('#D90B76', chepaihao, now_DateTime(), int(chewei))

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
        sql = "UPDATE `reptile_values`.`button_states` SET `color` = '#DC8439', `LicensePlateNumber` = NULL, `DateOfNntry` = NULL WHERE (`button_id` = %s);"

        # 执行查询语句
        cursor.execute(sql, (int(chewei),))

        cnx.commit()

        # 关闭游标和连接
        cursor.close()
        cnx.close()


    def Button_value(button):
        buttona = button

        def button_click():
            print(buttona["text"])
            button_value = buttona['text'][:-4]
            if int(button_value) in range(1, 8, 1):
                xianglie = 1
            elif int(button_value) in range(8, 12):
                xianglie = 2
            elif int(button_value) in range(12, 15, 1):
                xianglie = 3
            Zhiyin(xianglie)

            chewei_color_panding = chewei_panding(chewei=button_value)
            if chewei_color_panding == "#DC8439":
                buttona.configure(bg="#D90B76")
                tingfang(generate_license_plate(), chewei=button_value)
            elif chewei_color_panding == "#D90B76":
                hours = jisuanriqi(button_value)
                if int(button_value) in range(1, 8, 1):
                    zongjia = round(jifei(hours=hours, chewei=button_value), 2)
                    messagebox.showinfo("提示", f"您的停车时间为：{round(hours)}小时，费用为：{zongjia}元")
                    buttona.configure(bg="#DC8439")
                    chewei_zhuangtai_qingli(chewei=button_value)
                elif int(button_value) in range(8, 12, 1):
                    if hours >= 720:
                        zongjia = round(jifei(hours=hours, chewei=button_value), 2)
                        messagebox.showinfo("提示", f"您的停车时间为：{round(hours)}小时，费用为：{zongjia}元")
                        messagebox.showinfo("提示", "您的停车时间不足1月哦！")
                        buttona.configure(bg="#DC8439")
                        chewei_zhuangtai_qingli(chewei=button_value)
                    else:
                        messagebox.showinfo("提示", "您的停车时间不足1月哦！")
                elif int(button_value) in range(12, 15, 1):
                    if hours >= 8640:
                        zongjia = round(jifei(hours=hours, chewei=button_value), 2)
                        messagebox.showinfo("提示", f"您的停车时间为：{round(hours)}小时，费用为：{zongjia}元")
                        messagebox.showinfo("提示", "您的停车时间不足1月哦！")
                        buttona.configure(bg="#DC8439")
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
