from tkinter import *
from yt_dlp import YoutubeDL  

def hight_quality():  
    try:  
        url = entry.get()  

        yd1_opts = {  
            'format': 'worst',  
            'outtmpl': 'downloads%/(title)s.%(ext).s'  
        }  

        with YoutubeDL(yd1_opts) as yd1:  
            yd1.download([url])  

        print("The video has been downloaded")  

    except Exception as e:  
        print("Error downloading:", e)


def low_quality():  
    try:  
        url = entry.get()  

        yd1_opts = {  
            'format': 'best',  
            'outtmpl': 'downloads%/(title)s.%(ext).s'  
        }  

        with YoutubeDL(yd1_opts) as yd1:  
            yd1.download([url])  

        print("The video has been downloaded")  

    except Exception as e:  
        print("Error downloading:", e)

def get_audio():  
    try:  
        url = entry.get()  

        yd1_opts = {  
            'format': 'bestaudio',  
            'outtmpl': 'downloads/%(title)s.%(ext)s'


        }  

        with YoutubeDL(yd1_opts) as yd1:  
            yd1.download([url])  

        print("The audio has been downloaded")  

    except Exception as e:  
        print("Error downloading:", e)

# إعداد نافذة tkinter
Window = Tk()
Window.title("YouTube Downloader")
Window.geometry("600x400")
Window.configure(bg = "#6E8B3D")

# إضافة النص
Label = Label(Window, text="Add Your YouTube Link", font="bold", bg=Window['bg'])
Label.place(x=200, y=30)

# إضافة حقل الإدخال
entry = Entry(Window, width=50)
entry.place(x=150, y=100)

# إضافة الأزرار
hight = Button(Window, text="High Quality", command=hight_quality, font="bold", activeforeground="green")
hight.place(x=100, y=200)

low = Button(Window, text="Low Quality", command=low_quality, font="red", activeforeground="green")
low.place(x=250, y=200)

audio = Button(Window, text="Get Audio", command=get_audio, font="bold", activeforeground="blue")
audio.place(x=400, y=200)

# بدء التطبيق
Window.mainloop()
