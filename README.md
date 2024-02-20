# nextDirClass

English:

Imagining a directory structure based on /X/Y/W/Z, where files are written to these directories.
The class below allows files to be balanced as evenly as possible. With this class it is also possible to generate 
the text used to create this directory tree at N levels, with characters from 0..9-A-F


Português:

Imaginando uma estrutura de diretórios baseada em /X/Y/W/Z, onde os arquivos são gravados nesses diretórios. 
A classe abaixo, permite que os arquivos sejam balanceados da forma mais uniforme possível. Com essa classe também 
é possivel gerar o texto usado para a criação dessa arvore de diretórios em N niveis, com caracteres de 0..9-A-F


## Usage:

```python
nextDir = nextDirClass(dir_levels=4,random_start=True)
while True:
    print(nextDir.get_next())
```

```
/2/3/4/9/
/2/3/4/0/
/2/3/4/A/
/2/3/4/B/
/2/3/4/C/
/2/3/4/D/
/2/3/4/E/
/2/3/4/F/
/2/3/5/1/
/2/3/5/2/
/2/3/5/3/
.
.
.
/2/4/F/B/
/2/4/F/C/
/2/4/F/D/
/2/4/F/E/
/2/4/F/F/
/2/5/1/1/
/2/5/1/2/
/2/5/1/3/
.
.
.
/2/F/F/B/
/2/F/F/C/
/2/F/F/D/
/2/F/F/E/
/2/F/F/F/
/3/1/1/1/
/3/1/1/2/
/3/1/1/3/
/3/1/1/4/
.
.
.
```

## License: MIT
