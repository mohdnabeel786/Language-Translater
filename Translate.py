from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from textblob import TextBlob

root = Tk()
root.geometry('500x400')
root.title('Translator')
root.iconbitmap('Goodstuff-No-Nonsense-Free-Space-Earth.ico')
root.configure(bg = 'red')
root.resizable(0,False)
lang_dict = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}

def tt(event=None):
    try:
        word3 = TextBlob(varname1.get())
        lan = word3.detect_language()
        lan_todict = language.get()
        lan_to = lang_dict[lan_todict]
        word3 = word3.translate(from_lang=lan,to=lan_to)
        #label3.configure(text=word3)
        varname2.set(word3)
    except:
        varname2.set('Try to right keyword')

def main_exit():
    rr = messagebox.askyesno('Notification', 'Are you sure',parent = root)
    if(rr == True):
        root.destroy()

############################################# Binding Function

def on_enterentry1(e):
    entry1['bg'] = 'yellow'

def on_leaveentry1(e):
    entry1['bg'] = 'white'

def on_enterentry2(e):
    entry2['bg'] = 'yellow'

def on_leaveentry2(e):
    entry2['bg'] = 'white'

def on_enterbut1(e):
    but1['bg'] = 'yellow'

def on_leavebut1(e):
    but1['bg'] = 'black'

def on_enterbut2(e):
    but2['bg'] = 'yellow'

def on_leavebut2(e):
    but2['bg'] = 'black'

############################################## Combobox Languages

language = StringVar()
font_box = Combobox(root,textvariable=language, state='readonly')
font_box['values'] = [e for e in lang_dict.keys()]
font_box.current(37)
font_box.place(x=350, y=2)

############################################### Entry box

varname1 = StringVar()
entry1 = Entry(root, width=30, textvariable=varname1, font=('times', 15, 'bold italic'))
entry1.place(x=150, y=40)

varname2 = StringVar()
entry2 = Entry(root, width=30, textvariable=varname2, font=('times', 15, 'bold italic'))
entry2.place(x=150, y=100)

############################################# Labels

label1 = Label(root, text='Enter Words :', font=('times', 15, 'bold italic'), bg='red')
label1.place(x=10, y=40)

label2 = Label(root, text='Translated :', font=('times', 15, 'bold italic'), bg='red')
label2.place(x=10, y=100)

label3 = Label(root, text=' ', font=('times', 15, 'bold italic'), bg='red')
label3.place(x=10, y=250)

########################################## Button
#
# imgbt1 = PhotoImage(file='pay-per-click-icon.png')
# imgbt2 = PhotoImage(file='Users-Exit-icon.png')

# imgbt1.subsample(2,2)
# imgbt2.subsample(2,2)
but1 = Button(root,text='Click ', bd=10, bg='black', fg='white', activebackground='white', width=10, font=('times', 15, 'bold italic'), command=tt)# image=imgbt1, compound=RIGHT
but1.place(x=70, y=170)

but2 = Button(root,text='Exit ', bd=10, bg='black', fg='white', activebackground='white', width=10, font=('times', 15, 'bold italic'), command=main_exit)#, image=imgbt2, compound=RIGHT
but2.place(x=280, y=170)
root.bind('<Return>', tt)

######################################### Binding

entry1.bind('<Enter>', on_enterentry1)
entry1.bind('<Leave>', on_leaveentry1)

entry2.bind('<Enter>', on_enterentry2)
entry2.bind('<Leave>', on_leaveentry2)

but1.bind('<Enter>', on_enterbut1)
but1.bind('<Leave>', on_leavebut1)

but2.bind('<Enter>', on_enterbut2)
but2.bind('<Leave>', on_leavebut2)


root.mainloop()