import os

def cls():
	os.system('clear')

def ask(phrase : str) -> str:
    print('>>>Answer the question then press enter<<<\n')
    print(phrase)
    response = input('>> ')
    input('\nPlease press enter and pass the computer...')
    cls()
    return response


### BEGIN PROGRAM ###
cls()

#Adjective 1
adjective1 = ask('Please enter an adjective')

#Season 
print('Choose a season...')
print('\t1. Summer\n\t2. Autumn\n\t3. Winter\n\t4. Spring\n')
ask("""Choose a season...\n""")

story_string = ""
story_string += noun1+" was "+verb1+" there way to the "+place1+" with their "+noun2+'. But suddenly, a wild '+noun3+' approaches! Your '+noun2+' '+verb2+' '+adverb1+'.'

print(story_string)

