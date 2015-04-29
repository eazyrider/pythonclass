__author__ = 'jstahle'
#Jay Stahle
#Homework2

initial=input("Please Enter Search Words\n")

datalist=["For millions of years flowers have been producing thorns. For millions of years sheep have been eating them all the same. And it's not serious, trying to understand why flowers go to such trouble to produce thorns that are good for nothing? It's not important, the war between the sheep and the flowers? It's no more serious and more important than the numbers that fat red gentleman is adding up? Suppose I happen to know a unique flower, one that exists nowhere in the world except on my planet, one that a little sheep can wipe out in a single bite one morning, just like that, without even realizing what he'd doing - that isn't important? If someone loves a flower of which just one example exists among all the millions and millions of stars, that's enough to make him happy when he looks at the stars. He tells himself 'My flower's up there somewhere...' But if the sheep eats the flower, then for him it's as if, suddenly, all the stars went out. And that isn't important?","If you love a flower that lives on a star, it is sweet to look at the sky at night. All the stars are a-bloom with flowers..."]

if " and " in initial:
    andsplit=initial.split(" and ")
    count=0
    for each in datalist:
        isfound=False

        for word in andsplit:
            if word in each:
                isfound=True
            else:
                isfound=False
                break
        count=count+1
        if isfound==True:
            print("Found at " + str(count) + " '" + each + "'")

elif " or " in initial:
    orsplit=initial.split(" or ")
    count=0
    for each in datalist:

        for word in orsplit:
            if word in each:
                print("Found at " + str(count) + " '" + each + "'")
        count=count+1
        
