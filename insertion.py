



def isort(arr):

	for i in range(1,len(arr)):
		point=arr[i]
		j=i-1

		while j>=0 and point<arr[j]:
			arr[j+1]=arr[j]
			j-=1

		arr[j+1]=point


	return arr


b=list(map(int,input().split(',')))

print(isort(b))





# def isort(arr):
	# b=[arr[0]]
	# for i in range(1,len(arr)):
	# 	k=len(b)-1
	# 	while k>=0:

	# 		if arr [i]<b[k]:
	# 			b.insert(k,arr[i])
	# 		elif arr [i]>b[k]:
	# 			b.insert(k+1,arr[i])

	# 		k-=1

	# 	return b


