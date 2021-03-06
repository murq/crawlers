# vim: set filencoding=UTF-8

import requests
import datetime
import json
import demjson
from pymongo import MongoClient

def connect():
    url = "http://sinqlair.carm.es/calidadaire/obtener_datos.aspx?tipo=tablaRedVigilancia"
    query_string = "tipo=tablaRedVigilancia"
    headers = {
        "Host": "sinqlair.carm.es",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": "http://sinqlair.carm.es/calidadaire/redvigilancia/redvigilancia.aspx",
        "Content-Length": 698,
        "Connection": "keep-alive"
    }

    query_type = "tipoConsulta=medias_horarias"
    stations="estacionesSelec=e_alcantarilla_Alcantarilla-e_aljorra_Aljorra-e_alumbres_Alumbres-e_caravaca_Caravaca-e_lorca_Lorca-e_mompean_Mompe%C3%A1n-e_sanbasilio_San%20Basilio-e_valle_Valle%20de%20Escombreras-eh_benizar_Ben%C3%ADzar-eh_launion_La%20Uni%C3%B3n-eh_sangines_San%20Gin%C3%A9s"
    pollutants="contaminantesSelec=cc_C6H6*Ben_Benceno_ug%2Fm3-cc_CO_CO_mg%2Fm3-cc_NO_NO_ug%2Fm3-cc_NO2_NO2_ug%2Fm3-cc_O3_O3_ug%2Fm3-cc_PM10_PM10_%26micro%3Bg%2Fm3-cc_SO2_SO2_ug%2Fm3-cc_C7H8*Tol_Tolueno_ug%2Fm3-cc_XIL*Xil_Xileno_ug%2Fm3-cm_HR_Humedad%20Relativa_%25%20Hr-cm_TMP_Temperatura_%C2%BA%20C"
    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=1)
    time_period ="periodoConsulta=sel_hoy&fechaInicioConsulta="+str(now.day)+"%2F"+str(now.month)+"%2F"+str(now.year)+"&fechaFinConsulta="+str(tomorrow.day)+"%2F"+str(tomorrow.month)+"%2F"+str(tomorrow.year)
    data_type = "tipo_dato=grid"

    data_string = query_type+"&"+stations+"&"+pollutants+"&"+time_period+"&"+data_type


    r = requests.post(url, data=data_string, headers=headers)
    
    #We format the JSON response to be RFC4627 compliant
    formatted_json_string = demjson.decode(r.text[3:].replace("'","\""))
    formatted_json_string = json.dumps(formatted_json_string)
    formatted_json = json.loads(formatted_json_string)
    
    time_format = "%d/%m/%Y %H:00"
    
    #MongoDB information
    client = MongoClient()
    db = client['Estacions']
    coll = db['Murcia']

    for row in formatted_json:
        date_field = row["fecha"]
        if date_field == now.strftime(time_format):
            for key in row.keys():
                if key!="contaminante" and key!="fecha" and row[key] != "---":
                    json_insert={
                        "nombre": str(key),
                        "fecha": datetime.datetime.strptime(row["fecha"],time_format),
                        "tipo_dato": row["contaminante"],
                        "valor": row[key]
                    }
                    #Units depend on the pollutants
                    json_units={}
                    if row["contaminante"] == "CO":
                        json_units = {"unidades": "mg/m3"}
                    elif row["contaminante"] == "TMP":
                        json_units = {"unidades": "°C"}
                    elif row["contaminante"] == "HR":
                        json_units = {"unidades": "%"}
                    else:
                        json_units = {"unidades": "µg/m3"}
                    #Joining the two JSON objects
                    json_insert = {key: value for (key, value) in (json_insert.items() + json_units.items())}
                    coll.insert_one(json_insert)


connect()
