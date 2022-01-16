from typing import Dict
import requests as _requests
import bs4 as _bs4
import login as _login
import json as _json


def _generate_url():
    url = f"https://my.jurnal.id/accounts/chart_of_accounts"
    return url

def _jurnal_list():
    url = _generate_url()
    page_rs = _login._login_auth(url)

    soup = _bs4.BeautifulSoup(page_rs, "html.parser")
    raw_accounts = soup.find_all(class_="collapse in")
    print("File parsing started...")

    accounts = dict()
    i = 1
    for account in raw_accounts:
        accounts[i] = dict()

        td_list = account.find_all("td") # Python starts counting list items from 0, not 1
        accounts[i]["Account Code"] = td_list[3].text.replace("\n", "").strip()
        accounts[i]["Account Name"] = td_list[4].text.replace("\n", "").strip()
        accounts[i]["Category"] = td_list[5].text.replace("\n", "").strip()
        accounts[i]["Balance"] = td_list[7].text.replace("\n", "").strip()
        i = i + 1

    print("File parsing completed!")
    print("Open accounts.json file to see the results")
    return accounts

if __name__ == '__main__':
    accounts_rs = _jurnal_list()
    with open("accounts.json", mode="w", encoding='utf8') as accounts_file:
        _json.dump(accounts_rs, accounts_file, ensure_ascii = False)
