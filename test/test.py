#%%
char = "['C:/Users/taesu/Documents/GitHub/RDF_from_X-ray_Scattering/PSM_BCP/HS-TRWAXS_0_2M_19KeV_PSPMMA_DIS_att0_060C_3sec_0270.dat_bsub']"
print(char)
p = char.rfind('/')
print(p)
char2 = char[0:p]
print(char2)
p2 = char.count('_',0,p)
print(p2)
# %%
