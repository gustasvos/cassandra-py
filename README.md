# Como rodar

Crie o database Cassandra em https://astra.datastax.com.

Após isto adicione na raiz do projeto os arquivos `secure-connect.zip` e `token.json` que podem ser gerados na aba "Connect" dentro do database criado. Na raiz há exemplos já nos mesmos nomes usados pelo código.

Depois instalar as dependencias e rodar o `main.py`:

```bash
> pip install -r requirements.txt
> python3 main.py
```
