# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 22:44:05 2019

@author: william
"""

#https://www.kaggle.com/residentmario/creating-reading-and-writing
#https://www.kaggle.com/residentmario/creating-reading-and-writing
#https://www.kaggle.com/residentmario/creating-reading-and-writing

import pandas as pd

pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})

pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']})


pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])

pd.Series([1, 2, 3, 4, 5])

pd.Series([30, 35, 40], 
          index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')


crime = pd.read_csv("C:\\Users\willi\\Desktop\\working\\RAW_DATA\\Boston Crime\\crime.csv",
                    encoding ='raw_unicode_escape')

crime.shape

crime.head(5)

#the course also showed how to import and export data in excel and sql format.



























