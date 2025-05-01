import urllib.parse

def create_query_url(pl_number):
    base_url = "https://ags.iplan.gov.il/arcgisiplan/rest/services/PlanningPublic/Xplan/MapServer/1/query"
    params = {
        "f": "json",
        "where": f"pl_number LIKE '{pl_number}'",
        "returnGeometry": "true",
        "spatialRel": "esriSpatialRelIntersects",
        "outFields": "pl_number,pl_name,pl_url,pl_area_dunam,quantity_delta_120,station_desc,internet_short_status,pl_date_advertise,pl_date_8,plan_county_name,pl_landuse_string",
        "orderByFields": "pl_number"
    }
    
    # קידוד כל הערכים של הפרמטרים
    encoded_params = {key: urllib.parse.quote(value) for key, value in params.items()}
    
    # יצירת כתובת דינמית על ידי חיבור פרמטרים מקודדים
    query_url = base_url + "?" + "&".join([f"{key}={value}" for key, value in encoded_params.items()])
    return query_url