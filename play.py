
from random import choice
import sys

def main():
 a = raw_input('enter your choice:: ')
 c= comp_turn()
 u = user_turn(a)
 winner_is(c,u)

def option():
 
 o = raw_input("wish to play again? Press--> p. q--> quit:  " )
 if o=='p':
	main()
 elif o=='q':
	sys.exit(0)
 else:
	print "wrong option, try again "	
	option()
	


def winner_is(c,u):
 if c=='r' and u=='s' :
	print "computer option was 'r', it wins"
 elif c=='s' and u=='p':
	print "computer option was 's', it wins'"
 elif c=='p' and u=='r':
	print "computer option was 'p', it wins'"
 else:
	print 'you win'
 option()


def user_turn(a):
 if a =='r':
	return 'r'
 elif a =='p':
	return 'p'
 elif a =='s':
	return 's'
 else: 
	return ('wrong option')
 

def comp_turn():
 option = ['r', 'p','s']
 comp = choice(option)
 return comp


if __name__=='__main__':
 print "ready to play rock, paper, scissors with your computer?"
 print "select r - rock, p- paper and s- scissors. "
 main()

