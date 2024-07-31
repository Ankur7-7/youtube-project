import datetime

import pytz


def zeno_timestamp(t: datetime.datetime):
    """ mainly removes the timezone """
    return t.isoformat().replace("T", " ")[:19]


def ist_now():
    """

    :return: IST time now
    """
    ist = pytz.timezone('Asia/Kolkata')
    ist_time_now = datetime.datetime.now(ist).replace(tzinfo=None)
    return ist_time_now
