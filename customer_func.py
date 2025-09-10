def insertData(custlist, page):
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
    page = len(custlist)-1
    return page

def curView(custlist,page):
    if page >= 0:
            print(f"현재 페이지는 {page + 1}페이지 입니다.")
            print(custlist[page])
    else:
        print("입력된 내용이 없습니다.")

def preView(custlist,page):
    if page <= 0:
            print("첫번째 페이지 입니다.")
            print(custlist[page])
    else:
        page = page-1
        print(f"현재 페이지는 {page + 1}페이지 입니다.")
        print(custlist[page])
    return page

def nextView(custlist,page):
    if page >= len(custlist)-1:
            print("마지막 페이지입니다.")
            print(custlist[page])
    else:
        page = page+1
        print(f"현재 페이지는 {page + 1}페이지 입니다.")
        print(custlist[page]) 

def updateData():
    pass

def deleteData():
    pass