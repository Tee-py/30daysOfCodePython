"""A python function that converts integer to mandarin"""


def toMandarin(num):
    mandarin_dict = {1:'Yi', 2:'Er', 3:'San', 4:'Si', 5:'Wu', 6:'Liu',\
                    7:'Qi', 8:'Ba', 9:'Jiu', 10:'Shi', 0:'Ling'}
    if type(num)!=int or num<0:
        return 'Argument should be a positive integer'
    else:
        try:
            if num>10 and num<100:
                if num%10==0:res = mandarin_dict[num//10]+' '+mandarin_dict[10]
                else:
                    if num//10==1:res = mandarin_dict[10]+' '+mandarin_dict[num%10]
                    else:res = mandarin_dict[num//10]+' '+mandarin_dict[10]+' '+mandarin_dict[num%10]
            elif num>=100 and num<110:
                if num%100==0:res = mandarin_dict[num//100]+' bai'
                else:res = mandarin_dict[num//100]+' bai '+mandarin_dict[0]+' '+mandarin_dict[num%100]
            else:res = mandarin_dict[num]
            return res
        except:
             return 'Argument should be a positive integer'

man = [x for x in range(1,50)]
print(toMandarin(106))