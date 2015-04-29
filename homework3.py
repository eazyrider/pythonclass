
__author__ = 'jstahle'
#Jay Stahle
#Homework3
#Bunny Ears

def bunny_ears(p):
    if p<1:
        return 0
    else:

        return bunny_ears(p-1) + 2

ears=input("Please input number of bunnies\n")


print(bunny_ears(int(ears)))

#Dictionary Function


def count_frequency (mylist):
    result={}

    for each_word in mylist:
        if result.get(each_word)==None:
            result[each_word]=1
        else:
            result [each_word] = result [each_word] +1
    return result


mylist=["one", "two","eleven",  "one", "three", "two", "eleven", "three", "seven", "eleven"]

print(count_frequency(mylist))
