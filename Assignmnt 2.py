import numpy as np
import scipy, stat

print("Qno. 1: Find the mean of this particular dataset")

Salman_1 = [99, 86 , 87 , 88 , 111 , 86 , 103 , 87 , 94 , 78 , 77 , 85 , 86]
me = np.mean(salman_1)
print(me)


print("Qno. 2: Find the median of the dataset of odd value?")

salman_2 = [77, 78, 85,86,86,86,87,87,88,94,99,103,111]

med = np.median(salman_2)
print(med)

# even value

_salman = [77, 78, 85,86,86,86,87,87,88,94,99,103]

even = np.median(_salman)
print(even)

# print("Qno. 3: Find the mode of the dataset, hence we use salman_1 dataset")
#
# sp = np.mod(salman_1)
# print(sp)



print("How to do standard derivation in python?")

salman = [99, 86 , 7 , 88 , 11 , 80 , 1233 , 833]
st = np.std(salman)
print(st)

print("How to find a variance? Use a same list ")

v = np.var(salman)
print(v)



