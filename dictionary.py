import json
from difflib import get_close_matches

data=json.load(open("data.json"))
 
def translate(search_word):
    if (search_word in data):
        i=1
        print(f"\nMeaning of {search_word}:")
        for line in data[search_word]:
            print('\n'+str(i)+". "+line)
            i+=1
    elif (len(get_close_matches(search_word,data.keys()))>0):
        print('\nDid you mean "%s" instead'%get_close_matches(search_word,data.keys())[0])
        decide=input('Press y for YES and n for NO: ').lower()
        if (decide=='y'):
            k=1
            print(f"\nMeaning of {get_close_matches(search_word,data.keys())[0]}:")
            for line in data[get_close_matches(search_word,data.keys())[0]]:
                print('\n'+str(k)+". "+line)
                k+=1
        elif (decide=='n'):
            print("\nSorry we do not have this word in our dictionary")
    else:
        print("\nSorry we do not have this word in our dictionary")


        

flag='Y'
while(flag=='Y'):
    search_word=input("Enter the word to be searched: ").lower()
    translate(search_word)
    opt=input("\nDo you want to continue to search:  Enter Y/N :").upper()
    if (opt=='Y'):
        flag=opt
    elif (opt=='N'):
        break
    else:
        print("Invalid Input !!!")
        break

    