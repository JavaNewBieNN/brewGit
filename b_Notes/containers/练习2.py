"""
1.自定义程序实现如下要求
2.能够获取测试人员输入的信息(登录/测试)
3.获取每组测试数据的用户名,密码和预期结果,组成以下的数据格式进行打印
[(),(),()]或者[[],[],[]]

比如:
输入 登录 组成的列表为
[("admin","123456","登录成功"),("root","123456","登录失败")]
或者
[["admin","123456","登录成功"],["root","123456","登录失败"]]

输入 注册 组成的列表为
[("abcd","123456"),("xyz","123456")]
"""

def login_or_register(my_dict,user_input):
    
    catch_list = list()
    if user_input == "登录":
        catch_list = my_dict.get('登录')
    elif user_input == "注册":
        catch_list = my_dict.get('注册')
        
    output_list = list()
        
    for dicts in catch_list:
            
        temp_list = list()
            
        for value in dicts.values():
            temp_list.append(value)
            
        temp_list.pop(0)
            
        output_list.append(temp_list)
        
    return output_list



my_dict = {
    '登录':[{'desc': '正确的用户名密码','username': 'admin','password': '123456','expect': '登录成功'},
          {'desc':'错误的用户名','username': 'root','password': '123456','expect': '登录失败'},
          {'desc':'错误的密码','username': 'admin','password': '123123','expect': '登录失败'},
          {'desc':'错误的用户名和密码','username': 'aaaa','password': '123123','expect': '登录失败'},
         ],
       
    '注册':[{'desc':'注册1','username':'abcd','password':'123456'},
          {'desc':'注册1','username':'xyz','password':'123456'},
        ]
}

user_input = input("请输入 '登录' 或者 '注册'")

output_lists = login_or_register(my_dict,user_input)


print(output_lists)
    
            
            
        
    
    
