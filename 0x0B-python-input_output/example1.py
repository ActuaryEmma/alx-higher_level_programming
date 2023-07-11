import os

with open("mydata.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Some random text\nMore random text\nAnd some more")
with open("mydata.txt", encoding="utf-8") as myFile:
    """This read size number of bytes from the file. If size is not passed, the entire file is read."""
    print(myFile.read())
    print("----------------------------------")
    """reads size number of bytes from the line. if no argument is passed it reads the entire line """
    print(myFile.readline())
    print("------------------------------------")
    """ read all the lines from a file and returns a list of the lines separating them from one another with commas"""
    print(myFile.readlines())

"""check if file is closed"""
print(myFile.closed)

"""check the file name you are reading, opening and closing"""
print(myFile.name)

"""check mode of the file"""
print(myFile.mode)

"""rename the file"""
os.rename("mydata.txt", "mydata2.txt")

"""remove the file"""
os.remove("mydata2.txt")

"""create dir"""
"""os.mkdir("mydir")"""

"""change the dir"""
os.chdir("mydir")

print("Current directory :", os.getcwd())

"""move to dir before"""
os.chdir("..")

print("Current directory :", os.getcwd())

"""remove dir"""
os.rmdir("mydir")
