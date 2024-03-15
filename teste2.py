import socket

def ping_port(host, port):
    try:
        # Cria um objeto socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Define um timeout para a conexão (opcional)
        s.settimeout(2)
        # Tenta conectar ao host na porta especificada
        result = s.connect_ex((host, port))
        # Verifica se a conexão foi bem-sucedida
        if result == 0:
            print(f"A porta {port} está aberta em {host}.")
        else:
            print(f"A porta {port} está fechada em {host}.")
        # Fecha o socket
        s.close()
    except socket.error as e:
        print(f"Erro ao conectar ao host {host} e porta {port}: {e}")

# Exemplo de uso
host = '18.234.73.132 3306'  # Endereço IP ou nome do host
port = 3306         # Número da porta que você deseja pingar
ping_port(host, port)