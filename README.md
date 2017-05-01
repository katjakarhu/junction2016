# junction2016

See https://github.com/katjakarhu/HAPI-API for new API implementation

# Running Hapi Server

The Hapi API is built on Python3, Django and Django Rest Framework.

1. Install requirements: 

   pip install -r hateapi/requirements.txt

2. Run server (it will start at https://localhost:8000 by default):

   python3 manage.py runsslserver
   
3. Give an URL to the API, you will get a JSON response in return, e.g. type https://localhost:8000/fakenews?url=urlhere&url=secondurl&url=thirdurl

# Installing Hapi Chrome extension
1. Visit chrome://extensions in your browser (or open up the Chrome menu by clicking the icon 
to the far right of the Omnibox:  The menu's icon is three horizontal bars. and select Extensions 
under the Tools menu to get to the same place).

2. Ensure that the Developer mode checkbox in the top right-hand corner is checked.

3. Click Load unpacked extension… to pop up a file-selection dialog.

4. Navigate to the directory (repo/chrome_extension) and select it.

5. Start a happier life with no fake news and hate speech Wuhu!
