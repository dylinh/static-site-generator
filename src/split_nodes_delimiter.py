from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
            continue

        split_node = node.text.split(delimiter)

        if len(split_node) % 2 == 0:
            raise Exception("Unmatched closing delimiter")
        
        for i in range(len(split_node)):
            if split_node[i] == "":
                continue
            if i % 2 != 0:
                node2 = TextNode(split_node[i], text_type)
                new_list.append(node2)
            else:
                node2 = TextNode(split_node[i], TextType.TEXT)
                new_list.append(node2)
        
    return new_list


#     "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",

# inputs are a list of old nodes, a delimiter, and text_type
# each old node contains text and the text_type TextType.TEXT
# output is a list of text nodes their corresponding text type
# uses extend to add a list to the end of another list
# split to split the string

# initialize an empty list
# iterate through the old nodes
#    if it's not TextType.TEXT add it to the new list of nodes
#.   question 1) how do I determine if there's a matching closing delimiter?
#.   when I split the string into say 3 pieces based off the delimiter how do I know which string its in
#.   # uneven indices are the elements that contain the delimiter