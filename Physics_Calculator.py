#Name: Oladun Oladiran, Email: ooladiran@uncc.edu

print("Welcome to online Physics Calculator")
print("There are five calculators in this program. please, make your selection")

def hooke_law(displacement, force_constant): # define hooke's law function, with displacement and force constant as the parameters       
    f = -(displacement*force_constant)  # Force in springs is -K* displacement
    return f


def potential_energy(Mass, Height, Grav_Acceleration):   #  define potential energy function which takes mass, height and gravittational acel. as parameters
    P_E = Mass *Height * Grav_Acceleration  #potential energy is mgh
    return P_E


def pressure(force, length):  # define pressure function, force and length as parameters
    p=force/(length)**2         #pressure = force/area
    return p


 # other functions to use the pressures function
def pressure_convert():         # let user see what options of conversions are available
    print("1. pascal to psi")
    print("2. pascal to torr")
    print("3. pascal to bar")
    print("4. pascal to atm")
    print("5. pascal to mmHg")

# define all to convert pascal to other unit to reduce redundancy in the main 
def pascal_to_psi(p):            
    psi_c=p*0.000145038
    return psi_c

def pascal_to_torr(p):
    torr_c=p*0.00750062 
    return torr_c 

def pascal_to_bar(p):
    bar_c=p*(10**-5)
    return bar_c 

def pascal_to_atm(p):
    atm_c=p*9.869*10**-6
    return atm_c



def convert_to_C(temp): #define temperature conversion Fahrenheight to celcius
        tempc=(temp-32)*(5/9)
        return tempc

def convert_to_f(temp): # celcius to Fahrenheight 
        return -1


def before_crash(Car_speed, your_weight, time_of_collision): #define car crash force
    impact=Car_speed*your_weight/time_of_collision
    return impact




def main():  # This is the main
    while True:          
        try:        # Handle exceptions
            calculator_choice = int(input("\n\tSelect 1 for hooke's law\n\tselect 2 for potential energy\n\tselect 3 for pressure\
    \n\tselect 4 for temperature\n\tselect 5 for car crash: ")) 
        except Exception:
            print("You must enter a value to proceed")
        else:
      
            if  calculator_choice  >5 or  calculator_choice  < 0:  # prevent negative and invalid selection
                print("That was an invalid selection!")
                
          
            else:   
                if calculator_choice == 1:  # if a user chose 1, they want to perform hooke'law calculation
                    print("I see you would to perform calculation on Hooke's Law!")
                    print("The unit of Force is Newton(N), the force_constant is measured in Newton/Meter.Thus the dsiplacement must be in meters.You can specify your dsiplacement unit and we can convert meters ")
                
        try:                    #validate user input 
            displacement_unit=int(input("What's you displacement unit\n\t1.meters(m)\n\t2.millimeters(mm)\
            \n\t3.inches\n\t4.yard\n\t5.feet: "))
        except Exception:
            print("You must enter a value to proceed")
            
        else:
            if  displacement_unit  > 5 or  displacement_unit < 0:  # prevent negative and invalid selection
                print("That was an invalid selection!")
                

            else:
                try:        #validate user input                       
                    displacement = float(input("Input Displacement value: "))
                except Exception:
                    print("You must enter a value to proceed")
                    

            try:            #validate user input
                force_constant = float(input("Specify the force constant: "))
            except Exception:
                print("You must enter a value to proceed")
                break

            else:
                if displacement_unit == 1: # if a user chose 1, they prefer to work in meters
                    print("You chose meters as your displacement unit")
                    displacement=displacement
                    choice=hooke_law(displacement, force_constant) # call the funtion and assign to variable
                    print("The force in the spring is {:.2f}J".format(choice))  # print output with string format


                elif displacement_unit == 2:  # if a user chose 2, they prefer to work in millimeters
                    print("You chose millimeters as your displacement unit")
                    displacement=displacement/1000
                    choice=hooke_law(displacement, force_constant)  # call the funtion and assign to variable
                    print("The force in the spring is {:.2f}J".format(choice)) # print output with string format
        
            # the usage is the same across the remmaing elif statements
                
                elif displacement_unit == 3:
                    print("You chose inches as your displacement unit")
                    displacement=displacement*0.0254
                    choice=hooke_law(displacement, force_constant)
                    print("The force in the spring is {:.2f}J".format(choice))
                
                
                elif displacement_unit == 4:
                    print("You chose yard as your displacement unit")
                    displacement=displacement*0.9144
                    choice=hooke_law(displacement, force_constant)
                    print("The force in the spring is {:.2f}J".format(choice))
            
            
                elif displacement_unit == 5:
                    print("You chose feet as your displacement unit")
                    displacement=displacement*0.3048
                    choice=hooke_law(displacement, force_constant)
                    print("The force in the spring is {:.2f}J".format(choice))
                
                else:
                    print("You have made a wrong selection, you must choose values between 1 and 5")
                    break
            

        if calculator_choice ==2:
            print("I see you would to perform calculation potential energy!")
            print("The unit of Potential energy is Joule aka(Newton.meter) gravitational field strenght (g) is 9.80665m/s^2.\
            Height is measured in  meters(m).Mass is measured in kilograms (kg) ")


            try:                    #validate user input 
                Height_unit=int(input("What's height unit\n\t1.meters(m)\n\t2.millimeters(mm)\
                \n\t3.inches\n\t4.yard\n\t5.feet: "))
            except Exception:
                print("You must enter a value to proceed")
                break

            else:
                try:        #validate user input                       
                    Height = float(input("Input Height value: "))
                except Exception:
                    print("You must enter a value to proceed")
                    break

            try:                    #validate user input 
                mass_unit=int(input("What's  the mass unit\n\t1.kilogram(kg)\n\t2.milligram(mg)\
                \n\t3.grams(g)\n\t4.ounces(oz)\n\t5.pounds(lb): "))
            except Exception:
                print("You must enter a value to proceed")
                #break


            else:
                try:            #validate user input
                    Mass = float(input("Specify the mass of the object: "))
                except Exception:
                    print("You must enter a value to proceed")
                    #break
                else:


                    if Height_unit == 1 and mass_unit ==1: # if a user chose 1, they prefer to work in meters
                        print("You chose meter as your height unit and kilogram as your mass unit")
                        Height=Height
                        Mass = Mass
                        Grav_Acceleration=9.800665
                        choice=potential_energy(Mass, Height, Grav_Acceleration) # call the funtion and assign to variable
                        print("The potential energy is {:.2f}J".format(choice))  # print output with string format


                        
                    elif Height_unit == 2 and mass_unit == 2:  # if a user chose 2, they prefer to work in millimeters
                        print("You chose millimeters(mm) as your height unit and mass is in milligram(mg) ")
                        Height=Height/1000
                        Mass = Mass/1000000
                        Grav_Acceleration=9.800665
                        choice=potential_energy(Mass, Height, Grav_Acceleration)  # call the funtion and assign to variable
                        print("The potential energy is {:.2f}N".format(choice))  # print output with string format
                # the usage is the same across the remmaing elif statements


                    elif Height_unit == 3 and mass_unit == 3:  # if a user chose 2, they prefer to work in millimeters
                        print("You chose inches as your height unit and mass is in gram(g) ")
                        Height=Height*0.0254
                        Mass = Mass/1000
                        Grav_Acceleration=9.800665
                        choice=potential_energy(Mass, Height, Grav_Acceleration)  # call the funtion and assign to variable
                        print("The potential energy is {:.2f}N".format(choice)) 

                    elif Height_unit == 4 and mass_unit == 4:  # if a user chose 2, they prefer to work in millimeters
                        print("You chose yard(y) as your height unit and mass is in ounces(oz) ")
                        Height=Height*0.9144
                        Mass = Mass*0.02835
                        Grav_Acceleration=9.800665
                        choice=potential_energy(Mass, Height, Grav_Acceleration)  # call the funtion and assign to variable
                        print("The potential energy is {:.2f}N".format(choice)) 


                    elif Height_unit == 5 and mass_unit == 5:  # if a user chose 2, they prefer to work in millimeters
                        print("You chose feet(f) as your height unit and mass is in pounds(lb) ")
                        Height=Height*0.3048
                        Mass = Mass*0.4536
                        Grav_Acceleration=9.800665
                        choice=potential_energy(Mass, Height, Grav_Acceleration)  # call the funtion and assign to variable
                        print("The potential energy is {:.2f}N".format(choice)) 


                    else:
                        print("You have made a wrong selection, you must choose values between 1 and 5")
                        #break
        if calculator_choice ==3:
            print("I see you would to perform calculation on pressure!")
            print("The unit of Pressure varies, e.g pascals,psi, bar and so on. You will specify your unit")
            
            try:                    #validate user input 
                force_unit=int(input("specify the unit of force\n\t1.newton(N)\n\t2.kilonewton(kN)\
                \n\t3.meganewton(mN)\n\t4.pound-force(lbf): "))
            except Exception:
                print("You must enter a value to proceed")
                #break

            else:
                try:        #validate user input                       
                    force = float(input("Input Force value: "))
                except Exception:
                    print("You must enter a value to proceed")
                    #break
            try:                    #validate user input 
                length_unit=int(input("specify the unit of distance\n\t1.meter(m)\n\t2.mile(mi))\
                \n\t3.Kilometer(km)\n\t4.feet(ft): "))
            except Exception:
                print("You must enter a value to proceed")
                #break
            else:
                try:            #validate user input
                    length= float(input("Specify the length: "))
                except Exception:
                    print("You must enter a value to proceed")
                    #break

            
                if force_unit == 1 and length_unit == 1: # if a user chose 1, they prefer to work in meters
                    print("You chose newton(N) as your force unit and area in meter**2")
                    force=force
                    length=length
                    choice=pressure(force, length) # call the funtion and assign to variable
                    print("The presure is {:.2f}pa".format(choice))  # print output with string format
                    

                elif force_unit == 2 and length_unit == 2:  # if a user chose 2, they prefer to work in millimeters
                    print("You chose Kilonewton(kN) as your force unit and length in miles(mi) ")
                    force=force*1000
                    length=length*1609.34
                    choice=pressure(force, length) # call the funtion and assign to variable
                    print("The pressure is {:.2f}pa".format(choice))  # print output with string format
            
            # the usage is the same across the remmaing elif statements
                
                elif force_unit == 3 and length_unit == 3:  # if a user chose 2, they prefer to work in millimeters
                    print("You chose meganewton(mN) as your force unit and area in kilometer(km) ")
                    force=force*(10**6)
                    length=length*1000
                    choice=pressure(force, length) # call the funtion and assign to variable
                    print("The  pressure is {:.2f}pa".format(choice))  # print output with string format
                
                elif force_unit == 4 and length_unit == 4:  # if a user chose 2, they prefer to work in millimeters
                    print("You chose pound-force(lb-f) as your force unit and length in feet ")
                    force=force*4.44822
                    length=length*0.3048
                    choice=pressure(force, length) # call the funtion and assign to variable
                    print("The pressure is {:.2f}pa".format(choice))  # print output with string format
                
                
        
                else:
                    print("You have made a wrong selection, note;if you chose 1 for force, you must also choose 1 for length")
                    
            press_convert_choice=input("Do you want to convert the pressure to another unit? Yes or No ").lower()
            if press_convert_choice == "yes":
                pressure_convert()
                user_convert_choice=int(input("which conversion do you want?: "))
                if user_convert_choice == 1:
                    choice2=pascal_to_psi(choice)
                    
                    print("The pressure is {:.4f}psi".format(choice2))
                elif user_convert_choice == 2:
                    choice2=pascal_to_torr(choice)

                    print("The pressure is {:.4f}torr".format(choice2))
                elif user_convert_choice == 3:
                    choice2=pascal_to_bar(choice)
                    print("The pressure is {:.4f}bar".format(choice2))
                elif user_convert_choice == 4:
                    choice2=pascal_to_atm(choice)
                    print("The pressure is {:.4f}atm".format(choice2))
                else:
                    print("You didn't make a correct selection")

            else:
                print("You have either enter 'no' or you enter something else!")   # if a user enter anything other than yes exit the loop
                print("...exiting")
               
            

        if calculator_choice ==4:
            print("I see you would to perform temperature calculation!")
            print("Do you want to convert to celsious or Farehnheit")
            f_or_c=input("\n\t1.to convert farrehheiht\n\t2.to convert to celcius: ")
            
            if f_or_c =="1":
                temp_c =int(input("What is the temp  in c? "))
                temp_f=convert_to_f(temp_c)
                print("The converted temp is " + str(temp_f))
            elif  f_or_c =="2": 
                
                tempf =int(input("What is the temp  in f? "))      
                tempC = convert_to_C(tempf)
                print("The converted temp is " + str(tempC))
            else:
                break


        if calculator_choice ==5:
            
            print("I see you would like to estimate car crash force!")
        
            #seat_belt=input("Did the victim use seat belt? Yes or No: ").lower()
            car_speed=int(input("What was the car speed in meter per second (m/s): "))
            your_weight=float(input("What is your weight in  kilogram (kg)? "))
            time_of_collision = float(input("How long was the collision in second (s)? "))
            force=before_crash(car_speed, your_weight, time_of_collision)
            print("The force of impact is {:.2f}Newton".format(force))


            seat_belt=input("Did you use your seat belt?:Yes or No:  ").lower()
            if seat_belt == "no" and force > 1000:
                print("The crash may cause severy injury or death")
            elif seat_belt == "yes" and force > 1000:
                print("The crash may be severe but you may survive")
            elif seat_belt == "yes" and force < 1000:
                print("You may likely survive the crash")
            else:
                break
    
    


            


                
                




if __name__ == "__main__":
    main()

    






