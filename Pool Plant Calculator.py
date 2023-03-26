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
'''Manual Dosing [START]''' # These subroutines will be used to work out the manual dosing
def ManualDosing(): # Calculating amount of Chlorine needed to reach a Free Chlorine target
 Cl_Increase() 
 VolumeCalculation()
 global FCgrams # Makes it a global variable so we can use it in ChlorineDosing()
 FCgrams = Difference * Volume # Calculates the amount of Free Chlorine needed
 print("\nYou need " + (str(FCgrams)) +" grams of Free Chlorine \n") # Tells the user how much grams of Free Chlorine they need - NOT the amount of chlorine they need to put into the pool (as the amount of free chlorine per gram or chlorine depends on its strength)
 Concentration()
 ChlorineDosing()
  

def Cl_Increase(): # To determine the amount of FC needed
 print("Clorine Difference:") # Shows the difference in Free Chlorine Required
 Current = float(input("Current Free Chlorine: ")) # Sets the Current Free Chlorine
 Target = float(input("Target Free Chlorine: ")) # Sets the Target Free Chlorine
 global Difference # Makes the Difference in the Target and Current FC global so we can use it in the ManualDosing subroutine
 Difference = Target - Current # Finding out the amount of chlorine to increase by
 print("Free Chlorine Difference = " + (str(Difference)) + " Mg/l \n" )


def VolumeCalculation(): # Calculates the Volume of the pool in Cubic Metres (m3)
 global Volume # Makes the Volume a global variable so we can use it in the calculation above
 UserInput = input("Do you know the pool volume? (Yes/No): ") # Question to get a user input to lead to two possible outcomes of the subroutine
 if UserInput == "Yes": # If the user types Yes
     UserInput2 = float(input("Pool Volume in m3: ")) # Asks the user for the volume of the pool in m3
     Volume = UserInput2 # Assigns the userinput value to the volume of the pool
     print ("Total Volume = " + (str(Volume)) + " m3") # Prints the total volume of the pool
 elif UserInput == "No": # If the user types No
   print("Volume Calculation:") #  To make it clear that we are calculating the volume of the pool 
   Length = float(input("Pool Length in Meters: "))
   Width = float(input("Pool Width in Meters: "))
   Depth = float(input("Pool Depth in Meters: "))
   Volume = Length * Width * Depth # Calculation to find the Volume of the pool in cubic meters
   print ("Total Volume = " + (str(Volume)) + " m3") # Prints the total volume of the pool

def Concentration(): # Figuring out the concentration of Free Chlorine (e.g. 65% = 65% Active Free Chlorine)
 global Strength # Makes the concentration of chlorine a global variable to be used in the calculation in ManualDosing()
 Strength = int(input("e.g. Calcium Hypochlorite = 65% or 70%, write 65 or 70. \nStrength of the Chlorine (in %): ")) # To find the concentration of Free Chlorine (as a whole number) 
 Strength = Strength / 100 # To have the concentration of Free Chlorine as a decimal

def ChlorineDosing(): # The final value in the formula for manual dosing - i.e. how much chlorine to put into the pool to reach the desired free chlorine level
  global ChlorineDose # Makes the value a global variable so we can use it in ManualDosing()
  ChlorineDose = FCgrams / Strength
  print ("This is how much Chlorine you need to dose into the pool: " + str((ChlorineDose)) + " grams.")
  
'''Manual Dosing [END]'''


# Program
ManualDosing() # Starts the ManualDosing subroutine to work out how many grams of chlorine to put into the pool
