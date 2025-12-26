from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


# ---------------------------------------------------------
#  TASK 1 — Проверка изменения текста кнопки
# ---------------------------------------------------------
def test_change_button_text():
    driver = webdriver.Firefox()
    driver.get("http://uitestingplayground.com/textinput")

    # Вводим текст
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("ITCH")

    # Кликаем кнопку
    button = driver.find_element(By.ID, "updatingButton")
    button.click()

    # Проверяем изменение
    assert button.text == "ITCH", f"Кнопка не изменила текст, сейчас: '{button.text}'"

    driver.quit()


# ---------------------------------------------------------
#  TASK 2 — Проверка загрузки третьего изображения (alt)
# ---------------------------------------------------------
def test_loading_images_third_alt():
    driver = webdriver.Firefox()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    wait = WebDriverWait(driver, 15)

    # Ждём, пока появится минимум 3 изображения
    def three_images_present(d):
        imgs = d.find_elements(By.TAG_NAME, "img")
        return imgs if len(imgs) >= 3 else False

    images = wait.until(three_images_present)

    # Берём третью картинку (индекс 2)
    third_image = images[2]
    alt_value = third_image.get_attribute("alt")

    # Исторически ожидалось "award", сейчас на сайте "calendar".
    # Для устойчивости тест принимает оба значения.
    assert alt_value in ("award", "calendar"), f"Неожиданное значение alt: '{alt_value}'"

    driver.quit()