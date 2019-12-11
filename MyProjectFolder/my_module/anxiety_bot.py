import random
import string
import nltk

#Takes the input and makes it all lower case
def same_input(letter):
    letter = letter.lower()
    return letter

def should_continue(ans):
    """
    Checks answer to question to see if it should iterate 
    to next question or stops asking questions.
    
    Parameters
    ----------
    ans: str
        The input from the user.
        
    Returns
    ----------
    return: bool
        Shows if answer matches expected input.
        
    """
    if ans == 'b':
        return False
    elif ans == 'a':
        return True

def end_chat(input_list): #From A3-Chatbots, Q16 - End Chat
    if 'b' in input_list:
        output = True
    else:
        output = False
    return output

def question(num):
    """
    Defines a dictionary that stores the questions 
    and its answers to a number for the counter
    
    Parameters
    ----------
    num: int
        The number of the question and answer that shoul be printed.
    
    Return
    ----------
    qlist = string
        Returns the specified key as a statement.
    """
    qlist = {
        1: "Hello. What is the problem? \n A) I have anxiety. \n B) I'm okay.",
        2: "Do you feel excessive danger, worry, or panic? \n A) Yes. \n B) No.",
        3: "Are your fears based on reality? \n A: Yes. \n B: No.",
        4: "Why are you feeling anxious? \n A: I'm unsure \n B: I located the source",
        5: "Is there evidence to support how I feel? \n A) Yes. \n B) No.",
        6: "What kind of evidence? \n A) Scenarios I created \n B) Facts of matter",
        7: "What kind of scenarios? \n A) Worst case. \n B) Realistic ones",
        8: "Let's practice a grounding technique. \n Enter A to begin.",
        9: "Idenitfy 5 things you can SEE. \n Enter A) once you have finished.",
        10: "Identify 4 things you can TOUCH. \n Enter A) once you have finished.",
        11: "Identify 3 things you can SMELL. \n Enter A) once you have finished.",
        12: "Identify 2 things you can HEAR. \n Enter A) once you have finished.",
        13: "Identify 1 emotion you can FEEL. \n Enter A)."
    }
    
    return qlist.get(num, "Thanks for chatting. Hope you feel better.")

def anxiety_help():
    """
    Uses a counter to go through the dictionary
    and acts as the main function of the chatbot
    """
    treat = True
    count = 1
    while treat:
        print(question(count))
       
        if count > 13:
            break
        ans = input('Answer:\t')
        ans = same_input(ans)
        if ans == 'a' and should_continue(ans) == True:
            count += 1
        elif ans == 'b' and should_continue(ans) == False:
            end_chat(ans)
            treat = False
            print("Come back if you need anymore help, goodbye!")
        else:
            print("Sorry that answer is not valid. Try again.")
            
        #out_ans = None
        
        #ans = prepare_text(ans)
        
        #if end_chat(ans):
            #out_ans = 'Come back if you need anymore help, goodbye!'
            #treat = False