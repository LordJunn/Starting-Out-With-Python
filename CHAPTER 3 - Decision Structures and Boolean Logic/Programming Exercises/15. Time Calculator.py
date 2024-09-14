"""
Write a program that asks the user to enter a number of seconds and works as follows:
• There are 60 seconds in a minute. If the number of seconds entered by the user is greater
than or equal to 60, the program should convert the number of seconds to minutes and
seconds.
• There are 3,600 seconds in an hour. If the number of seconds entered by the user is
greater than or equal to 3,600, the program should convert the number of seconds to
hours, minutes, and seconds.
• There are 86,400 seconds in a day. If the number of seconds entered by the user is
greater than or equal to 86,400, the program should convert the number of seconds to
days, hours, minutes, and seconds.
"""

seconds = int(input("Enter a number of seconds: "))

if(seconds >= 86400):
    days = seconds // 86400
    temp1 = seconds - (days * 86400)
    if(seconds >= 3600):
        hours = temp1 // 3600
        temp2 = temp1 - (hours * 3600)
        if(seconds >= 60):
            minutes = temp2 // 60
            temp3 = temp2 - (minutes * 60)
            s = temp3
    else:
        hours = 0
        temp2 = temp1 - (hours * 3600)
        if(seconds >= 60):
            minutes = temp2 // 60
            temp3 = temp2 - (minutes * 60)
            s = temp3   
        else:
            minutes = 0
            s = seconds
else:
    days = 0
    temp1 = seconds - (days * seconds)
    if(seconds >= 3600):
        hours = temp1 // 3600
        temp2 = temp1 - (hours * 3600)
        if(seconds >= 60):
            minutes = temp2 // 60
            temp3 = temp2 - (minutes * 60)
            s = temp3   
    else:
        hours = 0
        temp2 = temp1 - (hours * 3600)
        if(seconds >= 60):
            minutes = temp2 // 60
            temp3 = temp2 - (minutes * 60)
            s = temp3   
        else:
            minutes = 0            
            s = seconds            
                        
print(f'Days: {days}, Hours: {hours}, Minutes: {minutes}, Seconds: {s}')    
            