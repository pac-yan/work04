from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 move: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing
See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
	file = open(fname)
	lines = file.readlines()
	for x in range(len(lines)): 
		if lines[x] == "line\n": 
			c = lines[x+1].split(" ") 
			add_edge(points, int(c[0]), int(c[1]), int(c[2]), int(c[3]), int(c[4]), int(c[5]))
		elif lines[x] == "ident\n": 
			ident(transform)
		elif lines[x] == "scale\n": 
			num = lines[x+1].split(" ")
			s = make_scale(int(num[0]), int(num[1]), int(num[2]))
			matrix_mult(s, transform)
		elif lines[x] == "move\n": 
			num = lines[x+1].split(" ")
			tr = make_translate(int(num[0]), int(num[1]), int(num[2]))
			matrix_mult(tr, transform)
		elif lines[x] == "rotate\n": 
			commands = lines[x+1].split(" ")
			if commands[0] == "x": 
				r = make_rotX(int(commands[1]))
			if commands[0] == "y": 
				r = make_rotY(int(commands[1]))
			if commands[0] == "z": 
				r = make_rotZ(int(commands[1]))
			matrix_mult(r, transform)
		elif lines[x] == "apply\n": 
			matrix_mult(transform, points)
		elif lines[x] == "display\n": 
			for x in range(len(points)): 
				for y in range(len(points[0])): 
					points[x][y] = int(points[x][y])
			clear_screen(screen)
			draw_lines(points, screen, color)
			display(screen)
		elif lines[x] == "save\n": 
			save_extension(screen, lines[x+1].strip())
		elif lines[x] == "quit\n": 
			break
