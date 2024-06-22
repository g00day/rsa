from rsa import Receiver, Encoder 

m = 97 # For instance we want to encode this integer as a message

r = Receiver() # initialize the receiver
e, n = r.get_public_encryption_keys() # Getting public keys of the receiver
en = Encoder(e, n, m) # initialize the encoder and pass our message(m) into the arguments
c = en.get_c() # Getting the encrypted data
r.get_decoded_msg(c) # Decode our encrypted message(m). This method will return the encoded message
