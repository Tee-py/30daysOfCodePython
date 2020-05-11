def find_edit_distance(str1, str2):
    if type(str1)!=str or type(str2)!=str:
        return 'Invalid argument... argument should be a string'
    else:
        try:
            if str1 == "":return len(str2)
            elif str2 == "":return len(str1)
            if str1[-1] == str2[-1]:init = 0
            else:init = 1
            distance = min([find_edit_distance(str1[:-1], str2)+1,find_edit_distance(str1, str2[:-1])+1,find_edit_distance(str1[:-1], str2[:-1]) + init])
            return distance
        except:
            return 'Invalid argument passed..argument should be a string'

print(find_edit_distance('Tayolade', "float"))
