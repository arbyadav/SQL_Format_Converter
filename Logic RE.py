import re

f= open("C:\\Users\\52038474\\Documents\\LEARNING\\PYTHON 3\\Python\\MINI PROJECTS\\SQL_Format\\A.txt",'r')

a=(f.read()).strip()

a=re.sub('\s+','\',\'',a)

a=re.sub(r'^\A','(\'',a)

a=re.sub(r'\Z','\')',a)

print(a)


################################################################
'''
raw_data='   Amit Yadav python is     t    '

raw_data=raw_data.strip()

raw_data=re.sub('\s+','\',\'',raw_data)

raw_data=re.sub(r'^\A','(\'', raw_data)

raw_data=re.sub(r'\Z','\')',raw_data)

print(raw_data)
'''
#########################################################

#when one or more spaces at beginning
#rf= re.sub(r'^\A\s{0,}','(\'', raw_data)

#when one or more spaces at end
#rb= re.sub(r'[ \t{0,}]+$','\')',raw_data)

#########################################################

# #if spaces found at beginning
# raw_data = re.sub(r'^[ \t]', '(\'', raw_data)

# #if spaces found at end
# raw_data = re.sub(r'[ \t]+$', '\')', raw_data)

########################################################

# def convertstr(str2): 
#     strk = str2.split()
#     return strk

# tup2 = convertstr(raw_data)

# # # for s in raw_data.split():
# # #     print(s)
# # raw_data.replace( ,'\',\',count='/new')


# # Final=[s for s in raw_data.split()]
# # print(Final)

# # # rqd_data='\'AMIT\',\'YADAV\''

# # # print(rqd_data)

# def convertTuple(tup): 
#     strr =  ''.join(tup) 
#     return strr
  
# # Driver code 
# tuple1 = ('g', 'e', 'e', 'k', 's') 
# str1 = convertTuple(tuple1) 
# print(str1) 
