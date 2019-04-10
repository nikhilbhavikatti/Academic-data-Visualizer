import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np

#function to provide Overall summary Division wise
def division_summary(division):
    grades = 'S+','S','A','B','C','D','E','F'
    colors = ['gold','yellowgreen', 'lightskyblue', 'lightcoral', 'silver','orange','pink','red']
    countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0

    while(division == 1 or division == 2 or division == 3 or division == 4 or division == 0):
        ME = []
        DC = []
        CD = []
        CG = []
        OOMD = []
        OE = []
        SD_Lab = []
        CG_Lab = []
        CIP = []
        print("Enter the Division :")
        print("1 -> A   2 -> B   3 -> C   4 -> D")
        print("Press 0 to go back ")
        division = input("Division : ")
        try :
            division = int(division)
        except :
            print('Invalid option')
            division = 0
            continue

        if(division == 0):
            break
        if(division > 4 or division < 0):
            print("Invalid Option!")
            division = 0
            continue
        if(division == 1):
            for GPA in Sort_ME_A :
                if(GPA == 10 ):
                    countSS = countSS + 1
                if(GPA == 9 ):
                    countS = countS + 1
                if(GPA == 8 ):
                    countA = countA + 1
                if(GPA == 7 ):
                    countB = countB + 1
                if(GPA == 6 ):
                    countC = countC + 1
                if(GPA == 5 ):
                    countD = countD + 1
                if(GPA == 4 ):
                    countE = countE + 1
                if(GPA == 0 ):
                    countF = countF + 1
            ME.append(countSS)
            ME.append(countS)
            ME.append(countA)
            ME.append(countB)
            ME.append(countC)
            ME.append(countD)
            ME.append(countE)
            ME.append(countF)
            countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0

            for GPA in Sort_DC_A :
                if(GPA == 10 ):
                    countSS = countSS + 1
                if(GPA == 9 ):
                    countS = countS + 1
                if(GPA == 8 ):
                    countA = countA + 1
                if(GPA == 7 ):
                    countB = countB + 1
                if(GPA == 6 ):
                    countC = countC + 1
                if(GPA == 5 ):
                    countD = countD + 1
                if(GPA == 4 ):
                    countE = countE + 1
                if(GPA == 0 ):
                    countF = countF + 1
            DC.append(countSS)
            DC.append(countS)
            DC.append(countA)
            DC.append(countB)
            DC.append(countC)
            DC.append(countD)
            DC.append(countE)
            DC.append(countF)
            countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0

            for GPA in Sort_CD_A :
                if(GPA == 10 ):
                    countSS = countSS + 1
                if(GPA == 9 ):
                    countS = countS + 1
                if(GPA == 8 ):
                    countA = countA + 1
                if(GPA == 7 ):
                    countB = countB + 1
                if(GPA == 6 ):
                    countC = countC + 1
                if(GPA == 5 ):
                    countD = countD + 1
                if(GPA == 4 ):
                    countE = countE + 1
                if(GPA == 0 ):
                    countF = countF + 1
            CD.append(countSS)
            CD.append(countS)
            CD.append(countA)
            CD.append(countB)
            CD.append(countC)
            CD.append(countD)
            CD.append(countE)
            CD.append(countF)
            countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0

            for GPA in Sort_CG_A :
                if(GPA == 10 ):
                    countSS = countSS + 1
                if(GPA == 9 ):
                    countS = countS + 1
                if(GPA == 8 ):
                    countA = countA + 1
                if(GPA == 7 ):
                    countB = countB + 1
                if(GPA == 6 ):
                    countC = countC + 1
                if(GPA == 5 ):
                    countD = countD + 1
                if(GPA == 4 ):
                    countE = countE + 1
                if(GPA == 0 ):
                    countF = countF + 1
            CG.append(countSS)
            CG.append(countS)
            CG.append(countA)
            CG.append(countB)
            CG.append(countC)
            CG.append(countD)
            CG.append(countE)
            CG.append(countF)
            countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0

            for GPA in Sort_OOMD_A :
                if(GPA == 10 ):
                    countSS = countSS + 1
                if(GPA == 9 ):
                    countS = countS + 1
                if(GPA == 8 ):
                    countA = countA + 1
                if(GPA == 7 ):
                    countB = countB + 1
                if(GPA == 6 ):
                    countC = countC + 1
                if(GPA == 5 ):
                    countD = countD + 1
                if(GPA == 4 ):
                    countE = countE + 1
                if(GPA == 0 ):
                    countF = countF + 1
            OOMD.append(countSS)
            OOMD.append(countS)
            OOMD.append(countA)
            OOMD.append(countB)
            OOMD.append(countC)
            OOMD.append(countD)
            OOMD.append(countE)
            OOMD.append(countF)
            countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0

            for GPA in Sort_OE_A :
                if(GPA == 10 ):
                    countSS = countSS + 1
                if(GPA == 9 ):
                    countS = countS + 1
                if(GPA == 8 ):
                    countA = countA + 1
                if(GPA == 7 ):
                    countB = countB + 1
                if(GPA == 6 ):
                    countC = countC + 1
                if(GPA == 5 ):
                    countD = countD + 1
                if(GPA == 4 ):
                    countE = countE + 1
                if(GPA == 0 ):
                    countF = countF + 1
            OE.append(countSS)
            OE.append(countS)
            OE.append(countA)
            OE.append(countB)
            OE.append(countC)
            OE.append(countD)
            OE.append(countE)
            OE.append(countF)
            countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0

            for GPA in Sort_SD_A_Lab :
                if(GPA == 10 ):
                    countSS = countSS + 1
                if(GPA == 9 ):
                    countS = countS + 1
                if(GPA == 8 ):
                    countA = countA + 1
                if(GPA == 7 ):
                    countB = countB + 1
                if(GPA == 6 ):
                    countC = countC + 1
                if(GPA == 5 ):
                    countD = countD + 1
                if(GPA == 4 ):
                    countE = countE + 1
                if(GPA == 0 ):
                    countF = countF + 1
            SD_Lab.append(countSS)
            SD_Lab.append(countS)
            SD_Lab.append(countA)
            SD_Lab.append(countB)
            SD_Lab.append(countC)
            SD_Lab.append(countD)
            SD_Lab.append(countE)
            SD_Lab.append(countF)
            countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0

            for GPA in Sort_CG_A_Lab :
                if(GPA == 10 ):
                    countSS = countSS + 1
                if(GPA == 9 ):
                    countS = countS + 1
                if(GPA == 8 ):
                    countA = countA + 1
                if(GPA == 7 ):
                    countB = countB + 1
                if(GPA == 6 ):
                    countC = countC + 1
                if(GPA == 5 ):
                    countD = countD + 1
                if(GPA == 4 ):
                    countE = countE + 1
                if(GPA == 0 ):
                    countF = countF + 1
            CG_Lab.append(countSS)
            CG_Lab.append(countS)
            CG_Lab.append(countA)
            CG_Lab.append(countB)
            CG_Lab.append(countC)
            CG_Lab.append(countD)
            CG_Lab.append(countE)
            CG_Lab.append(countF)
            countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0

            for GPA in Sort_CIP_A :
                if(GPA == 10 ):
                    countSS = countSS + 1
                if(GPA == 9 ):
                    countS = countS + 1
                if(GPA == 8 ):
                    countA = countA + 1
                if(GPA == 7 ):
                    countB = countB + 1
                if(GPA == 6 ):
                    countC = countC + 1
                if(GPA == 5 ):
                    countD = countD + 1
                if(GPA == 4 ):
                    countE = countE + 1
                if(GPA == 0 ):
                    countF = countF + 1
            CIP.append(countSS)
            CIP.append(countS)
            CIP.append(countA)
            CIP.append(countB)
            CIP.append(countC)
            CIP.append(countD)
            CIP.append(countE)
            CIP.append(countF)
            countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0

        elif(division == 2):
            for GPA in Sort_ME_B :
                if(GPA == 10 ):
                    countSS = countSS + 1
                if(GPA == 9 ):
                    countS = countS + 1
                if(GPA == 8 ):
                    countA = countA + 1
                if(GPA == 7 ):
                    countB = countB + 1
                if(GPA == 6 ):
                    countC = countC + 1
                if(GPA == 5 ):
                    countD = countD + 1
                if(GPA == 4 ):
                    countE = countE + 1
                if(GPA == 0 ):
                    countF = countF + 1
            ME.append(countSS)
            ME.append(countS)
            ME.append(countA)
            ME.append(countB)
            ME.append(countC)
            ME.append(countD)
            ME.append(countE)
            ME.append(countF)
            countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0

            for GPA in Sort_DC_B :
                if(GPA == 10 ):
                    countSS = countSS + 1
                if(GPA == 9 ):
                    countS = countS + 1
                if(GPA == 8 ):
                    countA = countA + 1
                if(GPA == 7 ):
                    countB = countB + 1
                if(GPA == 6 ):
                    countC = countC + 1
                if(GPA == 5 ):
                    countD = countD + 1
                if(GPA == 4 ):
                    countE = countE + 1
                if(GPA == 0 ):
                    countF = countF + 1
            DC.append(countSS)
            DC.append(countS)
            DC.append(countA)
            DC.append(countB)
            DC.append(countC)
            DC.append(countD)
            DC.append(countE)
            DC.append(countF)
            countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0

            for GPA in Sort_CD_B :
                if(GPA == 10 ):
                    countSS = countSS + 1
                if(GPA == 9 ):
                    countS = countS + 1
                if(GPA == 8 ):
                    countA = countA + 1
                if(GPA == 7 ):
                    countB = countB + 1
                if(GPA == 6 ):
                    countC = countC + 1
                if(GPA == 5 ):
                    countD = countD + 1
                if(GPA == 4 ):
                    countE = countE + 1
                if(GPA == 0 ):
                    countF = countF + 1
            CD.append(countSS)
            CD.append(countS)
            CD.append(countA)
            CD.append(countB)
            CD.append(countC)
            CD.append(countD)
            CD.append(countE)
            CD.append(countF)
            countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0

            for GPA in Sort_CG_B :
                if(GPA == 10 ):
                    countSS = countSS + 1
                if(GPA == 9 ):
                    countS = countS + 1
                if(GPA == 8 ):
                    countA = countA + 1
                if(GPA == 7 ):
                    countB = countB + 1
                if(GPA == 6 ):
                    countC = countC + 1
                if(GPA == 5 ):
                    countD = countD + 1
                if(GPA == 4 ):
                    countE = countE + 1
                if(GPA == 0 ):
                    countF = countF + 1
            CG.append(countSS)
            CG.append(countS)
            CG.append(countA)
            CG.append(countB)
            CG.append(countC)
            CG.append(countD)
            CG.append(countE)
            CG.append(countF)
            countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0

            for GPA in Sort_OOMD_B :
                if(GPA == 10 ):
                    countSS = countSS + 1
                if(GPA == 9 ):
                    countS = countS + 1
                if(GPA == 8 ):
                    countA = countA + 1
                if(GPA == 7 ):
                    countB = countB + 1
                if(GPA == 6 ):
                    countC = countC + 1
                if(GPA == 5 ):
                    countD = countD + 1
                if(GPA == 4 ):
                    countE = countE + 1
                if(GPA == 0 ):
                    countF = countF + 1
            OOMD.append(countSS)
            OOMD.append(countS)
            OOMD.append(countA)
            OOMD.append(countB)
            OOMD.append(countC)
            OOMD.append(countD)
            OOMD.append(countE)
            OOMD.append(countF)
            countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0

            for GPA in Sort_OE_B :
                if(GPA == 10 ):
                    countSS = countSS + 1
                if(GPA == 9 ):
                    countS = countS + 1
                if(GPA == 8 ):
                    countA = countA + 1
                if(GPA == 7 ):
                    countB = countB + 1
                if(GPA == 6 ):
                    countC = countC + 1
                if(GPA == 5 ):
                    countD = countD + 1
                if(GPA == 4 ):
                    countE = countE + 1
                if(GPA == 0 ):
                    countF = countF + 1
            OE.append(countSS)
            OE.append(countS)
            OE.append(countA)
            OE.append(countB)
            OE.append(countC)
            OE.append(countD)
            OE.append(countE)
            OE.append(countF)
            countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0

            for GPA in Sort_SD_B_Lab :
                if(GPA == 10 ):
                    countSS = countSS + 1
                if(GPA == 9 ):
                    countS = countS + 1
                if(GPA == 8 ):
                    countA = countA + 1
                if(GPA == 7 ):
                    countB = countB + 1
                if(GPA == 6 ):
                    countC = countC + 1
                if(GPA == 5 ):
                    countD = countD + 1
                if(GPA == 4 ):
                    countE = countE + 1
                if(GPA == 0 ):
                    countF = countF + 1
            SD_Lab.append(countSS)
            SD_Lab.append(countS)
            SD_Lab.append(countA)
            SD_Lab.append(countB)
            SD_Lab.append(countC)
            SD_Lab.append(countD)
            SD_Lab.append(countE)
            SD_Lab.append(countF)
            countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0

            for GPA in Sort_CG_B_Lab :
                if(GPA == 10 ):
                    countSS = countSS + 1
                if(GPA == 9 ):
                    countS = countS + 1
                if(GPA == 8 ):
                    countA = countA + 1
                if(GPA == 7 ):
                    countB = countB + 1
                if(GPA == 6 ):
                    countC = countC + 1
                if(GPA == 5 ):
                    countD = countD + 1
                if(GPA == 4 ):
                    countE = countE + 1
                if(GPA == 0 ):
                    countF = countF + 1
            CG_Lab.append(countSS)
            CG_Lab.append(countS)
            CG_Lab.append(countA)
            CG_Lab.append(countB)
            CG_Lab.append(countC)
            CG_Lab.append(countD)
            CG_Lab.append(countE)
            CG_Lab.append(countF)
            countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0

            for GPA in Sort_CIP_B :
                if(GPA == 10 ):
                    countSS = countSS + 1
                if(GPA == 9 ):
                    countS = countS + 1
                if(GPA == 8 ):
                    countA = countA + 1
                if(GPA == 7 ):
                    countB = countB + 1
                if(GPA == 6 ):
                    countC = countC + 1
                if(GPA == 5 ):
                    countD = countD + 1
                if(GPA == 4 ):
                    countE = countE + 1
                if(GPA == 0 ):
                    countF = countF + 1
            CIP.append(countSS)
            CIP.append(countS)
            CIP.append(countA)
            CIP.append(countB)
            CIP.append(countC)
            CIP.append(countD)
            CIP.append(countE)
            CIP.append(countF)
            countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0

        elif(division == 3):
            for GPA in Sort_ME_C :
                if(GPA == 10 ):
                    countSS = countSS + 1
                if(GPA == 9 ):
                    countS = countS + 1
                if(GPA == 8 ):
                    countA = countA + 1
                if(GPA == 7 ):
                    countB = countB + 1
                if(GPA == 6 ):
                    countC = countC + 1
                if(GPA == 5 ):
                    countD = countD + 1
                if(GPA == 4 ):
                    countE = countE + 1
                if(GPA == 0 ):
                    countF = countF + 1
            ME.append(countSS)
            ME.append(countS)
            ME.append(countA)
            ME.append(countB)
            ME.append(countC)
            ME.append(countD)
            ME.append(countE)
            ME.append(countF)
            countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0

            for GPA in Sort_DC_C :
                if(GPA == 10 ):
                    countSS = countSS + 1
                if(GPA == 9 ):
                    countS = countS + 1
                if(GPA == 8 ):
                    countA = countA + 1
                if(GPA == 7 ):
                    countB = countB + 1
                if(GPA == 6 ):
                    countC = countC + 1
                if(GPA == 5 ):
                    countD = countD + 1
                if(GPA == 4 ):
                    countE = countE + 1
                if(GPA == 0 ):
                    countF = countF + 1
            DC.append(countSS)
            DC.append(countS)
            DC.append(countA)
            DC.append(countB)
            DC.append(countC)
            DC.append(countD)
            DC.append(countE)
            DC.append(countF)
            countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0

            for GPA in Sort_CD_C :
                if(GPA == 10 ):
                    countSS = countSS + 1
                if(GPA == 9 ):
                    countS = countS + 1
                if(GPA == 8 ):
                    countA = countA + 1
                if(GPA == 7 ):
                    countB = countB + 1
                if(GPA == 6 ):
                    countC = countC + 1
                if(GPA == 5 ):
                    countD = countD + 1
                if(GPA == 4 ):
                    countE = countE + 1
                if(GPA == 0 ):
                    countF = countF + 1
            CD.append(countSS)
            CD.append(countS)
            CD.append(countA)
            CD.append(countB)
            CD.append(countC)
            CD.append(countD)
            CD.append(countE)
            CD.append(countF)
            countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0

            for GPA in Sort_CG_C :
                if(GPA == 10 ):
                    countSS = countSS + 1
                if(GPA == 9 ):
                    countS = countS + 1
                if(GPA == 8 ):
                    countA = countA + 1
                if(GPA == 7 ):
                    countB = countB + 1
                if(GPA == 6 ):
                    countC = countC + 1
                if(GPA == 5 ):
                    countD = countD + 1
                if(GPA == 4 ):
                    countE = countE + 1
                if(GPA == 0 ):
                    countF = countF + 1
            CG.append(countSS)
            CG.append(countS)
            CG.append(countA)
            CG.append(countB)
            CG.append(countC)
            CG.append(countD)
            CG.append(countE)
            CG.append(countF)
            countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0

            for GPA in Sort_OOMD_C :
                if(GPA == 10 ):
                    countSS = countSS + 1
                if(GPA == 9 ):
                    countS = countS + 1
                if(GPA == 8 ):
                    countA = countA + 1
                if(GPA == 7 ):
                    countB = countB + 1
                if(GPA == 6 ):
                    countC = countC + 1
                if(GPA == 5 ):
                    countD = countD + 1
                if(GPA == 4 ):
                    countE = countE + 1
                if(GPA == 0 ):
                    countF = countF + 1
            OOMD.append(countSS)
            OOMD.append(countS)
            OOMD.append(countA)
            OOMD.append(countB)
            OOMD.append(countC)
            OOMD.append(countD)
            OOMD.append(countE)
            OOMD.append(countF)
            countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0

            for GPA in Sort_OE_C :
                if(GPA == 10 ):
                    countSS = countSS + 1
                if(GPA == 9 ):
                    countS = countS + 1
                if(GPA == 8 ):
                    countA = countA + 1
                if(GPA == 7 ):
                    countB = countB + 1
                if(GPA == 6 ):
                    countC = countC + 1
                if(GPA == 5 ):
                    countD = countD + 1
                if(GPA == 4 ):
                    countE = countE + 1
                if(GPA == 0 ):
                    countF = countF + 1
            OE.append(countSS)
            OE.append(countS)
            OE.append(countA)
            OE.append(countB)
            OE.append(countC)
            OE.append(countD)
            OE.append(countE)
            OE.append(countF)
            countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0

            for GPA in Sort_SD_C_Lab :
                if(GPA == 10 ):
                    countSS = countSS + 1
                if(GPA == 9 ):
                    countS = countS + 1
                if(GPA == 8 ):
                    countA = countA + 1
                if(GPA == 7 ):
                    countB = countB + 1
                if(GPA == 6 ):
                    countC = countC + 1
                if(GPA == 5 ):
                    countD = countD + 1
                if(GPA == 4 ):
                    countE = countE + 1
                if(GPA == 0 ):
                    countF = countF + 1
            SD_Lab.append(countSS)
            SD_Lab.append(countS)
            SD_Lab.append(countA)
            SD_Lab.append(countB)
            SD_Lab.append(countC)
            SD_Lab.append(countD)
            SD_Lab.append(countE)
            SD_Lab.append(countF)
            countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0

            for GPA in Sort_CG_C_Lab :
                if(GPA == 10 ):
                    countSS = countSS + 1
                if(GPA == 9 ):
                    countS = countS + 1
                if(GPA == 8 ):
                    countA = countA + 1
                if(GPA == 7 ):
                    countB = countB + 1
                if(GPA == 6 ):
                    countC = countC + 1
                if(GPA == 5 ):
                    countD = countD + 1
                if(GPA == 4 ):
                    countE = countE + 1
                if(GPA == 0 ):
                    countF = countF + 1
            CG_Lab.append(countSS)
            CG_Lab.append(countS)
            CG_Lab.append(countA)
            CG_Lab.append(countB)
            CG_Lab.append(countC)
            CG_Lab.append(countD)
            CG_Lab.append(countE)
            CG_Lab.append(countF)
            countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0

            for GPA in Sort_CIP_C :
                if(GPA == 10 ):
                    countSS = countSS + 1
                if(GPA == 9 ):
                    countS = countS + 1
                if(GPA == 8 ):
                    countA = countA + 1
                if(GPA == 7 ):
                    countB = countB + 1
                if(GPA == 6 ):
                    countC = countC + 1
                if(GPA == 5 ):
                    countD = countD + 1
                if(GPA == 4 ):
                    countE = countE + 1
                if(GPA == 0 ):
                    countF = countF + 1
            CIP.append(countSS)
            CIP.append(countS)
            CIP.append(countA)
            CIP.append(countB)
            CIP.append(countC)
            CIP.append(countD)
            CIP.append(countE)
            CIP.append(countF)
            countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0

        elif(division == 4):
            for GPA in Sort_ME_D :
                if(GPA == 10 ):
                    countSS = countSS + 1
                if(GPA == 9 ):
                    countS = countS + 1
                if(GPA == 8 ):
                    countA = countA + 1
                if(GPA == 7 ):
                    countB = countB + 1
                if(GPA == 6 ):
                    countC = countC + 1
                if(GPA == 5 ):
                    countD = countD + 1
                if(GPA == 4 ):
                    countE = countE + 1
                if(GPA == 0 ):
                    countF = countF + 1
            ME.append(countSS)
            ME.append(countS)
            ME.append(countA)
            ME.append(countB)
            ME.append(countC)
            ME.append(countD)
            ME.append(countE)
            ME.append(countF)
            countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0

            for GPA in Sort_DC_D :
                if(GPA == 10 ):
                    countSS = countSS + 1
                if(GPA == 9 ):
                    countS = countS + 1
                if(GPA == 8 ):
                    countA = countA + 1
                if(GPA == 7 ):
                    countB = countB + 1
                if(GPA == 6 ):
                    countC = countC + 1
                if(GPA == 5 ):
                    countD = countD + 1
                if(GPA == 4 ):
                    countE = countE + 1
                if(GPA == 0 ):
                    countF = countF + 1
            DC.append(countSS)
            DC.append(countS)
            DC.append(countA)
            DC.append(countB)
            DC.append(countC)
            DC.append(countD)
            DC.append(countE)
            DC.append(countF)
            countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0

            for GPA in Sort_CD_D :
                if(GPA == 10 ):
                    countSS = countSS + 1
                if(GPA == 9 ):
                    countS = countS + 1
                if(GPA == 8 ):
                    countA = countA + 1
                if(GPA == 7 ):
                    countB = countB + 1
                if(GPA == 6 ):
                    countC = countC + 1
                if(GPA == 5 ):
                    countD = countD + 1
                if(GPA == 4 ):
                    countE = countE + 1
                if(GPA == 0 ):
                    countF = countF + 1
            CD.append(countSS)
            CD.append(countS)
            CD.append(countA)
            CD.append(countB)
            CD.append(countC)
            CD.append(countD)
            CD.append(countE)
            CD.append(countF)
            countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0

            for GPA in Sort_CG_D :
                if(GPA == 10 ):
                    countSS = countSS + 1
                if(GPA == 9 ):
                    countS = countS + 1
                if(GPA == 8 ):
                    countA = countA + 1
                if(GPA == 7 ):
                    countB = countB + 1
                if(GPA == 6 ):
                    countC = countC + 1
                if(GPA == 5 ):
                    countD = countD + 1
                if(GPA == 4 ):
                    countE = countE + 1
                if(GPA == 0 ):
                    countF = countF + 1
            CG.append(countSS)
            CG.append(countS)
            CG.append(countA)
            CG.append(countB)
            CG.append(countC)
            CG.append(countD)
            CG.append(countE)
            CG.append(countF)
            countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0

            for GPA in Sort_OOMD_D :
                if(GPA == 10 ):
                    countSS = countSS + 1
                if(GPA == 9 ):
                    countS = countS + 1
                if(GPA == 8 ):
                    countA = countA + 1
                if(GPA == 7 ):
                    countB = countB + 1
                if(GPA == 6 ):
                    countC = countC + 1
                if(GPA == 5 ):
                    countD = countD + 1
                if(GPA == 4 ):
                    countE = countE + 1
                if(GPA == 0 ):
                    countF = countF + 1
            OOMD.append(countSS)
            OOMD.append(countS)
            OOMD.append(countA)
            OOMD.append(countB)
            OOMD.append(countC)
            OOMD.append(countD)
            OOMD.append(countE)
            OOMD.append(countF)
            countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0

            for GPA in Sort_OE_D :
                if(GPA == 10 ):
                    countSS = countSS + 1
                if(GPA == 9 ):
                    countS = countS + 1
                if(GPA == 8 ):
                    countA = countA + 1
                if(GPA == 7 ):
                    countB = countB + 1
                if(GPA == 6 ):
                    countC = countC + 1
                if(GPA == 5 ):
                    countD = countD + 1
                if(GPA == 4 ):
                    countE = countE + 1
                if(GPA == 0 ):
                    countF = countF + 1
            OE.append(countSS)
            OE.append(countS)
            OE.append(countA)
            OE.append(countB)
            OE.append(countC)
            OE.append(countD)
            OE.append(countE)
            OE.append(countF)
            countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0

            for GPA in Sort_SD_D_Lab :
                if(GPA == 10 ):
                    countSS = countSS + 1
                if(GPA == 9 ):
                    countS = countS + 1
                if(GPA == 8 ):
                    countA = countA + 1
                if(GPA == 7 ):
                    countB = countB + 1
                if(GPA == 6 ):
                    countC = countC + 1
                if(GPA == 5 ):
                    countD = countD + 1
                if(GPA == 4 ):
                    countE = countE + 1
                if(GPA == 0 ):
                    countF = countF + 1
            SD_Lab.append(countSS)
            SD_Lab.append(countS)
            SD_Lab.append(countA)
            SD_Lab.append(countB)
            SD_Lab.append(countC)
            SD_Lab.append(countD)
            SD_Lab.append(countE)
            SD_Lab.append(countF)
            countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0

            for GPA in Sort_CG_D_Lab :
                if(GPA == 10 ):
                    countSS = countSS + 1
                if(GPA == 9 ):
                    countS = countS + 1
                if(GPA == 8 ):
                    countA = countA + 1
                if(GPA == 7 ):
                    countB = countB + 1
                if(GPA == 6 ):
                    countC = countC + 1
                if(GPA == 5 ):
                    countD = countD + 1
                if(GPA == 4 ):
                    countE = countE + 1
                if(GPA == 0 ):
                    countF = countF + 1
            CG_Lab.append(countSS)
            CG_Lab.append(countS)
            CG_Lab.append(countA)
            CG_Lab.append(countB)
            CG_Lab.append(countC)
            CG_Lab.append(countD)
            CG_Lab.append(countE)
            CG_Lab.append(countF)
            countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0

            for GPA in Sort_CIP_D :
                if(GPA == 10 ):
                    countSS = countSS + 1
                if(GPA == 9 ):
                    countS = countS + 1
                if(GPA == 8 ):
                    countA = countA + 1
                if(GPA == 7 ):
                    countB = countB + 1
                if(GPA == 6 ):
                    countC = countC + 1
                if(GPA == 5 ):
                    countD = countD + 1
                if(GPA == 4 ):
                    countE = countE + 1
                if(GPA == 0 ):
                    countF = countF + 1
            CIP.append(countSS)
            CIP.append(countS)
            CIP.append(countA)
            CIP.append(countB)
            CIP.append(countC)
            CIP.append(countD)
            CIP.append(countE)
            CIP.append(countF)
            countSS,countS,countA,countB,countC,countD,countE,countF = 0,0,0,0,0,0,0,0
        #end of if-else

        # Plot
        # Make square figures and axes
        plt.figure(1, figsize=(20,10))
        the_grid = GridSpec(3, 3)

        plt.subplot(the_grid[0, 0], aspect=1, title='ME')
        plt.pie(ME, labels=grades, colors=colors, pctdistance = 0.85,
        autopct='%.0f%%', textprops={'size': 'smaller'}, shadow=True, startangle=90, radius=1.165)

        plt.subplot(the_grid[0, 1], aspect=1, title='DC')
        plt.pie(DC, labels=grades, colors=colors, pctdistance = 0.85,
        autopct='%.0f%%', textprops={'size': 'smaller'}, shadow=True, startangle=90, radius=1.165)

        plt.subplot(the_grid[0, 2], aspect=1, title='CD')
        plt.pie(CD, labels=grades, colors=colors, pctdistance = 0.85,
        autopct='%.0f%%', textprops={'size': 'smaller'}, shadow=True, startangle=90, radius=1.165)

        plt.subplot(the_grid[1, 0], aspect=1, title='CG')
        plt.pie(CG, labels=grades, colors=colors, pctdistance = 0.85,
        autopct='%.0f%%', textprops={'size': 'smaller'}, shadow=True, startangle=90, radius=1.165)

        plt.subplot(the_grid[1, 1], aspect=1, title='OOMD')
        plt.pie(OOMD, labels=grades, colors=colors, pctdistance = 0.85,
        autopct='%.0f%%', textprops={'size': 'smaller'}, shadow=True, startangle=90, radius=1.165)

        plt.subplot(the_grid[1, 2], aspect=1, title='OE')
        plt.pie(OE, labels=grades, colors=colors, pctdistance = 0.85,
        autopct='%.0f%%', textprops={'size': 'smaller'}, shadow=True, startangle=90, radius=1.165)

        plt.subplot(the_grid[2, 0], aspect=1, title='SD Lab')
        plt.pie(SD_Lab, labels=grades, colors=colors, pctdistance = 0.85,
        autopct='%.0f%%', textprops={'size': 'smaller'}, shadow=True, startangle=90, radius=1.165)

        plt.subplot(the_grid[2, 1], aspect=1, title='CG Lab')
        plt.pie(CG_Lab, labels=grades, colors=colors, pctdistance = 0.85,
        autopct='%.0f%%', textprops={'size': 'smaller'}, shadow=True, startangle=90, radius=1.165)

        plt.subplot(the_grid[2, 2], aspect=1, title='CIP')
        plt.pie(CIP, labels=grades, colors=colors, pctdistance = 0.85,
        autopct='%.0f%%', textprops={'size': 'smaller'}, shadow=True, startangle=90, radius=1.165)

        plt.suptitle('6th semester ' + divisions[division] + ' Division Overall performance', fontsize=16)
        plt.show()

#function to compare division scores subject wise
def subject_summary(subject):
    while(subject >= 0 and subject <= 9):
        print("Enter the subject  :")
        print("1 -> ME      2 -> DC       3 -> CD")
        print("4 -> CG      5 -> OOMD     6 -> OE")
        print("7 -> SD Lab  8 -> CG Lab   9 -> CIP")
        print("Press 0 to go back ")
        subject = input("Subject : ")
        try :
            subject = int(subject)
        except :
            print('Invalid option')
            subject = 0
            continue

        if(subject == 0):
            break
        if(subject > 9 or subject < 0):
            print("Invalid Option!")
            subject = 0
            continue
        #Plot a histogram comparing scores of selected subject division wise
        plt.hist([subject_scores_A[subject],subject_scores_B[subject],subject_scores_C[subject],
                subject_scores_D[subject]],bins=[-0.9,0.1,1.1,2.1,3.1,4.1,5.1,6.1,7.1,8.1,9.1,10.1],rwidth=0.75)
        plt.grid(axis='y', alpha=0.6)
        #plt.xlabel("GPA")
        plt.ylabel("Number of Students")
        plt.xticks(range(0, 0))
        plt.yticks(range(1, 30))
        plt.title('6th Semester ' + subject_names[subject] + ' Subject Overall Performance')
        plt.legend(['A Division','B Division','C Division','D Division'])
        plt.text(-0.5,-1, r'$0$')
        plt.text(0.5,-1, r'$1$')
        plt.text(1.5,-1, r'$2$')
        plt.text(2.5,-1, r'$3$')
        plt.text(3.5,-1, r'$4$')
        plt.text(4.5,-1, r'$5$')
        plt.text(5.5,-1, r'$6$')
        plt.text(6.5,-1, r'$7$')
        plt.text(7.5,-1, r'$8$')
        plt.text(8.5,-1, r'$9$')
        plt.text(9.5,-1, r'$10$')
        plt.show()

#function to compare subject scores division wise
def subject_compare(division,subject1,subject2):
    while(division == 1 or division == 2 or division == 3 or division == 4 or division == 0):
        print("Enter the Division :")
        print("1 -> A   2 -> B   3 -> C   4 -> D")
        print("Press 0 to go back ")
        division = input("Division : ")
        try :
            division = int(division)
        except :
            print('Invalid option')
            division = 0
            continue

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
            subject1 = input("Subject 1 : ")
            try :
                subject1 = int(subject1)
            except :
                print('Invalid option')
                subject1 = 0
                continue

            if(subject1 == 0):
                break
            subject2 = input("Subject 2 : ")
            try :
                subject2 = int(subject2)
            except :
                print('Invalid option')
                subject2 = 0
                continue

            if(subject1 > 9 or subject2 > 9 or subject1 <= 0 or subject2 <= 0):
                print("Invalid Option!")
                subject1 = 0
                subject2 = 0
                continue
            if(division == 1):
                plt.hist([subject_scores_A[subject1],subject_scores_A[subject2]],
                        bins=[-0.9,0.1,1.1,2.1,3.1,4.1,5.1,6.1,7.1,8.1,9.1,10.1],rwidth=0.75)
                plt.title('6th Semester A Division Subject wise performance')
            elif(division == 2):
                plt.hist([subject_scores_B[subject1],subject_scores_B[subject2]],
                        bins=[-0.9,0.1,1.1,2.1,3.1,4.1,5.1,6.1,7.1,8.1,9.1,10.1],rwidth=0.75)
                plt.title('6th Semester B Division Subject wise performance')
            elif(division == 3):
                plt.hist([subject_scores_C[subject1],subject_scores_C[subject2]],
                        bins=[-0.9,0.1,1.1,2.1,3.1,4.1,5.1,6.1,7.1,8.1,9.1,10.1],rwidth=0.75)
                plt.title('6th Semester C Division Subject wise performance')
            elif(division == 4):
                plt.hist([subject_scores_D[subject1],subject_scores_D[subject2]],
                        bins=[-0.9,0.1,1.1,2.1,3.1,4.1,5.1,6.1,7.1,8.1,9.1,10.1],rwidth=0.75)
                plt.title('6th Semester D Division Subject wise performance')
            #end of if-else
            plt.grid(axis='y', alpha=0.6)
            #plt.xlabel("GPA")
            plt.ylabel("Number of Students")
            plt.xticks(range(0, 0))
            plt.yticks(range(1, 30))
            plt.legend([subject_names[subject1],subject_names[subject2]])
            plt.text(-0.5,-1, r'$0$')
            plt.text(0.5,-1, r'$1$')
            plt.text(1.5,-1, r'$2$')
            plt.text(2.5,-1, r'$3$')
            plt.text(3.5,-1, r'$4$')
            plt.text(4.5,-1, r'$5$')
            plt.text(5.5,-1, r'$6$')
            plt.text(6.5,-1, r'$7$')
            plt.text(7.5,-1, r'$8$')
            plt.text(8.5,-1, r'$9$')
            plt.text(9.5,-1, r'$10$')
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

#Dictionary having integer keys and a list of subject scores as value  for 4 divisions
subject_scores_A = {1 : Sort_ME_A, 2 : Sort_DC_A, 3 : Sort_CD_A, 4 : Sort_CG_A, 5 : Sort_OOMD_A,
            6 : Sort_OE_A, 7 : Sort_SD_A_Lab, 8 : Sort_CG_A_Lab, 9 : Sort_CIP_A }
subject_scores_B = {1 : Sort_ME_B, 2 : Sort_DC_B, 3 : Sort_CD_B, 4 : Sort_CG_B, 5 : Sort_OOMD_B,
            6 : Sort_OE_B, 7 : Sort_SD_B_Lab, 8 : Sort_CG_B_Lab, 9 : Sort_CIP_B }
subject_scores_C = {1 : Sort_ME_C, 2 : Sort_DC_C, 3 : Sort_CD_C, 4 : Sort_CG_C, 5 : Sort_OOMD_C,
            6 : Sort_OE_C, 7 : Sort_SD_C_Lab, 8 : Sort_CG_C_Lab, 9 : Sort_CIP_C }
subject_scores_D = {1 : Sort_ME_D, 2 : Sort_DC_D, 3 : Sort_CD_D, 4 : Sort_CG_D, 5 : Sort_OOMD_D,
            6 : Sort_OE_D, 7 : Sort_SD_D_Lab, 8 : Sort_CG_D_Lab, 9 : Sort_CIP_D }

#Dictionary having integer keys and subject names as value
subject_names = {1 : 'ME', 2 : 'DC', 3 : 'CD', 4 : 'CG', 5 : 'OOMD',
            6 : 'OE', 7 : 'SD Lab', 8 : 'CG Lab', 9 : 'CIP' }

#Dictionary having integer keys and name of the division as value
divisions = {1 : 'A' , 2 : 'B' , 3 : 'C' , 4 : 'D'}

number = 0
subject = 0
subject1 = 0
subject2 = 0
division = 0

#Main Loop
while(number == 1 or number == 2 or number == 0 or number == 3 or number == 4):
    #Display the Menu and accept the user input
    print("--------------------WELCOME TO ACADEMIC INFORMATION VISUALIZER---------------------")
    print("MENU")
    print("1 --> Get Summary of 6th semester CSE")
    print("2 --> Get Summary Division wise")
    print("3 --> Get Summary Subject wise")
    print("4 --> Compare by subject scores")
    print("0 --> Exit")
    print("-----------------------------------------------------------------------------------")
    number = input("Enter Option : ")
    try :
        number = int(number)
    except :
        print('Invalid option')
        number = 0
        continue

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
                bins=[0,1,2,3,4,5,6,7,8,9,10,11],rwidth=0.75)
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
    #To compare by subject scores division wise
    elif(number == 4) :
        subject_compare(division,subject1,subject2)
    #Exit from the Program
    elif(number == 0) :
        print("Thank You")
        exit()
    else :
        print("Invalid Option!")
        number = 0
