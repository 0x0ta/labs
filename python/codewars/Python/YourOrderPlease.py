import re
def order(sentence):
    words = str(sentence).split(' ')
    output = [None] * len(words)
    outputlist = []
    for each in words:
        try:
            number = re.findall("\d+", each)
            num = str(number).replace("['",'').replace("']",'')
            output[int(num)-1] = each
        except ValueError:
            output[0] = each
    return str(output).replace("['",'').replace("']",'').replace('"','').replace("', ",' ').replace(" '",' ')