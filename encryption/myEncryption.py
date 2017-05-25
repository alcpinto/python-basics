import base64
from boto3.session import Session
import time


def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    encryptedbytes = base64.urlsafe_b64encode(''.join(enc).encode())
    return encryptedbytes.decode()


def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


access_key = 'AKIAINRDS3M2D6SWC5TQ'
secret_key = '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'

session = Session(aws_access_key_id=access_key,
                  aws_secret_access_key=secret_key)

s3 = session.resource('s3',
                      aws_access_key_id=access_key,
                      aws_secret_access_key=secret_key
                      )

bucket = s3.Bucket('sessioncam-cs-analytics')
print(bucket.name)

# prefix = 'cxbatched/'+time.strftime("%Y/%m/%d")+'/'
# for key in bucket.list(prefix=prefix):
#         print("{name}\t{size}\t{modified}".format(
#                 name=key.name,
#                 size=key.size,
#                 modified=key.last_modified)
#               )

#aws_access_key_id=access_key,
#                   aws_secret_access_key=secret_key
encypted = encode('', access_key)

decrypted = decode('', encypted)

print(encypted)
print(decrypted)
