import os
from google.cloud import storage
from oauth2client.service_account import ServiceAccountCredentials

dir_path = 'path'
original_path = 'path'
creds = 'path'

storage_client = storage.Client.from_service_account_json(creds)


def upload_file(file,bucketID):
	"""
	uploads specified file to google cloud storage bucket
	Deletes compressed file after upload
	"""
	bucket = storage_client.get_bucket(bucketID)
	os.chdir(dir_path)
	print("Uploading", file, "to bucket")
	blob = bucket.blob(file)
	blob.upload_from_filename(file)
	print(blob.public_url)
	os.remove(file)
	os.chdir(original_path)

def check_bucket(file,bucketID):
	"""
	checks bucket for file and returns bool
	"""
	bucket = storage_client.bucket(bucketID)
	check = storage.Blob(bucket=bucket, name=file).exists(storage_client)
	return check

def main():
	file = ''
	bucketID = ''
	check_bucket(file,bucketID)
	upload_file(file,bucketID)

if __name__ == "__main__":
    main()
