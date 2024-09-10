import unittest
import listing

class testlisting(unittest.TestCase):
    def test_listing_is_existing(self):
        listing.listing([1,2,3,4,5])

