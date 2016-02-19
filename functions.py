#Q1

hours = int(raw_input("Enter number of hours (integer): "))
minutes = int(raw_input("Enter number of minutes (integer): "))
seconds = int(raw_input("Enter number of seconds (integer): "))

def convert_to_seconds(hours, minutes, seconds):
	convert_minutes = minutes * 60         #converts minutes to seconds
	convert_hours = hours * 60 * 60        #converts hours to seconds
	total_seconds = convert_minutes + convert_hours + seconds  #sums all seconds
	return total_seconds

total_seconds = convert_to_seconds(hours, minutes, seconds)

print "%i hours, %i minutes and %i seconds is equivalent to %i seconds" % (hours, minutes, seconds, total_seconds)


#Q2

feet = int(raw_input("Enter number of feet (integer): "))
inches = int(raw_input("Enter number of inches (integer): "))

def convert_to_inches(feet, inches):
	convert_feet = feet * 12        #converts feet to inches
	total_inches = convert_feet + inches #sums all inches
	return total_inches

total_inches = convert_to_inches(feet, inches)

print "%i feet, %i inches is equivalent to %i inches" % (feet, inches, total_inches)