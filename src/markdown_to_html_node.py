from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_blocktype, BlockType
from htmlnode import LeafNode, ParentNode, text_node_to_html_node
from text_to_textnodes import text_to_textnodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    div_children = []

    for block in blocks:
        block_type = block_to_blocktype(block)
        if block_type == BlockType.PARAGRAPH:
            # block.replace("\n", " ")
            children = text_to_children(block.replace("\n", " "))
            parent_node = ParentNode("p", children)
        elif block_type == BlockType.HEADING:
            count = count_headings(block)
            children = text_to_children(block[count+1:])
            # h + 1 characters total. and i'd need to start at the character after the space
            # so say that count was 2, 0 1 2 3
            parent_node = ParentNode(f"h{count}", children)
        elif block_type == BlockType.CODE:
            # block[4:-3]
            child_node = LeafNode("code", block[4:-3])
            parent_node = ParentNode("pre", [child_node])
        elif block_type == BlockType.QUOTE:
            if block.startswith("> "):
                new_block = block[2:]
            else:
                new_block = block[1:]
            children = text_to_children(new_block)
            parent_node = ParentNode("blockquote", children)
        elif block_type == BlockType.UNORDERED_LIST:
            children = []
            block_split = block.split("\n")
            for line in block_split:
                nodes = text_to_children(line[2:])
                wrap = ParentNode("li", nodes)
                children.append(wrap)
            parent_node = ParentNode("ul", children)
        elif block_type == BlockType.ORDERED_LIST:
            children = []
            block_split = block.split("\n")
            for line in block_split:
                new_line = line[line.find('.')+2:] 
                nodes = text_to_children(new_line)
                wrap = ParentNode("li", nodes)
                children.append(wrap)
            parent_node = ParentNode("ol", children)

        div_children.append(parent_node)

    return ParentNode("div", div_children)

def count_headings(block):
    count = 0
    for char in block:
        if char == "#":
            count += 1
        else:
            break
    return count

def text_to_children(text):
    nodes = text_to_textnodes(text)
    nodes_html = []
    for node in nodes:
        html_node = text_node_to_html_node(node)
        nodes_html.append(html_node)
    return nodes_html