def parse(line):
    """
    Parses a given line of text and returns a dictionary representation.

    Args:
        line (str): The input string to parse.
    
    Returns:
        dict: A dictionary containing the parsed data from the line.
    """

    columns = ["sector", "subsector", "area", "subarea", "seccion", "poderes", "entidad", "capitulo", "subcapitulo", "unidad_ejecutora", "denominacion"]
    fields = line.split("|")

    assert len(columns) == len(fields), \
    f"Mismatch: Expected {len(columns)} columns, but found {len(fields)} fields in the row."

    result =  {}

    for index, value in enumerate(fields):
        column_name  = columns[index]
        result[column_name] = value

    return result


def saludar(nombre):
    print("abc 123")