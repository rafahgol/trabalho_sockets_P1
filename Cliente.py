import socket

def iniciar_cliente():
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect(('localhost', 12345))

    while True:
        mensagem = cliente_socket.recv(1024).decode()
        escolha = input(mensagem)
        cliente_socket.send(escolha.encode())

        if escolha == '1':
            mensagem = cliente_socket.recv(1024).decode()
            numero = input(mensagem)
            cliente_socket.send(numero.encode())

            mensagem = cliente_socket.recv(1024).decode()
            base_origem = input(mensagem)
            cliente_socket.send(base_origem.encode())

            mensagem = cliente_socket.recv(1024).decode()
            base_destino = input(mensagem)
            cliente_socket.send(base_destino.encode())

            resultado = cliente_socket.recv(1024).decode()
            print(resultado)
        elif escolha == '2':
            mensagem = cliente_socket.recv(1024).decode()
            operacao = input(mensagem)
            cliente_socket.send(operacao.encode())

            mensagem = cliente_socket.recv(1024).decode()
            num1 = input(mensagem)
            cliente_socket.send(num1.encode())

            mensagem = cliente_socket.recv(1024).decode()
            num2 = input(mensagem)
            cliente_socket.send(num2.encode())

            resultado = cliente_socket.recv(1024).decode()
            print(resultado)
        elif escolha == '3':
            mensagem = cliente_socket.recv(1024).decode()
            num1 = input(mensagem)
            cliente_socket.send(num1.encode())

            mensagem = cliente_socket.recv(1024).decode()
            num2 = input(mensagem)
            cliente_socket.send(num2.encode())

            resultado = cliente_socket.recv(1024).decode()
            print(resultado)
        elif escolha == '4':
            mensagem = cliente_socket.recv(1024).decode()
            numero = input(mensagem)
            cliente_socket.send(numero.encode())

            resultado = cliente_socket.recv(1024).decode()
            print(resultado)
        elif escolha == '5':
            mensagem = cliente_socket.recv(1024).decode()
            string = input(mensagem)
            cliente_socket.send(string.encode())

            resultado = cliente_socket.recv(1024).decode()
            print(resultado)
        elif escolha == '0':
            mensagem = cliente_socket.recv(1024).decode()
            print(mensagem)
            break

    cliente_socket.close()

if __name__ == "__main__":
    iniciar_cliente()
