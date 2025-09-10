import customer_func as cf

custlist=[{'name': '김성현', 'gender': 'M', 'email': 'tjdgus1947@aaa.com', 'birthyear': 2001},
          {'name': '정민혁', 'gender': 'M', 'email': 'MIN01@aaa.com', 'birthyear': 2002},
          {'name': '문상현', 'gender': 'F', 'email': 'tkdgus5837@aaa.com', 'birthyear': 2003},
          {'name': '홍성일', 'gender': 'F', 'email': 'HONG01@aaa.com', 'birthyear': 2004}]
page=3
 
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
    ''').upper()

    if choice=="I":                
        print("고객 정보 입력")
        page = cf.insertData(custlist, page)
        
    elif choice=="C":
        print("현재 고객 정보 조회")
        cf.curView(custlist,page)
            
    elif choice == 'P':
        print("이전 고객 정보 조회")
        cf.preView(custlist,page)
        
    elif choice == 'N':
        print("다음 고객 정보 조회")
        cf.nextView(custlist,page)    
            
    elif choice=='D':
        print("고객 정보 삭제")
    elif choice=="U": 
        print("고객 정보 수정")
    elif choice=="Q":
        print("프로그램 종료")
        break
