
#Functions that handle triangle type
def isRightAngled(tuple):
    tuple_lst = list(tuple);tuple_lst.sort()
    if tuple_lst[-1]**2==tuple_lst[0]**2+tuple_lst[1]**2:return True
    else:return False
def isIsoceles(tuple):
    for i in list(tuple):
        if list(tuple).count(i)==2:return True;break
        else:continue
    return False
def isEquilateral(tuple):
    if list(tuple).count(list(tuple)[0])==3:return True
    else:return False

def desc_triangle(s_tuple):
    if type(s_tuple)!=tuple:
        return 'Argument should be a tuple with the three sides of the triangle'
    elif len(s_tuple)!=3:
        return 'Incomplete sides...the tuple should contain the three sides of the triangle'
    elif type(s_tuple[0])==str or type(s_tuple[1])==str or type(s_tuple[2])==str:
        return 'Input tuple should contain int or floats only'
    elif s_tuple[0]==0 or s_tuple[1]==0 or s_tuple[2]==0:
        return 'A triangle cannot have a side with length of 0'
    else:
        output = []
        if isRightAngled(s_tuple)==True:output.append('Right Angled Triangle')
        elif isEquilateral(s_tuple)==True:output.append('Equilateral Triangle')
        elif isIsoceles(s_tuple)==True:output.append('Isosceles Triangle')
        else:output.append('Scalene Triangle')
        #the area using Hero's formulae
        s = (s_tuple[0]+s_tuple[1]+s_tuple[2])*0.5
        area = (s*(s-s_tuple[0])*(s-s_tuple[1])*(s-s_tuple[2]))**0.5
        output.append(area)

        return tuple(output)

print(desc_triangle((2,5,6)))
