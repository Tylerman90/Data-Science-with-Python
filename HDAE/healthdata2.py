import pandas as pd

#csv files being used in code
diagnosis = pd.read_csv('diagnosis.csv')
visit_diagnosis = pd.read_csv('visit_diagnosis.csv')


#List ICD9 codes of interest
ICD_bool = ((diagnosis['ICD9_CD']=='995.0') |
(diagnosis['ICD9_CD']=='995.3') | (diagnosis['ICD9_CD']=='995.6') |
(diagnosis['ICD9_CD']=='995.60') | (diagnosis['ICD9_CD']=='995.61') |
(diagnosis['ICD9_CD']=='995.62') | (diagnosis['ICD9_CD']=='995.63') | (diagnosis['ICD9_CD']=='995.64') | (diagnosis['ICD9_CD']=='995.65') | (diagnosis['ICD9_CD']=='995.66') | (diagnosis['ICD9_CD']=='995.67') | (diagnosis['ICD9_CD']=='995.68') | (diagnosis['ICD9_CD']=='995.69') | (diagnosis['ICD9_CD']=='995.7') | (diagnosis['ICD9_CD']=='999.4') | (diagnosis['ICD9_CD']=='999.41') | (diagnosis['ICD9_CD']=='999.42') | (diagnosis['ICD9_CD']=='999.49'))

#filtered ICD9 codes
ICD_codes = diagnosis[ICD_bool]
#print(ICD_codes)


#Primary and Seconday indicators of interest
ED_diagnosis = ((visit_diagnosis['DICT_DX_STS_KEY']==313) | (visit_diagnosis['DICT_DX_STS_KEY']==314))
prim_sec = visit_diagnosis[ED_diagnosis]
#print(prim_sec)



#merge (innerjoin) both DataFrames on similar DX_KEY values
df3=pd.merge(ICD_codes,prim_sec,on='DX_KEY')
print(df3)
