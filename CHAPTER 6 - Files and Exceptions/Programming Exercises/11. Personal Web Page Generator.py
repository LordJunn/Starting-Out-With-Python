"""
Write a program that asks the user for his or her name, then asks the user to enter a sen-
tence that describes himself or herself. Here is an example of the program’s screen:
Enter your name: Julie Taylor [Enter]
Describe yourself: I am a computer science major, a member of the
Jazz club, and I hope to work as a mobile app developer after I
graduate. [Enter]
Once the user has entered the requested input, the program should create an HTML file,
containing the input, for a simple Web page. Here is an example of the HTML content,
using the sample input previously shown:
<html>
<head>
</head>
<body>
<center>
<h1>Julie Taylor</h1>
</center>
<hr />
I am a computer science major, a member of the Jazz club,
and I hope to work as a mobile app developer after I graduate.
<hr />
</body>
</html>
"""

def main():
    file = input('Name of file to write into? ')
    infile = open(file, 'w')
    name = input('Enter your name: ')
    desc = input('Describe yourself: ')
    infile.write(html(name, desc))
    infile.close()
    
def html(name, desc):
    return(f"""
<html>
    <head>
    </head>
    <body>
        <center>
            <h1>{name}</h1>
        </center>
        <hr>
        {desc}
        <hr/>
    </body>
</html>          
    """)
    
main()
    