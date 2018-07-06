import datetime as date

def create_genisis_block():
  #Construct a block manully with index 0 and
  #arbitrary previous hash
  return Block(0, date.datetime.now(), "Genisis Block", "0")