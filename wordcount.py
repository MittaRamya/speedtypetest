import time
String="welcome to c language"
wordcount=len(String.split())
print(String)
while True:
    t0=time.time()
    inputtext=str(input("enter the sentance:"))
    t1=time.time()
    accuracy=len(set(inputtext.split())&set(String.split()))
    accuracy=accuracy/wordcount
    timetaken=t1-t0
    wpm=wordcount/timetaken
    print("WPM",wpm,"accuracy",accuracy,"Timetaken",timetaken)
