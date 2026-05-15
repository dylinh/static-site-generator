import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from split_nodes_delimiter import split_nodes_delimiter

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("<h1/>")
        node2 = HTMLNode("<h1/>")
        self.assertEqual(node.tag, node2.tag)

    def test_props_to_html(self):
        example = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        answer = ' href="https://www.google.com" target="_blank"'
        node = HTMLNode("<h1/>", "test", "none", example)
        self.assertEqual(node.props_to_html(), answer)

    def test_value(self):
        node = HTMLNode("<h1/>", "test", "none")
        node2 = HTMLNode("<h1/>", "poop", "none")
        self.assertNotEqual(node.value, node2.value)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_p(self):
        node = LeafNode("a", "Hello, world!")
        self.assertEqual(node.to_html(), "<a>Hello, world!</a>")

    def test_leaf_to_html_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        result = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            ]
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, result)

    # def test_props(self):node = HTMLNode("<h1/>")


if __name__ == "__main__":
    unittest.main()