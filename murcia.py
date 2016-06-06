import requests

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
        "Cookie": "ASP.NET_SessionId=zv2xmfql3k3oeu45tayn31ru",
        "Connection": "keep-alive"
    }
    data_string = "tipoConsulta=medias_horarias&estacionesSelec=e_alcantarilla_Alcantarilla-e_aljorra_Aljorra-e_alumbres_Alumbres-e_caravaca_Caravaca-e_lorca_Lorca-e_mompean_Mompe%C3%A1n-e_sanbasilio_San%20Basilio-e_valle_Valle%20de%20Escombreras-eh_benizar_Ben%C3%ADzar-eh_launion_La%20Uni%C3%B3n-eh_sangines_San%20Gin%C3%A9s&contaminantesSelec=cc_C6H6*Ben_Benceno_ug%2Fm3-cc_CO_CO_mg%2Fm3-cc_NO_NO_ug%2Fm3-cc_NO2_NO2_ug%2Fm3-cc_O3_O3_ug%2Fm3-cc_PM10_PM10_%26micro%3Bg%2Fm3-cc_SO2_SO2_ug%2Fm3-cc_C7H8*Tol_Tolueno_ug%2Fm3-cc_XIL*Xil_Xileno_ug%2Fm3-cm_HR_Humedad%20Relativa_%25%20Hr-cm_TMP_Temperatura_%C2%BA%20C&periodoConsulta=sel_hoy&fechaInicioConsulta=06%2F06%2F2016&fechaFinConsulta=07%2F06%2F2016&tipo_dato=grid"
    data = {
        "tipoConsulta": "medias_horarias",
        "estaciones_Selec": "e_alcantarilla_Alcantarilla-e_aljorra_Aljorra-e_alumbres_Alumbres-e_caravaca_Caravaca-e_lorca_Lorca-e_mompean_Mompe%C3%A1n-e_sanbasilio_San%20Basilio-e_valle_Valle%20de%20Escombreras-eh_benizar_Ben%C3%ADzar-eh_launion_La%20Uni%C3%B3n-eh_sangines_San%20Gin%C3%A9s",
        "contaminantesSelec": "cc_C6H6*Ben_Benceno_ug%2Fm3-cc_CO_CO_mg%2Fm3-cc_NO_NO_ug%2Fm3-cc_NO2_NO2_ug%2Fm3-cc_O3_O3_ug%2Fm3-cc_PM10_PM10_%26micro%3Bg%2Fm3-cc_SO2_SO2_ug%2Fm3-cc_C7H8*Tol_Tolueno_ug%2Fm3-cc_XIL*Xil_Xileno_ug%2Fm3-cm_HR_Humedad%20Relativa_%25%20Hr-cm_TMP_Temperatura_%C2%BA%20C",
        "periodo_consulta": "sel_hoy",
        "fechaInicioConsulta": "06%2F06%2F2016",
        "fechaFinConsulta": "07%2F06%2F2016",
        "tipo_dato": "grid"
    }

    r = requests.post(url, data=data_string, headers=headers)

    print(r.text)


connect()
