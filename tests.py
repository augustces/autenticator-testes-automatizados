from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Caminho do WebDriver
driver_path = "C:/webdriver/chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# URL da aplicação
URL_LOGIN = "http://localhost:8000/accounts/login/"

def test_login_sucesso():
    """Teste: Login com credenciais corretas"""
    driver.get(URL_LOGIN)
    driver.find_element(By.NAME, "username").send_keys("usuario_teste1")
    driver.find_element(By.NAME, "password").send_keys("123456")
    driver.find_element(By.XPATH, "/html/body/div/div/div/form/button").click()
    time.sleep(2)
    assert "Você está logado no sistema." in driver.page_source, "Erro: Mensagem de campos obrigatórios não apareceu."

def test_login_credenciais_invalidas():
    """Teste: Login com credenciais inválidas"""
    driver.get(URL_LOGIN)
    driver.find_element(By.NAME, "username").send_keys("usuario_errado")
    driver.find_element(By.NAME, "password").send_keys("senha_errada")
    driver.find_element(By.XPATH, "/html/body/div/div/div/form/button").click()
    time.sleep(2)
    assert "Credenciais inválidas" in driver.page_source, "Erro: Mensagem de credenciais inválidas não apareceu."

def test_login_campos_vazios():
    """Teste: Login com campos vazios"""
    driver.get(URL_LOGIN)
    url_antes = driver.current_url
    driver.find_element(By.XPATH, "/html/body/div/div/div/form/button").click()
    time.sleep(2)
    url_depois = driver.current_url
    assert url_antes == url_depois, "Erro: Não houve redirecionamento após o login."

def test_link_esqueci_senha():
    """Teste: Verificar se o link 'Esqueceu sua senha?' redireciona corretamente"""
    driver.get(URL_LOGIN)
    driver.find_element(By.XPATH, "/html/body/div/div/div/div/a[2]").click()
    time.sleep(2)
    assert "Informe seu e-mail para redefinir a senha" in driver.page_source, "Erro: Redirecionamento incorreto para recuperação de senha."

def test_link_cadastro():
    """Teste: Verificar se o link 'Cadastre-se' redireciona corretamente"""
    driver.get(URL_LOGIN)
    driver.find_element(By.XPATH, "/html/body/div/div/div/div/a[1]").click() 
    time.sleep(2)
    assert "Criar Conta" in driver.page_source, "Erro: Redirecionamento incorreto para página de cadastro."


# Executando os testes
test_login_sucesso()
test_login_credenciais_invalidas()
test_login_campos_vazios()
test_link_esqueci_senha()
test_link_cadastro()

# Fecha o navegador após os testes
driver.quit()
