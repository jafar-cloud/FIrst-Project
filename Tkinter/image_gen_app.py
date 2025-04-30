import tkinter as tk
import requests
from io import BytesIO
from PIL import Image, ImageTk



window = tk.Tk()

label_img = tk.Label(window)
label_img.pack()

messagebox = tk.Label(window)
messagebox.pack()

window.geometry("1000x1000")

entry = tk.Entry(window)
entry.pack()

def generate_image():
    api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Ijk3NTYyMWRlNTkzYzllZGVlOWUxOWIzY2Y5ZmRjYmMxIiwiY3JlYXRlZF9hdCI6IjIwMjUtMDQtMzBUMTE6NDI6MTEuNzc3NzY5In0.Y443QfbkZ95eeczcmXPxDy52cZZ9mdpgwjFFFGj6VhI"
    url = "https://api.monsterapi.ai/v1/generate/txt2img"
    headers = {"Authorization": f"Bearer {api_key}"}

    prompt = entry.get()

    response = requests.post(url, json={"prompt": prompt, "safe_filter": True}, headers=headers)

    if response.status_code == 200:
        process_id = response.json().get("process_id")

        

        while True:
            status_data = requests.get(f"https://api.monsterapi.ai/v1/status/{process_id}", headers=headers).json()
            status = status_data.get("status")

            if status == "COMPLETED":
                image_url = status_data['result']['output'][0]
                img_data = requests.get(image_url).content
                img = Image.open(BytesIO(img_data))

                img_tk = ImageTk.PhotoImage(img)
                label_img.config(image=img_tk)
                label_img.image = img_tk
                break
                
            elif status == "FAILED":
                label_img.config(text="Image generation failed.")
                break
        

generate_image = tk.Button(window, text="Generate Image", command=generate_image)
generate_image.pack()


window.mainloop()