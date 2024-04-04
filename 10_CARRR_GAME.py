''' car = input() 
if car == "help":
    print("Start - to start the car")
    print("Stop - to stop the car")
    print("quit - to exit the car")
else:
    print("I dont Understand!!!!!")

command = input()
if command == 'Start':
    start_car = True
elif command == 'Stop':
    stop_car = True
elif command == 'Stop':
     quit_car = True


if start_car:
    print("ready TO Go..")
elif stop_car:
    print("Car stopped")
elif quit_car:
    print("exited")   '''  



command = ''
started = False
while True:
      command = input(">").lower()
      if command == "start":
          if started:
               print("Car is already started")
          else:
               started = True
               print("Car Started....")
      elif command == "stop":
          if not started:
                print("car is already stopped")
          else:
               started = False
               print("Car Stopped..")
      elif command == "help":
          print('''
Start - to start the car)
Stop - to stop the car
quit - to exit the car
                ''')
      elif command == 'quit':
           break   
      else:
           print("Sorry, I don't Understand!!!!!")

         
               