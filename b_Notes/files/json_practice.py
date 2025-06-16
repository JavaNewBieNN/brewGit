"""
我叫小明，我今年18岁，性别男，爱好 听歌，游戏，吃饭，睡觉，打豆豆
我的记住地址为 国家 us， 城市 la

我叫小红，我今年18岁，性别女，爱好 听歌，游戏，吃饭，睡觉，打豆豆
我的记住地址为 国家 us， 城市 ny



"""

import json

with open() as f:

    info_list = json.load(f)
    for info in info_list:
        info.get("name"),info.get("age"),info.get("address").get("city")


    pass
