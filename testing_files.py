import os
import random
import time
from termcolor import colored, cprint

twenty = "~~~~~~~~~~~~~~~~~~~~~"


# FUNCTIONS
def create_random_files(filedirectory, filenum, file_type):
    count = 1
    double_check = []
    while count <= filenum:
        value = random.randint(1, 100)
        if value not in double_check:
            double_check.append(value)
            print(value)
            count += 1
        elif value in double_check:
            pass
        else:
            return colored("\nTHERE'S A PROBLEM CAPTAIN!", "green")

        open(filedirectory + str(value) + file_type, "w")
        count += 1


def cleanup_directory(file_directory, file_name_input):
    count2 = 0
    renamed = []
    old_rename = []
    old_files = (os.listdir(file_directory))
    old_files = tuple(old_files)
    num_of_old_files = len(os.listdir(file_directory))
    timecount = 0
    while True:
        for file in os.listdir(file_directory):
            #cleaned_file = open(cleaned_file)
            src = file_directory + file
            dst = file_directory + file_name_input + "_" + str(count2) + file
            #split_file_name = os.listdir(file_directory)
            #split_file_name = str(split_file_name)
            #split_file_name = split_file_name.split(".")
            #print(type(split_file_name))
            count2 += 1
            print(num_of_old_files)
            if num_of_old_files >= count2:

                print("passed first if statement")
                os.rename(src, dst)
                if file in old_rename:
                    print("passed second if statement")
                    pass
                elif file not in old_files:
                    os.rename(src, dst)
            else:
                timecount += 1
                if timecount >= 3:
                    time.sleep(5)
                    print("sleeping")
               #cleaned_file.write(str(count2**count2)*count2)
                #cleaned_file.close()
        # return endswith
        # file = open(str(value) + ".txt","w")
        # print(cl)


create_random_files("me\\", 35, ".txt")

print(twenty)
for i in range(5):
    print(colored("Cleaning Files...", "red"))
    print(twenty)
    time.sleep(.1)

time.sleep(.5)
cleanup_directory("me\\","text_document")
print(colored("\nCHECK YOU DIRECTORY! IT SHOULD BE CLEANED NOW!", "blue"))

"""
##RUNNING
print("THIS PROGRAM WILL HELP YOU SORT FILES. IT CAN EITHER CHANGE ALL FILES IN A GIVEN FOLDER BY LABELING THEM NUMBERS, OR, YOU CAN GIVE YOUR OWN UNIQUE IDENIFIER.")
print(twenty)
print(input("WOULD YOU RATHER USE YOUR OWN UNIQUE IDENTIFIER OR ITERATE THROUGH THE DIRECTORY?"))


# GARBAGE
# this means that you can just put the path of the file that you want. wow i already established this....well
# u can just put the path that is already being made from where the python project is if that makes sense
# os.rename("testingrename\\adddddddd.txt","testingrename\\1.txt")
#PAST CODE AND GARBAGGEEEEE YAYHAYAY

print("above is the listdir as a list")
split_file_name = str(os.listdir(file_directory))
print(split_file_name)
print("above is the listdir as a string")
split_file_name = split_file_name.split(".")
print(split_file_name)
print("above is the split string")
print(list(split_file_name))
print("above is splitfiledir as a list that has been converted to str backt into a laiset")
raise


# this just showed me that I don't need to enumerate the directory and that it will detect the files itselcd.
"""
"""
print(str(os.listdir("testingrename")))

for file in os.listdir("testingrename"):
    print(count)
    count += 1



def delete(saidfile):
    saidfile = open(saidfile, "w")
    saidfile.write("")
    saidfile.close


def converttolist(string):
    list = list(string.split(" "))
    return list
"""
