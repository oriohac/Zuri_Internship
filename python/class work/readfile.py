def read_f(filename):
    open_f = open("./story.txt","r")
    read_f = open_f.read()
    #print(read_file)
    new = read_f.split()
    count ={}
    for i in new:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count      
print(read_f("./story.txt"))