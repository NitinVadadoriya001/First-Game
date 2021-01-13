#snack water gun game
#global variable declare
from computer import computer
from gammer import gammer

def SWG_GAME(u_name):
	print("		🐉SNACK🐉 💦WATER 💦 🔫GUN 🔫")
	print("	..THIS GAME WILL OVER AFTER .5. TASK..	")
	count=0
	u_total=0 # we use also class & object
	c_total=0
	while(count<5):
		count+=1
		c=computer()
		u=gammer()
		print(f"\n\n\nyou selected == { u } computer selected == { c }")
		

		if c=="snack" and u=="gun":
			u_total +=1
			
			print("/n------------------------------------------------------------------")
			print(f"	`{u_name}` SCORE	|	 COMPUTER SCORE	")
			print(f"	    {u_total}		|	   	{c_total}	  ")	
			print("-------------------------------------------------------------------")
		
			
		elif c==u:
			
			print("\n------------------------------------------------------------------")
			print(f"	`{u_name}` SCORE	|	 COMPUTER SCORE	")
			print(f"	    {u_total}		|	   	{c_total}	  ")	
			print("-------------------------------------------------------------------")
			
		elif c=="water" and u=="gun":
			c_total +=1
			
			print("\n------------------------------------------------------------------")
			print(f"	`{u_name}` SCORE	|	 COMPUTER SCORE	")
			print(f"	    {u_total}		|	   	{c_total}	  ")	
			print("-------------------------------------------------------------------")
		
		elif c=="snck" and u=="water":
			c_total +=1
			
			print("\n------------------------------------------------------------------")
			print(f"	`{u_name}` SCORE	|	 COMPUTER SCORE	")
			print(f"	    {u_total}		|	   	{c_total}	  ")	
			print("-------------------------------------------------------------------")
		
		elif u=="snack" and c=="water":
			u_total+=1
			
			print("\n------------------------------------------------------------------")
			print(f"	`{u_name}` SCORE	|	 COMPUTER SCORE	")
			print(f"	    {u_total}		|	   	{c_total}	  ")	
			print("-------------------------------------------------------------------")
		
		elif c=="gun" and u=="snack":
			c_total+=1
			
			print("\n------------------------------------------------------------------")
			print(f"	`{u_name}` SCORE	|	 COMPUTER SCORE	")
			print(f"	    {u_total}		|	   	{c_total}	  ")	
			print("-------------------------------------------------------------------")
		
		else:
			
			print(" \" Invalid Choice From Grammer \"")
			
			print("\n------------------------------------------------------------------")
			print(f"	`{u_name}` SCORE	|	 COMPUTER SCORE	")
			print(f"	    {u_total}		|	   	{c_total}	  ")	
			print("-------------------------------------------------------------------")
		
	print("\n\n\n\n\n\n")	
	if(c_total < u_total):
		print("\n")
		print("	🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉	")
		print("	🏆🏆|| WOW YOU WINNER THIS GAME ||🀼�	")
		print("\n------------------------------------------------------------------")
		print(f"	`{u_name}` SCORE	|	 COMPUTER SCORE	")
		print(f"	    {u_total}		|	   	{c_total}	  ")	
		print("-------------------------------------------------------------------")
		
	elif c_total==u_total:
		print("	🎮🎮 GAME IS DROE 🎮🎮	")
		print("\n------------------------------------------------------------------")
		print(f"	`{u_name}` SCORE	|	 COMPUTER SCORE	")
		print(f"	    {u_total}		|	   	{c_total}	  ")	
		print("-------------------------------------------------------------------")
		
	else:
		print("\n")
		print("	😖😖you lose the game😖😖	")
		
		print("\n------------------------------------------------------------------")
		print(f"	`{u_name}` SCORE	|	 COMPUTER SCORE	")
		print(f"	    {u_total}		|	   	{c_total}	  ")	
		print("-------------------------------------------------------------------")
		


char=input(" Do You Want To Play This  Game (y/n) : ")
if char=="yes":
		u_name=input(" Enter a Your Name Hear : ")
		SWG_GAME(u_name)
else:
		print(". THANKS YOU !! SEE YOU AGAIN... ")
		
		
	
	
	
	
	