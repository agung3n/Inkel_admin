import pathlib
from flask import Flask, render_template, jsonify, make_response
import requests
import json
import pandas as pd

basedir = pathlib.Path(__file__).parent.resolve()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/tables')
def tables():
    return render_template("tables.html", )

@app.route('/data_suhu')
def data_suhu():
    url1 = "https://okh-itkipb.info/TblDataInkel/INKEL01"
    url2 = "https://okh-itkipb.info/TblDataInkel/INKEL02"
    url3 = "https://okh-itkipb.info/TblDataInkel/INKEL03"
    
    get_data_url1 = requests.get(url1)
    data_json_raw1 = json.dumps(get_data_url1.json())
    alist_kel1 = json.loads(data_json_raw1)
    
    get_data_url2 = requests.get(url2)
    data_json_raw2 = json.dumps(get_data_url2.json())
    alist_kel2 = json.loads(data_json_raw2)
    
    get_data_url3 = requests.get(url3)
    data_json_raw3 = json.dumps(get_data_url3.json())
    alist_kel3 = json.loads(data_json_raw3)
    
    
    df1 = pd.DataFrame.from_records(alist_kel1)
    df1.set_index('Id', inplace=True)
    df1.sort_values(by=['Id'], inplace=True)
    
    df2 = pd.DataFrame.from_records(alist_kel2)
    df2.set_index('Id', inplace=True)
    df2.sort_values(by=['Id'], inplace=True)
    
    df3 = pd.DataFrame.from_records(alist_kel3)
    df3.set_index('Id', inplace=True)
    df3.sort_values(by=['Id'], inplace=True)
    
    
    #df['dt'] = pd.to_datetime(df['time_stamp'], format="%Y-%m-%d %H:%M:%S")
    #df['tt_00'] = df['dt'] - pd.Timedelta(hours=7)
    #print(df3)
    
    df1['suhu_num'] = pd.to_numeric(df1['suhu'], errors='coerce')
    df1['humid_num'] = pd.to_numeric(df1['humid'], errors='coerce')
    data_suhu_max_kel1 = df1['suhu_num'].max()
    data_suhu_min_kel1 = df1['suhu_num'].min()
    data_suhu_mean_kel1 = df1['suhu_num'].mean()
    data_humid_max_kel1 = df1['humid_num'].max()
    data_humid_min_kel1 = df1['humid_num'].min()
    data_humid_mean_kel1 = df1['humid_num'].mean()
    data_last_kel1 = df1['time_stamp'].iloc[-1]
    
    df2['suhu_num'] = pd.to_numeric(df2['suhu'], errors='coerce')
    df2['humid_num'] = pd.to_numeric(df2['humid'], errors='coerce')
    data_suhu_max_kel2 = df2['suhu_num'].max()
    data_suhu_min_kel2 = df2['suhu_num'].min()
    data_suhu_mean_kel2 = df2['suhu_num'].mean()
    data_humid_max_kel2 = df2['humid_num'].max()
    data_humid_min_kel2 = df2['humid_num'].min()
    data_humid_mean_kel2 = df2['humid_num'].mean()
    data_last_kel2 = df2['time_stamp'].iloc[-1]
    
    df3['suhu_num'] = pd.to_numeric(df3['suhu'], errors='coerce')
    df3['humid_num'] = pd.to_numeric(df3['humid'], errors='coerce')
    data_suhu_max_kel3 = df3['suhu_num'].max()
    data_suhu_min_kel3 = df3['suhu_num'].min()
    data_suhu_mean_kel3 = df3['suhu_num'].mean()
    data_humid_max_kel3 = df3['humid_num'].max()
    data_humid_min_kel3 = df3['humid_num'].min()
    data_humid_mean_kel3 = df3['humid_num'].mean()
    data_last_kel3 = df3['time_stamp'].iloc[-1]
    
    #print(data_suhu_max_kel3)
    #print(data_suhu_mean_kel3)
    #print(data_last_kel3)
    
    return jsonify(data_all1=df1.to_json(orient ='records'), 
                   data_suhu_max_kel1=data_suhu_max_kel1,
                   data_suhu_min_kel1=data_suhu_min_kel1, 
                   data_suhu_mean_kel1=data_suhu_mean_kel1,
                   data_humid_max_kel1=data_humid_max_kel1,
                   data_humid_min_kel1=data_humid_min_kel1,
                   data_humid_mean_kel1=data_humid_mean_kel1,
                   data_last_kel1 = data_last_kel1,
                   data_all2=df2.to_json(orient ='records'),
                   data_suhu_max_kel2=data_suhu_max_kel2,
                   data_suhu_min_kel2=data_suhu_min_kel2, 
                   data_suhu_mean_kel2=data_suhu_mean_kel2,
                   data_humid_max_kel2=data_humid_max_kel2,
                   data_humid_min_kel2=data_humid_min_kel2,
                   data_humid_mean_kel2=data_humid_mean_kel2,
                   data_last_kel2 = data_last_kel2,
                   data_all3=df3.to_json(orient ='records'),
                   data_suhu_max_kel3=data_suhu_max_kel3,
                   data_suhu_min_kel3=data_suhu_min_kel3, 
                   data_suhu_mean_kel3=data_suhu_mean_kel3,
                   data_humid_max_kel3=data_humid_max_kel3,
                   data_humid_min_kel3=data_humid_min_kel3,
                   data_humid_mean_kel3=data_humid_mean_kel3,
                   data_last_kel3 = data_last_kel3)

@app.route('/download')
def download():
    url = "https://okh-itkipb.info/TblDataInkel/INKEL02"
    
    
    get_data = requests.get(url)
    data_json_raw = json.dumps(get_data.json())
    alist = json.loads(data_json_raw)
    
    
    df = pd.DataFrame.from_records(alist)
    df.set_index('Id', inplace=True)
   

    print(df)
    
    resp = make_response(df.to_csv())
    resp.headers["Content-Disposition"] = "attachment; filename=export.csv"
    resp.headers["Content-Type"] = "text/csv"
    return resp


if __name__ == '__main__':
    app.run()
