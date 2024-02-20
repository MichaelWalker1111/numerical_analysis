# Change the name:

Name = "Feldo"

#From file: 
# parameters_23_7.py 
# Import the function f and number of iterations a number between 2 and 20
# Also import the initial point ipt
# You will be solving the equation f(x) = x

from parameters_23_7 import f     #function
from parameters_23_7 import n     #number of iterations
from parameters_23_7 import ipt   #initial point

#Type here your code, please use above parameters:
def fixed_pt(function, num_iter, int_pt):
    p = int_pt
    for i in range(num_iter):
        p = function(p)
    return p


roo = fixed_pt(f,n,ipt)







# Use file answers_22_5.txt as an output
# Just append that file!
# Feel free to change the name of variables or your output to file in a different way.
# Do not forget to provide a short explanation for the order of convergence 

fil=open("answers_23_7.txt","a+")
for i in range(0, n):
	fil.write(Name + ": Iteration number %i yields %f \n" % (i, roo))
fil.write("Observed order of convergence is: PROVIDE YOUR ANSWER")
fil.write("-----------------------------------------------\n\n")
fil.close()