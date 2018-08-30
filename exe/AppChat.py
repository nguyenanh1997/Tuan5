from model import model
from view import view

MODEL = model()
VIEW = view()
request = 0
while request != "3":
    print("1 Dang nhap")
    print("2 Dang ky")
    print("3 thoat chuong trinh")
    print("ban chon chuc nang nao")
    request = input()
    if request == "1":
        status = MODEL.SignIn()
        VIEW.signIn(status)
        if status == 1:
            request1 = "chua ro"
            while request1 != "9":
                print("1 ket ban")
                print("2 Hien thi danh sach ban be")
                print("3 xoa ban be")
                print("4 Chan")
                print("5 loi moi ket ban")
                print("6 Hien thi thong tin chi tiet cua 1 nguoi ban")
                print("7 gui tin nhan")
                print("8 hien thi danh sach tin nhan")
                print("9 thoat")
                request1 = input()
                if request1 == "1":
                    MODEL.addFriendDefault()
                if request1 == "2":
                    MODEL.ShowListFriend()
                if request1 == "3":
                    status = MODEL.delfriend()
                    VIEW.delFriend(status)
                if request1 == "4":
                    status = MODEL.blockFriend()
                    VIEW.blockFriend(status)
                if request1 == "5":
                    request2 = "chua ro"
                    while request2 != "0":
                        status = MODEL.checkRequestAddFriend()
                        VIEW.checkAddFriend(status)
                        print("--------ban co muon tiep tuc(1 || 0 )--------")
                        request2 = input()
                if request1 == "6":
                    MODEL.watchInformationFriend()
                if request1 == "7":
                    MODEL.sendMessageUseName()
                if request1 == "8":
                    MODEL.showMessage()
    if request == "2":
        status = MODEL.SignUp()
        VIEW.signUp(status)
