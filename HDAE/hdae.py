import csv

f = open('visit.csv')

csv_f = csv.reader(f)

cohort1 = []

for row in csv_f:
	if row[5] == '83':
	#'83' is Hospital Encounter
		cohort1.append(row)
print(cohort1)

cohort2 = []
for row in cohort1:
	if row[6] >= '1' and row[6]<= '18.9999':
		cohort2.append(row)




f.close()