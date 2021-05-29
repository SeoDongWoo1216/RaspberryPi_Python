# 계산기를 무한반복 실행하는 프로그램

try:
   # 무한 반복
   while True:
      a = int(input("첫번째 수 입력 : "))
      b = int(input("두번째 수 입력 : "))
      c = input("연산 기호 입력 : ")

      def calcul(a, b, c):
         if(c == '+'):
         #어자피 input이 int로 받으므로 문자열 검사가  필요없긴함
         #if(type(a) == type(1) and type(b) == type(1)):
            print("더하기 값 = ", end=' ')
            return a + b
         #else:
         #  print("문자를 입력했습니다. 0을 반환합니다.")
         #  return 0
         elif(c == '-'):
            print("빼기   값 = ", end=' ')
            return a - b
         elif(c == '*'):
            print("곱하기 값 = ", end=' ')
            return a * b
         elif(c == '/'):
            if(b == 0):
               print("0으로는 나눌 수 없습니다. 0을 반환합니다.")
               return 0
            else:
               print("나누기 값 = ", end=' ')
               return a/b
         else:
            print("연산 기호를 입력해주세요. 0을 반환합니다.")
            return 0

# 컨트롤 + C를 입력할 경우
except KeyboardInterrupt:
   print("종료합니다.")
   exit()


res = calcul(a, b, c)
print(res)
print()
