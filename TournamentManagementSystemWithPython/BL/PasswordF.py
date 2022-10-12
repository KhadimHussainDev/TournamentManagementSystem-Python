class logInfo:
    userName = ""
    password=""
    def init(self,userName,password):
        self.userName=userName
        self.password=password
    def athentication(self):
        if self.userName == passwordDL.get_log().get_username() and self.password == passwordDL.get_log().get_password():
            return True
        return False
