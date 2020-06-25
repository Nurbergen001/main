if False:  
    questions = ["Выбери класс:","Луник","РАЗВЕДЧИК"]
    userAnswers = []
    userAnswersNum = []
    i = 0
    for question in questions:
        if not i:
            print(question)
        else: 
            print("{0}.{1}".format(i,question))
        i += 1
    tmp = int(input())
    userAnswersNum.append(tmp)
    userAnswers.append(questions[tmp])
    print(userAnswersNum)
    print(userAnswers)
    print("Нам как раз таки нужен {0}".format(userAnswers[0]))


#https://support.microsoft.com/ru-kz/help/306541/how-to-https://support.microsoft.com/ru-kz/help/306541/how-to-manage-stored-user-names-and-passwords-on-a-computer-that-is-no




#https://1cloud.ru/help/windows/sistemy-kontrolya-versij-git-v-windows

a = input()
print(len(a))
#x = len(a)

x = 1
if a[0] == a[x]:
    print("True")
else:
    print("False")


 