# python-stock-notifier
## ![bull](images/bull.ico)
Python Script that push windows 10 notifications on selected stock price.
## Configuration
The script loads confoguration from [config.py](config.py) file.
### Config Variables
* **API_KEY** --> The api key for rapidAPI yahoo finance.
* **LOG_PATH** --> Log file path.
* **STOCK_SYMBOL** --> Stock Symbol.
* **STOCK_REGION** --> Stock Region.
* **ICON_PATH** --> Path to Icon. 
* **CHECK_INTERVAL** --> Interval For Checking stock price in seconds.
```bash
API_KEY = ''
LOG_PATH = r"{}\DEBUG.log".format(os.path.dirname(os.path.realpath(__file__)))
STOCK_SYMBOL = "FVRR"
STOCK_REGION = "US"
ICON_PATH = r"{}\bull.ico".format(os.path.dirname(os.path.realpath(__file__)))
CHECK_INTERVAL = 60 # Check every x seconds
```
## How to Run?
1. Create rapid API account [here](https://rapidapi.com/).
2. Generate API key.
3. Fill the configuration in [config.py](config.py).
4. Install requirements for script.
5. Create Windows Service for the script/Run the script background or foreground.
