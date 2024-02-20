# Change the name:

Name = "Feldo"

#From file: 
# parameters_24_14.py 
# Import the function f and precision -- function f won't be changed in testing
# You will look for ALL solutions of f(x) = 0

from parameters_24_14 import f     #function
from parameters_24_14 import g     #derivative of f
from parameters_24_14 import pr     #precision goal

#Type here your code, please use above parameters:

def newtons_method(function, derivative, prec, init):
    p = init
    p_tup = [p, p - (function(p))/derivative(p)]
    condition = abs(p_tup[0]-p_tup[1])
    while condition > prec:
        p = p - (function(p))/derivative(p)
        p_tup[0] = p
        p_tup[1] = p - (function(p))/derivative(p)
        condition = abs(p_tup[0]-p_tup[1])
    return p

roo1 = newtons_method(f,g,pr,1)

roo2 = newtons_method(f,g,pr,-1)








# Use file answers_24_14.txt as an output
# Just append that file!
# Feel free to change the name of variables or your output to file in a different way.


fil=open("answers_24_14.txt","a+")
fil.write(Name + ": The first root is %0.12f within precision %0.12f \n" % (roo1, pr))
fil.write(Name + ": The second root is %0.12f within precision %0.12f \n" % (roo2, pr))
fil.write("-----------------------------------------------\n\n")
fil.close()