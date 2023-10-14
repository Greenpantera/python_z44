import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
lst_r, lst_h = [],[]
random.shuffle(lst)
print(lst)
lst_r = [1 if el == 'robot' else 0 for el in lst ]
lst_h = [1 if el == 'human' else 0 for el in lst ]
print(pd.DataFrame({'robot': lst_r, 'human': lst_h}))


# решение через get_dummilst
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(pd.get_dummies(data.head()))



# еще одно решение

def create_lst_one(lst, lst_dict):
     print(lst, lst_dict)
     res, res1 = [], []
     for elem in lst_dict:
         res1 = [0 if y == elem else 1 for y in lst]
         res = [1 if x == elem else 0 for x in lst]
         for i in range(len(lst)):
             res1[i] = [res1[i],res[i]]
     return res1

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
a_col = list(set(el for el in lst))
a_one = create_lst_one(lst, a_col)

df = pd.DataFrame(a_one, columns=a_col)
print(df)