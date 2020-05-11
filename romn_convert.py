
def roman_convert_to_int(numeral):
    roman_list = ['I','V','X','L','C','D','M','IV','IX','XL','XC','CD','CM']
    int_list = [1,5,10,50,100,500,1000,4,9,40,90,400,900]
    numeral = numeral.upper()
    value = 0
    i=0
    while i<(len(numeral)):
        if numeral[i:i+2] in roman_list:
            p = roman_list.index(numeral[i:i+2])
            value += int_list[p]
            i+=2
        elif numeral[i] in roman_list:
            p = roman_list.index(numeral[i])
            value += int_list[p]
            i+=1
    return value
print(roman_convert_to_int('mcmcdxliv'))
print(roman_convert_to_int('cdiii'))
print(roman_convert_to_int('xxivlm'))
print(roman_convert_to_int('mcm'))

