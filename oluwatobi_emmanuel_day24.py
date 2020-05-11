"""
A python function that convert intensive properties to specified units by accepting
a tuple of the values of the temp and pressure and another tuple of the units to be converted
to and returns a tuple of the intensive properties in their appropriate units.
"""
def toPascal(pressure):return pressure
def to_atm(pressure):return pressure/101325
def to_mmHg(pressure):return pressure/133
def toBar(pressure):return pressure/100000
def toCelcius(temperature):return temperature-273
def toFarenheit(temperature):return temperature*9/5-459.67
def toRankine(temperature):return temperature*9/5

def intensive_properties(tupl1,tupl2):
    if type(tupl1)!=tuple or type(tupl2)!=tuple:
        return "Both arguments should be a tuple e.g intensive_properties((123,56),('atm','c'))"
    else:
        try:
            output_lst = []
            #Handle pressure conversion
            if tupl2[0].lower() == 'atm':output_lst.append(to_atm(tupl1[0]))
            elif tupl2[0].lower() == 'pa':output_lst.append(toPascal(tupl1[0]))
            elif tupl2[0].lower() == 'mmhg':output_lst.append(to_mmHg(tupl1[0]))
            elif tupl2[0].lower() == 'bar':output_lst.append(toBar(tupl1[0]))
            elif tupl2[0].lower() == 'n/m^2':output_lst.append(tupl1[0])
            else:return 'Invalid Pressure unit passed. Accepted pressure units are atm, Bar, mmHg, Pascal or N/m^2'
            #Handle temperature conversion
            if tupl2[1].lower() == 'c':output_lst.append(toCelcius(tupl1[1]))
            elif tupl2[1].lower() == 'f':output_lst.append(toFarenheit(tupl1[1]))
            elif tupl2[1].lower() == 'r':output_lst.append(toRankine(tupl1[1]))
            elif tupl2[1].lower() == 'k':output_lst.append(tupl1[1])
            else:return 'Invalid Temperature units passed. Accepted temperature units are K, C, and R'

            return tuple(output_lst)
        except:
            return 'The first tuple should contain int or float and the second tuple should contain str only'
#test
press_units = ['atm', 'pa', 'mmhg', 'bar', 'N/m^2']
temp_units = ['k','r','c','f']
for i in press_units:
    for j in temp_units:
        print(intensive_properties((101325, 300),(i,j)))



