# tir104

## Docker
- [Docker](https://docs.uuboyscy.dev/docs/category/docker-tutorial)

## Data Pipeline
- [ETL](https://docs.uuboyscy.dev/docs/Data%20Pipeline/What%20is%20ETL)
- [What is API](https://docs.uuboyscy.dev/docs/intro)
- [Pandas](https://docs.uuboyscy.dev/docs/category/pandas-tutorial)
  - [Pandas sample code](https://github.com/uuboyscy/course-datamining/blob/master/module_05_Pandas_introduction/00_pandas.ipynb)
  - Pandas datetime
    ```
    """
    A general datetime format:
        yyyy-mm-dd HH:MM:ss
    """
    ```
## Orchestration
### Airflow
  - [Airflow demo repository](https://github.com/uuboyscy/airflow-demo)
  - [Airflow dosc](https://docs.uuboyscy.dev/docs/Orchestration/AirFlow/)

## Notes
  - [How to parse external arguments](https://github.com/uuboyscy/tir104/blob/main/airflow-demo/utils/parse_external_arg.py)

## Advanced
- [Dev container](https://github.com/uuboyscy/demo-devcontainer)
- [Decorator](https://github.com/uuboyscy/pycontw-2024-decorators/blob/main/PyConTW%20-%202024-PyConTW-decorators.ipynb)

### SeleniumGrid
  - Docker run
    ```bash
    docker run -it -d \
      --name selenium-dev \
      -p 14444:4444 \
      -p 15900:5900 \
      -p 17900:7900 \
      -v /dev/shm:/dev/shm \
      -e SE_NODE_OVERRIDE_MAX_SESSIONS=true \
      -e SE_NODE_MAX_SESSIONS=5 \
      -e JAVA_OPTS=-XX:ActiveProcessorCount=5 \
      selenium/standalone-chrome:120.0
    ```
  - Sample Python code
    ```python
    import time
    from selenium.webdriver import Chrome
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    import requests
    from bs4 import BeautifulSoup
    
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("window-size=1080,720")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--allow-insecure-localhost")
    chrome_options.add_argument("--headless")
    
    driver = webdriver.Remote(
        command_executor="http://localhost:14444/wd/hub",
        options=chrome_options,
    )
    # driver = Chrome()
    
    url = "https://www.ptt.cc/bbs/index.html"
    
    driver.get(url)
    time.sleep(10)
    
    driver.find_element(by=By.CLASS_NAME, value="board-name").click()
    time.sleep(10)
    
    driver.find_element(by=By.CLASS_NAME, value="btn-big").click()
    time.sleep(10)
    
    cookie = driver.get_cookies()
    time.sleep(10)
    
    driver.quit()
    
    ss = requests.session()
    
    # Extract cookies
    for c in cookie:
        ss.cookies.set(c["name"], c["value"])
    
    res = ss.get("https://www.ptt.cc/bbs/Gossiping/index.html")
    soup = BeautifulSoup(res.text, "html.parser")
    print(soup.prettify())
    ```

### Install Docker on Compute Engine
1. Login to Compute Engine via gcloud
2. Install docker
   - https://docs.docker.com/engine/install/ubuntu/
     ```bash
      # Add Docker's official GPG key:
      sudo apt-get update
      sudo apt-get install ca-certificates curl
      sudo install -m 0755 -d /etc/apt/keyrings
      sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
      sudo chmod a+r /etc/apt/keyrings/docker.asc
      
      # Add the repository to Apt sources:
      echo \
        "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
        $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
        sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
      sudo apt-get update
     ```

     ```bash
     sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
     ```
3. Add permission of Docker to normal user
   ```bash
   sudo usermod -aG docker $(whoami)
   ```
4. Re-login (via gcloud), then you can use docker command
5. Run a sample MySQL container
   ```bash
   docker run -d --name my-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -p 3306:3306 mysql:latest
   ```

## GCP note
https://uuboyscy.notion.site/GCP-6301fc45c4924b9f929d5aac5049e52c?pvs=4
