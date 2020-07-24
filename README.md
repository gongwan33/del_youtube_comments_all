# A Simple Selenium Script to Clear Your Youtube Comments

Deleting your Youtube comment history can be stressing. This python script utilises Selenium to automatically delete all your Youtube comments.

Before using this script please install selenium and chromedriver.

### Install selenium
`pip install selenium`

### chromedriver
Please download the driver from the following URL. Then put the downloaded binary file in to your PATH enviroment variable.
[https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)

After the installation, please execute this script by using the following command.

`python youtube_comment_del_all.py`

A chrome window will be automatically opened and targeted to the login page of stackoverflow. Please use your google account to login. Then the script will direct to your Youtube comment history page. And the automated deleting process will begin. 

The reason for using the stackoverflow login page instead of the youtube login page is because the latest Google scurity rules don't allow the browser opened by Selenium to login. It will be recognised as an 'inscure browser'. So this is just a work around.
