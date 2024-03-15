from datetime import datetime, timedelta
from pytz import timezone


def get_after_tomorrow_str() -> str:
    now = datetime.now(tz=timezone('Asia/Hong_Kong'))

    after_tomorrow = now + timedelta(days=2)

    return after_tomorrow.strftime("%Y%m%d")


if __name__ == '__main__':
    print(get_after_tomorrow_str())
