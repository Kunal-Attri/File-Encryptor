from cryptography.fernet import Fernet

class Encryptor():

    def key_create(self):
        key = Fernet.generate_key()
        return key

    def key_write(self, key, key_name):
        with open(key_name, 'wb') as mykey:
            mykey.write(key)

    def key_load(self, key_name):
        with open(key_name, 'rb') as mykey:
            key = mykey.read()
        return key


    def file_encrypt(self, key, original_file, encrypted_file):
        
        f = Fernet(key)

        with open(original_file, 'rb') as file:
            original = file.read()

        encrypted = f.encrypt(original)

        with open (encrypted_file, 'wb') as file:
            file.write(encrypted)

    def file_decrypt(self, key, encrypted_file, decrypted_file):
        
        f = Fernet(key)

        with open(encrypted_file, 'rb') as file:
            encrypted = file.read()

        decrypted = f.decrypt(encrypted)

        with open(decrypted_file, 'wb') as file:
            file.write(decrypted)


encryptor=Encryptor()

while True:
   print("""\nOperations available:
1. Encrypt File
2. Decrypt FIle
3. Exit""")
   inp = int(input("Operation: "))
   if inp == 1:
      input_file = input("Input File location: ")
      output_file = input("Output File name or location: : ")
      mykey=encryptor.key_create()
      encryptor.key_write(mykey, 'mykey.key')
      loaded_key=encryptor.key_load('mykey.key')
      encryptor.file_encrypt(loaded_key, input_file, output_file)
      print("File encrypted. Please store the key file securely.")
   elif inp == 2:
      keyFile = input("Key file location [Default - mykey.key]: ")
      if keyFile == "":
          keyFile = "mykey.key"
      loaded_key=encryptor.key_load(keyFile)
      input_file = input("Input File location: ")
      output_file = input("Output File name or location: : ")
      encryptor.file_decrypt(loaded_key, input_file, output_file)
   elif inp == 3:
      exit()
   else:
      print("Invalid Input, try again...")
