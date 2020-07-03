###########################
def fibBinet(n):
    phi = (1 + 5**0.5)/2.0
    return int(round((phi**n - (1-phi)**n) / 5**0.5))
print ("Let's compute the first few terms in the Fibonacci sequence.")

n = 20 # How many terms shall we include?

###################################
# 3. Using Binet's formula
########
for i in range(n + 1):

    print (fibBinet(i))
