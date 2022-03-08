import jwt

# Payload
data_to_encode = {'some':'payload'}

# setting up secret keys 
encryption_secret = 'secrete'

algorithm = 'HS256'

encoded = jwt.encode(data_to_encode, encryption_secret, algorithm=algorithm)

decoded = jwt.decode(encoded, encryption_secret, algorithms=[algorithm])

print (f'encoded:{encoded}\n')
print (f'decoded:{decoded}')
