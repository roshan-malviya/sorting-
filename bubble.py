 

def b_sort(a):

	for i in range(len(a)):

		for j in range(len(a)-1):

			if a[j]>a[j+1]:

				a[j],a[j+1]=a[j+1],a[j]

	return a
b=list(map(int,input().split(',')))

print (b_sort(b))