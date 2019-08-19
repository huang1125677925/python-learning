

def seven_check_method(l,value,threshold,count):
    num=0
    for i in l:
        if abs(value-i)>threshold:
            num+=1
        
    if num>count:
        return True
    else:
        return False

def ewma_check_method(l):
    d=pd.Series(l)
    exp=d.ewm(span=5,adjust=True).mean()
    staDev=d.ewm(span=5,adjust=True).std()
    if abs(l[-1]-exp.values[-1])>3*staDev.values[-1]:
        return True
    else:
        return False
    

def seven_point_check_method(l,value,max_threshlod,min_threshlod):
    if value>max(l)*max_threshlod or value<min(l)*min_threshlod:
        return True
    else:
        return False


def amplitude_check_method(l,value):
    def cal_apmlitude(value):
        return round((value[1]-value[0])/value[0],3)



    


















if __name__ == '__main__':
    import numpy
    l=list(numpy.random.randint(1,199,100))
    ewma_check_method(l)
    
