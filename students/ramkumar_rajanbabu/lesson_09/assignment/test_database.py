"""Module for testing database"""

import unittest
from unittest import TestCase
import database as db

PATH = "C:/Users/kumar/Documents/GitHub/SP_Python220B_2019/" \
       "students/ramkumar_rajanbabu/lesson_05/assignment"


class TestDatabase(TestCase):
    """Test Database"""
    def test_import_data(self):
        """Testing import data"""
        db.clear_database()
        actual = db.import_data(PATH, "products.csv", "customers.csv",
                                "rentals.csv")
        expected = ((4, 3, 4), (0, 0, 0))
        self.assertEqual(actual, expected)

    def test_show_available_products(self):
        """Tetsing showing available products"""
        db.clear_database()
        actual = db
        actual.import_data(PATH, "products.csv", "customers.csv",
                           "rentals.csv")
        expected = {"51": {"description": "TV",
                           "product_type": "Electric",
                           "quantity_available": "4"},
                    "999": {"description": "Couch",
                            "product_type": "Furniture",
                            "quantity_available": "15"},
                    "325": {"description": "Laptop",
                            "product_type": "Electric",
                            "quantity_available": "112"},
                    "223": {"description": "Table",
                            "product_type": "Furniture",
                            "quantity_available": "25"}}
        self.assertEqual(actual.show_available_products(), expected)

    def test_show_rentals(self):
        """Testing show rentals"""
        db.clear_database()
        actual = db
        actual.import_data(PATH, "products.csv", "customers.csv",
                           "rentals.csv")
        expected = {"200": {"name": "Iron Man",
                            "address":
                            "17801 International Blvd, Seattle, WA 98101",
                            "phone_number": "206-787-5388",
                            "email": "iron.man@gmail.com"},
                    "300": {"name": "Ramkumar Rajanbabu",
                            "address": "7525 166th Ave NE, Redmond, WA 98052",
                            "phone_number": "425-556-2900",
                            "email": "ram.kumar@gmail.com"}}
        self.assertEqual(actual.show_rentals("999"), expected)


if __name__ == "__main__":
    unittest.main()
