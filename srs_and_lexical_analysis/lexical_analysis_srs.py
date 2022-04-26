import nltk 
from nltk import tokenize, word_tokenize, sent_tokenize, pos_tag
import numpy as np
import xlwt
from xlwt import Workbook
sentence1 = "The system must remember the order of the users"
sentence2 = "The system must execute every order requested by the user, even if some of or all the elevators stop working for a while."
sentence3 = "After reaching a floor, the doors must be open at least 3 seconds to ensure that the user has gotten out of the elevator"
sentence4 = "The elevator must stand still at the closest floor if it is affected by an obstruction"
sentence5 = "The lights on the hall panel and the floor panel must be switched on if the buttons are clicked by a user, and switch off when the elevator has gone tothe desired floor"
sentence6 = "The elevators must communicate with each other, so that they don’t try to pick up the same user"
sentence7 = "The elevator that gets the order by the user on its hall panel must distribute the order to the elevator that should optimally take it."
sentence8 = "If the elevators lose contact with each other, the elevator(s) must take the orders of the elevator(s) they have lost contact with."
sentence9 = "In case of motorstop of one or more elevators, the functioning elevator(s) must take on the order(s) of the elevator(s) that got the motorstop"
sentence10 = "The user of the elevators is a person. When the person presses a button on the buttonpanel, an elevator is supposed to come and get the person to its destination, specified by the button the person pushes inside of the elevator."
sentence11 = "The user of the elevators is a person."
sentence12 = "When the person presses a button on the buttonpanel, an elevator is supposed to come and get the person to its destination, specified by the button the person pushes inside of the elevator."
sentence13 = "If the doors don’t close, the elevator won’t run to ensure the safety of the passenger, and optimally the closest elevator should get the passenger. Expectations of the user can be that the order of the user is not lost, multiple elevators should get the user faster than only one, an individual elevator should behave sensibly and efficiently, meaning that it should get the passenger, get it to the desired floor, open doors when it is safe and not run if it is not safe. The lights and buttons should also function as expected."



functional_requirements_user_needs = "The system must remember the orders of the users. The system must execute every order requested by the user, even if some of or all the elevators stop working for a while. After reaching a floor, a timer should check that the doors are open at least 3 seconds, to ensure that the user has gotten out of the elevator. The elevator must stand still at the closest floor if it is affected by an obstruction. The lights on the hall panel and the floor panel must be switched on if the buttons are clicked by a user, and switch off when the elevator has gone to the desired floor. The elevators must communicate with each other via a network, so that they don’t try to pick up the same user. The elevator that gets the order by the user on its hall panel must distribute the order to the elevator that should optimally take it. If the elevators lose contact with each other, the elevator(s) must take the orders of the elevator(s) they have lost contact with. In case of motorstop of one or more elevators, the functioning elevator(s) must take on the order(s) of the elevator(s) that got the motorstop. The user of the elevators is a person. When the user presses a button on the buttonpanel, an elevator is supposed to come and get the user to its destination, specified by the button the user pushes inside of the elevator. If the doors don’t close, the elevator won’t run to ensure the safety of the user, and optimally the closest elevator should get the user. Expectations of the user can be that the order of the user is not lost, multiple elevators should get the user faster than only one, an individual elevator should behave sensibly and efficiently, meaning that it should get the user, get it to the desired floor, open doors when it is safe and not run if it is not safe. The lights and buttons should also function as expected."
#nltk.download('punkt')
nltk.download('words')
sentences = nltk.sent_tokenize(functional_requirements_user_needs)

tokens = nltk.word_tokenize(sentence8)

#for sentence in sentences: 
    #print(sentence, "\n")
#print(tokens)
#gives what kind of verb it is (preposition, noun etc)
tagged = pos_tag(tokens)

selectedtag = tagged[1]
selectedtokensynon = ['word', 0]


def get_nouns_verbs_adjectives(sentences): 
    nn_list = []
    nn_list_synon = []
    
    nn_verb_list = []
    nn_verb_list_synon = []

    nn_adj_list = []
    nn_adj_list_synon = []
    for sentence in sentences: 
        tokens = nltk.word_tokenize(sentence)
        tagged = pos_tag(tokens)
        for i in range(len(tagged)): 
            selectedtag = tagged[i] 
            selectedtype = selectedtag[1]
            selectedtoken = selectedtag[0]
    
            selectedtokensynon[0] = selectedtag[0]
            selectedtokensynon[1] = i
            if "NN" in selectedtype and len(selectedtoken) > 1: #== "NN" or selectedtype == "NNP" or selectedtype == "NNS" or selectedtype == "NNPS":
                if(selectedtoken in nn_list): 
                    nn_list_synon[nn_list.index(selectedtoken)][1] += 1
                else:     
                    nn_list.append(selectedtoken)
                    nn_list_synon.append([selectedtokensynon[0], 1])
            if selectedtype == "VB" and len(selectedtoken) > 1: 
                if(selectedtoken in nn_verb_list): 
                    nn_verb_list_synon[nn_verb_list.index(selectedtoken)][1] += 1
                else:     
                    nn_verb_list.append(selectedtoken)
                    nn_verb_list_synon.append([selectedtokensynon[0], 1])
            if "JJ" in selectedtype and len(selectedtoken) > 1:
                if(selectedtoken in nn_adj_list): 
                    nn_adj_list_synon[nn_adj_list.index(selectedtoken)][1] += 1
                else:     
                    nn_adj_list.append(selectedtoken)
                    nn_adj_list_synon.append([selectedtokensynon[0], 1])
                    
    return(
    nn_list_synon,
    nn_verb_list_synon,  
    nn_adj_list_synon)
    

def get_words_and_freq_in_excel(): 
    nn_list_synon, nn_verb_list_synon, nn_adj_list_synon = get_nouns_verbs_adjectives(sentences)
    wb = Workbook()
    sheet1 = wb.add_sheet('Sheet 1')
    sheet1.write(0, 0, 'Nouns')
    sheet1.write(0,1, 'frequency')
    sheet1.write(0,3, 'Verbs')
    sheet1.write(0,4, 'frequency')
    sheet1.write(0,6, 'Adjectives')
    sheet1.write(0,7, 'frequency')
    for i in range(len(nn_list_synon)): 
        sheet1.write(i+1, 0, nn_list_synon[i][0])
        sheet1.write(i+1, 1, nn_list_synon[i][1])
        
    for i in range(len(nn_verb_list_synon)): 
        sheet1.write(i+1, 3, nn_verb_list_synon[i][0])
        sheet1.write(i+1, 4, nn_verb_list_synon[i][1])
        
    for i in range(len(nn_adj_list_synon)): 
        sheet1.write(i+1, 6, nn_adj_list_synon[i][0])
        sheet1.write(i+1, 7, nn_adj_list_synon[i][1])

    wb.save('wordtypes and frequency.xls')
                    

get_words_and_freq_in_excel()
            
"""       

i = 1 
nn_list = []
nn_list_synon = []
for i in range(len(tagged)): 
    selectedtag = tagged[i] 
    selectedtype = selectedtag[1]
    selectedtoken = selectedtag[0]
    
    selectedtokensynon[0] = selectedtag[0]
    selectedtokensynon[1] = i
    if "NN" in selectedtype: #== "NN" or selectedtype == "NNP" or selectedtype == "NNS" or selectedtype == "NNPS":
        if(selectedtoken in nn_list): 
            nn_list_synon[nn_list.index(selectedtoken)][1] += 1
        else:     
            nn_list.append(selectedtoken)
            nn_list_synon.append([selectedtokensynon[0], 1])
            #nn_list_synon.append(selectedtokensynon[0:2])
print("nouns: ", nn_list)
print("nouns and place: ", nn_list_synon)


#make list with nouns, words and adjectives 

i = 1 
nn_verb_list = []
nn_verb_list_synon = []
for i in range(len(tagged)): 
    selectedtag = tagged[i] 
    selectedtype = selectedtag[1]
    selectedtoken = selectedtag[0]
    selectedtokensynon[0] = selectedtag[0]
    selectedtokensynon[1] = i
    if selectedtype == "VB": 
        if(selectedtoken in nn_verb_list): 
            nn_verb_list_synon[nn_verb_list.index(selectedtoken)][1] += 1
        else:     
            nn_verb_list.append(selectedtoken)
            nn_verb_list_synon.append([selectedtokensynon[0], 1])
        
print("verbs: ", nn_verb_list)
print("verbs and place: ", nn_verb_list_synon)

i = 1 
nn_adj_list = []
nn_adj_list_synon = []
for i in range(len(tagged)): 
    selectedtag = tagged[i] 
    selectedtype = selectedtag[1]
    selectedtoken = selectedtag[0]
    
    selectedtokensynon[0] = selectedtag[0]
    selectedtokensynon[1] = i
    if "JJ" in selectedtype and selectedtoken != 's':
        if(selectedtoken in nn_adj_list): 
            nn_adj_list_synon[nn_adj_list.index(selectedtoken)][1] += 1
        else:     
            nn_adj_list.append(selectedtoken)
            nn_adj_list_synon.append([selectedtokensynon[0], 1])

print("adjectives: ", nn_adj_list)
print("adjectives and place: ", nn_adj_list_synon)
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')
  
sheet1.write(0, 0, 'Nouns')
sheet1.write(0,1, 'frequency')
sheet1.write(0,2, 'Verbs')
sheet1.write(0,3, 'frequency')
sheet1.write(0,4, 'Adjectives')
sheet1.write(0,5, 'frequency')
for i in range(len(nn_list)): 
    sheet1.write(i+1, 0, nn_list_synon[i][0])
    sheet1.write(i+1, 1, nn_list_synon[i][1])
    
for i in range(len(nn_verb_list)): 
    sheet1.write(i+1, 2, nn_verb_list_synon[i][0])
    sheet1.write(i+1, 3, nn_verb_list_synon[i][1])
    
for i in range(len(nn_adj_list)): 
    sheet1.write(i+1, 4, nn_adj_list_synon[i][0])
    sheet1.write(i+1, 5, nn_adj_list_synon[i][1])

wb.save('wordtypes and frequency.xls')




a = 1
"""