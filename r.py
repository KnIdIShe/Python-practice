# import random

# s = ['om', 'uk', 'ay']
# s = ['te', 'i', 'ai']
s = ['ia', 'i', 'et']

# 
# s = ['T', 'E', 'I', 'A', 'I']

# s = ['ya', 'ku', 'mo']
# s = ['o', 'm', 'u', 'k', 'a', 'y']

# t = s
# for i in range(0,10):
# 	random.shuffle(t)
# 	print(t[0]+t[1]+t[2])
# 	
import itertools
t = list(itertools.permutations(s, len(s)))

for i in range(len(t)):
	s = ''
	for j in range(len(t[i])):
		s += t[i][j]
	t[i] = s
# t = [('a', 'b', 'c')]
# s = list(t[0])
# s = s[0]+s[1]+s[2]
# t[0] = s
# print(t[0])
# t1 = t[:]
# print(t)
# for item in t1:
# 	if 'may' in item or 'kay' in item:
# # 		# t.remove(t[i])
# 		t.remove(item)
# 		# print(t[i][j])



# t = list(itertools.permutations(s, 6))
# print(t)
for item in t:
		# print(t[i][j] ,end = '')
		print(item)
# 	print()
# print(6*5*4*3*2)
# 	
# 	
# import random
 
# list = [20, 16, 10, 5];
# random.shuffle(list)
# print ("随机排序列表 : ",  list)
 
# random.shuffle(list)
# print ("随机排序列表 : ",  list)