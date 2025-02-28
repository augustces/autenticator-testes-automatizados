# Testes Automatizados com Selenium

Testes automatizados para uma tela de login de uma aplicação web.

## Pré-requisitos

Antes de rodar os testes, você precisará:

1. Ter o **Python** instalado, na versão acima de 3.
2. Instalar o **Selenium**.
3. Baixar o **ChromeDriver** adequado à sua versão do Google Chrome.

### 1. Instalar as dependências

Instale as dependências:

```bash
pip install -r requirements.txt

```

### 2. Instalar o ChromeDriver

Verifique a versão do chromedriver antes de instalá-la, pois ela deve ser a mesma do seu navegador. Para verificar a versão do seu chrome pesquise clique [aqui](chrome://settings/help). E para instalar a o chromedriver clique [aqui](https://googlechromelabs.github.io/chrome-for-testing/). Coloque o arquivo chromedriver.exe (no Windows) ou chromedriver (no Linux/macOS) no diretório `C:/webdriver/`, ou ajuste o caminho no código como quiser. Copie o caminho para o arquivo chromedriver e depois altere no código na variável indicada.

### 3. Executar os testes

Execute no diretório do arquivo `tests.py`:

```bash
python tests.py

```

## Estrutura do código:

```bash
test_login_sucesso: Testa o login com credenciais corretas e verifica se o usuário é redirecionado.
test_login_credenciais_invalidas: Testa o login com credenciais incorretas e verifica se a mensagem de erro é exibida.
test_login_campos_vazios: Testa o login com campos vazios e verifica se a página não é redirecionada.
test_link_esqueci_senha: Verifica se o link "Esqueci a senha?" redireciona para a página de recuperação.
test_link_cadastro: Verifica se o link "Cadastre-se" redireciona para a página de cadastro.
```