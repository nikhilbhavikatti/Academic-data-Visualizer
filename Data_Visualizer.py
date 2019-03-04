import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

while(True):
    #Display the Menu and accept the user input
    print("--------------------WELCOME TO ACADEMIC INFORMATION VISUALIZER---------------------")
    print("MENU")
    print("1 --> Get Overall Summary")
    print("0 --> Exit")
    number = input()
    number = int(number)

    #Get Overall Summary
    if(number == 1):
        #Plot a histogram comparing all the subjects
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
    #Exit from the Program
    elif(number == 0) :
        print("Thank You")
        exit()
