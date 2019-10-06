class data():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def printdata(self):
        print(self.username)
        print(self.password)


    def menu(self):
        print("--------------------- Selamat Datang " + self.username + " ---------------------")
        print('')
        print("----------------------------------------------------------------------")
        print("|                                                                    |")
        print("|                            I Love You                              |")
        print("|                                                                    |")
        print("----------------------------------------------------------------------")
    
loginData = data(input('Masukkan username: '), input('Masukkan password: '))


if(loginData.username != 'alvinakbar'):
    print ("Username Salah")
elif(loginData.password != '1234'):
    print("Password Salah")
else:
    loginData.menu()
