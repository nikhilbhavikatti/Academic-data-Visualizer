import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#function to compare subject scores
def subject_compare(division,subject1,subject2):
    while(division == 1 or division == 2 or division == 3 or division == 4 or division == 0):
        print("Enter the Division :")
        print("1 -> A   2 -> B   3 -> C   4 -> D")
        print("Press 0 to go back ")
        division = input()
        division = int(division)
        if(division == 0):
            break
        if(division > 4 or division < 0):
            print("Invalid Option!")
            division = 0
            continue
        while(subject1 <= 9 and subject2 <= 9 and subject1 >= 0 and subject2 >= 0):
            print("Enter the 2 subjects which you want to compare in "
                  + divisions[division] + " division :")
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
            if(subject1 > 9 or subject2 > 9 or subject1 <= 0 or subject2 <= 0):
                print("Invalid Option!")
                subject1 = 0
                subject2 = 0
                continue
            if(division == 1):
                plt.hist([subject_scores_A[subject1],subject_scores_A[subject2]],
                        bins=[0,1,2,3,4,5,6,7,8,9,10,11],rwidth=0.85)
                plt.title('6th Semester A Division Subject wise performance')
            elif(division == 2):
                plt.hist([subject_scores_B[subject1],subject_scores_B[subject2]],
                        bins=[0,1,2,3,4,5,6,7,8,9,10,11],rwidth=0.85)
                plt.title('6th Semester B Division Subject wise performance')
            elif(division == 3):
                plt.hist([subject_scores_C[subject1],subject_scores_C[subject2]],
                        bins=[0,1,2,3,4,5,6,7,8,9,10,11],rwidth=0.85)
                plt.title('6th Semester C Division Subject wise performance')
            elif(division == 4):
                plt.hist([subject_scores_D[subject1],subject_scores_D[subject2]],
                        bins=[0,1,2,3,4,5,6,7,8,9,10,11],rwidth=0.85)
                plt.title('6th Semester D Division Subject wise performance')
            #end of if-else
            plt.grid(axis='y', alpha=0.5)
            plt.xlabel("GPA")
            plt.ylabel("Number of Students")
            plt.xticks(range(0, 11))
            plt.yticks(range(1, 30))
            plt.legend([subject_names[subject1],subject_names[subject2]])
            plt.show()

#function to provide Overall Summary Subject wise
def subject_summary(subject):
    while(subject >= 0 and subject <= 9):
        print("Enter the subject  :")
        print("1 -> ME      2 -> DC       3 -> CD")
        print("4 -> CG      5 -> OOMD     6 -> OE")
        print("7 -> SD Lab  8 -> CG Lab   9 -> CIP")
        print("Press 0 to go back ")
        subject = input()
        subject = int(subject)
        if(subject == 0):
            break
        if(subject > 9 or subject < 0):
            print("Invalid Option!")
            subject = 0
            continue
        #Plot a histogram comparing scores of selected subject division wise
        plt.hist([subject_scores_A[subject],subject_scores_B[subject],subject_scores_C[subject],
                subject_scores_D[subject]],bins=[0,1,2,3,4,5,6,7,8,9,10,11],rwidth=0.85)
        plt.grid(axis='y', alpha=0.5)
        plt.xlabel("GPA")
        plt.ylabel("Number of Students")
        plt.xticks(range(0, 11))
        plt.yticks(range(1, 30))
        plt.title('6th Semester ' + subject_names[subject] + ' Subject Overall Performance')
        plt.legend(['A Division','B Division','C Division','D Division'])
        plt.show()

#function to provide Overall summary Division wise
def division_summary(division):
    while(division == 1 or division == 2 or division == 3 or division == 4 or division == 0):
        print("Enter the Division :")
        print("1 -> A   2 -> B   3 -> C   4 -> D")
        print("Press 0 to go back ")
        division = input()
        division = int(division)
        if(division == 0):
            break
        if(division > 4 or division < 0):
            print("Invalid Option!")
            division = 0
            continue
        if(division == 1):
            #Plot a histogram comparing all the subject scores for A division
            plt.hist([Sort_ME_A,Sort_DC_A,Sort_CD_A,Sort_CG_A,Sort_OOMD_A,Sort_OE_A,Sort_SD_A_Lab,
            Sort_CG_A_Lab,Sort_CIP_A,Sort_SGPA_A], bins=[0,1,2,3,4,5,6,7,8,9,10,11],rwidth=0.85)
            plt.title('6th Semester A Division Overall Performance')
        elif(division == 2):
            #Plot a histogram comparing all the subject scores for B division
            plt.hist([Sort_ME_B,Sort_DC_B,Sort_CD_B,Sort_CG_B,Sort_OOMD_B,Sort_OE_B,Sort_SD_B_Lab,
            Sort_CG_B_Lab,Sort_CIP_B,Sort_SGPA_B], bins=[0,1,2,3,4,5,6,7,8,9,10,11],rwidth=0.85)
            plt.title('6th Semester B Division Overall Performance')
        elif(division == 3):
            #Plot a histogram comparing all the subject scores for C division
            plt.hist([Sort_ME_C,Sort_DC_C,Sort_CD_C,Sort_CG_C,Sort_OOMD_C,Sort_OE_C,Sort_SD_C_Lab,
            Sort_CG_C_Lab,Sort_CIP_C,Sort_SGPA_C], bins=[0,1,2,3,4,5,6,7,8,9,10,11],rwidth=0.85)
            plt.title('6th Semester C Division Overall Performance')
        elif(division == 4):
            #Plot a histogram comparing all the subject scores for C division
            plt.hist([Sort_ME_D,Sort_DC_D,Sort_CD_D,Sort_CG_D,Sort_OOMD_D,Sort_OE_D,Sort_SD_D_Lab,
            Sort_CG_D_Lab,Sort_CIP_D,Sort_SGPA_D], bins=[0,1,2,3,4,5,6,7,8,9,10,11],rwidth=0.85)
            plt.title('6th Semester D Division Overall Performance')
        #end of if-else
        plt.grid(axis='y', alpha=0.5)
        plt.xlabel("GPA")
        plt.ylabel("Number of Students")
        plt.xticks(range(0, 11))
        plt.yticks(range(1, 30))
        plt.legend(['ME Score','DC Score','CD Score','CG Score','OOMD Score',
                    'OE Score','SD Lab Score','CG Lab Score','CIP Score','SGPA'])
        plt.show()



#read excel file data of all 4 divisions
df1 = pd.read_excel("Result_6.xlsx","Sheet1")
df2 = pd.read_excel("Result_6.xlsx","Sheet2")
df3 = pd.read_excel("Result_6.xlsx","Sheet3")
df4 = pd.read_excel("Result_6.xlsx","Sheet4")

#read data from the excel sheet column wise and convert the columnar data into list for A division
SGPA_A = df1['SGPA'].values.tolist()
ME_A = df1['ME'].values.tolist()
DC_A = df1['DC'].values.tolist()
CD_A = df1['CD'].values.tolist()
CG_A = df1['CG'].values.tolist()
OOMD_A = df1['OOMD'].values.tolist()
OE_A = df1['OE'].values.tolist()
SD_A_Lab = df1['SD_Lab'].values.tolist()
CG_A_Lab = df1['CG_Lab'].values.tolist()
CIP_A = df1['CIP'].values.tolist()
USN_A = df1['USN'].values.tolist()

#sort the list and create a sorted list for A division
Sort_ME_A = sorted(ME_A)
Sort_DC_A = sorted(DC_A)
Sort_CD_A = sorted(CD_A)
Sort_CG_A = sorted(CG_A)
Sort_OOMD_A = sorted(OOMD_A)
Sort_OE_A = sorted(OE_A)
Sort_SD_A_Lab = sorted(SD_A_Lab)
Sort_CG_A_Lab = sorted(CG_A_Lab)
Sort_CIP_A = sorted(CIP_A)
Sort_SGPA_A = sorted(SGPA_A)

#read data from the excel sheet column wise and convert the columnar data into list for B division
SGPA_B = df2['SGPA'].values.tolist()
ME_B = df2['ME'].values.tolist()
DC_B = df2['DC'].values.tolist()
CD_B = df2['CD'].values.tolist()
CG_B = df2['CG'].values.tolist()
OOMD_B = df2['OOMD'].values.tolist()
OE_B = df2['OE'].values.tolist()
SD_B_Lab = df2['SD_Lab'].values.tolist()
CG_B_Lab = df2['CG_Lab'].values.tolist()
CIP_B = df2['CIP'].values.tolist()
USN_B = df2['USN'].values.tolist()

#sort the list and create a sorted list for B division
Sort_ME_B = sorted(ME_B)
Sort_DC_B = sorted(DC_B)
Sort_CD_B = sorted(CD_B)
Sort_CG_B = sorted(CG_B)
Sort_OOMD_B = sorted(OOMD_B)
Sort_OE_B = sorted(OE_B)
Sort_SD_B_Lab = sorted(SD_B_Lab)
Sort_CG_B_Lab = sorted(CG_B_Lab)
Sort_CIP_B = sorted(CIP_B)
Sort_SGPA_B = sorted(SGPA_B)

#read data from the excel sheet column wise and convert the columnar data into list for C division
SGPA_C = df3['SGPA'].values.tolist()
ME_C = df3['ME'].values.tolist()
DC_C = df3['DC'].values.tolist()
CD_C = df3['CD'].values.tolist()
CG_C = df3['CG'].values.tolist()
OOMD_C = df3['OOMD'].values.tolist()
OE_C = df3['OE'].values.tolist()
SD_C_Lab = df3['SD_Lab'].values.tolist()
CG_C_Lab = df3['CG_Lab'].values.tolist()
CIP_C = df3['CIP'].values.tolist()
USN_C = df3['USN'].values.tolist()

#sort the list and create a sorted list for C division
Sort_ME_C = sorted(ME_C)
Sort_DC_C = sorted(DC_C)
Sort_CD_C = sorted(CD_C)
Sort_CG_C = sorted(CG_C)
Sort_OOMD_C = sorted(OOMD_C)
Sort_OE_C = sorted(OE_C)
Sort_SD_C_Lab = sorted(SD_C_Lab)
Sort_CG_C_Lab = sorted(CG_C_Lab)
Sort_CIP_C = sorted(CIP_C)
Sort_SGPA_C = sorted(SGPA_C)

#read data from the excel sheet column wise and convert the columnar data into list for D division
SGPA_D = df4['SGPA'].values.tolist()
ME_D = df4['ME'].values.tolist()
DC_D = df4['DC'].values.tolist()
CD_D = df4['CD'].values.tolist()
CG_D = df4['CG'].values.tolist()
OOMD_D = df4['OOMD'].values.tolist()
OE_D = df4['OE'].values.tolist()
SD_D_Lab = df4['SD_Lab'].values.tolist()
CG_D_Lab = df4['CG_Lab'].values.tolist()
CIP_D = df4['CIP'].values.tolist()
USN_D = df4['USN'].values.tolist()

#sort the list and create a sorted list for D division
Sort_ME_D = sorted(ME_D)
Sort_DC_D = sorted(DC_D)
Sort_CD_D = sorted(CD_D)
Sort_CG_D = sorted(CG_D)
Sort_OOMD_D = sorted(OOMD_D)
Sort_OE_D = sorted(OE_D)
Sort_SD_D_Lab = sorted(SD_D_Lab)
Sort_CG_D_Lab = sorted(CG_D_Lab)
Sort_CIP_D = sorted(CIP_D)
Sort_SGPA_D = sorted(SGPA_D)

subject_scores_A = {1 : Sort_ME_A, 2 : Sort_DC_A, 3 : Sort_CD_A, 4 : Sort_CG_A, 5 : Sort_OOMD_A,
            6 : Sort_OE_A, 7 : Sort_SD_A_Lab, 8 : Sort_CG_A_Lab, 9 : Sort_CIP_A }
subject_scores_B = {1 : Sort_ME_B, 2 : Sort_DC_B, 3 : Sort_CD_B, 4 : Sort_CG_B, 5 : Sort_OOMD_B,
            6 : Sort_OE_B, 7 : Sort_SD_B_Lab, 8 : Sort_CG_B_Lab, 9 : Sort_CIP_B }
subject_scores_C = {1 : Sort_ME_C, 2 : Sort_DC_C, 3 : Sort_CD_C, 4 : Sort_CG_C, 5 : Sort_OOMD_C,
            6 : Sort_OE_C, 7 : Sort_SD_C_Lab, 8 : Sort_CG_C_Lab, 9 : Sort_CIP_C }
subject_scores_D = {1 : Sort_ME_D, 2 : Sort_DC_D, 3 : Sort_CD_D, 4 : Sort_CG_D, 5 : Sort_OOMD_D,
            6 : Sort_OE_D, 7 : Sort_SD_D_Lab, 8 : Sort_CG_D_Lab, 9 : Sort_CIP_D }
subject_names = {1 : 'ME', 2 : 'DC', 3 : 'CD', 4 : 'CG', 5 : 'OOMD',
            6 : 'OE', 7 : 'SD Lab', 8 : 'CG Lab', 9 : 'CIP' }
divisions = {1 : 'A' , 2 : 'B' , 3 : 'C' , 4 : 'D'}
number = 0
subject = 0
subject1 = 0
subject2 = 0
division = 0

while(number == 1 or number == 2 or number == 0 or number == 3 or number == 4):
    #Display the Menu and accept the user input
    print("--------------------WELCOME TO ACADEMIC INFORMATION VISUALIZER---------------------")
    print("MENU")
    print("1 --> Get Summary of 6th semester CSE")
    print("2 --> Get Summary Division wise")
    print("3 --> Get Summary Subject wise")
    print("4 --> Compare by subject scores")
    print("0 --> Exit")
    number = input()
    number = int(number)

    #Get Overall Summary of 6th semester CSE
    if(number == 1):
        '''plt.plot(Sort_SGPA_A)
        plt.plot(Sort_SGPA_B)
        plt.plot(Sort_SGPA_C)
        plt.plot(Sort_SGPA_D)
        plt.ylabel('SGPA')
        plt.title('6th sem CSE Overall Summary')
        plt.legend(['A Division','B Division','C Division','D Division'])
        plt.show()'''

        plt.hist([Sort_SGPA_A,Sort_SGPA_B,Sort_SGPA_C,Sort_SGPA_D],
                bins=[0,1,2,3,4,5,6,7,8,9,10,11],rwidth=0.85)
        plt.grid(axis='y', alpha=0.5)
        plt.xlabel("SGPA")
        plt.ylabel('Number of Students')
        plt.xticks(range(0, 11))
        plt.yticks(range(1, 30))
        plt.title('6th sem CSE Overall Summary')
        plt.legend(['A Division','B Division','C Division','D Division'])
        plt.show()
    #Get Overall Summary division wise
    elif(number == 2):
        division_summary(division)
    #Get Overall Summary Subject wise
    elif(number == 3):
        subject_summary(subject)
    #To compare by subject scores call to function subject_compare()
    elif(number == 4) :
        subject_compare(division,subject1,subject2)
    #Exit from the Program
    elif(number == 0) :
        print("Thank You")
        exit()
    else :
        print("Invalid Option!")
