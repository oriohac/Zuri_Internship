#Accept inputs and assign the inputs to variable enter_words.
enter_words = input("Type a thing or two : ")

#this line gets the length of each splitted alphabet, 
#which are the words and saves the length in variable count_words.
count_words = len(enter_words.split())

#this line outputs the words that were received on a new line, 
#with the format specifier \n responsible for that.
print("You Typed these :\n " + str(enter_words))

#This line outputs the number of words that were typed in.
print("Number of words you typed is : " + str(count_words))