from pybitcoin import BitcoinPrivateKey

class NamecoinPrivateKey(BitcoinPrivateKey):
  _pubkeyhash_version_byte = 52
  
private_key = BitcoinPrivateKey()  
namecoin_private_key = NamecoinPrivateKey(private_key.to_hex())
ncpkwif = namecoin_private_key.to_wif()
print ncpkwif 
#'73zteEjenBCK7qVtG2yRPeco2TP5w93qBW5sJkxYoGYvbWwAbXv'
namecoin_public_key = namecoin_private_key.public_key()
ncaddr = namecoin_public_key.address()
#'MyMFt8fQdZ6rEyDhZbe2vd19gD8gzagr7Z'
print "NMC.addr: "+ ncaddr

#explorer https://bchain.info/NMC/addr/N83EcwrAMDWicACS7u42E1X8x8d4vua1Av
