

def html_export(adjectives: dict[str, list[tuple[str, str]]]):
    """
    Creates an HTML file from the given adjectives dictionary.

    Parameters:
        adjectices (dict[str, list[tuple[str, str]]]): A dictionary of adjectives, containing a list of (name, key) tuples for each animal with this adjective.

    Returns:
        None - Creates an HTML file at index.html
    """
    body = ""

    for adjective in adjectives.keys():
        body += f"<h1>{adjective}</h1>"
        body += "<ul>"
        for name in adjectives[adjective]:
            body += f"<li>{name[0]}</li>"
            body += f"<img src='tmp/{name[0]}.{name[1]}'/>"
        body += "</ul>"
    
    html = f"""
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
            </head>
            <body>
            {body}
            </body>
        </html>
    """

    with open('index.html', 'w') as file:
        file.write(html)