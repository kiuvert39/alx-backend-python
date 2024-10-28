#!/usr/bin/env python3

def index_range(page: int, page_size: int) -> tuple:

    page_start_index = (page - 1) * page_size
    end_index =  page_start_index + page_size

    return (page_start_index, end_index)
    