
import time


g_bl = 100


def Aa():
	global g_bl
	g_bl +=1
	print("____this is the %d____" % g_bl)

def Bb():
	print("____this is the %d____" % g_bl)


def main():
	Aa()
	time.sleep(1)
	Bb()

print("____this is the %d____" % g_bl)

if __name__ == '__main__':
	main()
