class Read:
    q_list=[]
    def __init__(self):
        self.f=open("1.txt")
    def readfile(self):
		global quastion,optiona,optionb,optionc,optiond,answer
		#time.sleep(3)
		try:
			self.f_line=self.f.readline()
			
			self.q_list=self.f_line.split(":");#print(self.q_list)
		
			quastion=self.q_list[0]
		
			optiona,optionb,optionc,optiond=self.q_list[1],self.q_list[2],self.q_list[3],self.q_list[4]
		except Exception as e:
			pygame.quit()
			print("Game over")
			print("Your score",points)
			
	#print(self.q_list)
        