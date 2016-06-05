import utils


l = utils.read_file('in.txt')
a = utils.circle_area(l)
utils.write_file('out.txt', a)
