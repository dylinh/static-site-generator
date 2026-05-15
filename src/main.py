from transfer import transfer
from generate_page import generate_page_recursive
import sys

if len(sys.argv) > 1:
    base_path = sys.argv[1]
else:
    base_path = "/"

def main():
    transfer("static", "docs")
    generate_page_recursive("content", "template.html", "docs", base_path)

main()