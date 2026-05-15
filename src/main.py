from transfer import transfer
from generate_page import generate_page_recursive

def main():
    transfer("static", "public")
    generate_page_recursive("content", "template.html", "public")

main()