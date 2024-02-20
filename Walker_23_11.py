# Change the name:

Name = "Feldo"

#From file: 
# parameters_23_11.py 
# Import the function f and precision
# Also import the initial point
# You will look for the fixed point of f(x) = x

from parameters_23_11 import f     #function
from parameters_23_11 import pr     #precision goal
from parameters_23_11 import ipt   #initial point

#Type here your code, please use above parameters:
def fixed_pt(function, precision, int_pt):
    p = int_pt
    prime = (function(function(p))-function(p))/(function(p)-p)
    condition = abs(prime/(prime-1))*abs((function(function(p))-function(p)))
    while condition > precision:
        p = function(p)
        prime = (function(function(p))-function(p))/(function(p)-p)
        condition = abs(prime/(prime-1))*abs((function(function(p))-function(p)))
    return p

roo = fixed_pt(f, pr, ipt)









# Use file answers_23_11.txt as an output
# Just append that file!
# Feel free to change the name of variables or your output to file in a different way.


fil=open("answers_23_11.txt","a+")
fil.write(Name + ": The fixed point is %0.12f within precision %0.12f \n" % (roo, pr))
fil.write("-----------------------------------------------\n\n")
fil.close()