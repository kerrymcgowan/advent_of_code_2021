# Read in input file
input_file = open("./day2_input.txt", "r")
submarine_path = input_file.read()

# Check variable type
#print(type(submarine_path))

# Convert to a list, needs to be a list for the for loop
path_list = submarine_path.split("\n")

# Check variable type
#print(type(path_list))

# Print list
#print(path_list)

# Set starting variables
horizontal_position = 0
down_distance = 0
up_distance = 0

# Check range
#print(range(len(path_list)))
#for i in path_list:
#	print(i.split(' '[0]))

for i in path_list:
	#print(i)

	# Moving forward
	if i[0:7] == "forward":
		#print(i[0:7])
		#print(i[8])
		horizontal_position += int(i[8])
		#print(forward_distance)

	# Moving down
	elif i[0:4] == "down":
		#print(i[0:4])
		#print(i[5])
		down_distance += int(i[5])
		#print(down_distance)

	# Moving up
	elif i[0:2] == "up":
		#print(i[0:2])
		#print(i[3])
		up_distance += int(i[3])
		#print(up_distance)

# Calculate final depth
depth = down_distance - up_distance
#print(depth)

# Calculate final horizontal position multiplied by final depth
final_position = horizontal_position * depth
print(final_position)

# Close the input file
input_file.close()