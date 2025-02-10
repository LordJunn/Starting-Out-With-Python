"""
Write a class named Employee that holds the following data about an employee in attrib-
utes: name, ID number, department, and job title.
Once you have written the class, write a program that creates three Employee objects to
hold the following data:
Name ID Number Department Job Title
Susan Meyers 47899 Accounting Vice President
Mark Jones 39119 IT Programmer
Joy Rogers 81774 Manufacturing Engineer
The program should store this data in the three objects, then display the data for each
employee on the screen.
"""
import Employee # oh i need to type .Employee as well instead of just Employee if im importing
    
def main():
    emp1 = Employee.Employee("Susan Meyers", 47899, "Accounting", "Vice President")
    emp2 = Employee.Employee("Mark Jones", 39119, "IT", "Programmer")
    emp3 = Employee.Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")
    
    print('Name\t\tID Number\tDepartment\tJob Title')
    print(f'{emp1.nameG()}\t{emp1.IDG()}\t\t{emp1.departmentG()}\t{emp1.titleG()}')
    print(f'{emp2.nameG()}\t{emp2.IDG()}\t\t{emp2.departmentG()}\t\t{emp2.titleG()}')
    print(f'{emp3.nameG()}\t{emp3.IDG()}\t\t{emp3.departmentG()}\t{emp3.titleG()}')    
        
main()