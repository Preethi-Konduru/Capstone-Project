
#Meet Ted: your friend

#import necessary libraries

import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')
import requests
import nltk
from datetime import datetime
import pyfiglet as py

#Reading in the corpus
with open('chatbot.txt','r', encoding = 'utf8',  errors ='ignore') as fin:
    raw = fin.read().lower()

#TOkenisation
sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences 
word_tokens = nltk.word_tokenize(raw)# converts to list of words

# Keyword Matching
GREETING_INPUTS = ["hello", "hi", "greetings", "what's up", "hey"]
GREETING_RESPONSES = ["hi", "hey", "hi there", "hello", "I am glad! You are talking to me"]

def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


# Generating response
def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(stop_words = "english")
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    #print(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    #print(idx)
    flat = vals.flatten()
    #print(flat)
    flat.sort()
    req_tfidf = flat[-2]
    #print(req_tfidf)
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response


flag=True
print(py.figlet_format("WELCOME TO CHATBOT DASHBOARD",font='digital'))
#print("{•̃_•̃}")
#print("d[ 0_0 ]b")
print("""  
         \_-_/
        <[p q]>
         |===|
          d b    
""")

print("Ted: Hi There! My name is Ted. I am here to answer your queries. If you want to exit, type Bye!")
name = input("What's your name?\n")
from news import *
print(Fore.MAGENTA, pf.figlet_format(name, font='starwars'))
print("Glad to meet you," + name)
print("How can I help you?\n")
while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("Ted: You are welcome..")
        else:
            if(greeting(user_response)!=None):
                print("Ted: "+greeting(user_response))
            else:
                if(user_response=='date' or user_response=='datetime'):
                    now = datetime.now()
                    #print("now =", now)
                    # dd/mm/YY H:M:S
                    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                    print("Ted: ","date and time =", dt_string)
                else:
                    if (user_response == 'anything interesting'):
                        print("Ted: Okay! I have something interesting for you\n")
                        print("forecast\nnews\nstock\nWhat would you like to see?\n")
                    else:
                        if (user_response == 'forecast' or user_response=='weather' or user_response=='climate'):
                            city = input('Ted: input the city name\n')
                            print(name +  " : "  + city)

                            print('Ted: Displaying Weather report for: ' + city)

                            # fetch the weather details
                            url = 'https://wttr.in/{}'.format(city)
                            res = requests.get(url)

                            # display the result!
                            print(res.text)
                        else:
                            if (user_response == 'news'):
                                print("Ted: Hold on ! I shall get you some latest news\n")

                                print("1.top news\n2.sports\n3.business\n4.technology\n5.entertainment\n6.health\nWhat would you like to see?\n")
                                newstype = input('Ted: input the news type you want to see\n')
                                print(name +  " : "  + newstype)
                                print('Ted: Displaying News for: ' + newstype)

                                if(newstype == 'top news' or newstype == '1'):
                                    from news import *
                                    news()
                                else:
                                    if(newstype == 'sports' or newstype == '2'):
                                        from news import *
                                        sport()
                                    else:
                                        if(newstype == 'business' or newstype == '3'):
                                            from news import *
                                            business()
                                        else:
                                            if(newstype == 'technology' or newstype == '4'):
                                                from news1 import *
                                                tech()
                                            else:
                                                if (newstype == 'entertainment' or newstype == '5'):
                                                    from newstest import *
                                                    ent()
                                                else:
                                                    from newstest import *
                                                    health()

                            else:
                                if (user_response == 'stock'):
                                    print("Ted: Hmmm, Looks like someone wants to look at the equity stock!\n")
                                    print("Ted: Please wait while I get you more details\n")

                                    print("1.Fundamental Analysis\n2.Quarterly Performance\n3.Stock Recommendation\nWhat would you like to see?\n")
                                    data = input('Ted: input the type you want to see\n')
                                    print('Ted: Displaying data for: ' + data)

                                    if(data == '2' or data == 'Quarterly Performance' or data == 'quarterly performance'):
                                        from stock import *
                                        quarterly()

                                    else:
                                        if(data == '3' or data == 'Stock Recommendation' or data == 'stock recommendation'):
                                            stock= input('Ted: input the stock name: ')
                                            from stockrec import *
                                            get_price_data_NSE(stock)
                                        else:
                                            from fundamental import *
                                            fundamental()

                                else:
                                    print("Ted: ",end="")
                                    print(response(user_response))
                                    sent_tokens.remove(user_response)
    else:
        flag = False
        print("Ted: Bye! take care. Have a wonderful day,"  + name)
        
        

