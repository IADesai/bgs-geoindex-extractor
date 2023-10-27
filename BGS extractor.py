"""This module contains functions used to download all the scans from the text file provided"""
import pandas as pd
import requests
import os
import sys


def find_file_path() -> str:
    """Finds the path to the folder when run and returns it"""
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.dirname(__file__)
    return application_path


def read_lines(source_path: str) -> pd.DataFrame:
    """Finds the file and saves the lines to a dataframe"""
    text_file_name = [file for file in os.listdir(f"{source_path}/File/") if ".txt" in file]
    df = pd.read_csv(f'{source_path}/File/{text_file_name[0]}', delimiter='\t', index_col=False)
    return df


def extract_line(line_provided: str) -> str:
    """Extracts the link from each provided line of text"""
    split_line = line_provided.split("'")
    return split_line[1]
    

def download_pdf(link_string: str, reference_string: str, downloads_path: str) -> None:
    """Uses the link to download the scan to the downloads folder"""
    response = requests.get(link_string)
    with open(f'{downloads_path}/Downloads/{reference_string}.pdf', 'wb') as f:
        f.write(response.content)


if __name__ == "__main__":
    path = find_file_path()

    text_dataframe = read_lines(path)
    links_strings = text_dataframe["Record"]

    links = []
    for line in links_strings:
        if "href" in line:
            links.append(extract_line(line))

    references = text_dataframe["REFERENCE"].str.replace("/", "-")

    append=0
    for link in links: 
        download_pdf(link, references[append], path)
        append += 1
        