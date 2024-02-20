# Change the name:

Name = "Feldo"

#From file: 
# parameters_26_8.py 
# Import the function f and number of iterations a number between 2 and 20
# Also import initial point ipt
# You will be solving the equation f(x) = x by Aitken and Steffensen's method

from parameters_26_8 import f     #function
from parameters_26_8 import n     #number of iterations
from parameters_26_8 import ipt   #initial point

#Type here your code, please use above parameters:
def fixed_pt(function, num_iter, int_pt):
    p = int_pt
    for i in range(num_iter):
        p = function(p)
    return p

roo1 = fixed_pt(f, n, ipt)

def acc_fixed_pt(function, num_iter, int_pt):
    p_tup = [int_pt,function(int_pt), function(function(int_pt))]
    for i in range(num_iter):
        p_tup[0] = p_tup[1]
        p_tup[1] = p_tup[2]
        p_tup[2] = function(p_tup[2])
    return p_tup[2] - (p_tup[2]-p_tup[1])**2/(p_tup[2]-2*p_tup[1]+p_tup[0])

roo2 = acc_fixed_pt(f,n, ipt)
 
def steffenssen(function, num_iter,init):
    p_tup = [init,function(init), function(function(init))]
    for i in range(num_iter):
        p = p_tup[2] - (p_tup[2]-p_tup[1])**2/(p_tup[2]-2*p_tup[1]+p_tup[0])
        p_tup = [p,function(p), function(function(p))]
    return p_tup[0]

roo3 = steffenssen(f,n,ipt)








# Use file answers_26_8.txt as an output
# Just append that file!
# Feel free to change the name of variables or your output to file in a different way.
# Do not forget to include answers to given questions - reduction of asymptotic 
# error constant and order of convergence of Steffensen method


fil=open("answers_26_8.txt","a+")
for i in range(0, n):
	fil.write(Name + ": Fixed point iteration number %i yields %f \n" % (i, roo1))
for i in range(0, n):
	fil.write(Name + ": Accelerated method iteration number %i yields %f \n" % (i, roo2))
for i in range(0, n):
	fil.write(Name + ": Steffensen's method iteration number %i yields %f \n" % (i, roo3))
fil.write("-----------------------------------------------\n\n")
fil.close()