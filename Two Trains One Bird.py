# This function will find the time a bird flies at Vb km/h between a train going at Vt km/h
# and a wall. The train and bird start at a distance D from the wall and go in the direction
# of the wall. 

# This is a modified (though equivalent) version of problem of the "two trains one bird" problem. 


#      Bird->>----------------------------------------|Wall
#Train->----------------------------------------------|Wall

T = [0] # will keep all the times in this list
D = 100. # distance the train and bird start from the wall
Vt = 50. # speed of train
Vb = 1000. # speed of bird

N = 150 # Number of iterations

for i in xrange(1,N+1):
    if i %2== 0:
        t = (D - sum(T)*Vt)/(Vb+Vt)
    else:
        t = (D - sum(T)*Vt)/Vb
    T.append(t)

print sum(T)


# The iterative version of the above is:

#T_(i+1) = T_i + (D - T_i * Vt)/(Vb + Vt*([i+1]%2)) 
