# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 20:58:36 2023

@author: T
"""
import os
def calc_dir_size(dir_path):
    file_size=0
    for r,d,f in os.walk(dir_path):
            for file in f:
                file_size+=os.path.getsize(os.path.join(r,file))
    return round(float(file_size)/1048576, 2)
    
    
if __name__=='__main__':
    entry_dir=r'C:\Users\T\AppData\Local\Google\Chrome\User Data'
    for dr in os.listdir(entry_dir):
        print(f' {dr}:')
        try:
            size=calc_dir_size(os.path.join(entry_dir,dr))
            if size > 400:
                print(f'dir : {dr} size:{size} mb')
        except:
            pass