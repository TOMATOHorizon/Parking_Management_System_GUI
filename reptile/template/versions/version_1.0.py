import tkinter as tk
import mysql.connector
from template.ChatGPT import ChatGPT_view


class ParkingAuxiliarySystemforParkingLot:
    def __init__(self):
        CAR_SLOTS = 10

        DB_HOST = 'localhost'
        DB_USER = 'root'
        DB_PASSWORD = '744214Sgg'
        DB_NAME = 'parking_lot_db'
        TABLE_NAME = 'parking_status'

        class ParkingLot:
            def __init__(self, slots):
                self.slots = slots
                self._available = set(range(1, slots + 1))
                self.init_database()

            def reserve(self, slot):
                if slot not in self._available:
                    self.release(slot)
                    return False
                self._available.remove(slot)
                self.update_status_in_db(slot, '已占用')
                return True

            def release(self, slot):
                self._available.add(slot)
                self.update_status_in_db(slot, '未占用')

            def available_slots(self):
                return len(self._available)

            def slot_status(self):
                return ['已占用' if i not in self._available else '未占用' for i in range(1, self.slots + 1)]

            def is_available(self, slot):
                return slot in self._available

            def init_database(self):
                try:
                    conn = mysql.connector.connect(
                        host=DB_HOST,
                        user=DB_USER,
                        password=DB_PASSWORD,
                    )
                    cursor = conn.cursor()

                    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
                    cursor.execute(f"USE {DB_NAME}")

                    cursor.execute(
                        f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} (slot INT PRIMARY KEY, status VARCHAR(10))"
                    )
                    conn.commit()

                except mysql.connector.Error as error:
                    print(f"Error initializing database: {error}")

                finally:
                    if conn.is_connected():
                        cursor.close()
                        conn.close()

            def update_status_in_db(self, slot, status):
                try:
                    conn = mysql.connector.connect(
                        host=DB_HOST,
                        user=DB_USER,
                        password=DB_PASSWORD,
                        database=DB_NAME
                    )
                    cursor = conn.cursor()

                    cursor.execute(
                        f"INSERT INTO {TABLE_NAME} (slot, status) VALUES (%s, %s) "
                        f"ON DUPLICATE KEY UPDATE status = VALUES(status)",
                        (slot, status)
                    )
                    conn.commit()

                except mysql.connector.Error as error:
                    print(f"Error updating status in database: {error}")

                finally:
                    if conn.is_connected():
                        cursor.close()
                        conn.close()

        class ParkingLotApp(tk.Canvas):
            def __init__(self, parent, master=None, **kwargs):
                # get the original screen width and height
                width_original = parent.winfo_screenwidth()
                height_original = parent.winfo_screenheight()

                # change the size of the window to 50% of the original size
                parent.geometry(f"{width_original // 2}x{height_original // 2}")

                # 添加一个启动 ChatGPTApp 的按钮
                super().__init__(master, **kwargs)
                self.chat_gpt_button = tk.Button(self, text="ChatGPT", command=self.start_chat_gpt)
                self.chat_gpt_button.pack()
                super().__init__(parent, width=parent.winfo_screenwidth(), height=parent.winfo_screenheight(),
                                 bg="white")
                self.parking_lot = ParkingLot(CAR_SLOTS)
                self.parent = parent
                self.pack()
                self.lines = []
                self.slot_buttons = []
                self.status_vars = []
                self.layout()

            def start_chat_gpt(self):
                root = tk.Tk()
                app = ChatGPT_view.ChatGPTApp.Application(master=root)
                root.mainloop()

            def do_something(self):
                chat_window = tk.Toplevel(self.parent)
                chat_app = ChatGPT_view.Application(chat_window)
                chat_app.run()

            def run(self):
                self.parent.mainloop()

            def layout(self):
                width = self.parent.winfo_screenwidth()
                height = self.parent.winfo_screenheight()
                entrance_x = width * 0.05
                entrance_y = height * 0.5

                title_label = tk.Label(self.parent, text="停车场管理系统", font=("Helvetica", 24))
                title_label.place(x=width * 0.35, y=20)

                entrance_label = tk.Label(self, text="入口", bg="white")
                entrance_label.place(x=entrance_x, y=entrance_y)

                available_slots_label = tk.Label(self, text="可用车位：", bg="white")
                available_slots_label.place(x=width * 0.3, y=height * 0.05)

                slot_status_label = tk.Label(self, text="车位状态：", bg="white")
                slot_status_label.place(x=width * 0.5, y=height * 0.05)

                self.available_slots_var = tk.StringVar()
                available_slots_entry = tk.Entry(self, textvar=self.available_slots_var)
                available_slots_entry.place(x=width * 0.4, y=height * 0.05)


                for i in range(1, self.parking_lot.slots + 1):
                    slot_x = width * 0.3
                    slot_y = (height * 0.25) + (50 * (i - 1))

                    def on_click(slot):
                        if self.parking_lot.is_available(slot):
                            self.reserve(slot)
                        else:
                            self.release(slot)

                        self.update_slots_status()
                        self.update_route(slot)

                    slot_button = tk.Button(self, text=f"车位 {i}", command=lambda i=i: on_click(i),
                                            bg="lightgreen" if self.parking_lot.is_available(i) else "red", width=6)
                    slot_button.place(x=slot_x, y=slot_y)
                    self.slot_buttons.append(slot_button)

                    status_var = tk.StringVar()
                    status_label = tk.Label(self, textvariable=status_var, bg="white")
                    status_label.place(x=slot_x + 70, y=slot_y)
                    self.status_vars.append(status_var)

                self.update_slots_status()

                route_label = tk.Label(self, text="路线：", bg="white")
                route_label.place(x=width * 0.3, y=height * 0.7)

                self.route_var = tk.StringVar()
                route_entry = tk.Entry(self, textvar=self.route_var)
                route_entry.place(x=width * 0.35, y=height * 0.7)

            def reserve(self, slot):
                self.parking_lot.reserve(slot)

            def release(self, slot):
                self.parking_lot.release(slot)

            def update_slots_status(self):
                self.available_slots_var.set(self.parking_lot.available_slots())
                slot_status = self.parking_lot.slot_status()

                for i, status_var in enumerate(self.status_vars):
                    status_var.set(slot_status[i])

                for i, slot_button in enumerate(self.slot_buttons, start=1):
                    slot_button.config(bg="lightgreen" if self.parking_lot.is_available(i) else "red")

            def draw_route(self, x1, y1, x2, y2):
                points = [x1, y1, x1 + 50, y1, x1 + 50, y2, x2, y2]

                line = self.create_line(points, fill="blue", smooth=False, arrow="last")
                self.lines.append(line)

            def update_route(self, slot):
                for line in self.lines:
                    self.delete(line)

                entrance_x = self.parent.winfo_screenwidth() * 0.05
                entrance_y = self.parent.winfo_screenheight() * 0.5
                slot_x = self.parent.winfo_screenwidth() * 0.3
                slot_y = (self.parent.winfo_screenheight() * 0.25) + (50 * (slot - 1))

                route_text = f"入口到车位 {slot} 的路线"
                self.draw_route(entrance_x, entrance_y, slot_x, slot_y)
                self.route_var.set(route_text)

            def run(self):
                self.parent.mainloop()

        def main():
            root = tk.Tk()
            app = ParkingLotApp(root)
            app.run()

        main()

ceshi = ParkingAuxiliarySystemforParkingLot()
