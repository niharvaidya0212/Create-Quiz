class quiz:
	topics=[]
	topic_ques={}
	topic_options={}
	topic_answers={}
	topic_difficultylvl={}
	student_responses={}
	student_data=[]
	total=0
	scores={}

	def __init__(self):
		self.menu()

	def menu(self):
		print("Enter your role:\n1:Admin\n2:Student\n3.Exit\n>>")
		n=int(input())
		if n==1:
			self.Admin()
		elif n==2:
			if quiz.topic_ques!={}:
				self.Student()
			else:
				print("\n!!!Quiz is not ready yet!!!\n")
				self.menu()
		elif n==3:
			return None
		else:
			print("Enter valid option\n")
			self.menu()

	def Admin(self):
		username=input("Enter the username: ")
		password=input("Enter the password: ")
		if username=='admin' and password=='admin123':
			self.Adminmenu()
		else:
			print("Enter valid username\n")
			self.Admin()

	def Adminmenu(self):
		print("\n1.Add questions\n2.Display questions\n3.Clear quiz\n4.Scoreboard\n5.Exit\n>>")
		n=int(input())
		if n==1:
			self.Addques()
		elif n==2:
			self.display()
		elif n==3:
			self.clear_quiz()
		elif n==4:
			self.scoreboard()
		elif n==5:
			self.menu()
		else:
			print("Enter valid choice\n")
			self.Adminmenu()

	def clear_quiz(self):
		quiz.topics=[]
		quiz.topic_ques={}
		quiz.topic_options={}
		quiz.topic_answers={}
		quiz.topic_difficultylvl={}
		quiz.student_responses={}
		quiz.student_data=[]
		quiz.total=0
		print("The quiz is deleted")
		self.Adminmenu()

	def scoreboard(self):
		print("Name".ljust(20),"Email".ljust(20),"Percentage")
		for i in quiz.student_data:
			print((i[0]).ljust(20),(i[1]).ljust(20),quiz.scores[i[0]])
		self.Adminmenu()


	def Addques(self):
		a=input("Enter the question:\n")
		x=input("Enter the question topic: ")
		c=int(input("Enter the difficulty level\n1-Easy  2-Medium  3-Hard\nChoose (1,2,3) >> "))
		while(c>3):
			c=int(input("Enter the difficulty level\n1-Easy  2-Medium  3-Hard\nChoose (1,2,3) >> "))
		b=x.lower()
		if b not in quiz.topics:
			quiz.topics.append(b)
			quiz.topic_ques[b]=[]
			quiz.topic_options[b]=[]
			quiz.topic_answers[b]=[]
			quiz.topic_difficultylvl[b]=[]

		quiz.topic_ques[b].append(a)

		if c==1:
			quiz.topic_difficultylvl[b].append(5)
			quiz.total+=5
		elif c==2:
			quiz.topic_difficultylvl[b].append(10)
			quiz.total+=10
		elif c==3:
			quiz.topic_difficultylvl[b].append(20)
			quiz.total+=20

		arr=[]
		print("Enter the options:")
		for i in range (1,5):
			print(i,":",end='')
			arr.append(input())
		quiz.topic_options[b].append(arr)

		print("Enter the correct answer options:\n>>")
		quiz.topic_answers[b].append(int(input()))

		if input("Do you want to add more questions? Y/N") in 'Yy':
			self.Addques()
		else:
			self.Adminmenu()

	def total_marks(self,name):
		if name in quiz.student_responses:
			sum1=0
			for i in quiz.topics:
				sum1+=sum(quiz.student_responses[name][i])
			return sum1
		else:
			print("!!!Name doesnt exit in the list!!!")

	def Student(self):
		self.stdname=input("Enter your name:")
		self.stdmail=input("Enter your email:")
		quiz.student_data.append([self.stdname,self.stdmail])
		quiz.student_responses[self.stdname]={}
		print("************Starting test************\nEasy question = 5 marks\nMedium question = 10 marks\nHard question=20 marks\n")
		if input("Type any key to start>>")!='':
			for i in range (len(quiz.topic_ques)):
				a=quiz.topics[i]
				quiz.student_responses[self.stdname][a]=[]
				print("____",a.upper(),"____")
				for j in range(len(quiz.topic_ques[a])):
					print("\n",quiz.topic_ques[a][j])
					for k in range(0,4):
						print(k+1,":",quiz.topic_options[a][j][k])
					check=int(input("Enter the option:"))
					if check==quiz.topic_answers[a][j]:
						quiz.student_responses[self.stdname][a].append(quiz.topic_difficultylvl[a][j])
					else:
						quiz.student_responses[self.stdname][a].append(0)
		print("\n\nCORRECT ANSWERS ARE\n")
		for i in range (len(quiz.topic_ques)):
			a=quiz.topics[i]
			print("\n____",a.upper(),"____\n")
			for j in range(len(quiz.topic_ques[a])):
				print("\n",quiz.topic_ques[a][j])
				for k in range(0,4):
					print(k+1,":",quiz.topic_options[a][j][k])
				print("ANSWER>>",quiz.topic_answers[a][j],"\n")


		
		res=self.total_marks(self.stdname)
		print(self.stdname,"your score is",res,"/",quiz.total,"\n\n")
		quiz.scores[self.stdname]=res/quiz.total*100
		self.menu()

	def display(self):
		for i in range (len(quiz.topic_ques)):
			a=quiz.topics[i]
			print("\n____",a.upper(),"____\n")
			for j in range(len(quiz.topic_ques[a])):
				print("\n",quiz.topic_ques[a][j])
				for k in range(0,4):
					print(k+1,":",quiz.topic_options[a][j][k])
		self.Adminmenu()
		

a=quiz()