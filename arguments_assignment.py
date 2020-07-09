def function(*details):
    average=sum(details[1:])/(len(details)-1)
    print(details[0]+" - "+str(average))

function("Mala",80,96,84,70,56)
