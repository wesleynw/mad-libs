from tkinter import *

q_num = 1

#function for when submit button is clicked
def click():
    answer = textentry.get() #get answer from program
    q_num += 1
    textentry.delete(0.0, END)

#create tkinter window, set title, background color, and size
window = Tk()
window.title('Mad-Libs')
window.configure(background='black')
window.geometry('1000x600')

#title
Label(window,text='Mad-Libs',bg='black',fg='white',font='Courier 50 bold').pack(pady='10')

#entry box for text
textentry = Entry(window,width=20,bg='white',font='Courier 18')
textentry.pack(pady='20')

#submit button
window.bind('<Return>',click)
Button(window,text='SUBMIT',width=6,command=click).pack()


#question number and instructions on the bottom
Label(window,bg='black',fg='white',text='Answer the question in the text box and press enter',font='Courier 15').pack(side="bottom")
Label(window,text='Question '+str(q_num)+' of 20',bg='black',fg='white',font='Courier 20').pack(side='bottom',pady='20')




#begin main GUI loop
window.mainloop()
