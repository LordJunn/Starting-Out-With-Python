"""
Figure 3-19 shows a simplified flowchart for troubleshooting a bad Wi-Fi connection. Use
the flowchart to create a program that leads a person through the steps of fixing a bad
Wi-Fi connection. Here is an example of the program’s output:
Reboot the computer and try to connect.
Did that fix the problem? no [Enter]
Reboot the router and try to connect.
Did that fix the problem? yes [Enter]
Notice the program ends as soon as a solution is found to the problem. Here is another
example of the program’s output:
Reboot the computer and try to connect.
Did that fix the problem? no [Enter]
Reboot the router and try to connect.
Did that fix the problem? no [Enter]
Make sure the cables between the router and modem are plugged in firmly.
Did that fix the problem? no [Enter]
Move the router to a new location.
Did that fix the problem? no [Enter]
Get a new router.
"""

print("Welcome to the Wi-Fi troubleshooting program.")
print("Follow the steps to fix your Wi-Fi connection issue.\n")

print("Reboot the computer and try to connect.")
choice = input('Did that fix the problem? ')
if(choice == 'no'):
    print("Reboot the router and try to connect.")
    choice = input('Did that fix the problem? ')
    if(choice == 'no'):
        print("Make sure the cables between the router and modem are plugged in firmly.")
        choice = input('Did that fix the problem? ')
        if(choice == 'no'):
            print("Move the router to a new location.")
            choice = input('Did that fix the problem? ')
            if(choice == 'no'):
                print("Get a new router.")
            elif(choice == 'yes'):
                print('Problem fixed by moving the router to a new location.')
        elif(choice == 'yes'):
            print('Problem fixed by making sure the cables between the router and modem are plugged in firmly.')
    elif(choice == 'yes'):
        print('Problem fixed by rebooting the router.')
elif(choice == 'yes'):
    print('Problem fixed by rebooting the computer.')