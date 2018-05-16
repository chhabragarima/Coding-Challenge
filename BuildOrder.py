# BONUS TASK 1

def assess_knowledge(dependencies):


	assess_pattern=[]
	counter=0

	for order in dependencies:
		
		counter=counter+1

		if order[0] in assess_pattern and order[1] in assess_pattern:
			index1=assess_pattern.index(order[0])
			index2=assess_pattern.index(order[1])

			if index1>index2:
				temp_var=assess_pattern[index2]
				assess_pattern[index2]=assess_pattern[index1]
				assess_pattern[index1]=temp_var
				assess_pattern=check_order_disruption(dependencies,assess_pattern,counter)
				#print("if",assess_pattern)

		elif order[0] in assess_pattern and order[1] not in assess_pattern:
			assess_pattern.append(order[1])
			#print("el1",assess_pattern)

		elif order[0] not in assess_pattern and order[1] in assess_pattern:
			index1=assess_pattern.index(order[1])
			assess_pattern[index1]=order[0]
			assess_pattern.append(order[1])
			assess_pattern=check_order_disruption(dependencies,assess_pattern,counter)
			#print("el2",assess_pattern)
		else:
			assess_pattern.append(order[0])
			assess_pattern.append(order[1])
			#print("else",assess_pattern)
			

	return assess_pattern

#This function checks that the order in which the projects should be done is not disrupted when a new dependency is encountered and fit into the assess pattern list
def check_order_disruption(dependencies,assess_pattern,counter):
	print("before",assess_pattern)
	for i in range(counter):
		index1=assess_pattern.index(dependencies[i][0])
		index2=assess_pattern.index(dependencies[i][1])
		if index1>index2:
			assess_pattern[index1]=dependencies[i][0]
			assess_pattern[index2]=dependencies[i][1]

	#print(assess_pattern)
	return assess_pattern
	

def main():
	
	print("Enter all the projects:")
	project_list=[str(x) for x in input().split()]
	no_of_dep=int(input("Enter the no of dependencies:"))
	print("Enter Dependencies:")
	dependencies=[[str(x) for x in input().split()] for i in range(no_of_dep)]
	#dependencies=[['a','d'], ['f','b'], ['b','d'], ['f','a'], ['d','c']]
	assess_pattern=assess_knowledge(dependencies)

	if(len(assess_pattern) != len(project_list)):
		for pro in project_list:
			if pro not in assess_pattern:
				assess_pattern.append(pro)
	
	print(assess_pattern)


if __name__=="__main__":
	main()
