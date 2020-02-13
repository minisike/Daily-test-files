

import time
import threading

lb = [11,22]

def Aa(temp):
	temp.append(33)
	print("this is the _____temp=%s" % str(temp))

def Bb(temp):
	print("this is the _____temp=%s" % str(temp))


def main():
	t1 = threading.Thread(target=Aa,args=(lb,))
	t2 = threading.Thread(target=Bb,args=(lb,))
	t1.start()
	time.sleep(1)
	t2.start()
	print("\nthis is the perfect %s %s" %("iii",str(lb)))
	print("\nName:%s lb:%s Height:%f" %("Aviad",str(lb),1.83))


if __name__ == '__main__':
	main()