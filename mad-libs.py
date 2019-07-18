#import tkinter for graphics
from tkinter import *

#list for questions and answers
#more questions will later be appended (.extend()) to the question list too
#answers are added onto answers list as the program runs
questions = ['Enter an adjective related to water...', 'Enter the name of the person sitting physically closest to you...', 'Use an adjective to describe aliens...', 'Name something red (singular)...', 'Enter a verb ending in ing...', 'Use an adjective to describe the sun...', 'Enter a number...any number...', 'Press '1' to send Kyles\nPress '2' to send Karens']
answers = []

#define question numbers where a break should occure
#then call do story to print story so far
#break is last question number is story section
breaks = [3,7,8,14]

#run everytime some of the story needs to be told
def do_story():
    # q_num and questions are global so they can be modified within the function globally
    global q_num
    global questions
    global breaks

    if q_num == 3:
        #print story so far and return
        story.set("""It is the morning of September 20th, 2019. Yet the sun can't be seen. The """+answers[0]+""" fog covers the desert. You and your "best friend" """+answers[1]+""" ;) are joining in on the raid of Area 51. People are chanting "Free them """+answers[2]+""" aliens!!!" And then you know, you and """+answers[1]+""" will be victorious today.""")
    elif q_num == 7:
        # 7 is right before choice, print story so far, and then go back to questions[7] (q_num=8) to make choice
        story.set("""Around you are middle-aged women with """+answers[3]+""" red lipstick, they look like they're itching to speak to the managers of Area 51. Obviously Karens. Further out, """+answers[4]+""" in the """+answers[5]+""" desert sun, Monster Energy drinks litter the ground, lightly dusted in """+answers[6]+""" inches of drywall dust. The Kyles. Definitely. You and """+answers[1]+""" are the chosen leaders of this raid, chosen because of how cute both of you are together ;). Do you chose to send out the Kyles or Karens into battle first? We really need them aliens.""")
    elif q_num == 8:
        #this is after use chooses between karens and kyles, need to add corresponding questions to end of questions list, which is a global
        if answers[7] == str(1):
            #if the answer to the choice answers[7] is 1, they chose Kyles
            #append the new corresponding questions to the questions list (which is global)
            questions.extend(['Enter an adjective that reminds you of power...', 'Enter a verb ending in ing...', 'Enter another verb ending in ing...', 'Enter an adverb (ends in -ly)...', 'Enter a body part (plural)...', 'Enter your favorite color...'])
            #after appending, you don't need to continue in do_story() loop because there is no new story to print
        else: 
            #if the answer to choice answers[7] is 2 (else), they chose Karens
            #append the new corresponding questions to the questions list (which is global)
            questions.extend(['Enter a verb ending in ing...', 'Enter an adjective...', 'Enter another verb ending in ing (something violent)...', 'Enter a superlative (ending in -est)...', 'Enter a 3-digit code...', 'Something you look for in a lover (adjective)...'])
            #after appending, you don't need to continue in do_story() loop because there is no new story to print
    #q_num 14 should be the end of the story (so far), so then print the remaining story
    elif q_num == 14:
        #check the answer to the choice so the right part of the story is printed
        #Kyles
        if answers[7] == str(1):
            story.set("""You chose to send the Kyles first. Their blood pumping with the """+answers[8]+""" power of good 'ol Monster Energy. As you are """+answers[9]+""" through the desert terrain, you feel the water in the air """+answers[10]+""" your face. The kyles pile up against the gates and begin punching the walls """+answers[11]+""". But this is concrete, not drywall. It won't break. Annoyed with their failure, they begin bashing their """+answers[12]+""" on the walls, and they slowly begin dying. """+answers[13].capitalize()+""" blood covers the ground, the Kyles are down. It's up to the Karens now.""")
        #Karens
        else:
            story.set("""The Karens march across the desert, """+answers[8]+""" at the """+answers[9]+""" guards. """+answers[1]+""" whispers to you, "I'm glad they're on our side xD". A high pitch droning starts, each of the Karens """+answers[10]+""" the guards. Using this as a distraction, the Kyles try to get through the door, which asks for a 3 digit pin. First, the """+answers[11]+""" Kyle tried the code '"""+answers[12]+"""'. It works! We're in! I can already smell them """+answers[13]+""" aliens.""")

    breaks.remove(q_num)
    #unpack all elements to show story
    q_text.pack_forget()
    q_input.pack_forget()
    q_num_label.pack_forget()
    submit_button.pack_forget()
    bottom_instructions.pack_forget()
    #pack label to show story
    story_lbl.pack(pady='20')
    #continue button to go back to story
    continue_button.pack(pady='15')


#function for when submit button is clicked
def ask(*args):
    #specify q_num as a global variable so it can be edited
    global q_num

    if not (len(q_input.get())) == 0:
        answers.append(q_input.get())
    #empty text box
    q_input.delete(0, END)

    print(answers)
    #if the current question number is in breaks, dont run continue story, go to print story: do_story()
    if q_num in breaks:
        do_story()
        if q_num != 8:
            return 
    
    #hide story and continue button
    story_lbl.pack_forget()
    continue_button.pack_forget()

    #add one to the question number
    #append answer from textbox to answers list
    #return string for question number and move to next question text
    q_num+=1
    q_act.set(questions[q_num-1])
    q_num_str.set('Question '+str(q_num)+' of '+str(len(questions)))

    #if the question number is in the breaks list, call do_story

    #get ready to ask new question
    #repackage (show) asking elements)
    q_text.pack(pady='10')
    q_input.pack(pady='20')
    q_num_label.pack(pady='10')
    submit_button.pack()
    bottom_instructions.pack(side='bottom')

#create tkinter window, set title, background color, and size
window = Tk()
window.title('Mad-Libs')
window.configure(background='black')
window.geometry('1300x700')

#initialize question numbers and initial question
#INITIAL ONLY
q_num = 1
story =  StringVar()
q_act = StringVar()
q_act.set(questions[0])
q_num_str = StringVar()
q_num_str.set("Question 1 of "+str(len(questions)))
#enter button does the same thing as the submit button
window.bind('<Return>', ask)


### MAIN ASKING GUI ###
#title
main_title = Label(window,text='Mad-Libs',bg='black',fg='red',font='Courier 50 bold').pack(pady='10')
#question text
q_text = Label(window,textvariable=q_act,bg='black',fg='red',font='Courier 20')
q_text.pack(pady='10')
#entry box for text
q_input = Entry(window,width=20,bg='white',font='Courier 16')
q_input.pack(pady='20')
#question number string
q_num_label = Label(window,textvariable=q_num_str,bg='black',fg='red',font='Roboto 20')
q_num_label.pack(pady='10')
#submit button
submit_button = Button(window,text='SUBMIT',width=10,command=ask)
submit_button.pack()
#question number and instructions on the bottom
bottom_credits = Label(window, bg='black',fg='red',text='Created by: BL4Z3, h4ckerm4n_z4ch, b1g n@te, and PW3Z',font='Courier 18').pack(side='bottom',pady='10')
#instructions at bottom for entering text
bottom_instructions = Label(window,bg='black',fg='white',text='Answer the question in the text box and press enter',font='Courier 15')
bottom_instructions.pack(side='bottom')

#HIDDEN WIDGETS
story_lbl = Label(window, textvariable=story, width='600', justify='center', wraplength='600', bg='black', fg='white', font='Courier 17')
continue_button = Button(window, text='CONTINUE', width='15', command=ask)


#begin main GUI loop
window.mainloop()
