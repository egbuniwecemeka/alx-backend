#!/usr/bin/env python3
""" A python script to execute simple pagination """

import csv
import math
from typing import Tuple, List


# Simple helper function
def index_range(page: int, page_size: int) -> Tuple:
    """
    Returns the start index and end index as indexes for pagination parameters

    Args:
        page (int) - The page number
        page_size (int) - The number of items contained in the page

    Returns:
        A list of parmeters corresponding to the start and end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """ Server class to paginate a database of popular baby names """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List:
        """ Cached dataset """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Retur list of dataset corresponding to a page"""
        # assert that both arguments are integers and greater than 0
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Calculate start and end index
        start_index, end_index = index_range(page, page_size)

        # Retrieve dataset and check If start index is out of range
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []
        else:
            # Return slice of dataset corresponding to list
            return dataset[start_index:end_index]
