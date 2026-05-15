from extract_markdown_images import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

def split_nodes_image(old_nodes):
    # given a list of nodes, create a list of new nodes 
    new_list = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_list.append(node)
            continue
        
        # so a node can have the images and the alt
        # right now I have a list of all the tuples that contain the image and alt
        # so I can create the nodes for all the ones that have images and tuples
        # how do I get the nodes without images/text
        original_text = node.text

        for i in range(len(images)):
            sections = original_text.split(f"![{images[i][0]}]({images[i][1]})", 1)
            before = TextNode(sections[0], TextType.TEXT)
            image = TextNode(images[i][0], TextType.IMAGE, images[i][1])
            if before.text != "":
                new_list.append(before)
            new_list.append(image)
            # now I need to change it to final
            # so before text + image, then need to change before text to the next one
            original_text = sections[1]
        if original_text != "":
            new_list.append(TextNode(original_text, TextType.TEXT))
    return new_list