# import os 
# os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
import matplotlib.pyplot as plt
# from cs1033_evaluator import evaluate_lab7

MODEL_1_INPUT_FILE, MODEL_2_INPUT_FILE, MODEL_3_INPUT_FILE = 'model1.txt', 'model2.txt', 'model3.txt'
################################################################################
# Please do not edit anything above this line.


# Function to read a file and return speed list.
def get_speed(file_name):
    speed = []
################## YOUR CODE STARTS HERE. ######################################

# Read the file and get the values into the list.
    with open(file_name) as in_file:
        speed = [int(line.strip().split()[-1]) for line in in_file.readlines()]
    
################## YOUR CODE ENDS HERE. ########################################     
    return speed

# Function gets the filename and returns the speeds in metres per second format.
def convert_kmph_to_ms(filename):
################## YOUR CODE STARTS HERE. ######################################

# Read the values using get_speed function and return the converted values as a list.
   return list(map(lambda x:round(x/3.6,4), get_speed(filename)))
   
# print(convert_kmph_to_ms(MODEL_1_INPUT_FILE))

################## YOUR CODE ENDS HERE. ########################################

# Function gets the speeds as a list of i ntegers in metres per second format and returns the acceleration.
def get_acceleration(speeds):
    #Acceleration list is initialized to zero.
    #i.e. acceleration at time=0 is zero.
    acceleration = [0]
################## YOUR CODE STARTS HERE. ######################################
    #Write the code to calculate the acceleration.  
    acceleration += list(map(lambda i:round((speeds[i]-speeds[i-1])*10,2), range(1,len(speeds))))
################## YOUR CODE ENDS HERE. ########################################
    return acceleration

# print(get_acceleration(convert_kmph_to_ms(MODEL_1_INPUT_FILE)))

######## WRITE THE CODE FOR TASK 1.4 and 1.5 BELOW #############################

        # Use MODEL_1_INPUT_FILE, MODEL_2_INPUT_FILE, MODEL_3_INPUT_FILE variable 
        # names instead of 'model1.txt', 'model2.txt', 'model3.txt' to read files
output_accl = []
for i in range(1,4):
    accelerations_list = get_acceleration(convert_kmph_to_ms(eval(f'MODEL_{i}_INPUT_FILE')))
    plt.plot(list(i/10 for i in range(0,11)),accelerations_list,label=f'model_{i}')
    output_accl.append(max(accelerations_list))
    
with open('max_acceleration.txt','w') as out_file:
    out_file.write('\n'.join([f'model{i+1} {accl}' for i,accl in enumerate(output_accl)]))
    
# Plotting the lines with different styles
# plt.plot(time, model_acceleration[0] , label='model_1')
        
# Adding labels and title
plt.xlabel('Time(s)')
plt.ylabel('Acceleration(ms-2)')
plt.title('Acceleration Vs Time')
plt.legend(['model_1','model_2','model_3'])
plt.show()

################################################################################
# Please do not edit anything below this line.
# evaluate_lab7()

##################### End of the programme #####################################