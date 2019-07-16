import os


def cls():
	os.system('clear')

def ask(phrase):
    #print('Question '+n+' of 20')
    print('>>>Answer the question then press enter<<<\n')
    print(phrase)
    response = input('>> ')
    input('\nPlease press enter and pass the computer...')
    cls()
    return response.lower()

### BEGIN PROGRAM ###
cls()

#Adjective 1
adjective1 = ask('Please enter an adjective')

#Season 
season = ask("""Choose a season...\n\t1. Summer\n\t2. Autumn\n\t3. Winter\n\t4. Spring\n""")
if season == 1:
    season = "summer"
elif season == 2:
    season = "autumn"
elif season == 3:
    season = "winter"
elif season == 4:
    season = "spring"
else: 
    season = "summer"

#Year
year1 = ask('Please enter a year')

#Age
age1 = ask('Please enter a number between 1 and 999')

#Noun 1
noun1 = ask ('Please enter a noun')

#Name 1 
name1 = ask('Please enter a name')

#Verb 1 
verb1 = ask("""Enter a verb (ending in 'ing')""")

#Street name 1 
street1 = ask('Enter the name of a street')

#Adverb 1 
adverb1 = ask("""Please enter an adverb (BTW adverbs end in '-ly')""")

#Adjective 1 
adjective1 = ask('Please enter an adjective')

#Noun 2
noun2 = ask('Please enter a noun')

#Place 1 
place1 = ask('Enter the name of a place')

#Body part 1 
body_part1 = ask('Enter the name of a body part')

#Verb 2 
verb2 = ask("""Please enter a verb (ending in 'ing')""")

#Verb 3 
verb3 = ask('Please enter a verb (Past tense)')

#Adjective 2
adjective2 = ask('Please enter an adjective')

#Verb 4 
verb4 = ask("""Please enter a verb (ending in 'ing')""")

#Name 2
name2 = ask('Enter a name')

#Animal 1 
animal1 = ask('Enter a type of animal')

story_string = 'In the '+adjective1+' '+season+' of '+year1+'. There was a '+age1+' year old '+noun1+', and it was named '+name1+'. It was '+verb1+' down '+street1+' street when '+adverb1+' a '+adjective2+' '+noun1+' popped out of the '+noun2+'. Scared out of his '+body_part1+', the '+noun1+' '+verb3+'. The rain was '+adjective2+' and the clouds closed in. All of a sudden, the clouds began to '+verb4+' and '+name2+' came down from the skies in the form of a '+animal1+'.'


print(story_string)
