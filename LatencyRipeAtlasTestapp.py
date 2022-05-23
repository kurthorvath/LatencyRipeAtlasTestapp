import requests
import psycopg2
import pandas as pd


conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="5f8n2Z5bsJVB8A909PlR",
    host="latency.ckg56f52vzhx.us-east-1.rds.amazonaws.com",
    port='5432'
)
cursor = conn.cursor()



print(" -> read measurement IDs")

df1 = pd.read_excel('INPUT.xlsx', index_col=None, header=None)  



print(df1)
print()
for MID in df1.iloc[:,0]:

    print(" -> Request Results from Ripe (ID: ", MID, ")")
    r = requests.get('https://atlas.ripe.net/api/v2/measurements/'+str(MID)+'/results')
    res = r.json()

    cnt = 1
    for item in res:
        print("insert ", cnt , " of ", len(res), "in ", MID)
        cnt = cnt + 1


        query =  """INSERT INTO public."resultsPING" (
        fw,
        lts,
        dst_name,
        af,
        dst_addr,
        src_addr,
        proto,
        size,
        result,
        dup,
        rcvd,
        sent,
        min,
        max,
        avg,
        msm_id,
        prb_id,
        timestamp,
        msm_name,
        fromdate,
        type,
        group_id,
        step,
        stored_timestamp
        ) VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s)
        ON CONFLICT DO NOTHING
        ;"""
        data = (item['fw'],
        item['lts'],
        item['dst_name'],
        item['af'],
        item['dst_addr'],
        item['src_addr'],
        item['proto'],
        item['size'],
        str(item['result']),
        item['dup'],
        item['rcvd'],
        item['sent'],
        item['min'],
        item['max'],
        item['avg'],
        item['msm_id'],
        item['prb_id'],
        item['timestamp'],
        item['msm_name'],
        item['from'],
        item['type'],
        item['group_id'],
        item['step'],
        item['stored_timestamp'])

        cursor.execute(query, data)
        
    conn.commit()
    print("done")