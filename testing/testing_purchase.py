import unittest
from unittest.mock import patch, MagicMock
import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backsend.purchase import Purchase

class Movie:
    def __init__(self, title, id, price):
        self._title = title
        self._id = id
        self._price = price

    def give_title(self):
        return self._title

    def give_id(self):
        return self._id

    def give_price(self):
        return self._price


class TestPurchase(unittest.TestCase):
    def setUp(self):
        self.time = MagicMock()
        self.time.get_time.return_value = "2025-04-19 12:00:00"
        self.movie1 = Movie("Movie One", "001", 10)
        self.movie2 = Movie("Movie Two", "002", 15)
        self.movie_list = [self.movie1, self.movie2]
        self.purchase = Purchase(self.movie_list, self.time)

    @patch("builtins.input", side_effect=["1", "1", "001", "5"])
    def test_add_by_id(self, mock_input):
        self.purchase.add_to_cart()
        self.assertIn("Movie One", self.purchase.cart)
        self.assertEqual(self.purchase.cost, 10)

    @patch("builtins.input", side_effect=["1", "2", "Movie Two", "5"])
    def test_add_by_title(self, mock_input):
        self.purchase.add_to_cart()
        self.assertIn("Movie Two", self.purchase.cart)
        self.assertEqual(self.purchase.cost, 15)

    @patch("builtins.input", side_effect=[
        "1", "1", "001",      
        "2", "Movie One",     
        "5"                   
    ])
    def test_remove_from_cart(self, mock_input):
        self.purchase.add_to_cart()
        self.assertNotIn("Movie One", self.purchase.cart)
        self.assertEqual(self.purchase.cost, 0)

    @patch("builtins.input", side_effect=["1", "1", "001", "3", "5"])
    def test_view_cart(self, mock_input):
        with patch("builtins.print") as mock_print:
            self.purchase.add_to_cart()
            calls = [" ".join(str(arg) for arg in call[0]) for call in mock_print.call_args_list]
            self.assertTrue(any("Items in your cart:" in c for c in calls))
            self.assertTrue(any("- Movie One" in c for c in calls))

    @patch("builtins.input", side_effect=["1", "2", "Movie Two", "4", "5"])
    def test_purchase_resets_cart(self, mock_input):
        self.purchase.add_to_cart()
        self.purchase.add_to_cart()
        self.assertEqual(self.purchase.cart, [])
        self.assertEqual(self.purchase.cost, 0)

if __name__ == "__main__":
    unittest.main()
