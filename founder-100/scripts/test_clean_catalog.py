import unittest, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from clean_catalog import clean, price, safe


class T(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(clean([]), ([], []))

    def test_dedupe_and_price(self):
        rows = [{"sku": "a 1", "name": "red  mug", "price": "$1,299.5", "qty": "3"},
                {"sku": "A1", "name": "dup", "price": "1", "qty": "1"}]
        out, log = clean(rows)
        self.assertEqual(len(out), 1)
        self.assertEqual(out[0]["price"], "1299.50")
        self.assertTrue(any(l[1] == "removed" for l in log))

    def test_bad_values_go_to_log_not_silent(self):
        out, log = clean([{"sku": "B", "name": "x", "price": "free", "qty": "-2"}])
        self.assertEqual(out[0]["price"], "")
        self.assertEqual(sum(1 for l in log if l[1] == "unresolved"), 2)

    def test_missing_sku(self):
        out, log = clean([{"sku": "", "name": "x", "price": "1", "qty": "1"}])
        self.assertEqual(out, [])
        self.assertEqual(log[0][1], "unresolved")

    def test_formula_injection(self):
        self.assertTrue(safe("=HYPERLINK(1)").startswith("'"))
        self.assertEqual(safe("-5"), "-5")
        self.assertEqual(price("-"), None)


if __name__ == "__main__":
    unittest.main()
