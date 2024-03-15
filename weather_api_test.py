import requests, pytest

WEATHER_URL = "https://pda.weather.gov.hk/locspc/android_data/ocf_data/HKO.v2.xml"
WEATHER_FND_URL = "https://pda.weather.gov.hk/locspc/android_data/fnd_uc.xml"


@pytest.mark.parametrize('api', [WEATHER_URL, WEATHER_FND_URL])
def test_response_pass(api):
    rsp = requests.get(api)
    assert rsp.status_code in range(200, 300)
