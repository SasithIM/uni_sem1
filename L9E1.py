import matplotlib.pyplot as plt
input_str = '''12, 5, 0.1
110, 32, 204, 124, 72, 176, 500, 80, 150, 91'''

def conv_input(input_str):
    input_list = input_str.split('\n')
    input_list[0] = list(map(int, input_list[0].split(', ')[:-1])) + [float(input_list[0].split(', ')[-1])]
    input_list[1] = sorted(list(map(int, input_list[1].split(', '))), reverse=bool(input_list[0][0]/2 < input_list[0][1]))
    return input_list

input_list = conv_input(input_str)
# print(input_list)

ratios = lambda v_in, v_out, t:( v_in / (v_out+t) - 1, v_in / (v_out-t) - 1)
r1_to_r2 = ratios(*input_list[0])
# print(r1_to_r2)

def find_r2(r1_to_r2,res_list):
    for index1 in range(len(res_list)-1,0,-1):
        for index2 in range(index1-1,-1,-1):
            if res_list[index1] / res_list[index2] >= r1_to_r2[0] and res_list[index1] / res_list[index2] <= r1_to_r2[1]:
                # print(res_list[index1], res_list[index2], res_list[index1] / res_list[index2])
                return res_list[index1], res_list[index2]
            

r1, r2 = find_r2(r1_to_r2,input_list[1])
re = lambda rl: 1 / (1+(r1*(r2+rl)/(r2*rl)))
plt.plot(range(10,1000,10),[input_list[0][0]*re(rl) for rl in range(10,1000,10)])
plt.xlabel('Resistance(ohms)')
plt.ylabel('Voltage(V)')
plt.title('Voltage vs Resistance')
plt.grid()
plt.show()
