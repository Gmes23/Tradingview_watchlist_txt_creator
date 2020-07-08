import cbpro
import re
public_client = cbpro.PublicClient()

getProducts = public_client.get_products()
mykeys = ['id']

f = open("coinbase.txt", "a")
for id in getProducts:
    if not 'USDC' in id['id']:
        if 'USD' in id['id']:
            f.write('COINBASE:')
            f.write(id['id'].replace("-", ""))
            f.write('\n')
f.close()

