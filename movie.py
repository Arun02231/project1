class Book_Ticket:
    def __init__(self):
        self.rows=input('Please enter no of rows:')
        self.cols=input('Please enter no of seats in each row:')
        while self.rows.isdigit()==False or self.cols.isdigit()==False:
            print("Please choose the rows and coloumns in numbers only!")
            self.rows=input('Please enter no of rows:')
            self.cols=input('Please enter no of seats in each row:')
            continue
        self.rows=int(self.rows)
        self.cols=int(self.cols)
        self.row=[]
        for i in range(self.rows):
            self.seats=[]
            for j in range(self.cols):
                self.seats.append('S')
            self.row.append(self.seats)
        self.details={}
        self.total_tickets=0
        for i in self.row:
            for j in i:
                self.total_tickets+=1
        self.current_income=0
    def show_seats(self):
        print('Seats:')
        for i in self.row:
            for j in i:
                print(j,end=' ')
            print( )
    def buy_ticket(self):
        print('Please select the rows from 1 and seats also!!')
        self.r=input('please select the row:')
        self.c=input('please select the seat:')
        while self.r=='0' or self.c=='0':
            print('Please select the row and seat from 1')
            self.r=input('please select the row:')
            self.c=input('please select the seat:')
            while self.r.isdigit()==False or self.c.isdigit()==False:
                print('Please select the rows and seats in numbers!!')
                self.r=input('please select the row:')
                self.c=input('please select the seat:')
                continue
            continue
        while self.r.isdigit()==False or self.c.isdigit()==False:
            print('Please select the rows and seats in numbers!!')
            self.r=input('please select the row:')
            self.c=input('please select the seat:')
            
            while self.r=='0' or self.c=='0':
                print('Please select the row and seat from 1')
                self.r=input('please select the row:')
                self.c=input('please select the seat:')
                continue
            continue
        
        self.r=int(self.r)
        self.c=int(self.c)
        while int(self.r)>self.rows or int(self.c)>self.cols:
            print('please chosse the seats with in the range of',self.rows,self.cols)
            self.r=input('please select the row:')
            self.c=input('please select the seat:')
            continue
        if (self.r,self.c) in self.details:
            print('Hey seat has already booked!, kindly choose another seat!')
        else:
            print('Please select the name in alphabets!')
            self.name=input('Please enter your name:')
            while self.name.isalpha()==False:
                print('Please select the name in alphabets!')
                self.name=input('Please enter your name:')
                continue
                
            self.age=input('Please enter your age:')
            while self.age.isdigit()==False:
                print('please select the age in numbers!')
                self.age=input('Please enter your age:')
                continue
            self.age=int(self.age)
            self.geneder=input('plase select your gender Male/Female/Other:')
            while self.geneder.casefold() not in ['male','female','other']:
                print('Choose correct gender!')
                self.geneder=input('plase select your gender Male/Female/Other:')
                continue   
            self.phone=input('Please enter your phone number:')
            while self.phone.isdigit()==False:
                print('Please choose the phone number in numbers only!')
                self.phone=input('Please enter your phone number:')
                continue
            self.phone=int(self.phone)    
            self.last=input('Confirm to Book seat Yes/No:')
            while self.last.isalpha()==False:
                print('Plases choose your options in alphabets only!')
                self.last=input('Confirm to Book seat Yes/No:')
                continue
            self.last=self.last.casefold()
            if self.last=='yes':  
                if self.total_tickets<=60:
                    self.opinion=input('You ticket price is 10 $, if you want to continue type Yes/No:')
                    while self.opinion.isalpha()==False:
                        print('Plases choose your options in alphabets only!')
                        self.opinion=input('You ticket price is 10 $, if you want to continue type Yes/No:')
                        continue                     
                    self.opinion=self.opinion.casefold()
                    if self.opinion=='yes':
                        self.current_income=self.current_income+10
                        self.row[self.r-1][self.c-1]='B'
                        self.details[(self.r,self.c)]=[self.name.capitalize(),self.age,self.geneder.capitalize(),self.phone]
                    else:
                        pass
                else:
                    if self.rows%2==0:
                        if self.r<(self.rows/2):
                            self.opinion=input('You ticket price is 10 $, if you want to continue type Yes/No:')
                            while self.opinion.isalpha()==False:
                                print('Plases choose your options in alphabets only!')
                                self.opinion=input('You ticket price is 10 $, if you want to continue type Yes/No:')
                                continue 
                            self.opinion=self.opinion.casefold()
                            if self.opinion=='yes':
                                self.current_income=self.current_income+10
                                self.row[self.r-1][self.c-1]='B'
                                self.details[(self.r,self.c)]=[self.name.capitalize(),self.age,self.geneder.capitalize(),self.phone]
                            else:
                                pass
                        else:
                            self.opinion=input('You ticket price is 8 $, if you want to continue type Yes/No:')
                            while self.opinion.isalpha()==False:
                                print('Plases choose your options in alphabets only!')
                                self.opinion=input('You ticket price is 10 $, if you want to continue type Yes/No:')
                                continue 
                            self.opinion=self.opinion.casefold()
                            if self.opinion=='yes':
                                self.current_income=self.current_income+8
                                self.row[self.r-1][self.c-1]='B'
                                self.details[(self.r,self.c)]=[self.name.capitalize(),self.age,self.geneder.capitalize(),self.phone]
                            else:
                                pass
                    else:
                        if self.r<=((self.rows//2)):
                            self.opinion=input('You ticket price is 10 $, if you want to continue type Yes/No:')
                            while self.opinion.isalpha()==False:
                                print('Plases choose your options in alphabets only!')
                                self.opinion=input('You ticket price is 10 $, if you want to continue type Yes/No:')
                                continue 
                            self.opinion=self.opinion.casefold()
                            if self.opinion=='yes':
                                self.current_income=self.current_income+10
                                self.row[self.r-1][self.c-1]='B'
                                self.details[(self.r,self.c)]=[self.name.capitalize(),self.age,self.geneder.capitalize(),self.phone]
                            else:
                                pass
                        else:
                            self.opinion=input('You ticket price is 8 $, if you want to continue type Yes/No:')
                            while self.opinion.isalpha()==False:
                                print('Plases choose your options in alphabets only!')
                                self.opinion=input('You ticket price is 10 $, if you want to continue type Yes/No:')
                                continue 
                            self.opinion=self.opinion.casefold()
                            if self.opinion=='yes':
                                self.current_income=self.current_income+8
                                self.row[self.r-1][self.c-1]='B'
                                self.details[(self.r,self.c)]=[self.name.capitalize(),self.age,self.geneder.capitalize(),self.phone]
                            else:
                                pass
                for m in self.row:
                    for n in m:
                        print(n,end=' ')
                    print()
            elif self.last=='no':
                        pass
    def statistics(self):
        self.total=0
        for i in range(len(self.row)):
            j=self.row[i].count('B')
            self.total+=j
        print('Total no of seats are booked is:',self.total)
        self.percentage=(self.total/self.total_tickets)*100
        print('Booking percentage is:',self.percentage)
        print('Current income is:',self.current_income,'$')
        self.total_income=0
        if self.total_tickets<=60:
            self.total_income=self.total_tickets*10
        else:
            self.z=(self.total_tickets//2)
            self.y=(self.total_tickets-self.z)
            self.total_income=(self.z*10+self.y*8)      
        print('Total income is:',self.total_income,'$')
    def get_details(self):
        try:
            self.rr=int(input('Please enter a row no you want:'))
            self.ss=int(input('Please eneter a seat no u want:'))
            self.u=(self.rr,self.ss)
            self.a=self.details[self.u]
            print('name:',self.a[0])
            print('age:',self.a[1])
            print('Gender:',self.a[2])
            print('phone-number:',self.a[3])    
            if self.total_tickets<=60:
                print('Ticket price: 10$')
            else:
                if self.rr<=self.rows//2:
                    print('Ticket price: 10$')
                else:
                    print('Ticket price: 8$')       
        except KeyError:
            print("we don't have that seat or please book the tickets")
            
