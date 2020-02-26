import pandas as pd
import csv

#Code to retrieve created data set

df = pd.read_csv('org_data.csv')
df = df.iloc[:,1::]
list_patents = df['patent_id'].tolist()
list_patents = [str(x) for x in list_patents]
bigdata=[]
count=0
csv.field_size_limit(1000000)
with open("claim.tsv") as fd:
    rd = csv.reader(fd, delimiter="\t", quotechar='"')
    #while count <1000000: 
      #if str(next(rd)[1]) in list_patents:
        #bigdata.append(next(rd))
      #count +=1
    for r in rd:
      if str(r[1]) in list_patents:
        bigdata.append(r)

df_bigdata = pd.DataFrame(bigdata)
df_bigdata.columns = ['uuid','patent_id','text','dependent','sequence','exemplary']
df_bigdata.to_csv('pat_text_data.csv')
print(df_bigdata.shape,df_bigdata.head())


