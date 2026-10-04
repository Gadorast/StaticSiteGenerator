import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_create_empty(self):
        node = HTMLNode()
        self.assertEqual(str(node), 'HTMLNode(None, None, None, None)')

    def test_create(self):
        node = HTMLNode('<p>', 'Test Eintrag', None, None)
        self.assertEqual(str(node), 'HTMLNode(<p>, Test Eintrag, None, None)')

    def test_create_children(self):
        node = HTMLNode('<span>', 'Test Eintrag span', None, None)
        node1 = HTMLNode('<p>', 'Test Eintrag p', [node], None)
        self.assertEqual(str(node1), 'HTMLNode(<p>, Test Eintrag p, [HTMLNode(<span>, Test Eintrag span, None, None)], None)')

    def test_props(self):
        node = HTMLNode('<p>', 'Test Eintrag p', None, {"style": "font-weight: bold;", "width": "100%"})
        self.assertEqual(node.props_to_html(), ' style="font-weight: bold;" width="100%"')

if __name__ == "__main__":
    unittest.main()
