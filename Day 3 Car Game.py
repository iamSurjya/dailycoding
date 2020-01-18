#Python code to create to a simple car game.

#1. Create a menu to take input from user(Start/Stop/Quit)
#2. Depending on the input start/stop the car.
#3. Game should continue to run until the user quits

#creating menu
print('Simple Car Game')

#declaring variables
command=''
isStarted=False

while True:
    command=input('>')
    if command==1:
        if isStarted==True:
            print('Car is already running')
        else:
            isStarted=True
            print('Car Started')
    elif command==2:
        if isStarted==False:
            print('Car is already at stop')
        else:
            isStarted=False
            print('Car Stopped')
    elif command==3:
        break
    else:
        print(''' Invalid Command
Your options are:
1. Start
2. Stop
3. Quit
''')
