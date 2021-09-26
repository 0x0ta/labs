def create_phone_number(n):
    area = '('+str(n[0])+str(n[1])+str(n[2])+") "+str(n[3])+str(n[4])+str(n[5])+"-"+str(n[6])+str(n[7])+str(n[8])+str(n[9]) 
    return area

def create_phone_number_refactor(n):
    area = f'({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}'
    return area
