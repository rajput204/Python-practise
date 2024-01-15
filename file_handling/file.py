#file handling ,only for changing the name of the file we have to import foem os i.e import os
import os
def writing(filename,text):
    f=open(filename,"w") #filename with mode of writing
    f.write(text)
    f.close()
def append(filename,text):#append with filename with mode of writing the file
    f=open(filename,"a")
    f.write(text)
    f.close()
def reading(filename):#reading the file 
    try:
      f=open(filename,"r")
      text=f.read() #preserved in text for printing text
      print(text)
      f.close()
    except FileNotFoundError:
        print("file not found error")
def search(filename,word): #searching the function of the required element of the data.
    try:
        f=open(filename,"r")
        line_count=0
        for line in f.readlines():#read lines is a function to read the lines in the file.
            line_count+=1
            strlist=line.split(' ')
            word_count=0
            for w in strlist:
                word_count+=1
                if word==w:
                    return (line_count,word_count)
        else:
            return None
        f.close()
    except FileNotFoundError:
        print("file not found error")
def modify(filename,oldword,newword): #modiying the oldname with the new name
    t=search(filename,oldword)
    if t!=None:
        mylist=[]
        try:
            f=open(filename,"r")
            for line in f.readlines():
                line=line.replace(oldword,newword)#replace old from new
                mylist.append(line)#it will append the changed to the list
            f.close()
            f=open(filename,"w")#for writing the newword from the oldword
            f.write(''.join(mylist))#it will give the string from the list
            f.close()
        except FileNotFoundError:
            print("file not found")
    else:
        print("search failed")
def delete(filename,oldword,newword=' '): #delete function in a file
    t=search(filename,oldword)
    if t!=None:
        mylist=[]
        try:
            f=open(filename,"r")
            for line in f.readlines():#for reading lines of the file
                line=line.replace(oldword,newword)#for replacing the new word with the old word
                mylist.append(line)#adding in the file line
            f.close()
            f=open(filename,"w")
            f.write(''.join(mylist))
            f.close()
        except FileNotFoundError:
            print("file not found")
    else:
        print("search failed")

os.rename("coderblood.txt","coderfile.txt")#for changing the name of the file from oldname to the new name.
# os.remove("coderfile.text")


# writing("coderblood.txt","hello\n")
# append("coderblood.txt","aditya is noob coder\n and he want to be the pro coder in python \n and he loves to lear new thing in the python language")
# reading("coderblood.txt")
modify("coderblood.txt","aditya","ADITYA")
delete("coderblood.txt","lear")
# print(search("coderblood.txt","aditya")) #(2,1) secondline ka first

print( )


