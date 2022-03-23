# id = "jamsuham75"
# pw = "1234"

# userid = input("사용자 아이디: ")
# userpw = input("사용자 비밀번호: ")

# if userid == id:
#     if userpw == pw:
#         print("로그인 되었습니다.")
#     else:
#         print("비밀번호가 틀렸습니다.")
# else:
#     print("아이디가 틀렸습니다.")

# id = "jamsuham75"
# pw = "1234"

# def account(userid, userpw):
#     if userid == id:
#         if userpw == pw:
#             print("로그인 되었습니다.")
#         else:
#             print("비밀번호가 틀렸습니다.")
#     else:
#         print("아이디가 틀렸습니다.")

# user_id = input("사용자 아이디: ")
# user_pw = input("사용자 비밀번호: ")

# account(user_id, user_pw)

coffee = '' # 비워도 되고 써도 됨 어차피 밑에서 입력값 받음

coffee = input("커피를 선택하세요(아메리카노, 카페라떼, 카페모카): ")
print()

print("1. 물을 준비한다.")
print("2. 커피를 탄다.")

if coffee == '아메리카노':
    print("3. 아메리카노를 탄다.")
elif coffee == '카페라떼':
    print("3. 카페라떼를 탄다.")
elif coffee == '카페모카':
    print("3. 카페모카를 탄다")
else: ("3. 아무거나 탄다.")

print("4. 물을 붓는다.")
print()
print(coffee, "한 잔 서비스 완료")