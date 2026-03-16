def max_points(book_list) -> tuple[str,int]:
    book_point_dict = {}
    for tupleBook in book_list:
        book,points = tupleBook
        if book not in book_point_dict:
            book_point_dict[book] = points
        elif book in book_point_dict:
            book_point_dict[book] += points
    
    #sorted_book_point_dict = {k: v for k, v in sorted(book_point_dict.items(), key=lambda item: item[1], reverse=True)}
    sorted_book_point_dict = {book_point_dict.items(), key=lambda item: item[1], reverse=True}
    for k,v in sorted(book_point_dict.items(), key=lambda item: item[1], reverse=True)
    top_subject, top_points = next(iter(sorted_book_point_dict.items()))
    print(top_subject, top_points)

if __name__ == "__main__":
    bookPointList = [ 
    ("math", 10), ("science", 7), ("history", 8),
    ("math", 12), ("art", 4), ("science", 15),
    ("history", 3), ("literature", 11)
    ]
    
    max_points(bookPointList)