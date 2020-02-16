import csv
import numpy as np

# with open('fullevents.csv',encoding='utf-8') as f:
#     data=np.loadtxt(f,str,delimiter=',',skiprows=1)
# print(data[:5])
import pickle
from flask import Flask,request,jsonify,make_response
# ans=[]
# ans = list(filter(lambda x: x[6]=="Pass" and x[1]=="Huskies",data))
# with open('data','wb') as fout:
#     pickle.dump(ans,fout)
with open('data','rb') as fin:
    dataall=pickle.load(fin)

dataall=np.array(dataall)

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def askdata():
    # ID=[]
    # begin=[] if len(ID)==1
    # end=[] if len(ID)==1
    data=request.form
    data=dict(data)
    ID=data['id']
    ID_data=ID[0].split(",")
    ID=[]
    print(data['begin'])
    for i in ID_data:
        ID.append(int(i))
    if len(ID)==1 and data['begin']!=[""] and data['end']!=[""]:
        begin=float(data['begin'][0])
        end=float(data['end'][0])
        ans=list(filter(lambda x: (int(x[0]) in ID) and float(x[5])<end and float(x[5])>begin,dataall))
    else:
        ans=list(filter(lambda x: (int(x[0]) in ID) ,dataall))
    final=[]
    for i in ans:
        # print(i)
        final.append([i[2],i[3]])
    res=make_response(jsonify(final))
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res