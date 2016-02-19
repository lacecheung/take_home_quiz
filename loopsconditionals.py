#Q1: Draw square of int x int size

input = int(raw_input("How big do you want the square: ")) 

def draw_square(input):
	#Number of rows in the square
	for num_rows in range(0, input):     
		# Number of asterisks in each row
		for num_col in range(0, input):   
			# References last asterisk in each row
			if num_col == input - 1:  
			# Start a new line after the last asterisk in each row   
				print "*"       
			# if not the last asterisk in the row, continue to print on same line         
			else: print "*",             

draw_square(input)



#Q2: Draw checkerboard  of int x int size, with alternating X's and O's

# same approch as q1, but:
# for even rows: even spaces should be X's, odd spaces O's
# for odd rows: even spaces should be O's, odd spaces X's


checkerboard_size = int(raw_input("How big do you want the checkerboard? ")) 


def draw_checkerboard(checkerboard_size):
	for num_rows in range(0, checkerboard_size):    
		if num_rows%2 == 0:
			for num_col in range(0, checkerboard_size):   
				if num_col == checkerboard_size - 1:    
					if num_col%2 == 0:
						print "O "
					else: print "X "       
				else: 
					if num_col%2 == 0:
						print "O ",
					else: print "X ",           
		else:
			for num_col in range(0, checkerboard_size):   
				if num_col == checkerboard_size - 1:    
					if num_col%2 == 0:
						print "X "
					else: print "O "       
				else: 
					if num_col%2 == 0:
						print "X ",
					else: print "O ", 


draw_checkerboard(checkerboard_size)