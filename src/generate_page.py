from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title
import os
import pathlib

def generate_page(from_path, template_path, dest_path, base_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_file = open(from_path) # markdown file
    read_from = from_file.read() # markdown file read
    temp_file = open(template_path) 
    read_temp = temp_file.read()
    string = markdown_to_html_node(read_from).to_html()
    title = extract_title(read_from)
    replace_title = read_temp.replace('{{ Title }}', title)
    replace_html = replace_title.replace('{{ Content }}', string)
    replace_html = replace_html.replace('href="/', f'href="{base_path}')
    replace_html = replace_html.replace('src="/', f'src="{base_path}')

    directories = os.path.dirname(dest_path)
    if os.path.exists(directories) == False:
        os.makedirs(directories)
    with open(dest_path, "w") as file:
        file.write(replace_html)

def generate_page_recursive(dir_path_content, template_path, dest_dir_path, base_path):
    entries = os.listdir(dir_path_content)
    for entry in entries:
        if os.path.isfile(os.path.join(dir_path_content, entry)):
            generate_page(os.path.join(dir_path_content, entry), template_path, pathlib.Path(os.path.join(dest_dir_path, entry)).with_suffix(".html"), base_path) # from path, template path, dest path
        else:
            generate_page_recursive(os.path.join(dir_path_content, entry), template_path, (os.path.join(dest_dir_path, entry)), base_path)