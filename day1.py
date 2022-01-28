# Read in measurements file
input_file = open("./day1_input.txt", "r")
measurements = input_file.read()

# Turn into a list
measurements_list = list(measurements.split("\n"))

# Make sure I have a list
#print(type(measurements_list))

# Set variables
i = 0
depth_increased = 0

#print(measurements_list[0])
#print(measurements_list[1])

#print(range(len(measurements_list)))
#print(range(0, (len(measurements_list)-1)))

# Count intervals where the depth increases
# need to subtract 1 from final measurement, otherwise increasing the index by 1 in the for loop causes an error
for i in range(0, (len(measurements_list)-1)):
	#print(measurements_list[i])
	#print(measurements_list[i+1])
	further = int(measurements_list[i+1])
	closer = int(measurements_list[i])
	if further > closer:
		print("Depth increased, add 1 to the tally")
		depth_increased += 1
	elif further < closer:
		print("Depth decreased, do nothing")
	else:
		print("Depths equal, do nothing")

print("\n~~~\nNumber of times depth increased: ", depth_increased)

input_file.close()


