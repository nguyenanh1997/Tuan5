import sqlite3
import msvcrt
import time
import os
class model:
    username ="chua ro"
    password = "chua ro"
    def insertdata(self, usernameIn, passwordIn, nameIn, sexIn, placeIn, birthdayIn):
        connectToSQlite = sqlite3.connect('appchat.db')
        c = connectToSQlite.cursor()
        c.execute("insert into userinformation(username, password, hoten, sex, birthday, place) values('"+usernameIn+"' , '"+passwordIn+"', '"+nameIn+"' , '"+sexIn+"' , '"+birthdayIn+"' , '"+placeIn+"' )")
        connectToSQlite.commit()

    def insertDataToFriend(self ,username,usernameoffriend,place,sex,birhtday,status):
        connectToSQlite = sqlite3.connect('appchat.db')
        c = connectToSQlite.cursor()
        c.execute("insert into friend(usernameofob, usernameoffriend, place, sex, birthday, statusfriend) values('"+username+"' , '" + usernameoffriend + "' , '" + place + "' , '" + sex + "' , '" + birhtday + "', "+status+")")
        connectToSQlite.commit()
    
    def insertDataToMessage(self, username, namefriend,content,timesecond):
        connectToSQlite = sqlite3.connect('appchat.db')
        c = connectToSQlite.cursor()
        time_uct = time.asctime( time.localtime(timesecond) )
        c.execute("insert into message(revicer,sender,content,statusmessage, statussender,statusrevicer, time_uct) values ( '" + namefriend + "' , '" + username + "' , '" + content + "' , 2, 1, 1, '" + time_uct + "')")
        connectToSQlite.commit()

    def updateData(self,sql):
        connectToSQlite = sqlite3.connect('appchat.db')
        c = connectToSQlite.cursor()
        c.execute(sql)
        connectToSQlite.commit()

    def selectdata(self, username,namefriend,id, function):
        connectToSQlite = sqlite3.connect('appchat.db')
        c = connectToSQlite.cursor()
        # chuc nang 1 lay thong tin trong bang userinformation
        # chuc nang 2 lay usernameofob trong friend
        # chuc nang 3 kiem tra su ton tai cua 1 quan he ban be
        # chuc nang 4 lay thong tin usrenameoffriend trong friend
        if function == 1:
            c.execute("select place , sex, birthday from userinformation where username = '"+username+"'")
            for row in c.fetchall() :
                return row
        if function == 2:
            c.execute("select usernameofob from friend where usernameoffriend = '"+username+"' and statusfriend = 2")
            rows = c.fetchall()
            if len(rows) == 0:
                return 0
            for row in rows:
                print(row[0])
            return 1
        if function == 3:
            c.execute("select id from friend where usernameofob = '" + username + "' and usernameoffriend = '" + namefriend+ "' and statusfriend = 1")
            rows = c.fetchall()
            return rows
        if function == 4:
            c.execute("select place , sex, birthday from friend where usernameofob = '" + username + "' and usernameoffriend = '" + namefriend + "' ")
            rows = c.fetchall()
            return rows
        if function == 5:
            c.execute("select usernameoffriend from friend where usernameofob = '" + username + "' and statusfriend = 1 and id ='"+ id+"'")
            rows = c.fetchone()
            return rows

    def selectDefault(self, sql):
        connectToSQlite = sqlite3.connect('appchat.db')
        c = connectToSQlite.cursor()
        c.execute(sql)
        rows = c.fetchall()
        return rows

    def checkusername(self, usernamecheck,password, function):
        connectToSQlite = sqlite3.connect('appchat.db')
        c = connectToSQlite.cursor()
        if function == 1 :
            c.execute("select id from userinformation where username = '"+usernamecheck+"' ")
        if function == 2 :
            c.execute("select id from userinformation where username = '"+usernamecheck + "' and password = '"+password +"'")
        for row in c.fetchall() :
            if row is None:
                return 0
            else :
                return 1

    def checkInput(self , a):
        x = len(a)
        if len(a) == 0:
            print("khong duoc de trong chuoi")  
            return 0
        else :
            if x > 8:
                print("khong duoc nhap chuoi qua lon")
                return 0
            if x < 4:
                print("khong duoc nhap chuoi qua nho")
                return 0
        if " " in a :
            print("co khoang trang trong chuoi ban vua nhap ")
            return 0


    def SignUp(self):
        print("hay nhap thong tin de dang ky nhung thong tin co * la bat buoc")
        # lay nhung thong tin can thiet de dang ky
        print("nhap username (*) ")
        username = input()
        check = self.checkInput(username)
        if check == 0:
            return 5
        print("nhap mat khau (*)")
        password = input()
        check = self.checkInput(password)
        if check == 0:
            return 5
        print("nhap ho ten (*)")
        name = input()
        check = self.checkInput(name)
        if check == 0:
            return 5
        print("nhap ngay thang nam sinh ")
        birthday = input()
        print("nhap gioi tinh ")
        sex = input()
        print("nhap noi o")
        place = input()
        if ( self.checkusername( username, None, 1) == 1) :
            return 0   
        else :
            self.insertdata( username, password, name, sex, place, birthday)
            return 1
    
    def SignIn(self):
        print("---------nhap username: ") # lay thong tin can thiet tu nguoi dung
        username = input()
        print("----------nhap mat khau: ")
        password = input()
        # lay du lieu tu sqlite de so sanh
        if ( self.checkusername( username, password, 2) == 1):
           self.username = username
           return 1
        else:
            return 0
            
    def checkBlock(self, usernameofob, usernameoffriend):
        connectToSQlite = sqlite3.connect('appchat.db')
        c = connectToSQlite.cursor()
        c.execute("select statusfriend from friend where usernameofob = '"+usernameofob+"' and usernameoffriend ='"+usernameoffriend+"' " )
        for row in c.fetchall():
            if row is None:
               return 0
            else :
                if row[0] == 1:
                    return 1 #da la ban be
                if row[0] == 2:
                    return 3 # da gui loi moi ket ban
                if row[0] == 0:
                    return 2 # da bi block roi

    def checkRequestAddFriend(self):
        check = self.selectdata(self.username,None,None,2) # in ra danh sach nhung thang dang muon ket ban voi minh
        if check == 1:
            print("----------ban muon dong y ket ban voi ai-----------")
            usernameoffriend = input() #nhap ten thang minh muon dong y ket ban vao 
            if self.checkusername(usernameoffriend,None,1) == 1:
                if self.checkBlock(usernameoffriend, self.username) == 3:
                    sql = "update friend set statusfriend = 1 where usernameofob = '"+usernameoffriend+"' and usernameoffriend = '"+self.username+"' "
                    self.updateData(sql)
                    row = self.selectdata( usernameoffriend,None,None, 1) # lay thong tin tuong ung voi usernameoffriend
                    self.insertDataToFriend(self.username,usernameoffriend,row[0],row[1],row[2],"1") #them vao bang friend moi quan he nay
                    return 1
                else : 
                    return 3
            else :
                return 0
        else :
            return 4
            
    def addFriendDefault(self):
        print("-----------nhap ten nguoi can ket ban:")
        usernameoffriend = input()
        check = self.checkusername( usernameoffriend, None, 1)
        if check == 1:
            check = self.checkBlock( self.username, usernameoffriend) # trang thai ket ban cua username
            check1 = self.checkBlock(usernameoffriend, self.username) #trang thai ket ban cua usernameoffriend
            if check == None and check1 == None: #2 dua chua gui loi moi ket ban
                print("vao roi")
                self.addFriend(usernameoffriend) # neu chua gui thi minh gui loi moi ket ban voi no
                print("xong roi")
            if check == None and check1 == 3: # neu no da gui loi moi ket ban roi thi minh update status friend cua no va them ban 
                sql = "update friend set statusfriend = 1 where usernameofob = '"+usernameoffriend+"' and usernameoffriend = '"+ self.username+"' "
                self.updateData(sql)
                row = self.selectdata( usernameoffriend, None,None, 1) # lay thong tin tuong ung voi usernameoffriend
                self.insertDataToFriend( self.username,usernameoffriend,row[0],row[1],row[2],"1") #them vao bang friend moi quan he nay
                print("----------ket ban thanh cong-----------")
            if check == 2:
                print("-----------ban da block nguoi nay----------")
            if check1 == 2:
                print("--------nguoi nay da block ban roi---------")
            if check == 1:
                print("----------2 nguoi da la ban cua nhau---------")
        else :
            print("--------- username :" +usernameoffriend + " khong ton tai-----------")
   
    def addFriend(self,usernameoffriend):  
        if self.username != usernameoffriend: # kiem tra xem co dang tu ket ban voi chinh ban than hay khong
            if self.checkusername( usernameoffriend, None, 1) == 1: #kiem tra xem thang nay co ton tai hay khong
                if self.checkBlock( self.username, usernameoffriend) == 2: # kiem tra xem minh da block no chua
                    print("ban da block " +usernameoffriend + " roi ")
                else :
                    if self.checkBlock(usernameoffriend,self.username) == 2: #kiem tra xem no ra block minh chua
                        print(usernameoffriend + " da block ban roi")
                    else :
                        row = self.selectdata( usernameoffriend, None, None, 1) # lay thong tin tuong ung voi usernameoffriend
                        self.insertDataToFriend( self.username,usernameoffriend,row[0],row[1],row[2],"2") #them vao bang friend moi quan he nay
                        print("da gui loi moi ket ban toi "+usernameoffriend + " thanh cong")
            else :
                        print("tai khoan " + usernameoffriend + " khong ton tai")
        else : print("ban dang tu ket ban voi chinh minh")

    def showListFriendUseplace(self):
        connectToSQlite = sqlite3.connect('appchat.db')
        c = connectToSQlite.cursor()
        c.execute("select distinct place from friend where statusfriend = 1 and usernameofob = '" + self.username + "'")
        rows = c.fetchall()
        count = 0
        
        while count < len(rows): # lay dia diem ra 
            l = list(rows[count])
            count = count + 1
            print(l[0])
            c.execute("select usernameoffriend from friend where place = '" + l[0] + "' and usernameofob = '"+ self.username +"' and statusfriend = 1 ")
            rows1 = c.fetchall() # lay ten nhung nguoi co cung place 
            count1 = 0
            while count1 < len(rows1): # in ra thoi
                l1 = list(rows1[count1])
                print(str(count1+1)+ ": "+ l1[0])
                count1 = count1 + 1

    def showListFriendUseTime(self):
        connectToSQlite = sqlite3.connect('appchat.db')
        c = connectToSQlite.cursor()
        c.execute("select usernameoffriend from friend where statusfriend = 1 and usernameofob = '"+ self.username+"' order by timecontact desc")
        rows = c.fetchall()
        count = 0
        while count <len(rows):
            l = list(rows[count])
            print(l[0])
            count += 1

    def ShowListFriend(self):
        self.showListFriendUseTime()
        print("An ctrl + c de hien thi theo thanh pho")
        request = msvcrt.getch()
        if request == b'\x03':
            self.showListFriendUseplace()
            request = input()
        else : 
            return 0

    def showInformation(self, namefriend):
        rows = self.selectdata( self.username,namefriend, None,3)
        if len(rows) == 0:
            print("--------------khong co trong danh sach ban be hoac da block roi nhe-------------- ")
        else :
            # in thong tin ra cho chung no xem
            rows = self.selectdata( self.username, namefriend,None, 4)
            print(rows[0][0])
            print(rows[0][1])
            print(rows[0][2])

            request = "chua ro"
            while request != b'\x1B':
                print("An ctrl + F de sua thong tin ")
                print("An ctrl + R de nhan tin ")
                print("An Esc de thoat ra")
                print("---------ban muon dung chuc nang nao-----------")
                request = msvcrt.getch()
                if request == b'\x06':
                    print("nhap thong tin moi: ")
                    print("nhap noi o:")
                    place = input()
                    print("nhao gioi tinh: ")
                    sex = input()
                    print("nhap ngay sinh: ")
                    birhtday = input()
                    self.updateData("update friend set place = '"+place+"' , sex= '"+sex+"' , birthday = '"+ birhtday +"' where usernameofob ='"+ self.username+"' and usernameoffriend ='"+namefriend+"'")
                if request == b'\x12':
                    self.replyMessage(namefriend)

    def watchInformationFriend(self):
        request = "chua ro"
        while request != "0":
            print("-----------nhap ten nguoi ban muon xem thong tin------------")
            namefriend = input()
            self.showInformation(namefriend)
            print("------ ban co muon tiep tuc khong (1 | 0) ------")
            request = input()

    def delfriend(self):
        print("-----------nhap ten nguoi ban muon xoa-----------")
        namefriend = input()
        check = self.checkusername( namefriend, None, 1)
        if check == 0:
            return 0
        if check == 1:
            check = self.checkBlock(self.username, namefriend)
            if check == None :
                print("---------- 2 nguoi khong phai la ban cua nhau----------")
            else:
                sql = "delete from friend where usernameofob ='" + self.username + "' and usernameoffriend = '" + namefriend + "'"
                self.updateData(sql)
                sql = "delete from friend where usernameofob ='" + namefriend + "' and usernameoffriend = '" +  self.username + "'"
                self.updateData(sql)
                return 1

    def blockFriend(self):
        print("--------nhap ten nguoi ban muon block------------")
        namefriend = input()
        check = self.checkusername( namefriend, None, 1)
        if check == 1:
            check = self.checkBlock( self.username, namefriend)
            if check == 2:
                return 2
            if check == 1 or check == 3:
                sql = "update friend set statusfriend = 0 where usernameofob = '" + self.username + "' and usernameoffriend = '" + namefriend + "'"
                self.updateData(sql)
                return 1 
            if check == None:
                sql ="insert into friend(usernameofob, usernameoffriend, statusfriend) values('" + self.username + "' , '" + namefriend + "' ,  0)"
                self.updateData(sql)
                return 1
        else : 
            return 0

    def sendMessageUseName( self):
        print("------Ten nguoi gui:")
        print("An ctrl + r de gui tin nhan theo id")
        request = msvcrt.getch()
        if request == b'\x12':
            sql = "select id , usernameoffriend from friend where usernameofob = '" + self.username + "'  and statusfriend = 1"
            rows = self.selectDefault(sql)
            for row in rows:
                print("id:" + str(row[0]))
                print("username : "+str(row[1]))
            self.sendMessageUseId()
        else:
            print("--------nhap ten nguoi ban muon gui toi")
            namefriend = input()
            if namefriend == self.username: # kiem tra xem ten    
                print("----------dung tu gui tin nhan cho minh----------")
            else: 
                check =  self.checkusername(namefriend,None, 1) 
                if check == 1:
                    check = self.checkBlock( self.username, namefriend)
                    check1 = self.checkBlock( namefriend, self.username)
                    if check == 2 or check1 == 2:
                        print("----------ban da block nguoi nay hoac username nay da block ban roi------------")
                    else:
                        print("---------Noi dung tin nhan:")
                        content = input()
                        rows = self.selectdata( self.username, namefriend, None, 3) # kiem tra xem co ton tai ban be voi nguoi nay khong
                        time_second = time.time()
                        if len(rows) != 0:
                            sql = "update friend set timecontact = '" + str(time_second) + "' where usernameofob = '" + namefriend + "' and usernameoffriend = '" + self.username + "' "
                            self.updateData(sql)
                            sql = "update friend set timecontact = '" + str(time_second) + "' where usernameofob = '" + self.username + "' and usernameoffriend = '" + namefriend + "' "
                            self.updateData(sql)
                        self.insertDataToMessage( self.username, namefriend, content, time_second)
                        print("----------gui tin nhan thanh cong----------")
                else:
                    print("------------username khong ton tai------------")

    def sendMessageUseId( self):
        print("---------------nhap id cua nguoi ban muon gui tin nhan-----------")
        id = input()
        print("gui toi:")
        row = self.selectdata( self.username, None, id, 5)
        
        if row == None: # ten namefriend
            print("----------khong co id phu hop----------")
        else:
            print(row[0])
            print("---------Noi dung tin nhan: -----------")
            content = input()
            time_second = time.time()
            sql = "update friend set timecontact = '" + str(time_second) + "' where usernameofob = '" + row[0] + "' and usernameoffriend = '" + self.username + "' "
            self.updateData(sql)
            sql = "update friend set timecontact = '" + str(time_second) + "' where usernameofob = '" + self.username + "' and usernameoffriend = '" + row[0] + "' "
            self.updateData(sql)
            self.insertDataToMessage( self.username, row[0], content, time_second)
            print("---------Gui tin nhan thanh cong --------")

    def showMessageSend( self):
        sql = "select id , revicer, content from message where sender = '" + self.username + "' and statussender = 1 "
        rows = self.selectDefault(sql)
        for row in rows:
            print("Stt : " + str(row[0]))
            print("Nguoi Nhan: " + str(row[1]))
            print("Noi dung :"+ str(row[2]))
            print("----------------------")
        print("Ctrl + R  de doc tin nhan")
        print("Ctrl + D de xoa tin nhan")
        print("--------ban dung chuc nang nao-------")
        request1 = msvcrt.getch()
        if request1 == b'\x12':
            self.readMessageSend()
        if request1 == b'\x04': 
            self.delMessageSend()

    def showMessageRevice( self):
        sql = "select id , sender, content from message where revicer = '" + self.username + "' and statusrevicer = 1 "
        rows = self.selectDefault(sql)
        for row in rows:
            print("Stt : " + str(row[0]))
            print("Nguoi gui: " + str(row[1]))
            print("Noi dung :"+ str(row[2]))
            print("----------------------")
        print("Ctrl + R  de doc tin nhan")
        print("Ctrl + D de xoa tin nhan")
        print("--------ban dung chuc nang nao-------")
        request1 = msvcrt.getch()
        if request1 == b'\x12':
            self.readMessageRevice()
        if request1 == b'\x04': 
            self.delMessageRevice()

    def delMessageRevice( self):
        id = input("---------nhap id tin nhan ban muon xoa:--------- ")
        sql = "select sender from message where statusrevicer = 1 and id =" + id + " and revicer = '" + self.username + "' "
        rows = self.selectDefault(sql)
        if len(rows) == 0:
            print("-----------id nay khong phu hop----------")
        else:
            sql = "update message set statusrevicer = 0 where id = '" + id + "'"
            self.updateData(sql)
            print("----------da xoa thanh cong roi nhe------------")

    def showMessage(self):
        print("---------nhap danh sach tin nhan ban muon xem-----------")
        print("1 danh sach tin nhan da nhan")
        print("2 danh sach tin nhan da gui")
        request = input("--------ban chon chuc nang nao---------")
        if request == "1":
            self.showMessageRevice()
        if request == "2":
            self.showMessageSend()
    
    def delMessageSend( self):
        print("----------nhap id tin nhan ban muon xoa:")
        id = input()
        sql = "select revicer from message where statussender = 1 and id =" + id + " and sender = '" + self.username + "'"
        rows = self.selectDefault(sql)
        if len(rows) == 0:
            print("---------- id nay khong phu hop-----------")
        else:
            sql = "update message set statussender = 0 where id = '" + id + "'"
            self.updateData(sql)
            print("--------da xoa thanh cong--------")
        
    def readMessageRevice( self):
        print("----------de nghi ban nhap id cua tin nhan can xem:")
        id = input()
        sql = "select sender from message where statusrevicer = 1 and id ='" + id + "' and revicer = '" + self.username + "' "
        rows = self.selectDefault( sql )
        if len( rows ) == 0:
            print("--------id nay khong phu hop----------")
        else :
            sql = "select content, sender from message where  statusrevicer = 1 and revicer = '" + self.username + "' and id =" + id
            rows = self.selectDefault( sql )
            print("Nguoi gui: " + rows[0][1])
            print("Noi dung:" + rows[0][0])
            request1 = input("co muon tra loi tin nhan nay khong? (1 | 0)")
            if request1 == "1":
                self.replyMessage( rows[0][1])

    def readMessageSend( self):
        print("---------de nghi nhap id cua tin nhan can xem------------")
        id = input()
        sql = "select revicer from message where statussender = 1 and id ='" + id + "' and sender = '" + self.username + "' "
        rows = self.selectDefault(sql)
        if len(rows) == 0:
            print("----------"+  id + " la id nay khong phu hop ----------")
        else :
            sql = "select content, revicer from message where  statussender = 1 and sender = '" + self.username + "' and id ='" + id+ "'"
            rows = self.selectDefault(sql)
            print("Nguoi nhan: " + rows[0][1])
            print("Noi dung: "+ rows[0][0])
            request1 = input("--------co muon gui lai tin nhan khong(1 | 0)--------")
            if request1 == "1":
                return self.reSendMessage( rows[0][1], rows[0][0])


    def reSendMessage(self, To , Content):
        time_second = time.time()
        sql = "update friend set timecontact = '" + str(time_second) + "' where usernameofob = '" + To + "' and usernameoffriend = '" + self.username + "' "
        self.updateData(sql)
        sql = "update friend set timecontact = '" + str(time_second) + "' where usernameofob = '" + self.username + "' and usernameoffriend = '" + To + "' "
        self.updateData(sql)
        self.insertDataToMessage( self.username, To, Content, time_second)
        print("------------da gui lai tin nhan toi " + To+ " ------------")

    def replyMessage(self, To):
        print("--------nhap noi dung tin nhan------")
        content = input()
        time_second = time.time()
        sql = "update friend set timecontact = '" + str(time_second) + "' where usernameofob = '" + To + "' and usernameoffriend = '" + self.username + "'"
        self.updateData(sql)
        sql = "update friend set timecontact = '" + str(time_second) + "' where usernameofob = '" + To + "' and usernameoffriend = '" + self.username + "'"
        self.updateData(sql)
        self.insertDataToMessage( self.username, To, content, time_second)
        print("-------------da gui tin nhan tra loi toi " + To +" -----")
