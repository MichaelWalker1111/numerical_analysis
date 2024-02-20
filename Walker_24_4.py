# Change the name:

Name = "Feldo"

#From file: 
# parameters_24_4.py 
# Import the function f and number of iterations a number between 2 and 20
# Also import initial point ipt
# You will be solving the equation f(x) = 0 by Newton's method

from parameters_24_4 import f     #function
from parameters_24_4 import g     #derivative of f
from parameters_24_4 import n     #number of iterations
from parameters_24_4 import ipt   #initial point

#Type here your code, please use above parameters:


def newtons_method(function, derivative, num_iter, init):
    p = init
    for i in range(num_iter):
        p = p - (function(p))/derivative(p)
    return p



roo = newtons_method(f,g,n,ipt)





# Use file answers_24_4.txt as an output
# Just append that file!
# Feel free to change the name of variables or your output to file in a different way.
# Do not forget to include solution to part (2) and (3)


fil=open("answers_24_4.txt","a+")
for i in range(0, n):
	fil.write(Name + ": Iteration number %i yields %f \n" % (i, roo))
fil.write("-----------------------------------------------\n\n")
fil.close()