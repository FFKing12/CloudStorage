import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token= access_token
    
    def upload_files(self,file_from, file_to):
        dbx= dropbox.Dropbox(self.access_token)
        
        f= open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token='9Wp9rsuQaJoAAAAAAAAAAb2JJiQb-pqw6pifTwZyPmNNkbUHfJuuwv3GIBZYQ3hl'
    transferData = TransferData(access_token)
    file_from = "My Self.txt"
    file_to="/test_dropbox/My Self.txt"
    transferData.upload_files(file_from, file_to)
    

main()