import requests

data = {
    "mail": "1002626613@qq.com",
    "opt": 1 ,
}

posts = {
    "Register": "https://api.a20safe.com/api.php?api=39&mail={data['mail']}&opt={data['opt']}",
    "ChatGPT": "https://api.a20safe.com/api.php?api=36&key=874b8e021569e42db3d0c3fe64317004&text=你是谁？",


}
responses = requests.get(f"https://api.a20safe.com/api.php?api=36&key=874b8e021569e42db3d0c3fe64317004&text=你是谁？")

print(responses.json())