# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 14:56:00 2019

@author: kenneth.leetf
references = https://stackabuse.com/association-rule-mining-via-apriori-algorithm-in-python/
"""

import pandas as pd
from apyori import apriori

pd.set_option('display.max_rows', 1500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df = pd.read_csv('bigcampaign.csv')
df = df.dropna()
df1 = df.groupby(['checkoutid']).main_category.apply(list).apply(pd.Series).add_prefix('item_').reset_index()
df1 = df1.drop(columns=['checkoutid'])
#each row in df1 is 1 transaction. Saved to temp.csv
df1.to_csv('temp.csv', header=False, index=False)
df2 = pd.read_csv('temp.csv',header=None)



records = []
count = 0
for i in range(0, len(df2)):
    count += 1
    percent = (count/len(df2))*100
#    print("Appending",count, "of",len(df2),"checkouts")
    print("Reading record Progress:","%.3f" % percent,"%")
    print("=====================")
    records.append([str(df2.values[i,j]) for j in range(0, df1.shape[1]) if str(df2.values[i,j]) != 'nan'])

# change Association rule parameters here
association_rules = apriori(records, min_support=0.000933, min_confidence=0.05, min_lift=1.5)
association_results = list(association_rules)

antecedent = []
consequent = []
support = []
confidence = []
lift =[]

index = 0
for item in association_results:

    for i in range(len(item[2])):
        index += 1
        print("Rule: " , item[2][i][0] , " ---> " , item[2][i][1])
        antecedent.append(item[2][i][0])
        consequent.append(item[2][i][1])
        
        print("Support: " + str(item[1]))
        support.append(item[1])
        
    
        print("Confidence: " + str(item[2][i][2]))
        confidence.append(item[2][i][2])
        print("Lift: " + str(item[2][i][3]))
        lift.append(item[2][i][3])
        print("=====================================")

print("No. of rules:",index)

#output Association Rule results to csv file
data = {'Antecedent':antecedent, 'Consequent':consequent, 'Support':support,
        'Confidence':confidence, 'Lift':lift}
df3 = pd.DataFrame.from_dict(data)

df3.to_csv('temp.csv',index=False)

temp = pd.read_csv('temp.csv')
cleaned = temp.replace(to_replace =r'frozenset\(\{', value = '', regex = True) 
cleaned = cleaned.replace(to_replace =r'\}\)', value = '', regex = True)
cleaned.to_csv('result.csv',index=False)
