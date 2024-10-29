#!/usr/bin/env python3
""" """

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Returns a tuple size containing start index and end index

    Args:
        page (int) - Page number
        page_size (int) - Number of items per page
    """
    start_page = (page - 1) * page_size
    end_page = start_page + page_size
    return (start_page, end_page)
