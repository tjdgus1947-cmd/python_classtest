import re
custlist=[]
page=-1

 
    
  
while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''')  

    if choice=="I":        
        print("고객 정보 입력")
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
        
        custlist.append(customer)
        print(customer)
        print(custlist)
        
    elif choice=="C":
        print("현재 고객 정보 조회")
    elif choice == 'P':
        print("이전 고객 정보 조회")
    elif choice == 'N':
        print("다음 고객 정보 조회")
    elif choice=='D':
        print("고객 정보 삭제")
    elif choice=="U": 
        print("고객 정보 수정")
    elif choice=="Q":
        print("프로그램 종료")
        break
