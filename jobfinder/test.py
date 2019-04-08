from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)

driver.get('http://www.glassdoor.com/index.htm')

driver.find_element_by_xpath("//*[@id='sc.keyword']").send_keys("Software Developer")

driver.find_element_by_xpath("//*@[id='SrchHero']/div/div[1]/div/div/form/button").click()

jobs_list = driver.find_elements_by_xpath("//ul[@class='jlGrid hover']/li")

keywords = ["python", "data analyst"]

jobs_outfile = open('./jobs.txt', 'w')

for job in jobs_list:
    jobs_outfile.write(job.text)

jobs_outfile.close()