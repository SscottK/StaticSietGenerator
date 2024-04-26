import unittest
from htmlnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = LeafNode(
            "p",
            "Hello, world!",                        
            
        )
        
        #self.assertEqual(
            #node.props_to_html(),
            #' class="greeting" href="https://boot.dev"',
        #)
        print(node)

if __name__ == "__main__":
    unittest.main()