class schedule:
    team1Name="";
    team2Name="";
    date=0;
    month=0;
    year=0;
    time=0;
    def storeScheduleInFile(schedule,path):
        file=open(path,'a')
        file.write(schedule.Team1Name + "," + schedule.Team2Name + "," + schedule.Date + "," + schedule.Month + "," + schedule.Time+"\n")
        file.close()
    def init(self,team1,team2,date,month):
        self.team1Name=team1 
        self.team2Name=team2 
        self.date=date 
        self.month=month 
        self.year=2022
        self.time=date+(month*30)

