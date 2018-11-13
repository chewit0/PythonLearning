import json
import requests
import os
import smtplib
from selenium import webdriver
from collections import OrderedDict
from bs4 import BeautifulSoup
from datetime import date
from glob import glob
from email.message import EmailMessage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

# config
configpath = 'bundle.conf'
with open(configpath, 'r') as f:
    config = json.loads(f.read())

recipent = config['recipent']
sender = config['sender']
gmailpassword = config['gmailpassword']
path = config['path']


def get_webpage(url):
    '''given a URL, returns webpage text in html parsed form'''
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    return soup


# Go to site and get dictionary of bundles with urls


def get_bundles():
    '''
    Returns Dictionary in format
    {
        Title: { URL: {}}
    }

    of  Title and URL to currently available bundles
    '''
    # driver = webdriver.Firefox()
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    print("Opening Chrome...")
    driver.implicitly_wait(2)

    driver.get("http://www.humblebundle.com")
    print("At humblebundle.com, fetching bundles...")
    bundles_dict = OrderedDict()

    bundle_dropdown = driver.find_element_by_class_name(
        "bundle-dropdown-content")

    bundles = bundle_dropdown.find_elements_by_class_name("simple-tile-view")

    for bundle in bundles:
        title = bundle.find_element_by_class_name(
            "name").get_attribute("textContent")

        url = bundle.find_element_by_class_name(
            "image-link").get_attribute("href")

        bundles_dict[title] = {url: OrderedDict()}

    driver.close()
    return bundles_dict

# Go to each bundle and retrieve information


def populate_bundle_dict(bundles):
    '''
    Expands on get_bundles by populating lower levels of dictionary with
    price brackets and list of items for each.

    bundles: pass a dictionary
    '''
    bundles_dict = bundles
    for key in bundles_dict:
        url = list(bundles_dict[key].keys())[0]
        soup = get_webpage(url)

        sections = soup.find_all("div", attrs={"class": "main-content-row"})

        for section in sections:
            items = section.find_all("div",
                                     attrs={"class": "dd-image-box-caption"})
            headline = section.find("h2",
                                    attrs={"class": "dd-header-headline"})
            try:
                cost = headline.text.strip()
            except:
                pass

            for item in items:
                title = item.text.strip()
                if cost in bundles_dict[key][url]:
                    bundles_dict[key][url][cost].append(title)
                else:
                    bundles_dict[key][url][cost] = [title]

    return bundles_dict

# for each bundle check it is in the previous:


def check_change(old_path, old, new):
    '''
    Given two dictionaries, old & new, checks for difference between
    dictionaries.
    New keys results in the old file being overwritten with a new save
    and the user emailed the updated JSON
    '''

    change = False

    for key in new:
        if key not in old:
            print("New Bundle: " + key)
            change = True
        else:
            pass

    if change:
        filename = path + 'bundle_json-' + str(date.today())
        ext = 1
        while os.path.isfile(filename):
            filename += '-{}'.format(str(ext))
            ext += 1

        with open(filename, 'w') as f:
            f.write(json.dumps(new, indent=4))
            f.close()
        if old_path is not 'None':
            os.remove(old_path)
        print("{} removed and replaced with {}".format(old_path, filename))

        try:
            email_update(new)
        except TypeError:
            print("Could not email update: config file incorrect")
        except SMTPAuthenticationError as e:
            print("Could not email update: config file incorrect: {}"
                  .format(e))
    else:
        print("No changes")


def email_update(data):

    print("Emailing update...")
    contents = json.dumps(data, indent=4, ensure_ascii=False)
    msg = EmailMessage()
    msg.set_content(contents)
    msg['Subject'] = 'Humble Bundle Update'
    msg['From'] = sender
    msg['To'] = recipent

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender, gmailpassword)
    s.send_message(msg)
    s.quit()


def main():

    new = populate_bundle_dict(get_bundles())
    print("Looking in {} for previous bundles file..."
          .format(os.getcwd() + "/" + path))
    try:
        old_path = glob(path + 'bundle_json*')[0]
    except IndexError:
        print("No previous file found! Creating file and sending to recipent")
        old_path = 'None'

    if old_path is not 'None':
        with open(old_path, 'r') as f:
            old = json.loads(f.read())
    else:
        old = 'None'

    check_change(old_path, old, new)


if __name__ == "__main__":
    main()
