from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=options)

driver.get("https://ashblogs12.vercel.app/")


def S(X): return driver.execute_script(
    'return document.body.parentNode.scroll'+X)


driver.set_window_size(S('Width'), S('Height'))
driver.find_element_by_tag_name('body').screenshot('blog.png')

driver.close()
