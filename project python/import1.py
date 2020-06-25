def questionsss(quest):
    i=0
    for question in quest:
        if not i:
            print(question)
        else:
            print("{0}.{1}".format(i, question))
        i +=1

