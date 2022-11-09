'''
-=============================-
# Made by Abdurrahman Choglay
-=============================-

Notes:
This program will aim to calculate certain calculations to help a Swimming Pool (Plant) Operator 

Glossary:
- FC = Free Chlorine
- Mg/l = Miligrams per Litre

Formulae Used;
Manual Dosing:
Additional FC Concentration Required * Pool Volume = Grams of FC needed / Concentration of the Chlorine
'''
#troubleshoot/testing

# Subroutines
def ManualDosing(): # Calculating amount of Chlorine needed to reach a Free Chlorine target
 Cl_Increase() 
 VolumeCalculation()
 FCgrams = Difference * Volume # Calculates the amount of Free Chlorine needed
 print("\nYou need " + (str(FCgrams)) +" grams of Free Chlorine \n")
 Concentration()
 print (Strength)
  

def Cl_Increase(): # To determine the amount of FC needed 
 print("Clorine Difference:") # Shows the difference in Free Chlorine Required
 Current = float(input("Current Free Chlorine: ")) # Sets the Current Free Chlorine
 Target = float(input("Target Free Chlorine: ")) # Sets the Target Free Chlorine
 global Difference # Makes the Difference in the Target and Current FC global so we can use it in the ManualDosing subroutine
 Difference = Target - Current # Finding out the amount of chlorine to increase by
 print("Free Chlorine Difference = " + (str(Difference)) + " Mg/l \n" )


def VolumeCalculation(): # Calculates the Volume of the pool in Cubic Metres (m3)
 print("Volume Test:")
 Length = float(input("Pool Length in Meters: "))
 Width = float(input("Pool Width in Meters: "))
 Depth = float(input("Pool Depth in Meters: "))
 global Volume
 Volume = Length * Width * Depth
 print ("Total Volume = " + (str(Volume)) + " m3")

def Concentration(): # Figuring out the concentration of Free Chlorine (e.g. 65% = 65% Active Free Chlorine)
 global Strength
 Strength = int(input("e.g. Calcium Hypochlorite = 65% or 70%, write 65 or 70. \n Strength of the Chlorine (in %): ")) # To find the concentration of Free Chlorine (as a whole number) 
 Strength = Strength / 100 # To have the concentration of Free Chlorine as a decimal



# Program
ManualDosing()
