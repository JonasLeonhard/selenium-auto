# selenium-auto
Selenium Python3 automation of browser tasks like clicking and writing. Written for https://universalmusic.digital/streamingcompetition/die-orsons/, where you have to click on the repeat button every 30 seconds to get points.

# About
Basic Selenium Automation Script.
Automate interval, maxInterval, WebsiteUrl, element
Modes : Write / Click
  
Pass input with argparse: fx:
```
cd selenium-auto
sudo python3 auto.py -u 'https://google.com' -nm 'q' -i 0.5 -wri 'args ' -i_m 10 
sudo python3 auto.py -u 'https://universalmusic.digital/streamingcompetition/die-orsons/#/player' -i 32 -noauto -xp '//*[@id="app"]/main/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div/div[1]/div[4]/div[2]/button[2]' -cli -deb
```

![Startscreen](../master/gitreadme/running.gif)

use -h for help

# Requirements:
```
Chrome Version 77.0.3865.90 (Official Build) (64-bit) or later
python3
python3 get-pip.py
pip3 install selenium
pip3 install keyboard
```
