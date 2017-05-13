import math
def binary_research(numbles,the_choose_point):
    alpha = 0
    new_numbles = numbles[:]
    #print len(numbles)
    for i in range(int(math.log(len(numbles),2))+1):

        l = len(new_numbles)

        #print new_numbles
        if(l > 2):
            if(new_numbles[int(l/2) - 1] > the_choose_point):
                new_numbles = new_numbles[:int(l/2)]
                alpha = alpha
            elif(new_numbles[int(l/2)] < the_choose_point):
                new_numbles = new_numbles[int(l/2):]
                alpha = alpha + int(l/2)
            elif(new_numbles[int(l/2) - 1] == the_choose_point):
                return alpha + int(l/2) - 1
                break
            elif(new_numbles[int(l/2)] == the_choose_point):
                return alpha + int(l/2)
                break
            else:
                return alpha + int(l/2)#the_choose_point_place
                break
        else:
            if(new_numbles[0] >= the_choose_point):

                return alpha#the_choose_point_place
                break
            elif(new_numbles[1] >= the_choose_point):

                return alpha + 1#the_choose_point_place
                break
            else:
                #the_choose_point_place = alpha + 2

                return alpha + 2#the_choose_point_place
                break
