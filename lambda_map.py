orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
	       ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "Einführung in Python3, Bernd Klein", 	3, 24.99]]

fn1 = lambda x : (x[0],x[2]*x[3])
temp = tuple(map(fn1,orders))

for i in temp:
    print(i)
    
final = map((lambda x : x if x[1]>=100 else (x[0],x[1]+10)),temp)

print("Final")
for i in final:
    print(i)
