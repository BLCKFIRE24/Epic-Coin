import hashlib 
import json
from time import time

class Block:
  def __init__(self, index, timestamp, data, previous_hash):
    self.transactions = []
    self.chain = []

#create genisis block
self.newblock(self, proof, previous_hash)

#create a new block to add to blockchain
def new_block(self, proof, previous_hash=None):
  block = {
  'index': len(self.chain) + 1,
  'timestamp': time(),
  'transactions': self.current_transactions,
  'proof': proof,
  'previous_hash': previous_hash or self.hash(self.chain[-1]),
  }
 self.current_transactions = []
 
 self.chain.append(block)
 return block

def new_transaction(self,sender,rescipenet, amount)
#creates new transaction to add to next mined block
self.current_transaction.append({
  'sender': sender,
  'recipient': recipient,
  'amount': amount,
  })
return self.last_block['index'] + 1
#implement proof of work algorithm
def proof_of_work(self, last_proof):
   proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof