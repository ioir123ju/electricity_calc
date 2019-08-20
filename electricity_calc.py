#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   electricity_calc.py    
@Contact :   juzheng@hxdi.com
@License :   (C)Copyright 2018-2019, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/6/12 18:22   juzheng      1.0         None
'''

pre_electric = {"public": 3830.2, "A": 1528.6, "B": 5203.9, "C": 2389.8, "D": 2164.7}
now_electric = {"public": 4006.3, "A": 1674.2, "B": 5426.7, "C": 2592.5, "D": 2376.4}

electric_cost = 383.1

pre_public_electric = pre_electric["public"]
pre_A_electric = pre_electric["A"]
pre_B_electric = pre_electric["B"]
pre_C_electric = pre_electric["C"]
pre_D_electric = pre_electric["D"]

public_electric = now_electric["public"]
A_electric = now_electric["A"]
B_electric = now_electric["B"]
C_electric = now_electric["C"]
D_electric = now_electric["D"]


all_use = (public_electric-pre_public_electric) + (A_electric - pre_A_electric) + \
          (B_electric - pre_B_electric) + (C_electric - pre_C_electric) + (D_electric - pre_D_electric)

public_cost = electric_cost*(public_electric-pre_public_electric)/all_use
A_cost = electric_cost*(A_electric - pre_A_electric)/all_use
B_cost = electric_cost*(B_electric - pre_B_electric)/all_use
C_cost = electric_cost*(C_electric - pre_C_electric)/all_use
D_cost = electric_cost*(D_electric - pre_D_electric)/all_use
A_public = public_cost*0.3
B_public = public_cost*0.1
C_public = public_cost*0.3
D_public = public_cost*0.3

A_cost += A_public
B_cost += B_public
C_cost += C_public
D_cost += D_public

print("A:{:.2f} B:{:.2f} C:{:.2f} D:{:.2f},total:{}".format(A_cost, B_cost, C_cost, D_cost, A_cost+B_cost+C_cost+D_cost))