import requests
import json

from datetime import datetime, timedelta
from settings import GECKOBOARD_API_KEY


def get_widgets():
    """
    dict of widget keys and their corrisponding values to be pushed up to
    geckoboard.
    Example usage: 
    'geckboard-widget-key: function_name_with_valid_json_return()'
    or
    
    """
    return {
    #'xxxxx-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx': super_secret_data()'
    }


class Gecko(object):
    PUSH_URL = 'https://push.geckoboard.com/v1/send'

    def __init__(self, api_key=None):
        self.api_key = api_key or GECKOBOARD_API_KEY

    def push(self, widget_key, data):
        url = "{}/{}".format(self.PUSH_URL, widget_key)
        post_data = json.dumps({'api_key': self.api_key, 'data': data})
        ret = requests.post(url, post_data)
        print post_data, ret.status_code
        if not (ret.status_code == 200 and ret.json().get('success')):
            raise ValueError(ret.content)
            

def update():
    gecko = Gecko()
    for widget, value in get_widgets().items():
        if isinstance(value, list):
            data = {'item': value}
        elif isinstance(value, dict):
            data = {'item': [value]}
        else:
            if isinstance(value, basestring):
                value = {'text': value}
            else:
                value = [value]
            data = {'item': [value]}

        gecko.push(widget, data)

if __name__ == '__main__':
    update()
