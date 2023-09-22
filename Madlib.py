def madlib_gen():

    # function to select story the user desires
    def story_selector(): 
        while True:
            story_select = input('Enter a value between one and three to select a story').lower()
            if story_select.isalpha(): 
            #checks if the user enter the value as a word, and converts it into a number    
                if story_select in ['one','two','three']:
                    int_story_select = {'one': 1, 'two': 2, 'three': 3}[story_select]
                    break
                else:
                    print("Please enter a value between one and three")    
            elif story_select.isnumeric():
            #checks if user entered an integer in the correct range
                int_story_select = int(story_select) 
                if 1 <= int_story_select <= 3:
                    break
                else:
                    print('Enter a value between one and three')
            else: 
                print('You have entered something not quire right, try again')
        print(f'You selected story {story_select}')
        return int_story_select   
    

    #function to ask user to input something for the story
    def storyadd(name):
        vowels = ['i','o','u','a','e']
        first_lett = name[0]
        if first_lett in vowels:
            question = f'Enter an {name}'
        else:
            question = f'Enter a {name}'
        #if-else statment ensures correct grammar  with a and an       
        while True:
        #while loop to ensure only words are entered (no numeric characthers)
            story_item = input(question)
            if story_item.isalpha():
                return story_item.lower()
            else:
                print('Please enter a word')                   

    if story_selector() == 1: 
        name = storyadd('name')
        verb = storyadd('verb')
        animal = storyadd('animal')
        story = 'During my data science bootcamp, I got bored so I decided to go out and ' + verb + '. Whilst I was out I forgot to pick up my ' + \
        animal + ' from my friend ' + name.capitalize() + ' so I had to leave. ' 
    elif story_selector() == 2:
        object = storyadd('object')
        name = storyadd('name')
        story = 'During my GP appointment, I met my friend ' + name.capitalize() + ' and left behind ' + object + '.'
    elif story_selector() == 3:
        adjective1 = storyadd('adjective')
        noun1 = storyadd('noun')
        animal = storyadd('animal')
        adjective2 = storyadd('adjective')
        noun2 = storyadd('noun')
        name = storyadd('name')
        story = 'Once upon a ' + adjective1 + ' ' + noun1 + ', there lived the ' + animal + ' named ' + name.capitalize() + ' who had a ' + adjective2 + ' ' + noun2 + '.'

    return story

madlib_gen()