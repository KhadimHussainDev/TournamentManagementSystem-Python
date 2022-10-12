class Team:
    teamName="";
    ownerName="";
    captainName="";
    captainAge=0;
    viceCaptainName="";
    viceCaptainAge=0;
    totalPlayedMatches=0;
    wonMatches=0;
    lostMatches=0;
    def storeTeamsInFile(team,path):
        file=open(path,'a')
        file.write(team.TeamName + "," + team.OwnerName + "," + team.CaptainName + "," + team.CaptainAge + "," + team.ViceCaptainName + "," + team.ViceCaptainAge+",")
        file.write(team.TotalPlayedMatches + "," + team.WonMatches + "," + team.LostMatches + "," + team.Points+"\n")
        file.close()
    