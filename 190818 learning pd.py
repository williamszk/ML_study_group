# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:43:35 2019

@author: william
"""

#190818 learning pd
#https://www.kaggle.com/williamszk/exercise-creating-reading-and-writing/edit

import pandas as pd
pd.set_option('max_rows', 5)
from learntools.core import binder; binder.bind(globals())
from learntools.pandas.creating_reading_and_writing import *
print("Setup complete.")


crime = pd.read_csv("C:\\Users\willi\\Desktop\\working\\RAW_DATA\\Boston Crime\\crime.csv",
                    encoding ='raw_unicode_escape')
crime.shape
crime.head(5)








































