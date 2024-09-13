import os
import smtplib
from email.message import EmailMessage
from senha import senha_a

email_seu = "pedrinhorrocha991@gmail.com"
senha_sua = senha_a

mensagem = EmailMessage()
mensagem["Subject"] = input("Insira o assunto: ")
mensagem["From"] = email_seu
mensagem["To"] = "hrga190@gmail.com"
mensagem.set_content(input("Escreva a mensagem: "))

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(email_seu, senha_sua)
        smtp.send_message(mensagem)
        print("E-mail enviado com sucesso!")
except smtplib.SMTPAuthenticationError:
    print("Erro de autenticação! Verifique o e-mail e a senha.")
except Exception as e:
    print(f"Ocorreu um erro: ")