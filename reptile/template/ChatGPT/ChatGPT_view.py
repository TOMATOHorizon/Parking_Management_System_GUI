import tkinter as tk
from tkinter import scrolledtext
import requests

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid(sticky="nsew")  # use grid layout manager
        self.create_widgets()

        # 用于保存用户文本的列表
        self.user_text = []

    def create_widgets(self):
        # 创建一个Text小部件并禁止编辑，同时增加滚动条
        self.conversation_text = scrolledtext.ScrolledText(self, state='disabled')
        self.conversation_text.grid(row=0, column=0, columnspan=2, sticky="nsew")  # use grid layout manager

        # 定义标签样式
        self.conversation_text.tag_config("user", foreground="blue")
        self.conversation_text.tag_config("bot", foreground="green")

        # 插入对话，使用不同的样式
        self.conversation_text.configure(state='normal')
        self.conversation_text.insert("end", "User: Hello, how are you?\n", "user")
        self.conversation_text.insert("end", "Bot: I am fine. How can I help you today?\n", "bot")
        self.conversation_text.configure(state='disabled')

        # 插入一个空标签作为分隔器
        self.separator = tk.Label(self, height=2)
        self.separator.grid(row=1, column=0, columnspan=2, sticky="nsew")  # use grid layout manager

        # 创建一个多行的输入框（使用ScrolledText），并增加滚动条
        self.input_text = scrolledtext.ScrolledText(self, height=5, bg='light gray')
        self.input_text.grid(row=2, column=0, sticky="nsew")  # use grid layout manager

        # 创建一个"发送"按钮，点击后将输入的内容添加到对话中
        self.send_button = tk.Button(self, text="Send", command=self.update_conversation)
        self.send_button.grid(row=2, column=1, sticky="nsew")  # use grid layout manager

        self.grid_columnconfigure(0, weight=1)  # make the first column expandable
        self.grid_rowconfigure(0, weight=1)  # make the first row expandable

        # 绑定Return键到update_conversation函数
        self.input_text.bind("<Return>", self.update_conversation)

    def update_conversation(self, event=None):
        user_input = self.input_text.get("1.0", tk.END).strip()
        self.user_text.append(user_input)
        self.conversation_text.configure(state='normal')
        self.conversation_text.insert("end", "User: " + user_input + "\n", "user")
        self.conversation_text.configure(state='disabled')
        # 这里插入你的对话机器人的处理代码，将结果保存在bot_response中
        bot_response = self.ChatGPT_Duihua()
        self.conversation_text.configure(state='normal')
        self.conversation_text.insert("end", "Bot: " + bot_response + "\n", "bot")
        self.conversation_text.configure(state='disabled')
        self.input_text.delete("1.0", tk.END)
        print(self.user_text)

    def ChatGPT_Duihua(self):
        responses = requests.get(
            f"https://api.a20safe.com/api.php?api=36&key=874b8e021569e42db3d0c3fe64317004&text={self.user_text[-1]}")
        ChatGPT_reply = responses.json()["data"][0]["reply"]
        return ChatGPT_reply

root = tk.Tk()
root.grid_columnconfigure(0, weight=1)  # make the first column expandable
root.grid_rowconfigure(0, weight=1)  # make the first row expandable
root.title("ChatGPT")
app = Application(master=root)
app.mainloop()