import json

data=json.load(open("data.json"))
 
def translate(search_word):
    try:
        if (search_word in data or search_word.title() in data or search_word.upper() in data or search_word.lower() in data):
            i=1
            print(f"\nMeaning of {search_word}:")
            for line in data[search_word]:
                print('\n'+str(i)+". "+line)
                i+=1
        else:
            print("\nSorry we do not have this word in our dictionary")
    except:
        print("\nSorry we do not have this word in our dictionary")

        

flag='Y'
while(flag=='Y'):
    search_word=input("Enter the word to be searched: ")
    translate(search_word)
    opt=input("\nDo you want to continue to search:  Enter Y/N :").upper()
    if (opt=='Y'):
        flag=opt
    elif (opt=='N'):
        break
    else:
        print("Invalid Input !!!")
        break

    