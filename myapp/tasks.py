from celery import shared_task
import requests
from myapp.models import SiteChecker
from datetime import datetime
from urllib.parse import urlparse


@shared_task
def testing():
    sites = SiteChecker.objects.all()
    for site in sites:
        web_url = site.web_url
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "max-age=0",
            "priority": "u=0, i",
            "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Linux"',
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        }

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Parse the domain from the URL to use as anchor text
        parsed_url = urlparse(web_url)
        url_text = parsed_url.netloc

        heading = f"*📊 Site Status Report*"
        time_info = f"🕒 *Checked at:* {timestamp}"
        # Make the URL a clickable link with the domain as the anchor text
        site_info = f"🌐 *Site:* <{web_url}|{url_text}>"

        divider = "```━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━```"

        try:
            response = requests.get(web_url, headers=headers)
            print(response)  # printing response
            if response.status_code == 200:
                if site.text in response.text:
                    new_status = "up"
                    if site.status != new_status:
                        status = f"✅ *Status:* The site is up and running smoothly!"
                        msg = {
                            "text": f"{divider}\n{heading}\n\n{time_info}\n{site_info}\n\n{status}\n{divider}"
                        }
                        requests.post(site.slack_url, json=msg)
                        site.status = new_status  # Update the status
                        site.save()  # Save the new status to the database
                else:
                    new_status = "text_missing"
                    if site.status != new_status:
                        text = site.text
                        status = f'⚠️ *Warning:* The site is up, but the text "*{text}*" was not found. It might be down.'
                        msg = {
                            "text": f"{divider}\n{heading}\n\n{time_info}\n{site_info}\n\n{status}\n{divider}"
                        }
                        requests.post(site.slack_url, json=msg)
                        site.status = new_status  # Update the status
                        site.save()  # Save the new status to the database
            else:
                new_status = "down"
                if site.status != new_status:
                    status = f"🔴 *Status:* The site is down!"
                    msg = {
                        "text": f"{divider}\n{heading}\n\n{time_info}\n{site_info}\n\n{status}\n{divider}"
                    }
                    requests.post(site.slack_url, json=msg)
                    site.status = new_status  # Update the status
                    site.save()  # Save the new status to the database
        except Exception as e:
            print(e)
