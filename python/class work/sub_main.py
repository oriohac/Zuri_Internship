#openfile = open("./story.txt","r")
#with open("./story.txt","r") as openfile:

#print(openfile)
def read_file(filename):
    with open('./story.txt','r') as openfile:
        read_file = openfile.read()
        #print(read_file)
       # print("this file is true")
read_file('./story.txt')
def countwords():
    text  = readfile("./story.txt")
    split_text = text.split()
    #print(split_text)
    count = {}
    for i in split_text:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
