import dropbox
import os


class TransferData(object):
    def __init__(self, access_key) -> None:
        self.access_key = access_key

    def upload_files(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_key)

        for root, dirs, files in os.walk(file_from):
            for file in files:
                local_path = os.path.join(root, file)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

            # local_path = input("Enter The folder You want to backup: \n")
            # relative_path = os.path.relpath(local_path, file_from)

            with open(local_path, 'rb') as f:
                dbx.files_upload(f.read(), dropbox_path,
                                 mode=dropbox.files.WriteMode('overwrite'))


def main():
    access_key = "sl.A3uOGageLBEjtsyx2unqk0A0QczaUv9WkjhY3g10IoaRgkHC520OUVpPizByfTLvbtp5aU-NsgXPnTE5Go9FY3mxeTMG0gZ4y-Zrk8Zm2TlkG7Xx2VHCS0dpcT2QOBxeO2NbM-woqBQ"

    transfer = TransferData(access_key)
    file_from = input("Enter the source folder\n")
    file_to = input("Enter the full path\n")
    transfer.upload_files(file_from, file_to)
    print("file/folder is uploaded successfully")


main()
