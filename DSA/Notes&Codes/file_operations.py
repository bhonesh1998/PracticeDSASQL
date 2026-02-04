name = input("tell me your name for appending into file")
file = open("/Users/bhoneshchawla/PycharmProjects/PracticeDSA/DSA/resources/testing_file.txt","w")
file.write(name)
file.close()


# mode - w for write / overwrite
# mode - a for append

