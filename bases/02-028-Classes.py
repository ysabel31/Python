class Store:
  def __init__(self,name):
    self.name = name
    self.items = []
  def add_items(self, name, price):
    self.items.append({
      'name' : name,
      'price' : price
    })
  def stock_price(self):
    total = 0
    for item in self.items:
      total+=item['price']

  @classmethod
  def funcname(cls, store):
    # Return another store, with the same name as the argument name + " - franchise"
    return Store(store.name.' - franchise')
    # = return cls(store.name.' - franchise')

  @staticmethod
  def store_detail(store):
    #return a string representing the argument
    #it should be in the format 'NAME, total stock price : TOTAL'
    return '{} total stock price : {}'.format(store.name, int(store.stock_price)))