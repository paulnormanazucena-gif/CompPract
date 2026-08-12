import socket

client = socket.socket()

client.connect(('127.0.0.1', 8000))


while True:
    print("""
    1. add
    2. find high load activity
    3. update status
    4. decomission
    5. get report
    
    """)
    datasend = input('Send to server: ')



    data = b''

    while b'\n\n' not in data:
        data += client.recv(1024)

    data = data.decode()


    print('Server says: ', data)
