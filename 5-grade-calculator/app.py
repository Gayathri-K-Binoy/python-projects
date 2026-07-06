print(f"GRADE CALCULATOR")
scores=[]#list 
while True:
    score=input("Enter a test score (or 'done') :")
    if score.lower()=="done" : #both lower and upper should work
        print("Goodbye!")
        break
    scores.append(float(score))
    #typecasting is important
    curravg= sum(scores)/len(scores)
    print(f"Average Score: {curravg:.1f}")
    if curravg>=90:
        print("Grade: A")
    elif curravg>=80:
        print("Grade: B")
    elif curravg>=70:
        print("Grade: C")
    else:
        print("Grade: D or F")
