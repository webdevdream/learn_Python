def num_list(start, end, inc):
 numbers = []
 while start < end:
     print ("Number is: %d" % start)
     numbers.append(start)
     start += inc
     print ("Numbers now:", numbers)
my_start = 0
my_end = 36
my_inc = 5
num_list(my_start, my_end, my_inc)


def num_list_2(start, end):
 numbers2 = []
 for i in range(start, end):
     if (i % 5) == 0:
         numbers2.append(i)
         print ("Number is: %d" % i)
         print ("Numbers Now:", numbers2)
start2 = 5
end2 = 70
num_list_2(start2, end2)
