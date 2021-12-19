from tkinter import *

window = Tk()
window['bg'] = '#FCA311'
window.geometry('200x100')
window.resizable(0, 0)
window.frames = None
window.title('pyClima')
window.wm_iconbitmap('images/weather.ico')

label = Label(window, text='40º', bg='#FCA311', font= 'impact 50 bold').place(x=90, y=5)
label2 = Label(window, text='nublado', bg='#FCA311', font= 'impact 10 bold').place(x=10, y=40)





window.mainloop()