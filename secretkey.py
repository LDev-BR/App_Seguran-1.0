import secrets
#Use isso para gerar a SECRET_KEY e colocar no .env
def segredo():
    print(f"\n{secrets.token_hex(32)}\n")
#Copie o resultado que aparecer no terminal e cole no .env da seguinte forma: SECRET_KEY=resultado
segredo()