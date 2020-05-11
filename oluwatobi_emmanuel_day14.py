"""This is a python function that returns all words in a list that are anagrams
by accepting a list as an argument."""

def anagram_finder(lst):
    #anagram function that returns true if two items are anagrams
    def is_anagram(item1,item2):
        if sorted(item1)==sorted(item2): return True
        else: return False
    i=0
    returned_list = []
    #The main anagram finder function
    while i<=(len(lst)-2):
        anagram_sub_list = []
        new_list = lst[:]
        for char in new_list:
            if is_anagram(char,lst[i])==True:
                anagram_sub_list.append(char)
            else:
                anagram_sub_list = anagram_sub_list
        if len(anagram_sub_list)>0:
            if is_anagram(anagram_sub_list[0],lst[i])==True:
                anagram_sub_list.append(lst[i])
                returned_list.append(anagram_sub_list)
            else:
                returned_list = returned_list
        else:
                returned_list = returned_list
        i+=1
    #remove the last element in every list in the returned list as it is the same as the first element
    for char in lst:
        for lis in returned_list:
            if lis[-1]==char:
                lis.remove(lis[-1])
    #sort every list in the returned list to prepare for elimination of redundancy
    for lis in returned_list:
        lis.sort()
    #removes every repetition in the list
    real_returned_list = []
    i=0
    while i<len(returned_list):
        if returned_list.count(returned_list[i])>1:
            real_returned_list.append(returned_list[i])
            i+=returned_list.count(returned_list[i])
        else:
            real_returned_list.append(returned_list[i])
            i+=1
    return real_returned_list
import time
now = time.time()
print(anagram_finder(['grut','rugt','gurt','ray','yra','rya','uya','yau','uay','ayu']))
qn = time.time()
print(qn-now)


