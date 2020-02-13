import time
import threading

def sing():
	for i in range(5):
		print("-----this is the %d---" % i)
		time.sleep(1)


def dance():
	for i in range(5):
		print("-----that is the %d---" % i)
		time.sleep(1) 


def main():
	t1 = threading.Thread(target=sing)
	t2 = threading.Thread(target=dance)
	t1.start()
	t2.start()


	while True:
		print(threading.enumerate())
		#if threading.enumerate<=1:
			#break
	time.sleep(2)

if __name__ == '__main__':
	main()

