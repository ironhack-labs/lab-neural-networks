import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import zipfile
import os 

zip_path = 

# opening the zipfile
with zipfile.ZipFile(zip_path, "r") as zip_ref:
    zip_ref.extractall("ridgeplot_data") 


# zip_ref is the variable we use to access the archive    

with zipfile.ZipFile(zip_path, "r") as zip_ref:
    zip_ref.extractall() 

# it lists everything inside a particular directory    

non_treated_files = os.listdir("ridgeplot_data/Non_Treated")

treated_files = os.listdir("ridgeplot_data/Treated") 

print(len(treated_files))
print(len(non_treated_files)) 

non_treated_files = [file for file in non_treated_files if file.endswith(".csv")]

treated_files = [file for file in treated_files if file.ends with(".csv")]  

non_treated_files = sorted(non_treated_files)
treated_files = sorted(treated_files)

df["Classification"].value_counts() # counts the frequency of each unique category 

df_tumor = df[df["Classification" == "Tumor: Positive"]]

nuclear_area = df_tumor["Nucleus: Area µm^2"] 

df_tumor["Nucleus_area"] = df_tumor["Nucleus: Area µm^2"]
