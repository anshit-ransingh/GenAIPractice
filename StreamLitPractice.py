# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 12:24:36 2023

@author: ANSHIT
"""

import streamlit as  slt

slt.title("THis is a test module")
slt.header('This is the HeadeR')

slt.text('Dungeon Unlocked | THis is a text')

slt.markdown('THis is a markdown')

slt.success('Success Tab')



slt.write("Text with write")




import numpy as np
import pandas as pd

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

slt.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
slt.table(dataframe)

chart_data = pd.DataFrame(
     np.random.randn(30, 5),
     columns=['a', 'b', 'c', 'd', 'e'])

slt.line_chart(chart_data)