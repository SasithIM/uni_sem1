# import os 
# os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
import matplotlib.pyplot as plt
# from cs1033_evaluator import evaluate_lab7

MODEL_1_INPUT_FILE, MODEL_2_INPUT_FILE, MODEL_3_INPUT_FILE = input().split()
################################################################################
# Please do not edit anything above this line.


# Function to read a file and return speed list.
def get_speed(file_name):
    speed = []
################## YOUR CODE STARTS HERE. ######################################
# Read the file and get the values into the list.
    
    for i in file_name:
        data = i.split()
        speed.append(int(data[1]))


################## YOUR CODE ENDS HERE. ########################################     
    return speed


# Function gets the filename and returns the speeds in metres per second format.
def convert_kmph_to_ms(file_name):
################## YOUR CODE STARTS HERE. ######################################
# Read the values using get_speed function and return the converted values as a list.
   
    for i in range(len(file_name)):
       file_name[i] = round((file_name[i]*5/18),4)
       
    return file_name
       
   
################## YOUR CODE ENDS HERE. ########################################


# Function gets the speeds as a list of integers in metres per second format and returns the acceleration.
def get_acceleration(speeds):
    #Acceleration list is initialized to zero.
    #i.e. acceleration at time=0 is zero.
    acceleration = [0]
################## YOUR CODE STARTS HERE. ######################################
    #Write the code to calculate the acceleration.
 
    for i in range(len(speeds)-1):
        acc =round(((speeds[i+1]-speeds[i] )/ 0.1),2)
        acceleration.append(acc)
        

    
    
################## YOUR CODE ENDS HERE. ########################################
    return acceleration


######## WRITE THE CODE FOR TASK 1.4 and 1.5 BELOW #############################
list_txt_files = [MODEL_1_INPUT_FILE, MODEL_2_INPUT_FILE, MODEL_3_INPUT_FILE]

# Adding labels and title
plt.xlabel('Time(s)')
plt.ylabel('Acceleration(ms-2)')
plt.title('Acceleration Vs Time')
time = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
    

for i in range(len(list_txt_files)):
    a = list(open(list_txt_files[i],'r'))
    b = get_speed(a)
    c = convert_kmph_to_ms(b)
    d = get_acceleration(c)
    max_acc = max(d)
    output_ith = f"model{i+1} {max_acc}\n"

    with open("max_acceleration.txt","a") as output:
        output.write(output_ith)
        
    
    plt.plot(time,d)
    
plt.legend(['model_1','model_2','model_3'])   
plt.show()
    
        # Use MODEL_1_INPUT_FILE, MODEL_2_INPUT_FILE, MODEL_3_INPUT_FILE variable 
        # names instead of 'model1.txt', 'model2.txt', 'model3.txt' to read files
        
# Plotting the lines with different styles
# plt.plot(time, model_acceleration[0] , label='model_1')      
        


################################################################################
# Please do not edit anything below this line.
# evaluate_lab7()

##################### End of the programme #####################################