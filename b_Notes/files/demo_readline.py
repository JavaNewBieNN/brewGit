"""
按行读取文件
"""

print('=====正确版本开始======')
with open('C:/Users/NingNie/brewGit/pythonCodes/b_Notes/files/b.txt',encoding='utf-8') as f:
   
   print("-" * 30)
   buf = f.readline() #只读一行
   print("-" * 30)
   print('buf =', repr(buf))
   print("-" * 30)


   lines = f.readlines() #返回一个数组
   print('lines =',repr(lines))

   for line in lines:
      print(line.strip())






   