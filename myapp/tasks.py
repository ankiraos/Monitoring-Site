from celery import shared_task
import requests
from myapp.models import SiteChecker


@shared_task
def testing():
    sites = SiteChecker.objects.all()
    for site in sites:
        web_url = site.web_url
        # print(web_url)
        try:
            response = requests.get(web_url)
            if response.status_code == 200:
                try:
                    if site.text in response.text:
                        msg = {"text": f"{web_url} site is up."}
                        requests.post(site.slack_url, json=msg)
                    else:
                        text = site.text
                        msg = {"text": f'the text "{text}" is not present in {web_url}'}
                        requests.post(site.slack_url, json=msg)
                except Exception as e:
                    print(e)
            else:
                msg = {"text": f"{web_url} site is down."}
                requests.post(site.slack_url, json=msg)
        except Exception as e:
            print(e)
