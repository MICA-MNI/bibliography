import pathlib
import re


def name_modifications(bib_directory=None) -> None:
    if bib_directory is None:
        bib_directory = pathlib.Path("../bibtex")
    else:
        bib_directory = pathlib.PurePosixPath(bib_directory)

    find_replace = (
        (("Benkarim, O",), "Benkarim, Oualid"),
        (("Bernasconi, A",), "Bernasconi, Andrea"),
        (("Bernasconi, N",), "Bernasconi, Neda"),
        (("Bernhardt, BC", "Bernhardt, Boris C"), "Bernhardt, Boris Christian"),
        (("Caciagli, L",), "Caciagli, Lorenzo"),
        (("Cruces, R",), "Cruces, Raul"),
        (("Lariviere, S",), "Larivi{\`e}re, Sara"),
        (("Lariviere", "Larivière", "Larivi{\`{e}}re"), "Larivi{\`e}re"),
        (("Li, Q",), "Li, Qiongling"),
        (("Lowe, A",), "Lowe, Alexander"),
        (("Paquola, C",), "Paquola, Casey"),
        (("Royer, J",), "Royer, Jessica"),
        (("Smallwood, J",), "Smallwood, Jonathan"),
        (("Tavakol, S",), "Tavakol, Shahin"),
        (
            (
                "Vos de Wael, R",
                "Vos de Wael, Reinder",
                "de Wael, R Vos",
                "de Wael, Reinder Vos",
            ),
            "{Vos de Wael}, Reinder",
        ),
    )
    for bib_file in bib_directory.glob("*.bib"):
        text = bib_file.read_text()
        for replacement in find_replace:
            for search_string in replacement[0]:
                text = re.sub(search_string + "(,| |})", replacement[1] + r"\1", text)
        bib_file.write_text(text)


def my_name_cv(bib_directory=None) -> None:
    if bib_directory is None:
        bib_directory = pathlib.Path("../bibtex")
    else:
        bib_directory = pathlib.PurePosixPathPath(bib_directory)

    for bib_file in bib_directory.glob("*.bib"):
        text = bib_file.read_text()
        text = text.replace(r"{Vos de Wael}, Reinder", "\myname")

        cv_directory = bib_file.parent / "cv"
        cv_directory.mkdir(exist_ok=True)
        new_file = cv_directory / (bib_file.stem + "_cv" + bib_file.suffix)
        new_file.write_text(text)


if __name__ == "__main__":
    name_modifications()
    my_name_cv()
