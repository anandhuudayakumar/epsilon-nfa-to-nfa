def epsilon_closure(hmap,element,stack):
	stack.append(element)
	if  hmap[element][2]!='_' and hmap[element][2]!=element:
		for k in hmap[element][2]:
			epsilon_closure(hmap,k,stack)
	else:
		return 
		
		
#-----------------------------------------------------		
		
n=int(input("enter number of states:"))
d={}
for i in range(n):
	key=input("enter state:")
	(a,b,c)=map(str,input().split(" "))
	d[key]=(a,b,c)
stack=[]
epsilon_map={}
#print(d.keys())
final_map1={}
final_map2={}
stack_0=[]
stack_1=[]
#------------------------------------------------------

print()
for i in d.keys():
	epsilon_closure(d,i,stack)
	stack=list(set(stack))
	print("epsilon closure of ",i,"is :","".join(stack))
	epsilon_map[i]="".join(stack)
	stack.clear()
#print(d)
#print(epsilon_map)

#--------------------------------------------------------
for m in epsilon_map.keys():
	for h in epsilon_map[m]:
		if d[h][0]==m:
			f=set(epsilon_map[h])
			f=list(f)
			if '_' in f:
				f.remove('_')
			for c in f:
				stack_0.append(c)
		else:
			stack_0.append(d[h][0])
		if d[h][1]==m:
			o=set(epsilon_map[h])
			o=list(o)
			if '_' in o:
				o.remove('_')
			for v in o:
				stack_1.append(v)
		else:
			stack_1.append(d[h][1])
	if '_' in stack_0:
		stack_0.remove('_')
	if '_' in stack_1:
		stack_1.remove('_')
	final_map1[m]="".join(list(set(stack_0)))
	final_map2[m]="".join(list(set(stack_1)))
	stack_0.clear()
	stack_1.clear()
print()
#print(final_map1)
#print(final_map2)
print()

new_final_map1={}
new_final_map2={}
stack.clear()
for i,j in final_map1.items():
	if j !='':
		for m in j:
			for k in epsilon_map[m]:
				stack.append(k)
		stack=list(set(stack))
		#print(stack)
		new_final_map1[i]="".join(stack)
		stack.clear()
	else:
		new_final_map1[i]="NULL"
for i,j in final_map2.items():
	if j !='':
		for m in j:
			for k in epsilon_map[m]:
				stack.append(k)
		stack=list(set(stack))
		#print(stack)
		new_final_map2[i]="".join(stack)
		stack.clear()
	else:
		new_final_map2[i]="NULL"
print("TRANSITION TABLE OF NFA WITHOUT EPSILON CLOSURE")
print("\nSTATE\t0\t1")
print('----------------------')
for i in d.keys():
	print(i,"\t",new_final_map1[i],"\t",new_final_map2[i])

#--------------------------------------------------------



	
