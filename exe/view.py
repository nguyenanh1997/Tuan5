class view:
    def signIn(self, status):
        if status == 1:
            print("dang nhap thanh cong")
        if status == 2:
            print("dang nhap that bai")

    def signUp(self, status):
        if status == 1:
            print("dang ky thanh cong ")
        if status == 0:
            print("tai khoan nay da ton tai")
    
    def addFriend(self, status, namefriend):
        if status == 4:
            print(namefriend +" nay da block ban")
        if status == 5:
            print("ban da block hoac ket ban voi " + namefriend)
        if status == 2:
            print(namefriend + " khong ton tai")
        if status == 3:
            print(namefriend + " la tai khoan cua ban ma")

    def checkAddFriend(self, status):
        if status == 1:
            print("them ban thanh cong")
        if status == 0:
            print("ten vua nhap khong ton tai")
        if status == 3:
            print("de nghi chi nhap ten nhung nguoi co trong danh sach")
        if status == 4:
            print("khong co ai gui loi moi ket ban")

    def delFriend(self, status):
        if status == 1:
            print("da huy ket ban")
        if status == 0:
            print("nguoi nay khong ton tai")

    def blockFriend(self, status):
        if status == 1:
            print("block thanh cong")
        if status == 0:
            print("tai khoan khong ton tai")
        if status == 2:
            print("da bi block tu truoc roi")
