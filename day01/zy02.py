# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 21:03:21 2021

@author: zhangkaiyu
"""

#课程作业2

import numpy as np
person_type=np.dtype({'names':['name','chinese','math','english'],'formats':['S32','i','i','i']})
peoples=np.array([("ZhangFei",68,65,30),("GuanYu",95,76,98),("LeiBei",98,86,88),("DianWei",90,88,77),("XuZhu",80,90,90)],dtype=person_type)
chineses=peoples[:]["chinese"]
maths=peoples[:]["math"]
englishs=peoples[:]["english"]
total=peoples[:]["chinese"]+peoples[:]["math"]+peoples[:]["english"]
print('语文平均成绩：',np.mean(chineses))
print('数学平均成绩：',np.mean(maths))
print('英语平均成绩：',np.mean(englishs))
print('语文最小成绩：',np.amin(chineses))
print('数学最小成绩：',np.amin(maths))
print('英语最小成绩：',np.amin(englishs))
print('语文最大成绩：',np.amax(chineses))
print('数学最大成绩：',np.amax(maths))
print('英语最大成绩：',np.amax(englishs))
print('语文方差：',np.var(chineses))
print('数学方差：',np.var(maths))
print('英语方差：',np.var(englishs))
print('语文标准差：',np.std(chineses))
print('数学标准差：',np.std(maths))
print('英语标准差：',np.std(englishs))
print('按总成绩排序：',np.sort(total))


                                                                                                        


