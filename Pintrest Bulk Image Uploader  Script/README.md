# Automatically upload as many Pins as you want to Pinterest.


## What does this bot do?

This script allows you to upload as many Pins (150 in a row) as you want to Pinterest, all automatically and quickly (about 4 Pins per minute).  
The upload limit on Pinterest is about 150 pins in a row. **You can do multiple upload sessions in a day but risk having your account suspended.**

## To do list:

* ✔ <strike>Pinterest automatic login.</strike>
* ❌ Pinterest two-factor authentication support.
* ✔ <strike>Automatic Pins uploader.</strike>
* ✔ <strike>Data file browsing feature.</strike>
* ✔ <strike>CSV structure reader and interpreter.</strike>
* ✔ <strike>JSON structure reader and interpreter.</strike>

## Instructions:

* ### Basic installation of Python for beginners:

  * Download this repository or clone it:
  * It requires [Python](https://www.python.org/) 3.7 or a newest version.
  * Install [pip](https://pip.pypa.io/en/stable/installation/) to be able to have needed Python modules.
  * Open a command prompt in repository folder and type:
```
pip install -r requirements.txt
```

* ### Configuration of bot:

  * Download and install [Google Chrome](https://www.google.com/intl/en_en/chrome/).
  * Download the [ChromeDriver executable](https://chromedriver.chromium.org/downloads) that is compatible with the actual version of your Google Chrome browser and your OS (Operating System). Refer to: _[What version of Google Chrome do I have?](https://www.whatismybrowser.com/detect/what-version-of-chrome-do-i-have)_
  * Extract the executable from the ZIP file and copy/paste it in the `assets/` folder of the repository. You may need to change the path of the file:
```python
class Pinterest:
    """Main class of the Pinterest uploader."""

    def __init__(self, email: str, password: str) -> None:
        """Set path of used file and start webdriver."""
        self.email = email  # Pinterest email.
        self.password = password  # Pinterest password.
        self.webdriver_path = os.path.abspath('assets/chromedriver.exe')  # Edit this line with your path.
        self.driver = self.webdriver()  # Start new webdriver.
        self.login_url = 'https://www.pinterest.com/login/'
        self.upload_url = 'https://www.pinterest.com/pin-builder/'
```
  * **Optional:** the email and the password are asked when you run the bot, but you can:
    * create and open the `assets/email.txt` file, and then write your Pinterest email;
    * create and open the `assets/password.txt` file, and then write your Pinterest password.
  * Create your Pins data file containing all details of each Pin. It can be a JSON or CSV file. Save it in the data folder.  
    
## Known issues:

* If you are using a Linux distribution or MacOS, you may need to change some parts of the code:  
  * ChromeDriver extension may need to be changed from `.exe` to something else.
* **If you use a JSON file for your Pins data, the file path should not contain a unique "\\". It can be a "/" or a "\\\\":**
```json
"file_path": "C:/Users/Admin/Desktop/Pinterest/image.png",
// or:
"file_path": "C:\\Users\\Admin\\Desktop\\Pinterest\\image.png",
// but not:
"file_path": "C:\Users\Admin\Desktop\Pinterest\image.png", // You can see that "\" is highlighted in red.
```

