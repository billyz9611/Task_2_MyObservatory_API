import utils

import requests, json

WEATHER_URL = "https://pda.weather.gov.hk/locspc/android_data/ocf_data/HKO.v2.xml"
WEATHER_FND_URL = "https://pda.weather.gov.hk/locspc/android_data/fnd_uc.xml"
after_tomorrow_str = utils.get_after_tomorrow_str()


def get_relative_humidity_after_tomorrow_ocf_data():
    rsp = requests.get(WEATHER_URL)
    weather_forecast = json.loads(rsp.content)
    hourly_forecast = weather_forecast['HourlyWeatherForecast']
    after_tomorrow_forecast = filter(lambda x: x['ForecastHour'].startswith(after_tomorrow_str), hourly_forecast)
    relative_humidity_list = [r['ForecastRelativeHumidity'] for r in after_tomorrow_forecast]
    return min(relative_humidity_list), max(relative_humidity_list)


def get_relative_humidity_after_tomorrow_fnd():
    rsp = requests.get(WEATHER_FND_URL)
    weather_forecast = json.loads(rsp.content)
    forecast_detail = weather_forecast['forecast_detail']
    after_tomorrow_forecast = list(filter(lambda x: x['forecast_date'] == after_tomorrow_str, forecast_detail))

    return after_tomorrow_forecast[0]['min_rh'], after_tomorrow_forecast[0]['max_rh']


if __name__ == '__main__':
    text_tmp = 'The relative humidity is {}% to {}% for the day after tomorrow, data from {} API.'

    min_relative_humidity, max_relative_humidity = get_relative_humidity_after_tomorrow_ocf_data()
    print(text_tmp.format(min_relative_humidity, max_relative_humidity, 'ocf_data'))

    min_relative_humidity, max_relative_humidity = get_relative_humidity_after_tomorrow_fnd()
    print(text_tmp.format(min_relative_humidity, max_relative_humidity, 'fnd'))
