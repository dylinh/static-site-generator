from textnode import TextNode, TextType

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None or self.props == "":
            return ""
        
        string = ""
        
        for key, value in self.props.items():
            string += f' {key}="{value}"'
        
        return string
    
    def __repr__(self):
        return f"Tag: {self.tag} Value: {self.value} Children: {self.children} Props: {self.props}"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        if self.props is not None:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        else:
            return f'<{self.tag}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f"Tag: {self.tag} Value: {self.value} Props: {self.props}"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError
        if self.children is None:
            raise ValueError("Children Missing")
        
        opening = f"<{self.tag}>"
        closing = f"</{self.tag}>"
        middle = ""

        if self.props is not None:
            opening = f"<{self.tag}{self.props_to_html}"

        for leaf in self.children:
            middle += leaf.to_html()

        return opening + middle + closing
        
def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)

    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url,
                                    "alt": text_node.text
                                    })