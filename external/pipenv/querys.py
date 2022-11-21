create_table = """ 
    CREATE TABLE IF NOT EXISTS alumnos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombe VARCHAR(255) NOT NULL,
        apellido VARCHAR(255) NOT NULL
    ); 
"""


def insert(alumnos: list) -> str:

    def formatValues(v: str):
        return f"'{v}'"

    def formatList(item):
        return f"({', '.join(map(lambda v2: formatValues(v2), item.values()))})"

    values = ', '.join(map(lambda v: formatList(v), alumnos))

    return f"""
        INSERT INTO alumnos (
            nombe,
            apellido
        )
        VALUES {values};
    """


select = """SELECT * FROM alumnos"""
