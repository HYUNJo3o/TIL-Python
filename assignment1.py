grade = int(input())

while 0<= grade <=100:

if 90<= grade <=100:
    print("A")
elif 80<= grade <90:
    print("B")
elif 70<= grade <80:
    print("C")
elif 60<= grade <70:
    print("D")
elif 0<= grade <60:
    print("F")
else:
    print("잘못된 값을 입력했습니다.")
    grade = int(input())