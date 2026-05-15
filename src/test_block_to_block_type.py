import unittest

from block_to_block_type import block_to_blocktype, BlockType

class TestBlockType(unittest.TestCase):
    def test_block_to_block_type(self):
        block = block_to_blocktype(
            "## Poop"
        )
        self.assertEqual(block, BlockType.HEADING)
    
    def test_block_to_block_type_paragraph(self):
        block = block_to_blocktype(
            "poopie"
        )
        self.assertEqual(block, BlockType.PARAGRAPH)

