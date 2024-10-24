import re
from pathlib import Path
import pandas as pd
import pymupdf4llm

# Parametros

ruta  = ""

class Clasificador:
    def __init__(self) -> None:
        self.sector: str = ""
        self.sub_sector: str = ""
        self.area: str = ""
        self.sub_area: str = ""
        self.seccion: str = ""
        self.poderes: str = ""
        self.entidad: str = ""
        self.capitulo: str = ""
        self.sub_capitulo: str = ""
        self.unidad_ejecutora: str = ""
        self.denominacion: str = ""

    # def __str__(self):
    #    return "|{sector:>5}|{sub_sector:>5}|{area:>5}|{sub_area:>5}|{seccion:>5}|{poderes:>5}|{entidad:>5}|{capitulo:>5}|{sub_capitulo:>5}|{unidad_ejecutora:>5}|{denominacion:>85}|".format(
    #        **self
    #    )


if __name__ == "__main__":
    folder_root = Path(__file__).parent
    file_pdf = folder_root / Path(ruta)
    file_md = folder_root / Path("Clasificador-Institucional.md")

    if not file_md.exists():
        md_text = pymupdf4llm.to_markdown(file_pdf)
        file_md.write_text(md_text)

    idx = 0

    list_objs = []
    content = file_md.read_text()
    for line in content.splitlines():
        if re.match(r"^\|\d+\|\d+\|\d+\|\d+\|\d+.*", line):
            data = line.split("|")
            row = data[1:-1]
            if row.count("") > 0:
                continue
            try:
                idx += 1

                objs = dict(list(zip(vars(Clasificador()).keys(), row)))
                c = Clasificador()
                c.__dict__.update(objs)
                if c.unidad_ejecutora.isnumeric():
                    list_objs.append(c)

                    print(
                        f"|{c.sector:>5}|{c.sub_sector:>5}|{c.area:>5}|{c.sub_area:>5}|{c.seccion:>5}|{c.poderes:>5}|{c.entidad:>5}|{c.capitulo:>5}|{c.sub_capitulo:>5}|{c.unidad_ejecutora:>5}|{c.denominacion:>85}|"
                    )

            except:
                pass

    print(idx)
    df = pd.DataFrame([o.__dict__ for o in list_objs])
    df.to_excel(folder_root / "clasificadores.xlsx", index=False)