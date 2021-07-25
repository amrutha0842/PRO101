import dropbox
import os

from dropbox.files import WriteMode


class TransferData:
    def __init__(self, accessToken):
        self.accessToken = accessToken

    def upload_file(self, file_from, file_to, fileName):
        dbx = dropbox.Dropbox(self.accessToken)

        path = file_from
        root = os.path.splitext(path)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), "/"+file_to+fileName+root[1], WriteMode("overwrite"))

        print("\nFile BackUp...successful")
        input()


def main():
    AccessToken = input("Please Input You DropBox access Token\n")
    transferData = TransferData(AccessToken)

    file_from = input("\nPlease ente the file location\n")
    if os.path.isfile(file_from):
        fileName = input("\nPlease Enter The Name Of the file\n\n")
        file_to = "Backup/"

    
        transferData.upload_file(file_from, file_to, fileName)

    else:
        print("\nPlease enter a file ")
        input()


if __name__ == '__main__':
    main()
