from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered"
    ORDERED_LIST = "ordered"

def  block_to_blocktype(block):
    if block.startswith(("# ", "## ","### ", "#### ", "##### ", "######")):
        return BlockType.HEADING
    
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    
    if block.startswith((">", "> ")):
        return BlockType.QUOTE
    
    if block.startswith("- "):
        return BlockType.UNORDERED_LIST
    
    test_block = block.split("\n")

    for i in range(1, len(test_block)+1):
        if test_block[i-1].startswith(f"{i}. "):
            continue
        else:
            return BlockType.PARAGRAPH
    
    return BlockType.ORDERED_LIST

