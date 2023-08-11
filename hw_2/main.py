import os

import keklib
from keklib import main


def dim_is_ok(lists):
    return len(list(filter(lambda line: len(line) != len(lists), lists))) == 0


def generate_table(lists):
    if not dim_is_ok(lists) or len(lists) == 0:
        raise Exception("Invalid input")
    return "\\begin{tabular}{" + "l" * len(lists[0]) + "}\n" + \
           "\\\\\n".join(map(lambda line: "&".join(line), lists)) + \
           "\n\\end{tabular}" + "\\\\" * 5 + "\n"


def generate_pic():
    main.print_ast(keklib.fib_numbers, "artifacts/fib_num_ast.png")
    return "\\includegraphics[width=\\linewidth]{artifacts/fib_num_ast.png}\n"


def generate_tex_doc(lists):
    pic = generate_pic()
    return "\\documentclass{article}\n\\usepackage[utf8]{inputenc}\n" \
           "\\usepackage{graphicx}\n\\begin{document}\n\n" \
           + generate_table(lists) + pic + "\n\\end{document}"


if __name__ == '__main__':
    with open("artifacts/task.tex", "w") as file:
        file.write(generate_tex_doc([["hello1", "hello22", "hello333"], ["hello4444", "hello55555", "hello666666"],
                                     ["hello7", "hello8", "hello9"]]))
    os.system("pdflatex -output-directory=artifacts artifacts/task.tex")
    os.system("rm artifacts/task.aux artifacts/task.log")
