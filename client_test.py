import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for item in quotes:
      _stock = item['stock']
      _bid_price = item['top_bid']['price']
      _ask_price = item['top_ask']['price']
      _price = (_bid_price + _ask_price) / 2
      self.assertEqual(getDataPoint(item), (_stock, _bid_price, _ask_price, _price))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for item in quotes:
      _stock = item['stock']
      _bid_price = item['top_bid']['price']
      _ask_price = item['top_ask']['price']
      _price = (_bid_price + _ask_price) / 2
      self.assertEqual(getDataPoint(item), (_stock, _bid_price, _ask_price, _price))

  def test_getDataPoint_calculatePriceIsNegative(self):
    quotes = [
      {'top_ask': {'price': -200.0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': -150.33, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for item in quotes:
      _stock = item['stock']
      _bid_price = item['top_bid']['price']
      _ask_price = item['top_ask']['price']
      _price = (_bid_price + _ask_price) / 2
      if _bid_price <= 0.0 and _ask_price <= 0.0:
        self.assertEqual(getDataPoint(item), (_stock, 0.0, 0.0, 0.0))
      if _bid_price <= 0.0:
        self.assertEqual(getDataPoint(item), (_stock, 0.0, _ask_price, _ask_price / 2))
      if _ask_price <= 0.0:
        self.assertEqual(getDataPoint(item), (_stock, _bid_price, 0.0, _bid_price / 2))
      

  """ ------------ Add more unit tests ------------ """
  def test_getRatio_calculateRatio(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for item in quotes:
      _price_a = float(item['top_ask']['price'])
      _price_b = float(item['top_bid']['price'])
      self.assertEqual(getRatio(_price_a, _price_b), _price_a / _price_b)

  def test_getRatio_calculateRatioWherePriceHasZero(self):
    quotes = [
      {'top_ask': {'price': 0.0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0.0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for item in quotes:
      _price_a = float(item['top_ask']['price'])
      _price_b = float(item['top_bid']['price'])
      self.assertEqual(getRatio(_price_a, _price_b), None)

def test_getRatio_calculateRatioWherePriceHasNegative(self):
    quotes = [
      {'top_ask': {'price': -13.45, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': -23.86, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for item in quotes:
      _price_a = float(item['top_ask']['price'])
      _price_b = float(item['top_bid']['price'])
      self.assertEqual(getRatio(_price_a, _price_b), None)


if __name__ == '__main__':
    unittest.main()
