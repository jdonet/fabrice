from modele.Question import Question
from modele.Reponse import Reponse
from modele.Quizz import Quizz
import datetime
import json


r1 = Reponse ( "fb", "le Dimanche 14 Juillet 2019.",  0, 0, 0, 0, "shortanswerquestionanswer",0)
r2 = Reponse ( "fb", "le Jeudi",  0, 0, 0, 0, "shortanswerqr",1)
r3 = Reponse ( "fb", "le Vendredi",  0, 0, 0, 0, "shortanswerqr",0)

f = open('reponse.json', 'w')
json.dump(r1, f)
f.close()


listRep = []
listRep.append(r1)
listRep.append(r2)
listRep.append(r3)

q1 = Question ("fb", "A travers le monde , leprochain Pi day ou jour de Pi tombera :", 0, 0, "shortanswer", "Le prochain Jour de Pi", listRep)

r1 = Reponse ( "fb", "oui",  0, 0, 0, 0, "shortanswerquestionanswer",0)
r2 = Reponse ( "fb", "non",  0, 0, 0, 0, "shortanswerquestionanswer",0)
r3 = Reponse ( "fb", "probablement",  0, 0, 0, 0, "shortanswerqr",1)

listRep = []
listRep.append(r1)
listRep.append(r2)
listRep.append(r3)

q2 = Question ("fb", "J'aime les frites", 0, 0, "shortanswer", "J'aime les frites", listRep)

listeQuestions = []
listeQuestions.append(q1)
listeQuestions.append(q2)

quizz = Quizz("le quizz", "la description", listeQuestions)

now = datetime.datetime.now()

nomF = "../web/out" + "_" + str(now.year) + "-" + str(now.month) + "-" + str(now.day) + "-" + str(now.hour) + "-" + str(now.minute) + "-" + str(now.second)
f = open(nomF, "w")

f.write(quizz.toJSON())
f.close()

print()
