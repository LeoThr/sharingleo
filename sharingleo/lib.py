# -*- coding: UTF-8 -*-
# Copyright (C) 2018 Jean Bizot <jean@styckr.io>
""" Main lib for sharingleo Project
"""

from os.path import split
import pandas as pd
import datetime

pd.set_option('display.width', 200)

def try_me():
    a = print('wesh wesh canne à pêche')
    print('wesh wesh canne à pêche')
    return a


if __name__ == '__main__':
    # For introspections purpose to quickly get this functions on ipython
    import sharingleo
    folder_source, _ = split(sharingleo.__file__)
    df = pd.read_csv('{}/data/data.csv.gz'.format(folder_source))
    clean_data = clean_data(df)
    print(' dataframe cleaned')
