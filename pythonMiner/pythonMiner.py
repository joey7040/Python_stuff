from hashlib import sha256
MAX_NONCE = 1000000000000



def Da_SHA_inator(text):

    return sha256(text.encode("ascii")).hexdigest()


def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0' * prefix_zeros
    for nonce in range (MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = Da_SHA_inator(text)
        if new_hash.startswith(prefix_str):
            print(f"Successfully mined bitcoins with nonce value reaching: {nonce}")
            return new_hash
    raise BaseException(f"This code sucks, It couldn't find the correct hash after trying {MAX_NONCE} times")

if __name__=='__main__':
    transactions ='''
        Dhavel->Bhavin->20,
        Mando->Cara->45
    '''

    # making one up
    difficulty=7

    import time 
    start = time.time()
    print("start mining")
    new_hash = mine(5,transactions,'0000000x335af140c22e059534470500f81388e46a543b35b97a382830d8582d',difficulty)
    total_time = str((time.time() - start))
    print(f"Total time taken for mining: {total_time} seconds")
    print(new_hash)
