import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#function to compare subject_scores
def subject_compare(subject1,subject2):
    while(subject1 < 9 and subject2 < 9 and subject1 >= 0 and subject2 >= 0):
        print("Enter the 2 subjects which you want to compare :")
        print("1 -> ME      2 -> DC       3 -> CD")
        print("4 -> CG      5 -> OOMD     6 -> OE")
        print("7 -> SD Lab  8 -> CG Lab   9 -> CIP")
        print("Press 0 to go back ")
        subject1 = input()
        subject1 = int(subject1)
        if(subject1 == 0):
            break
        subject2 = input()
        subject2 = int(subject2)
        if(subject1 > 9 or subject2 > 9 or subject1 < 0 or subject2 < 0):
            print("Invalid Option!")
            subject1 = 0
            subject2 = 0
            continue

        plt.hist([subject_scores[subject1],subject_scores[subject2]],
                bins=[0,1,2,3,4,5,6,7,8,9,10,11],rwidth=0.85)
        plt.grid(axis='y', alpha=0.5)
        plt.xlabel("GPA")
        plt.ylabel("Frequency")
        plt.xticks(range(0, 11))
        plt.yticks(range(1, 30))
        plt.title('6th Semester A Division Subject wise performance')
        plt.legend([subject_names[subject1],subject_names[subject2]])
        plt.show()

#read excel file data
df = pd.read_excel("Result_6.xlsx","Sheet1")

#read data from the excel sheet column wise and convert the columnar data into list
SGPA = df['SGPA'].values.tolist()
ME = df['ME'].values.tolist()
DC = df['DC'].values.tolist()
CD = df['CD'].values.tolist()
CG = df['CG'].values.tolist()
OOMD = df['OOMD'].values.tolist()
OE = df['OE'].values.tolist()
SD_Lab = df['SD_Lab'].values.tolist()
CG_Lab = df['CG_Lab'].values.tolist()
CIP = df['CIP'].values.tolist()
USN = df['USN'].values.tolist()

#sort the list and create a sorted list
Sort_ME = sorted(ME)
Sort_DC = sorted(DC)
Sort_CD = sorted(CD)
Sort_CG = sorted(CG)
Sort_OOMD = sorted(OOMD)
Sort_OE = sorted(OE)
Sort_SD_Lab = sorted(SD_Lab)
Sort_CG_Lab = sorted(CG_Lab)
Sort_CIP = sorted(CIP)
Sort_SGPA = sorted(SGPA)

subject_scores = {1 : Sort_ME, 2 : Sort_DC, 3 : Sort_CD, 4 : Sort_CG, 5 : Sort_OOMD,
            6 : Sort_OE, 7 : Sort_SD_Lab, 8 : Sort_CG_Lab, 9 : Sort_CIP }
subject_names = {1 : 'ME', 2 : 'DC', 3 : 'CD', 4 : 'CG', 5 : 'OOMD',
            6 : 'OE', 7 : 'SD Lab', 8 : 'CG Lab', 9 : 'CIP' }
number = 0
subject1 = 0
subject2 = 0
while(number == 1 or number == 2 or number == 0):
    #Display the Menu and accept the user input
    print("--------------------WELCOME TO ACADEMIC INFORMATION VISUALIZER---------------------")
    print("MENU")
    print("1 --> Get Overall Summary")
    print("2 --> Compare by subject_scores")
    print("0 --> Exit")
    number = input()
    number = int(number)

    #Get Overall Summary
    if(number == 1):
        #Plot a histogram comparing all the subject_scores
        plt.hist([Sort_ME,Sort_DC,Sort_CD,Sort_CG,Sort_OOMD,Sort_OE,Sort_SD_Lab,
        Sort_CG_Lab,Sort_CIP,Sort_SGPA], bins=[0,1,2,3,4,5,6,7,8,9,10,11],rwidth=0.85)
        plt.grid(axis='y', alpha=0.5)
        plt.xlabel("GPA")
        plt.ylabel("Frequency")
        plt.xticks(range(0, 11))
        plt.yticks(range(1, 30))
        plt.title('6th Semester A Division Overall Performance')
        plt.legend(['ME Score','DC Score','CD Score','CG Score','OOMD Score',
                    'OE Score','SD Lab Score','CG Lab Score','CIP Score','SGPA'])
        plt.show()
    #To compare by subject_scores call to function subject_compare()
    elif(number == 2) :
        subject_compare(subject1,subject2)
    #Exit from the Program
    elif(number == 0) :
        print("Thank You")
        exit()
    else :
        print("Invalid Option!")
