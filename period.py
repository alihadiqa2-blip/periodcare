print("===========================================")
print("welcome to periodcare")
print("period symptoms and PCOS awarness")
name=input("what is your name?")
print("hello",name)
print("welcome to your periodcare healthcare assessment")
print("\n--- menstrual health questions---")
cycle=int(input("how many days is your menstrual cycle"))
print("your cycle length is",cycle,"days.")
duration=int(input("how many days does your period last"))
print("your period lasts",duration,"days.")
print("\n--period symptoms --")
pain=input("do you experience any pain")
print("period pain recoreded:",pain)
mood_symptoms=input("do you experience mood symptoms")
print("mood symptoms recorded:",mood_symptoms)
acne=input("do you experience acne") 
print("experience acne:",acne)
import csv 
with open("period_data.csv","a",newline="")as file:   
     writer=csv.writer(file)
     writer.writerow([
      cycle,
      duration,
      pain,
      mood_symptoms,
      acne
])
print("data saved succesfully")
print("\n-- periodcare data analysis---")
if acne.lower()=="yes":
     print("acne reported by the user.")
else:
     print("no acne reported by this user.") 

if pain.lower()=="yes":
     print("period pain reported by this user.")
else:
     print("no period pain reporeted by this user")
import matplotlib.pyplot as plt
symptoms=["pain","mood","acne"]
values=[0,0,0]
if pain.lower().strip()=="yes":
     values[0]=1
if mood_symptoms.lower().strip()=="yes":
     values[1]=1
if acne.lower().strip()=="yes":
     values[2]=1
plt.bar(symptoms,values,color="pink")
plt.title("periodcare symptom analysis")
plt.xlabel("symptoms")
plt.ylabel("reported(1=yes,0=no)")
plt.savefig("periodcare_graph.png")
plt.show()


















