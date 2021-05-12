最近运行课件代码，发现pdf文件读取部分的函数失效。这里找到读取pdf文件的可运行代码，为了方便后续学习使用，我已将pdf和docx读取方法封装成pdfdocx包。



# pdfdocx

只有简单的两个读取函数

- read_pdf(file)
- read_docx(file)

file为文件路径，函数运行后返回file文件内的文本数据。

### 安装

```
pip install pdfdocx
```

### 使用

读取pdf文件

```python
from pdfdocx import read_pdf
p_text = read_pdf('test/data.pdf')
print(p_text)
```

Run

```
这是来⾃pdf⽂件内的内容
```



```python
from pdfdocx import read_docx
d_text = read_pdf('test/data.docx')
print(d_text)
```

Run

```
这是来⾃docx⽂件内的内容
```





### 拆开pdfdocx

希望大家能安装好，如果安装或者使用失败，可以使用下面的代码作为备选方法。虽然繁琐，能用就好。

**读取pdf**

```python
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
import re


def read_pdf(file):
    """
    读取pdf文件，并返回其中的文本内容
    :param file: pdf文件路径
    :return: docx中的文本内容
    """
    output_string = StringIO()
    with open(file, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
    text = output_string.getvalue()
    return text

  
```



**读取docx**

```python
import docx
  
def read_docx(file):
    """
    读取docx文件，并返回其中的文本内容
    :param file: docx文件路径
    :return: docx中的文本内容
    """
    text = ''
    doc = docx.Document(file)
    for para in doc.paragraphs:
        text += para.text
    return text
```



# 如果

如果您是经管人文社科专业背景，编程小白，面临海量文本数据采集和处理分析艰巨任务，可以参看[《python网络爬虫与文本数据分析》](https://ke.qq.com/course/482241?tuin=163164df)视频课。作为文科生，一样也是从两眼一抹黑开始，这门课程是用五年时间凝缩出来的。自认为讲的很通俗易懂o(*￣︶￣*)o，

- python入门
- 网络爬虫
- 数据读取
- 文本分析入门
- 机器学习与文本分析
- 文本分析在经管研究中的应用

感兴趣的童鞋不妨 戳一下[《python网络爬虫与文本数据分析》](https://ke.qq.com/course/482241?tuin=163164df)进来看看~

[![](img/课程.png)](https://ke.qq.com/course/482241?tuin=163164df)



# 更多

- [B站:大邓和他的python](https://space.bilibili.com/122592901/channel/detail?cid=66008)

- 公众号：大邓和他的python

- [知乎专栏：数据科学家](https://zhuanlan.zhihu.com/dadeng)

<br>

![](img/大邓和他的Python.png)

