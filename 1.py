i = 100
nums=[11,22]
def A100():
	global i
	i+=100


def A200():
	global nums
	nums+=[33.44]

print(i)

A100()

print(i)

A200()

print(nums)