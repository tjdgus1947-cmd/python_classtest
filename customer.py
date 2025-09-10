import sys

class Customer:
    def __init__(self):
        self.custlist=[{'name': '김성현', 'gender': 'M', 'email': 'tjdgus1947@aaa.com', 'birthyear': 2001},
          {'name': '정민혁', 'gender': 'M', 'email': 'MIN01@aaa.com', 'birthyear': 2002},
          {'name': '문상현', 'gender': 'F', 'email': 'tkdgus5837@aaa.com', 'birthyear': 2003},
          {'name': '홍성일', 'gender': 'F', 'email': 'HONG01@aaa.com', 'birthyear': 2004}]
        self.page=3
        while True:
            self.exe(self.display())
            
    def display(self):
        choice=input('''
        다음 중에서 하실 일을 골라주세요 :
        I - 고객 정보 입력
        C - 현재 고객 정보 조회
        P - 이전 고객 정보 조회
        N - 다음 고객 정보 조회
        U - 고객 정보 수정
        D - 고객 정보 삭제
        Q - 프로그램 종료
        ''').upper()
        return choice
        
    def exe(self,choice):
        if choice=="I":                
            print("고객 정보 입력")
            self.insertData()
        
        elif choice=="C":
            print("현재 고객 정보 조회")
            self.curView()
                
        elif choice == 'P':
            print("이전 고객 정보 조회")
            self.preView()
            
        elif choice == 'N':
            print("다음 고객 정보 조회")
            self.nextView()    
                
        elif choice=='D':
            print("고객 정보 삭제")
        elif choice=="U": 
            print("고객 정보 수정")
        elif choice=="Q":
            print("프로그램 종료")
            sys.exit()            
                    
    def insertData(self):
        customer={'name':'','gender':'',"email":'',"birthyear":''}
        customer['name'] = input("이름 : ")
            
        while True:
            gender = input("성별(M/F) : ")
            gender = gender.upper()
            if gender in ("M", "F"):
                customer["gender"] = gender
                break
                
        while True:
            email = input("이메일 : ")
            if "@" in email:
                customer["email"] = email
                break
            else:
                print("이메일에는 @가 포함되어야 합니다.")
                    
        while True:
            birthyear= input("출생년도(4자리) : ")
            if birthyear.isdigit() and len(birthyear) == 4:
                customer["birthyear"] = int(birthyear)
                break
            
        self.custlist.append(customer)
        print(customer)
        print(self.custlist)
        self.page = len(self.custlist)-1

    def curView(self):
        if self.page >= 0:
                print(f"현재 페이지는 {self.page + 1}페이지 입니다.")
                print(self.custlist[self.page])
        else:
            print("입력된 내용이 없습니다.")

    def preView(self):
        if self.page <= 0:
                print("첫번째 페이지 입니다.")
                print(self.custlist[self.page])
        else:
            self.page = self.page-1
            print(f"현재 페이지는 {self.page + 1}페이지 입니다.")
            print(self.custlist[self.page])
        return self.page

    def nextView(self):
        if self.page >= len(self.custlist)-1:
                print("마지막 페이지입니다.")
                print(self.custlist[self.page])
        else:
            self.page = self.page+1
            print(f"현재 페이지는 {self.page + 1}페이지 입니다.")
            print(self.custlist[self.page]) 

    def updateData(self):
        pass

    def deleteData(self):
        pass

    
Customer()