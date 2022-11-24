<img title="a title" alt="Alt text" src="C:\Users\Viktor\BI_Stat_2021\olimpic_games\report\images\BI_logo.png" width="200">

## Project 1
### [Smirnov Viktor](https://github.com/Smirness)
####  Date: 23/11/2022

## Table of Contents
1. [Introduction](#Introduction)

#### Introduction
This project looks at data on participants in the of the Olympic Games in the last 120 years. 
Completed 16 tasks on working with dataframe. Each title corresponds to one task.

#### Data description 
There are tables in archive. Access via link: https://stepik.org/media/attachments/lesson/603865/athlete_events.zip.
It's including 12 files with csv format.

```python
from zipfile import ZipFile

file = "C:/Users/Viktor/BI_Stat_2021/olimpic_games/data/athlete_events.zip"
# opening the zip file in READ mode
with ZipFile(file, 'r') as zip:
    zip.printdir()
```


```python
from zipfile import ZipFile
import pandas as pd


def merger(zipfile, file_type, save_type="csv", path_output="Default", name_output="Default"):
    """
    Merging into one data frame several files that are compressed into one zip file.
    :param zipfile: path to zip file with table datas
    :param file_type: file type of table datas. Accepting csv or excel.
    :param save_type: file type for merged table. Default is csv.
    :param path_output: path for saving merged table. Default save in folder where is zipfile.
    :param name_output: name for saved merged table. Default saving as zipfile name.
    :return file: saved merged table.
    """
    # for opening multiple file types
    ft_read = dict(csv=pd.read_csv, excel=pd.read_excel)
    ft_write = dict(csv="to_csv", excel="to_excel")

    pd_file_type = ft_read[file_type]
    ft_write_type = ft_write[save_type]

    # if path_output is Default, then saving in folder with zipfile
    if path_output == "Default":
        path_output = zipfile.split(sep="/")
        path_output = '/'.join(map(str, path_output[:-1]))

    # if name_output is Default, then saving as name of zipfile
    if name_output == "Default":
        path_file = zipfile.split(sep="/")
        name_output = path_file[-1].split(sep=".")[0]

    # merging into one data frame several files that are compressed into one zip file
    df = pd.concat(
        [pd_file_type(ZipFile(zipfile).open(i)) for i in ZipFile(zipfile).namelist()],
        ignore_index=True
    )
    getattr(df, ft_write_type)(path_output + "/" + name_output + "." + save_type)
```
