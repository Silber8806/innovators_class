prompt="""
Alright, let's talk about parameters. 

parameters are the magic of functions.  They 
add an extra level of flexibility that make 
them signicantly more useful than while or
for loops.

	def <name>(<parameters>):
		<code>
		return <object>

What is <parameters> in this case?  <parameters>
is a list of temporary variables, which are given
values during the function call.  We will show some
examples...
"""

raw_input(prompt)

def i_square_you(number):
	return number ** 2

def i_repeat_you_five_times(string_value):
	string_val = (string_value + " ") * 5
	return string_val 

print(i_square_you(5))
print(i_square_you(10))
print(i_square_you(12))
print(i_repeat_you_five_times("five"))
print(i_repeat_you_five_times("four"))

prompt="""
Our first examples are functions with a single
variable.  In the above case, we can pass in
a temporary variable, which is used in the body
of the <code>.  Notice how when you change
the value in the function call, it translates 
into a difference in how the code functions!
"""

raw_input(prompt)

def i_raise_you_to_a_power(number,power):
	return number ** power

print(i_raise_you_to_a_power(3,3))
print(i_raise_you_to_a_power(5,5))

def repeat_n_times(string_value, times):
	return string_value * times

print(repeat_n_times("many", 1000))
print(repeat_n_times("some?", 5))

prompt="""
We don't have to limit ourselves to a single
variable.  We can have many parameters.

The important thing to remember is that
the order of the variable names applies 
to the order of the values as well.
"""

raw_input(prompt)

def online_transaction(sale_type):
	if (sale_type == "first"):
		print("This is your first transaction!")
	elif (sale_type == "second"):
		print("This is your second transaction!")
	elif (sale_type == "re-occurring"):
		print("re-occurring transaction")
	return 0

online_transaction("first")
online_transaction("first")
online_transaction("first")
online_transaction("second")
online_transaction("first")
online_transaction("first")
online_transaction("first")

print("I'm getting tired of typing first!")

def online_transaction(sale_type="first"):
	if (sale_type == "first"):
		print("This is your first transaction!")
	elif (sale_type == "second"):
		print("This is your second transaction!")
	elif (sale_type == "re-occurring"):
		print("re-occurring transaction")
	return 0


online_transaction()
online_transaction()
online_transaction()
online_transaction("second")
online_transaction()
online_transaction()
online_transaction()
online_transaction("re-occurring")

prompt="""
What if a value of a parameter is really common.
It would be a pain to type it out every time.
The way we handle this is by defining a default 
parameter...
"""

raw_input(prompt)

def process_all_transactions(one,two,three,four,five,six,seven,eight,nine,ten):
	print(one,two,three,four,five,six,seven,eight,nine,ten)
	return "this is annoying too!"

print(process_all_transactions(1,2,3,4,5,6,7,8,9,10))

def process_all_transactions(one,two,three):
	print(one,two,three)
	return "this is annoying too!"

print(process_all_transactions(1,2,3))
print("what if we dont' need to use all parameters or we want more than 10?")

def process_all_transactions(*transactions):
	return " ".join([str(t) for t in transactions])

print(process_all_transactions(1,2,3,4,5,6,7,8,9,10))
print(process_all_transactions(1,2,3))


prompt="""
One major problem many new programmers face is designing functions when the number
of parameters is uncertain.  We can use the:

	*list

notation to treat all values passed into a function as a list.
"""

raw_input(prompt)


def process_healthcare_records(**insurance):
	if 'medicare' in insurance:
		print("we don't do medicare")
	else:
		for k,v in insurance.iteritems():
			print("processing:")
			print(k,v)
	return 0

process_healthcare_records(aetna="accept",harvard_pilgrim="accept",tufts="reject")

prompt="""
We can also take a set of key, value pairs using **kwargs argument.  In the example,
we have a bunch of key value pairs in the form of insurance_type and if they are 
accpeted.
"""

raw_input(prompt)

def process_healthcare_records(inspect=10, *insurance):
	for l in range(1,len(insurance)+1):
		if l % inspect == 0:
			print("Inspecting: %s record" % str(l))
			print(insurance[l-1])
	return 0

process_healthcare_records(2,"aetna","tufts","medicare","john hopkins")
print

def validate_is_health_insurance(*valid,**insurance):
	print("checking if valid...")
	for insure in insurance:
		if insure in valid:
			print(insure)
	return 0

validate_is_health_insurance("tufts","aetna", aetna="accept",harvard_pilgrim="accept",tufts="reject")
print 

def validate_is_health_insurance(ignore_medicare=True,*valid,**insurance):
	print("checking if valid...")
	for insure in insurance:
		if insure in valid:
			if (ignore_medicare and insure == "medicare"):
				print("skipping medicare...")
			else:
				print(insure)
	return 0

validate_is_health_insurance(True,"tufts","aetna","medicare", aetna="accept",harvard_pilgrim="accept",tufts="reject",medicare="accept")
print

validate_is_health_insurance(False,"tufts","aetna","medicare", aetna="accept",harvard_pilgrim="accept",tufts="reject",medicare="accept")
print
prompt="""
we can blend *list, **kwargs, arguments nad arguments with default values.  The trick is that:

	1. parameters with or without default values have to be first.
	2. *list parameter has to occur after the standard parameters.
	3. **kwargs has to follow *list.

You can use either: parameters, *list, and **kwargs within the function.
"""

raw_input(prompt)
