print("do you play the game")
ans=input()
points=0
if(ans=="YES"):
 print("go ahead")
 print("Q.1= Highest percentage of air consists of?")
 print("options:")
 print("A. Oxygen")
 print("B.carbon dioxide")
 print("C.nitrogen")
 print("D. Argon")
 ans1=input()
 if(ans1=="C"):
  print("correct")
  points=points+10
  print(points)
 else:
     print("wrong")
     print(points)
 print("Q.2= the taj mahal is being affected by?")
 print("options:")
 print("A. Nosie pollution")
 print("B. Air pollution")
 print("C. water pollution")
 print("D. none of these")
 ans2=input()
 if(ans2=="B"):
  print("correct")
  points=points+10
  print(points)
 else:
     print("wrong")
     print(points)

 print("Q.3= most polluted river in india?")
 print("options:")
 print("A. yamuna")
 print("B. cavery")
 print("C. chenba")
 print("D. ganga")
 ans3=input()
 if(ans3=="D"):
  print("correct")
  points=points+10
  print(points)
 else:
     print("wrong")
     print(points)

 print("Q.4= air pollution causes?")
 print("options:")
 print("A. Global warming")
 print("B.respiratory problems")
 print("C. Soil erosion")
 print("D. none of these")
 ans4=input()
 if(ans4=="B"):
  print("correct")
  points=points+10
  print(points)
 else:
     print("wrong")
     print(points)
 
 print("Q.5= Green house gas is?")
 print("options:")
 print("A. Oxygen")
 print("B.carbon dioxide")
 print("C.nitrogen")
 print("D. Argon")
 ans5=input()
 if(ans5=="B"):
  print("correct")
  points=points+10
  print("total points:",points)
 else:
     print("wrong")
     print(points)
else:
    print("chal nikal")
