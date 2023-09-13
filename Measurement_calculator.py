def check(number_mode):
    return number_mode not in ['0','1']
#Notifications
print("===== Measurement stats calculator =====")
print("===== Make sure the units in measurement results are all the same =====\n")

#Input handling
input_mode = input("Choose input mode (Type 0 to choose vertical mode, 1 to type horizontal mode): ")
while check(input_mode):
    input_mode = input("Choose input mode (Type 0 to choose vertical mode, 1 to type horizontal mode): ")
input_mode = int(input_mode)
if input_mode:
    #Input handling
    m_list = [float(i) for i in input("Type measurment results: ").split()]
else:
    n = int(input("How many times have you measure: "))
    m_list = [float(input(f"Measurement result #{i+1}: ")) for i in range(n)]
smallest_unit = float(input("Write the smallest unit (numbers) in your measurment: "))
mode = input("Choose the mode (Type 1 to divide the smallest unit by 2. Type 0 to not divide): \n")
while check(mode):
    mode = input("Choose the mode (Type 1 to divide the smallest unit by 2. Type 0 to not divide): \n")
mode = int(mode)

#Calculation
avg = sum(m_list)/len(m_list)
diff_avg = [abs(avg-i) for i in m_list]
avg_diff_avg = sum(diff_avg)/len(m_list)
if mode: absolute_error = avg_diff_avg + smallest_unit/2
else: absolute_error = avg_diff_avg + smallest_unit
accurarcy = 100-absolute_error/avg*100
    
#Output handling
print("===== RESULT =====\n")
print(f"Average: {avg}")
#print(f"Diff_avg: {diff_avg}")
#print(f"Avg_diff_avg: {avg_diff_avg}")
#print(f"Absolute_error{absolute_error}")
print(f"Accurarcy: {accurarcy}%")
print(f"Offset: ±{absolute_error}\n")
print(f"x = {avg}±{absolute_error}")
