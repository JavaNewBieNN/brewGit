"""
✅ 一句话本质解释:

	pass 什么都不做.就是占个位置,防止语法错误.
 
  它的核心功能是:"占位" ✅

在 Python 中,某些地方语法上必须要写点什么,但你又不想干任何事,这时就写 pass.
"""

#✅ 场景 1:函数体还没写好,先写个壳
def my_func():
    pass  # 以后再写具体逻辑

# 不写 pass 会报错, 📌 作用类似于:"我这里暂时先不写逻辑,但保证语法没错"

#✅ 场景 2:占位的类或控制结构
if True:
    pass  # 这里不想写任何内容

class MyClass:
    pass


#✅ 场景 3:在循环中写 pass,表示"当前这步啥也不干"
for i in range(5):
    if i == 2:
        pass  # 啥也不干,但语法合法
    print(i)
    #注意:这 不会跳过打印,不像 continue,只是"在 if 语句块中啥也不干".
    



"""
✅ 实用建议:
	•	写框架、空函数、空类时用 pass
	•	不能滥用 pass 代替控制流程语句(如 return 或 continue)    
    
"""