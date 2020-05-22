#!/usr/bin/env python3.5
"""Goes through all usernames and collects their information"""
import sys

from util.account import login
from util.chromedriver import SetupBrowserEnvironment
from util.cli_helper import get_all_user_names
from util.datasaver import Datasaver
from util.extractor import extract_information
from util.extractor_posts import InstagramPost
from util.settings import Settings
from time import sleep

import pandas as pd

username = pd.read_csv('result_1.csv', header=0)
username1 = username.dropna(subset=['username'])
list_username = username1['username'].to_list()


with SetupBrowserEnvironment() as browser:
    usernames = list_username
    for username in usernames:

        print('Extracting information from ' + username)
        information, user_commented_list = extract_information(browser, username, Settings.limit_amount)

        Datasaver.save_profile_json(username, information.to_dict())
        print("Number of users who commented on their profile is ", len(user_commented_list),"\n")

        Datasaver.save_profile_commenters_txt(username, user_commented_list)
        print("\nFinished. The json file and nicknames of users who commented were saved in profiles directory.\n")
