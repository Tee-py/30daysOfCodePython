



def gpa_calculator(score_list, unit_list):
    if type(score_list)!=list or type(unit_list)!=list:
        return 'The two args should be a list'
    else:
        weight = 0
        try:
            total_units = sum(unit_list)
            for i in score_list:
                if type(i)==str or type(unit_list[score_list.index(i)])==str:
                    return 'Score list should contain integers or floats as well as unit list'
                if int(i) in range(70,101):
                    weight += 5*unit_list[score_list.index(i)]
                elif int(i) in range(60,70):
                    weight += 4*unit_list[score_list.index(i)]
                elif int(i) in range(50,60):
                    weight += 3*unit_list[score_list.index(i)]
                elif int(i) in range(45,50):
                    weight += 2*unit_list[score_list.index(i)]
                elif int(i) in range(40,45):
                    weight += 1*unit_list[score_list.index(i)]
                elif i>100:
                    return 'maximum score is 100'
                else:
                    weight += 0
            return weight/total_units
        except:
            return 'Score list should contain integers or floats as well as unit list'


print(gpa_calculator([100,72,73,74,75],[3,2,2,1,2]))

