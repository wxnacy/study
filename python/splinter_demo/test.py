from splinter import Browser

browser = Browser(driver_name='chrome')
#  browser.driver.set_window_size(140, 100)
browser.visit('https://www.seamless.com/menu/tuba-express-mediterranean-grill--gryo-1550-california-st-san-francisco/682502')
#  browser.find_by_name('btnK').click()
#  html = browser.html
#  print(html)
res = browser.screenshot(name='/Users/wxnacy/PycharmProjects/study/python/splinter_demo/screenshot')
print(res)

if browser.is_text_present('splinter.readthedocs.io'):
    print("Yes, the official website was found!")
else:
    print("No, it wasn't found... We need to improve our SEO techniques")

browser.quit()
