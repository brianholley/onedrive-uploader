# onedrive-uploader

Easy onedrive uploader - I use this to upload 3d printer timelapses to OneDrive, but YMMV

## Dependencies and Setup

	- Python 2.7 (I haven't tested compatibility with 3.x)
	- 'pip install onedrivesdk'
	- Add your client id to secrets.py
	- 'python auth.py' to cache your auth code
	- 'python upload.py <source path> <dest path>'

## References

[OneDrive python SDK GitHub](https://github.com/onedrive/onedrive-sdk-python)

