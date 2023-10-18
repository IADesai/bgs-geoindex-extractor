"""This module contains functions used to download all the scans from the text file provided"""
import requests
import os

def read_lines() -> list:
    """Finds the file and saves the lines to a list"""
    source = os.path.abspath('File/')
    text_file_name = [file for file in os.listdir(source) if ".txt" in file]
    with open(f'File/{text_file_name[0]}') as f:
        lines = f.readlines()[1:]
    return lines


def extract_line(line_provided: str) -> str:
    """Extracts the link from each provided line of text"""
    split_line = line_provided.split("'")
    return split_line[1]
    

def download_pdf(link_string: str) -> None:
    """Uses the link to download the scan to the downloads folder"""
    pass


if __name__ == "__main__":
    text_lines_list = read_lines()

    links = []
    for line in text_lines_list:
        links.append(extract_line(line))

    for link in links:    
        download_pdf(link)
        