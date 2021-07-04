from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from textblob import TextBlob
from PIL import ImageTk,Image #PIL Module For Background Images

root = Tk()
root.geometry('500x500')
root.title('Translator')
root.iconbitmap('Earth.ico') #To Put Icon(ICO Images)
root.resizable(0,0)
root.config(bg='Pink')
canvas = Canvas(root,width=700,height=500)
image = ImageTk.PhotoImage(Image.open('isaac-li-shung-tan-41kK8u7N5eQ-unsplash.png'))
canvas.create_image(0,0,anchor=NW,image=image)


lan_dict = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar'
    , 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be',
            'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca',
            'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn',
            'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr',
            'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en',
            'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi',
            'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de',
            'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw',
            'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is',
            'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja',
            'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko',
            'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv',
            'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms',
            'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn',
            'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps',
            'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro',
            'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st',
            'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl',
            'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv',
            'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk',
            'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh',
            'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}

#############################################Message Box########################################################
def tt():
    try:
        word3 = TextBlob(Varname.get())
        lan = word3.detect_language()
        lantodict = languages.get()
        lan_to = lan_dict[lantodict]
        word3 = word3.translate(from_lang=lan, to=lan_to)
        Varname2.set(word3)
    except:
        print('Try another word')

def main_exit():
    rr = messagebox.askyesnocancel('Notification','Are you want to exit',parent=root)
    if(rr==True):
        root.destroy()

######################################ComboBox Lang############################################3
languages = StringVar()
font_box = Combobox(root,width=30,textvariable=languages,state='readonly')
font_box['values'] = [e for e in lan_dict.keys()]
font_box.current(37)
font_box.place(x=170,y=150)

#######################################Entry Box#################################################
Varname = StringVar()
entry1 = Entry(root,width=30,textvariable=Varname,font=('times',15,'bold'))
entry1.place(x=150,y=100)
Varname2 = StringVar()
entry2 = Entry(root,width=30,textvariable=Varname2,font=('times',15,'bold'))
entry2.place(x=150,y=200)

#######################################Labels#####################################################
label1 = Label(root,text='Enter Word  :',font=('times',15,'italic bold'),bg='White')
label1.place(x=5,y=100)
label2 =  Label(root,text='Translate',font=('times',15,'italic bold'),bg='white')
label2.place(x=5,y=200)
label3 = Label(root,text='',font=('times',15,'italic bold'),bg='white')
label3.place(x=5,y=100)

##################################Buttons#######################################################
btn1 = Button(root,text='click',fg='Blue',bd=10,bg='yellow',activebackground='green',width=10,font=('times',15,'bold'),compound=RIGHT,command=tt)
btn1.place(x=80,y=270)
btn2 = Button(root,text='Exit',fg='Blue',bd=10,bg='yellow',activebackground='red',width=10,font=('times',15,'bold'),compound=RIGHT,command=main_exit)
btn2.place(x=280,y=270)
canvas.pack()
root.mainloop()