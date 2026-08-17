#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
with open("./Input/Names/invited_names.txt") as names:
    name_list=names.read().split("\n")
    print(name_list)
    
    with open("./Input/Letters/starting_letter.txt") as starting:
        text=starting.read()
        for name in name_list:
            named_text=text.replace("[name]",name)
            with open(f"./Output\ReadyToSend/{name}_letter.txt",mode="w") as letter:
                letter.write(named_text)
    
    
    
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp