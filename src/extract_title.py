from markdown_to_blocks import markdown_to_blocks

def extract_title(markdown):
    split = markdown_to_blocks(markdown)

    for line in split:
        if line.startswith("# "):
            formatted_line = line[1:].strip()
            return formatted_line
    
    raise Exception()
