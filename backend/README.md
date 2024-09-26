## Instalação e Execução

1. Clone o repositório:

    ```
    git clone https://github.com/EduardoMeneghel/datasets
    ```

2. Entre na pasta do projeto:

    ```
    cd (diretório da pasta)
    ```

3. Crie e ative um ambiente virtual (opcional, mas recomendado):

    ```
    python -m venv venv
    ```

    - Ative o ambiente virtual no Windows:

      ```
      venv\Scripts\activate
      ```

      caso der erro em executar o comando acima execute isso no PowerShell dando permição de adiministrador
      ```
      Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
      ```

    - Ative o ambiente virtual no Unix ou MacOS:

      ```
      source venv/bin/activate
      ```

4. Instale as dependências:

    ```
    python.exe -m pip install --upgrade pip
    pip install setuptools
    pip install -r requirements.txt
    ```

5. Execute o servidor Flask:

    ```
    flask run
    ```

O servidor estará acessível em [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

6. Para parar o processo:

    ```
    ctrl + C
    ```

   Para sair do venv:

    ```
    deactivate
    ```

7. Rodar os testes

    ```
    pytest
    ```

7. Link do colab

    ```
    https://colab.research.google.com/drive/1IefGmeW42RnkPi4as9Atpwf6peRoosbW#scrollTo=by7iBzT1-Vvc
    ```