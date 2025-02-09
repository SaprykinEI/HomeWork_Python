def get_formatted_text():
    '''Возвращает аккуратно отформатированный текст'''
    formatted_text = (f"'Dont compare yourself with anyone in this word...\n"
                      f"if you do so, you are insulting yourself.'\n"
                      f"\t\t\t\t\t\t Bill Gates\n")
    return formatted_text


print(get_formatted_text())


def get_format_text(quote_1, quote_2, author):
    '''Возвращает аккуратно отформатированный текст'''
    return f"'{quote_1.capitalize()}...\n {quote_2}.'\n\t\t\t\t\t\t\t {author}"


print(get_format_text("dont compare yourself with anyone in this word",
                      "if you do so, you are insulting yourself",
                      "Bill Gates"))