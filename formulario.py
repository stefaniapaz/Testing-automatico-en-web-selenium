from selenium import webdriver
from faker import Faker
from selenium.webdriver.common.keys import Keys


fake = Faker()

# Configura el navegador y abre la página del formulario
url_formulario = "https://demoqa.com/text-box"
#Ruta de chromedriver
ruta_chromedriver = "/home/stefania/Documentos/Cursos/chromedriver_linux64/chromedriver"
# Puedes cambiar 'Chrome()' por 'Firefox()' u otro navegador compatible
driver = webdriver.Chrome(executable_path=ruta_chromedriver)


driver.get(url_formulario)

# Genera datos aleatorios con Faker
full_name = fake.name()
email = fake.email()
current_address = fake.address()
permanent_address = fake.address()

# Localiza los campos del formulario e ingresa la información
campo_full_name = driver.find_element_by_id("userName")  # Reemplaza con el nombre del campo de nombre completo en tu HTML
campo_email = driver.find_element_by_id("userEmail")  # Reemplaza con el nombre del campo de email en tu HTML
campo_current_address = driver.find_element_by_id("currentAddress")  # Reemplaza con el nombre del campo de dirección actual en tu HTML
campo_permanent_address = driver.find_element_by_id("permanentAddress")  # Reemplaza con el nombre del campo de dirección permanente en tu HTML

campo_full_name.send_keys(full_name)
campo_email.send_keys(email)
campo_current_address.send_keys(current_address)
campo_permanent_address.send_keys(permanent_address)

# Envía el formulario
boton_submit = driver.find_element_by_id("submit")  # Reemplaza con el nombre del botón de envío en tu HTML
boton_submit.click()

# Puedes agregar una pausa (sleep) para asegurar que la página se cargue completamente
# from time import sleep
# sleep(2)

# Cierra el navegador al finalizar
# driver.quit()

