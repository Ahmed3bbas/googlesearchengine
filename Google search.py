import webbrowser as web
from tkinter import *
from urllib.request import quote
from PIL import Image
import os

main_url = "https://www.google.com.eg/search?q="
facebook_url = "http://www.facebook.com"
youtube_url = "http://www.youtube.com"
gmail_url = "http://www.gmail.com"
nile_col = "#128fda"
window_bg = "#DDD"
font_color = "white"
size = "650x150"
raw1 = 0.35
raw2 = 0.75
SM_mg = 0.12 # social Media Margin
SM_relx = 0.95
icon_size = (25, 25)

fb_icon_Location = "icons/facebook-icon.png"
fb_icon_save = 'icons/resized-facebook-icon.png'
yt_icon_Location = "icons/youtube-icon.png"
yt_icon_save = "icons/resized-youtube-icon.png"
gm_icon_Location = "icons/gmail-icon.png"
gm_icon_save = "icons/resized-gmail-icon.png"




def quick_search():
    searched_word = entry.get()
    v.set("")
    if len(searched_word) != 0:
      URL = main_url + quote(searched_word)
      web.open(URL)

def open_url(url):
  web.open(url)


def create_butt(url, icon, relx, rely):
  butt = Button(root, image= icon,
               bg= window_bg,
               bd=  0,
               command =  lambda: open_url(url))
  butt.place(relx=relx, rely=rely, anchor=CENTER)
  return butt

########## root & Configrution
root = Tk()
root.title("Google Search")
root.iconbitmap(r"icons/google.ico")
root.configure(background= window_bg)
root.option_add("*Button.Background", "grey")
root.option_add("*Button.Foreground", nile_col)
root.geometry(size)
root.resizable(0, 0)
#frame = Frame(root,width = 300,height = 300,bg="grey")
#frame.pack()


########## Widgets
v = StringVar()
label = Label(root,font = "Helvetica 15 bold",
              text="Google Search \n Engine",
              bg =window_bg,
              fg = nile_col,
              padx = 10)
label.place(relx=0.13, rely=raw1 + 0.03, anchor=CENTER)
#label.grid(row=0)

entry = Entry(root,
              textvariable = v,
              bg=nile_col,
              fg=font_color,
              width = 25,
              bd = 1,
              font = "Helvetica 22 bold",
              justify="center",
              relief = 'solid')
entry.place(relx=0.60, rely=raw1, anchor=CENTER)
#entry.grid(row=0,column=1)
entry.focus_set()
entry.bind('<Return>',lambda event: quick_search())



##### Facebook Button
if os.path.exists(fb_icon_save):
  fb_icon = PhotoImage(file=fb_icon_save)
  facebutton = create_butt(facebook_url, fb_icon,relx=SM_relx, rely=raw1-SM_mg)

elif os.path.exists(fb_icon_Location):  
  image = Image.open(fb_icon_Location)
  image = image.resize(icon_size, Image.ANTIALIAS) ## The (250, 250) is (height, width)
  image.save(fb_icon_save) ## The only reason I included this was to convert
  
  fb_icon = PhotoImage(file=fb_icon_save)
  facebutton = create_butt(facebook_url, fb_icon,relx=SM_relx, rely=raw1 - SM_mg)


##### youtube Button
if os.path.exists(yt_icon_save):
  yt_icon = PhotoImage(file=yt_icon_save)
  facebutton = create_butt(youtube_url, yt_icon,relx=SM_relx, rely=raw1 + SM_mg)

elif os.path.exists(yt_icon_Location):  
  image = Image.open(yt_icon_Location)
  image = image.resize(icon_size, Image.ANTIALIAS) ## The (250, 250) is (height, width)
  image.save(yt_icon_save) ## The only reason I included this was to convert
  
  yt_icon = PhotoImage(file=yt_icon_save)
  facebutton = create_butt(youtube_url, yt_icon,relx=SM_relx, rely=raw1 + SM_mg)

##### Gmail Button
if os.path.exists(gm_icon_save):
  gm_icon = PhotoImage(file=gm_icon_save)
  facebutton = create_butt(gmail_url, gm_icon,relx=SM_relx, rely=raw1 + 2.8 * SM_mg)

elif os.path.exists(gm_icon_Location):  
  image = Image.open(gm_icon_Location)
  image = image.resize(icon_size, Image.ANTIALIAS) ## The (250, 250) is (height, width)
  image.save(gm_icon_save) ## The only reason I included this was to convert
  
  gm_icon = PhotoImage(file=gm_icon_save)
  facebutton = create_butt(gmail_url, gm_icon,relx=SM_relx, rely=raw1 + 2.8 * SM_mg)



#### Search Button
but = Button (root,font = "Helvetica 15 bold",text="Search",bg=nile_col,fg=font_color,bd =0,command=quick_search)
but.place(relx = 0.5, rely = raw2, anchor=CENTER)

root.mainloop()

