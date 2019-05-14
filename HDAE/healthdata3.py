import pandas as pd

visit_diagnosis = pd.read_csv('visit_diagnosis.csv')

ED_diagnosis = ((visit_diagnosis['DICT_DX_STS_KEY']==313) | (visit_diagnosis['DICT_DX_STS_KEY']==314))
prim_sec = visit_diagnosis[ED_diagnosis]
print(prim_sec)
