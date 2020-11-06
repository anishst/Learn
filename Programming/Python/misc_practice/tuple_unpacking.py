from selenium.webdriver.common.by import By

USERNAME_FIELD = 'username', By.ID

field, locator = USERNAME_FIELD

print(USERNAME_FIELD)
print(*USERNAME_FIELD)

print(field)
print(locator)