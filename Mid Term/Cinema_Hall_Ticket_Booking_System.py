class starCinema:
    hallList = []
    def __init__(self,hallID,rows,cols):
        if(rows < 0 or cols < 0):
            raise ValueError('Rows and Cols should be greater than 0')
        self.rows = rows
        self.cols = cols
        self.ID = hallID
    
    def entryHall(self,hall):
        self.hallList.append(hall)
    

class Hall(starCinema):
    def __init__(self,hallID,rows,cols):
        if(rows < 0 or cols < 0):
            raise ValueError('Rows and Cols should be greater than 0')
        self.showList = []
        self.seats = {}
        super().__init__(hallID,rows,cols)
        super().entryHall(self)

    def entryShow(self,showID,showName,showTime):
        self.seats[showID] = [[True for i in range(self.rows)] for j in range(self.cols)]
        self.showList.append((showName,showID,showTime))
    
    def checkID(self,showID):
        for i in self.showList:
            if i[1] == showID:
                return True
        return False
    
    def bookSeat(self,showID,seatNeed):
        inValid = []
        canBook = []
        booked = []
        for item in seatNeed:
            p , q = item[0], item[1]
            if p >= 0 and q >= 0 and p < self.rows and q < self.cols:
                if self.seats[showID][p][q] == True:
                    canBook.append((p,q))
                else:
                    booked.append((p,q))
            else:
                inValid.append((p,q))
        return canBook,booked,inValid
    
    def updateSeat(self,showID,seatNeed):
        for item in seatNeed:
            p, q = item[0],item[1]
            self.seats[showID][p][q] = False
    
    def viewShowList(self):
        if self.showList == []:
            print('Sorry!No Show For Today!')
            return
        for i in self.showList:
            print(f'MOVIE NAME: {i[0]}          SHOW ID: {i[1]}         TIME: {i[2]}')

    def viewAvailableSeats(self,showID):
        cnt = 0
        for key,matrix in self.seats.items():
            if key == showID:
                print('Following Seats are Available : ')
                print()
                for i in range(self.rows):
                    for j in range(self.cols):
                        if matrix[i][j] == True:
                            print(f'({i},{j})')
                            cnt += 1
                break
        print()
        print('-----------SEAT MATRIX------------')
        for key,matrix in self.seats.items():
            if key == showID:
                for i in range(self.rows):
                    for j in range(self.cols):
                        if matrix[i][j] == True:
                            print('-',end=' ')
                        else:
                            print('X',end=' ')
                    print()
        print()
        print(f'Total Available Seats: {cnt}')
        print()
        
cinePlex = Hall(101,7,7)
cinePlex.entryShow(101,'Avengers','01/05/2024 11:25 AM')
cinePlex.entryShow(102,'Furious','01/05/2024 02:25 PM')
cinePlex.entryShow(103,'Jumanji','01/05/2024 05:25 PM')

print()
print('----------------------***Cinema Hall Ticket Booking System***------------------------')
print()
while(True):
    print('1. View All Show Today')
    print('2. View Available Seats')
    print('3. Buy Ticket')
    print('4. Exit')
    print()
    choice = int(input('Enter Your Choice: '))
    print()
    if choice == 1:
        print('-----------------SHOW LIST-----------------')
        cinePlex.viewShowList()
        print('-------------------------------------------')

    elif choice == 2:
        showID = int(input('Enter Show ID: '))
        print()
        print('-----------------------------')
        if cinePlex.checkID(showID):
            print()
            cinePlex.viewAvailableSeats(showID)
        else:
            print('Oh Sorry! This Show isn\'t available today!')
        print('-----------------------------')
    
    elif choice == 3:
        showID = int(input('Enter Show ID: '))
        print()
        if(cinePlex.checkID(showID)):
            print('-----------------------------')
            numSeat = int(input('Enter Number of Seats: '))
            print()
            seatList = set()
            for i in range(numSeat):
                row = int(input(f'Enter row for seat {i + 1} : '))
                col = int(input(f'Enter col for seat {i + 1} : '))
                seatList.add((row,col))
                print()
            numSeat = len(seatList)
            seatAvailable = cinePlex.bookSeat(showID,seatList)
            if len(seatAvailable[0]) < numSeat:
                print('Sorry!',end='')
                if len(seatAvailable[1]) != 0:
                    print('Following Seats are already Booked:')
                    print()
                    for i in seatAvailable[1]:
                        print(i)
                    print()
                if len(seatAvailable[2]) != 0:
                    print('Following Seats are Invalid!')
                    print()
                    for i in seatAvailable[2]:
                        print(i)
                    print()
                print('Please Choose Your Seat Again!',end='')
                cinePlex.viewAvailableSeats(showID)
            else:
                print('Yooo!!! Following Seats are Booked!')
                print()
                for i in seatAvailable[0]:
                    print(i)
                print()
                cinePlex.updateSeat(showID,seatAvailable[0])
                print('Enjoy Your Show!')
            print('--------------------------------')
        else:
            print('-----------------------------')
            print('Oh Sorry! This Show isn\'t available today!')
            print('-----------------------------')
    elif choice == 4:
            print('-----------------------------')
            print('Oh Sorry! This Show isn\'t available today!')
            print('-----------------------------')
    else:
            print('-----------------------------')
            print('Please Enter Valid Choice Option(1 or 4)!')
            print('-----------------------------')
    print()