def create_adder(x):
    def add(y):
        return(x+y)
    return(add)

add_15 = create_adder(15)

print add_15(10)

	
