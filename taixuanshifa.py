# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 12:43:10 2020

@author: Ken Tang
@email: kinyeah@gmail.com
"""

import random, pickle, os

root = os.path.abspath(os.path.dirname(__file__))
data = os.path.join(root, 'data')
taixuandict_path  = os.path.join(root, 'data', 'taixuandict.p')
taixuandict = pickle.load( open( taixuandict_path, "rb" ))
chin_list = list('角亢氐房心尾箕斗牛女虛危室壁奎婁胃昴畢觜參井鬼柳星張翼軫')
yearsu = [item for sublist in [[chin_list[i]]* [12,9,15,5,5,18,11,26,8,12,10,17,16,9,16,12,14,11,16,2,9,33,4,15,7,18,18,17][i] for i in range(0,28)] for item in sublist]

def qigua_number():
    wai_dict = {7:1, 8:2, 9:3}
    shifa_results = []
    shifa_results2 = []
    for i in range(4):
        stalks_first = 36 - 3 - 1 #36策，虛三，掛一
        dividers = sorted(random.sample(range(25, stalks_first), 1))
        two_division  = [a - b for a, b in zip(dividers + [stalks_first+10], [10] + dividers)]
        two_division_left = two_division[0] % 3 
        if two_division_left == 0:
            two_division_left = 3
        two_division_right = two_division[1] % 3 
        if two_division_right == 0:
            two_division_right = 3
        stalks_second = stalks_first - two_division_left - two_division_right
        dividers_second = sorted(random.sample(range(25, stalks_second), 1))
        two_division_second  = [a - b for a, b in zip(dividers_second + [stalks_second+10], [10] + dividers_second)]
        two_division_left_second = two_division_second [0] % 3 
        if two_division_left_second == 0:
            two_division_left_second = 3
        two_division_right_second = two_division_second [1] % 3 
        if two_division_right_second == 0:
            two_division_right_second = 3
        stalks_third = stalks_second - two_division_left_second - two_division_right_second
        wai = stalks_third / 3 
        shifa_results.append(wai_dict.get(wai))
        shifa_results2.append(wai)
    zhan = (shifa_results2[0] + shifa_results2[1] + shifa_results2[2] + shifa_results2[3]) % 9 
    if zhan == 0:
        zhan = 9
    zhou = "".join(str(e) for e in shifa_results[:4])
    return zhou, int(zhan)

def qigua():
    gua_number = int(qigua_number()[0])
    gua_details = taixuandict.get(gua_number)
    gua = gua_details.get("卦")
    zhan_dict = {1:"初一", 2:"次二", 3:"次三", 4:"次四", 5:"次五", 6:"次六", 7:"次七", 8:"次八", 9:"上九"}
    zhan_number = zhan_dict.get(qigua_number()[1])
    zhan = gua_details.get(zhan_number)
    daynightselect = {"旦":["初一","次五","次七"], "夕":["次三","次四","次八"], "日中":["次二","次六","上九"], "夜中":["次二","次六","上九"]}
    hours = list(range(24))
    hour = datetime.now().hour
    dnn = daynightselect.get( multi_key_dict_get({tuple(hours[6:12]):"旦", tuple(hours[12:18]):"日中", tuple(hours[18:24]):"夕", tuple(hours[0:6]):"夜中"},hour))
    return gua_number, gua, [{i:gua_details.get(i)} for i in dnn], qigua_number()


