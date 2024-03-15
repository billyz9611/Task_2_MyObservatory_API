import requests, pytest, json

WEATHER_URL = "https://pda.weather.gov.hk/locspc/android_data/ocf_data/HKO.v2.xml"
WEATHER_FND_URL = "https://pda.weather.gov.hk/locspc/android_data/fnd_uc.xml"


@pytest.mark.parametrize('api', [WEATHER_URL, WEATHER_FND_URL])
def test_api_status_is_ok(api):
    rsp = requests.get(api)
    assert rsp.status_code in range(200, 300), "API status_code is {}".format(rsp.status_code)


@pytest.mark.parametrize('api,key_name,items_nums',
                         [[WEATHER_URL, 'DailyForecast', 10], [WEATHER_FND_URL, 'forecast_detail', 9]])
def test_api_response_data_is_ok(api, key_name, items_nums):
    rsp = requests.get(api)
    assert rsp.status_code in range(200, 300), "API status_code is {}".format(rsp.status_code)
    weather_forecast = json.loads(rsp.content)
    detail = weather_forecast[key_name]
    assert len(detail) == items_nums, '{} data len is {}, but expect {}'.format(key_name, len(detail),items_nums)
