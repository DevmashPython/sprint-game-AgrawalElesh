import msvcrt
import time
finish=10
count1=count2=count3=0
finish2=35
print "Press enter key to get started!"
raw_input()
s_time=time.time()
while(1):
	key=msvcrt.getch()
	if key=='d':
		count1=count1+1
		print "-->",
		if count1==finish:
			print "To go down press S"
			while(1):
				for j in range(0,41):
					key=msvcrt.getch()
					if key=='s':	
						j=j+4
						i=40-j
						print i*" "+"/"
						count2=count2+1
						if count2==finish2:
							print "To go right press A"
							while(1):
								key=msvcrt.getch()
								if key=="a":
									print "-->",     
									count3=count3+1
									if count3==finish:
										time_elapsed=time.time()-s_time
										print "\nCongrats you have finished the game"
										print "Time taken is "+str(time_elapsed)
										quit()
								else:
									print "Oops u lost the game try again:)"
									quit()
					
					else:
						print "Oops u lost the game try again:)"
						quit()
					
	else:
		print "Oops u lost the game try again:)"
		quit()


'''
1. Mention controls for the game.

'''
				
