import socket

def converter_base(numero, base_origem, base_destino):
    numero_base_10 = int(numero, base_origem)
    if base_destino == 10:
        return str(numero_base_10)
    else:
        base_num = ""
        while numero_base_10 > 0:
            digito = numero_base_10 % base_destino
            if digito >= 10:
                base_num += chr(ord('A') + digito - 10)
            else:
                base_num += str(digito)
            numero_base_10 //= base_destino
        return base_num[::-1]

def complemento_2_to_decimal(bin_str):
    if bin_str[0] == '1':
        return -((1 << len(bin_str)) - int(bin_str, 2))
    else:
        return int(bin_str, 2)

def decimal_to_complemento_2(num):
    if num < 0:
        num = (1 << 8) + num
    return format(num, '08b')

def soma_subtracao_complemento_2(num1, num2, operacao):
    if operacao == 'soma':
        resultado = complemento_2_to_decimal(num1) + complemento_2_to_decimal(num2)
    elif operacao == 'subtracao':
        resultado = complemento_2_to_decimal(num1) - complemento_2_to_decimal(num2)
    
    overflow = False
    if resultado > 127 or resultado < -128:
        overflow = True
        resultado = resultado & 0xFF  # Mantém apenas os 8 bits menos significativos

    return decimal_to_complemento_2(resultado), overflow

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(('localhost', 12345))
    servidor.listen(1)
    print("Servidor iniciado e aguardando conexões...")

    while True:
        cliente_socket, endereco = servidor.accept()
        print(f"Conexão estabelecida com {endereco}")

        while True:
            cliente_socket.send(b"Digite 1 para converter um numero, 2 para somar/subtrair numeros binarios ou 0 para encerrar: ")
            escolha = cliente_socket.recv(1024).decode()

            if escolha == '1':
                cliente_socket.send(b"Digite o numero a ser convertido: ")
                numero = cliente_socket.recv(1024).decode()

                cliente_socket.send(b"Digite a base de origem: ")
                base_origem = int(cliente_socket.recv(1024).decode())

                cliente_socket.send(b"Digite a base de destino: ")
                base_destino = int(cliente_socket.recv(1024).decode())

                resultado = converter_base(numero, base_origem, base_destino)
                cliente_socket.send(f"Resultado da conversao: {resultado}".encode())
            elif escolha == '2':
                cliente_socket.send(b"Digite 'soma' para somar ou 'subtracao' para subtrair: ")
                operacao = cliente_socket.recv(1024).decode()

                cliente_socket.send(b"Digite o primeiro valor binario (8 bits): ")
                num1 = cliente_socket.recv(1024).decode()

                cliente_socket.send(b"Digite o segundo valor binario (8 bits): ")
                num2 = cliente_socket.recv(1024).decode()

                resultado, overflow = soma_subtracao_complemento_2(num1, num2, operacao)
                mensagem = f"Resultado: {resultado}. Overflow: {'Sim' if overflow else 'Nao'}."
                cliente_socket.send(mensagem.encode())
            elif escolha == '0':
                cliente_socket.send(b"Encerrando a conexao.")
                cliente_socket.close()
                break

if __name__ == "__main__":
    iniciar_servidor()
