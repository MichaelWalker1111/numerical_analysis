# Change the name:

Name = "Feldo"

#From file: 
# parameters_25_6.py 
# Import the function f and number of iterations a number between 2 and 20
# Also import two initial points ipt and ipt2
# You will be solving the equation f(x) = 0 by Secant method

from parameters_25_6 import f     #function
from parameters_25_6 import n     #number of iterations
from parameters_25_6 import ipt   #initial point
from parameters_25_6 import ipt2   #second initial point


#Type here your code, please use above parameters:


def secant_method(function, num_iter,init1, init2):
    p_tup = [init1,init2]
    for i in range(num_iter):
        p = p_tup[1] - function(p_tup[1])*(p_tup[1]-p_tup[0])/(function(p_tup[1])-function(p_tup[0]))
        p_tup[0] = p_tup[1]
        p_tup[1] = p
    return p_tup[1]
roo = secant_method(f,n,ipt,ipt2)









# Use file answers_25_6.txt as an output
# Just append that file!
# Feel free to change the name of variables or your output to file in a different way.
# Do not forget to include solution to part (b) and (c)


fil=open("answers_25_6.txt","a+")
for i in range(0, n):
	fil.write(Name + ": Iteration number %i yields %f \n" % (i, roo))
fil.write("-----------------------------------------------\n\n")
fil.close()