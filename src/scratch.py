from requests import get
from json import loads
from wget import download
from pandas import read_csv


# NOAA stuff
token = 'WBtFHGISuLrFoPdVSVkEmLFzjhpWveRa'
buoy_id = '46050'
oregon = 'FIPS:41'
lat = '44.669'
long = '124.546'
stations_url = 'https://www.ncei.noaa.gov/cdo-web/api/v2/stations/{id}locationid={locationID}&limit=1000'


def get_standard_NOAA_data(url, token, buoy, fips):
    """TODO:"""
    header = {
        'token': token,
    }
    endpoint = url.format(id='?', locationID=oregon)
    print(endpoint)
    response = get(endpoint, headers=header)
    # data = response.json()
    
    decoded_json = loads(response.text)

    search_term = ''
    for i in decoded_json['results']:
        if search_term in i['id']: return i


def get_NBDC_data():
    """
    Retrieve the most recent, complete row of data from buoy number 46050.
    :return:
        - the top row of a pandas data frame.
    """
    url = 'https://www.ndbc.noaa.gov/data/realtime2/46050.txt'
    data = read_csv(url, sep='\s+')

    sub_frame = data.iloc[:, :-4]  # Cuts off 'DEWP' 'VIS' 'PTDY' 'TIDE'

    # Tricky boolean mask that returns a complete row of data
    complete_rows = sub_frame[~sub_frame.isin(['MM']).any(axis=1)]

    working_row = complete_rows.iloc[[1]]
    
    return data

print(get_NBDC_data())