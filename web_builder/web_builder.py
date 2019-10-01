from selenium import webdriver

class Web_Builder:
    # options, driver
    # 
    def __init__(self, *args, **kwargs):
        
        # Setup Selenium chromedriver with options 
        # Options list: https://peter.sh/experiments/chromium-command-line-switches/
        print("Web_Builder init: building options ...")
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument("--test-type")

        print("Web_Builder init: building driver ...\n")
        self.driver = webdriver.Chrome(
        executable_path="./driver/chromedriver", 
        options=self.options
        )

    def getElement_byId(self, el_id):
            try: 
                return self.driver.find_element_by_id(el_id)
            except:
                print(f'elementId exection, id: {el_id} not found in url')
    
    def getElement_byClass(self, el_class):
            try: 
                return self.driver.find_element_by_class(el_class)
            except:
                print(f'elementClass exection, class {el_class} not found in url')

    def getElement_byName(self, el_name):
            try: 
                return  self.driver.find_element_by_name(el_name)
                
            except:
                print(f'elementClass exection, class {el_class} not found in url')
    
    def getElement_byXpath(self, el_xpath):
            try: 
                return   self.driver.find_element_by_xpath(el_xpath)
                
            except:
                print(f'elementClass exection, class {el_class} not found in url')
       