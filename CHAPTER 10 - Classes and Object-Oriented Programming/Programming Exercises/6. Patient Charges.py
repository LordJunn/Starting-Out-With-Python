"""
Write a class named Patient that has attributes for the following data:
• First name, middle name, and last name
• Address, city, state, and ZIP code
• Phone number
• Name and phone number of emergency contact
The Patient class’s _ _init_ _ method should accept an argument for each attribute. The
Patient class should also have accessor and mutator methods for each attribute.
Next, write a class named Procedure that represents a medical procedure that has been
performed on a patient. The Procedure class should have attributes for the following data:
• Name of the procedure
• Date of the procedure
• Name of the practitioner who performed the procedure
• Charges for the procedure
The Procedure class’s _ _ init_ _ method should accept an argument for each attribute.
The Procedure class should also have accessor and mutator methods for each attribute.
Next, write a program that creates an instance of the Patient class, initialized with sample
data. Then, create three instances of the Procedure class, initialized with the following data:
Procedure #1: Procedure #2: Procedure #3:
Procedure name: Physical Exam
Date: Today’s date
Practitioner: Dr. Irvine
Charge: 250.00
Procedure name: X-ray
Date: Today’s date
Practitioner: Dr. Jamison
Charge: 500.00
Procedure name: Blood test
Date: Today’s date
Practitioner: Dr. Smith
Charge: 200.00
The program should display the patient’s information, information about all three of the
procedures, and the total charges of the three procedures.
""" # actually wat use is this program
class Patient: # no mutator, too long
    def __init__(self, first, middle, last, address, city, state, zip, phone, eName, ePhone):
        self.__first = first
        self.__middle = middle
        self.__last = last
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip = zip
        self.__phone = phone
        self.__eName = eName
        self.__ePhone = ePhone        
        
    def firstG(self):
        return self.__first
    
    def middleG(self):
        return self.__middle
    
    def lastG(self):
        return self.__last
    
    def addressG(self):
        return self.__address
    
    def cityG(self):
        return self.__city
    
    def stateG(self):
        return self.__state
    
    def zipG(self):
        return self.__zip
    
    def phoneG(self):
        return self.__phone
    
    def eNameG(self):
        return self.__eName
    
    def ePhoneG(self):
        return self.__ePhone
    
class Procedure:
    def __init__(self, name, date, practitioner, charge):
        self.__name = name
        self.__date = date
        self.__practitioner = practitioner
        self.__charge = charge
        
    def nameG(self):
        return self.__name
    
    def dateG(self):
        return self.__date
    
    def practitionerG(self):
        return self.__practitioner
    
    def chargeG(self):
        return self.__charge        
       
def main():
    today_date = "2024-08-13"
    
    first = input('What is your first name? ')
    middle = input('What is your middle name? ') 
    last = input('What is your last name? ')   
    address = input('What is your address? ') 
    city = input('What is your city? ')
    state = input('What is your state? ')
    zip = int(input('What is your zip? '))  
    phone = input('What is your phone number? ')
    ename = input('What is your phone number? ')
    ephone = input(f"What is {ename}'s phone number? ")
    
    patient = Patient(first, middle, last, address, city, state, zip, phone, ename, ephone)
        
    proc1 = Procedure("Physical Exam", today_date, "Dr. Irvine", 250.00)
    proc2 = Procedure("X-ray", today_date, "Dr. Jamison", 500.00)
    proc3 = Procedure("Blood test", today_date, "Dr. Smith", 200.00)
    
    procedures = [proc1, proc2, proc3]
    total = 0        

    print("Patient Information:")
    print(f"Name: {patient.firstG()} {patient.middleG()} {patient.lastG()}")
    print(f"Address: {patient.addressG()}, {patient.cityG()}, {patient.stateG()} {patient.zipG()}")
    print(f"Phone: {patient.phoneG()}")
    print(f"Emergency Contact: {patient.eNameG()} ({patient.ePhoneG()})")
 
    print("\nProcedures:")
    for proc in procedures:
        print(f"Procedure: {proc.nameG()}")
        print(f"Date: {proc.dateG()}")
        print(f"Practitioner: {proc.practitionerG()}")
        print(f"Charge: ${proc.chargeG():.2f}\n")
        total += proc.chargeG()
    
    print(f"Total Charges: ${total:.2f}")       
    
main()