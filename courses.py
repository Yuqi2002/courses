# courses.py
# Yuqi Zhou
# COP 2500
# 10/20/21

# define class and schedule
Class=()
# list to store user input in
schedule=[]
# while statement that repeatedly prompts user input
while len(schedule)!=5:
    while len(schedule)<5:
        Class=input("what courses would you like to take?\n")
        # splits input into parts based on commas and appends each 
        if "," in Class:
            commas=Class.count(",")
            entries=Class.split(",")
            for c in entries:
                schedule.append(c)
            print(schedule)
             
         
        else:
            schedule.append(Class)
        print("you are currently taking these courses\n", schedule)
        
    while len(schedule)>5:
        Class=input("you are taking too many classes, which would you like to drop?\n")
        if "," in Class:
            # splits input into parts based on commas and appends each
            commas=Class.count(",")
            plit(",")
            for c in entries:
                schedule.remove(c)
            print(schedule)
        else:
            schedule.remove(Class)
        print("you are currently taking these courses\n", schedule)

print("done! here is your completed schedule\n",schedule)
     

     
        

