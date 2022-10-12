class Tournament:
    name="";
    startingDate=0;
    startingMonth=0;
    startingYear=0;   
    def init(name,date,month,year,self):
        self.name=name
        self.startingDate=date 
        self.startingMonth=month 
        self.startingYear=year 
    def storeTournamentInFile(tour,path):
        file=open(path,'a')
        file.write(tour.name+","+tour.startingDate+","+tour.startingMonth+","+tour.startingMonth+","+tour.startingYear+"\n")
        file.close()



