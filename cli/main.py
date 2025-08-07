import argparse

from helpers import ipfs_client


def encrypt_upload(file):
    print(f"Encrypting and uploading {file}...")
    ipfs_client.upload_file_to_ipfs(file)

def download_decrypt(filename):
    print(f"Downloading and decrypting {filename}...")

def list_files():
    print(f"Listing all files in current directory...")

def main():
    parser = argparse.ArgumentParser(description='Post-Quantum file encryption/decryption and upload CLI tool for Filecoin-backed storage.')
    subparsers = parser.add_subparsers(dest='command')

    # encrypt_upload command
    upload_parser = subparsers.add_parser('encrypt-upload', help='Encrypt and upload a file')
    upload_parser.add_argument('file', help='File to encrypt and upload')

    # download_decrypt command
    download_parser = subparsers.add_parser('download-decrypt', help='Download and decrypt a file')
    download_parser.add_argument('filename', help='original filename to download and decrypt')

    # list command
    list_parser = subparsers.add_parser('list', help='List all tracked files')

    args = parser.parse_args()

    # command handling
    if args.command == 'encrypt-upload':
        encrypt_upload(args.file)
    elif args.command == 'download-decrypt':
        download_decrypt(args.filename)
    elif args.command == 'list':
        list_files()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()