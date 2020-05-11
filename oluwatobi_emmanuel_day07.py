"""This is a python function created by Emmanuel Oluwatobi
 that accepts a list of room numbers and returns the room number of a
 captain in an hotel. It includes a sort function
 that implements the insertion sort algorithm and also a count
 function that counts the number of occurences of a room number in the list
 using a for loop."""

def captains_room(room_list):
    def sort(lst):
        for i in range(1,len(room_list)):
            if type(room_list[i])==str:
                return False
                break
            else:
                pre = room_list[i]
                j = i
                while j>0 and room_list[j-1] > pre:
                    room_list[j] = room_list[j-1]
                    j-=1
                room_list[j] = pre
            return room_list
    try:
        sorted_room_list = sort(room_list)
        if sorted_room_list==False:
            return 'Items in list should be of type int'
        else:
            for k in sorted_room_list:
                count = len([n for n in sorted_room_list if n==k])
                if count == 1:
                    return ("Captain's room number: "+str(k))
                    break
    except TypeError:
        return 'Argument passed to the function must be of type list e.g [1,2,3]'
    except NameError:
        return 'Argument passed to the function must be of type list'
#Call the function here
print(captains_room(['ty',2]))