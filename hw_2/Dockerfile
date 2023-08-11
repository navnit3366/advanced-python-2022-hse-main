FROM python:3.8
WORKDIR /python_scripts/tex_gen

COPY . .

RUN apt-get update
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install pydot
RUN python3 -m pip install graphviz
RUN python3 -m pip install keklib
RUN apt-get -y install python3-networkx
RUN apt-get -y install texlive-latex-base

CMD python3 /python_scripts/tex_gen/main.py