

def merge(ar1,ar2):
	b=[]
	len_a=len(ar1)
	len_b=len(ar2)
	i=0
	j=0
	while i<len_a and j < len_b:

		if ar1[i]<ar2[j]:
			b.append(ar1[i])

			i+=1
		else:
			b.append(ar2[j])

			j+=1

	while i<len_a:
		b.append(ar1[i])
		i+=1
	while j<len_a:
		b.append(ar2[j])
		j+=1
	return b






def msort(arr):

	if len(arr)<=1:

		return arr
	mid=len(arr)//2

	left_subar=arr[:mid]

	righ_subar=arr[mid:]

	left=msort(left_subar)
	right=msort(righ_subar)

	return merge(left,right)


print(msort([1,9,3,8,4,7,5,6]))