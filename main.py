"""This module contains functions used to download all the scans from the text file provided"""
import pandas as pd
import requests
import os

def read_lines() -> pd.DataFrame:
    """Finds the file and saves the lines to a dataframe"""
    source = os.path.abspath('File/')
    text_file_name = [file for file in os.listdir(source) if ".txt" in file]
    df = pd.read_csv(f'File/{text_file_name[0]}', delimiter='\t', index_col=False)
    return df


def extract_line(line_provided: str) -> str:
    """Extracts the link from each provided line of text"""
    split_line = line_provided.split("'")
    return split_line[1]
    

def download_pdf(link_string: str, reference_string: str) -> None:
    """Uses the link to download the scan to the downloads folder"""
    response = requests.get(link_string)
    with open(f'Downloads/{reference_string}.pdf', 'wb') as f:
        f.write(response.content)


if __name__ == "__main__":
    text_dataframe = read_lines()
    links_strings = text_dataframe["Record"]

    links = []
    for line in links_strings:
        links.append(extract_line(line))

    references = text_dataframe["REFERENCE"]

    append=0
    for link in links:    
        download_pdf(link, references[append])
        append += 1
        