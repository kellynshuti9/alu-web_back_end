#!/usr/bin/env python3
"""Simple pagination module"""

import csv
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """Return start and end indexes"""
    start = (page - 1) * page_size
    end = start + page_size

    return (start, end)


class Server:
    """Server class to paginate database"""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]

            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(
        self,
        page: int = 1,
        page_size: int = 10
    ) -> List[List]:
        """Return requested page"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)

        dataset = self.dataset()

        if start >= len(dataset):
            return []

        return dataset[start:end]
