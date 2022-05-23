def openOrSenior(data):
    outputlist = []
    for each in data:
        print(str(each[0]) + " " + str(each[1]))
        if int(each[0]) >= 55 and int(each[1]) > 7:
            outputlist.append("Senior")
        else:
            outputlist.append("Open")
    return outputlist