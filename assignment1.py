grade = int(input())

while True:
  if 90<= grade <=100:
      print("A")
      break
  elif 80<= grade <90:
      print("B")
      break
  elif 70<= grade <80:
      print("C")
      break
  elif 60<= grade <70:
      print("D")
      break
  elif 0<= grade <60:
      print("F")
      break
  else:
      print("잘못된 값을 입력했습니다.")
      grade = int(input())