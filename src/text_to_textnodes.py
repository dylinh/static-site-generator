from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_link import split_nodes_link
from split_nodes_image import split_nodes_image
from textnode import TextType, TextNode

def text_to_textnodes(text):
    nodes = split_nodes_delimiter([TextNode(text, TextType.TEXT)], "**", TextType.BOLD) 
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC) 
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

