import os
#os.system('clear')


#def nameit(firstname,lastname):
	#print("Hello " + firstname + " " + lastname)

#nameit("King", "Spirit")



#def add(x,y):
#	z = x + y
#	return z

#Outcome = add(3,6)
#print(Outcome * 10)

# Using *args functions:
#def add(*nums):
#	return sum(nums)

#print (add(10,20,30,40,50))

# Using *kwargs functions:
#def record(**data):
#	print(data)

#record(name = "Nikhili", rollno = 85, age = 20)

#def <func-name> (fargs, *args, **kwargs)
	#<statements>


def get_data(engine, *queries, **properties):
		print(engine, queries, properties)


get_data('google', 'python', 'flask', 'django', limit = 10, verbose = True)

