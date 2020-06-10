# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 16:52:02 2019

@author: Ashish.Gupta
"""

import re


x='234jguj'

print(len(x))
regex = '\w[0-9]'
y = re.search(regex, x)
print(y[1])  