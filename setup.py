from setuptools import setup
import setuptools

setup(
    name='pdfdocx',     # 包名字
    version='1.1',   # 包版本
    description='读取pdf、docx文件，返回文件内的文本数据。',   # 简单描述
    author='大邓',  # 作者
    author_email='thunderhit@qq.com',  # 邮箱
    url='https://github.com/hidadeng/pdfdocx',      # 包的主页
    packages=setuptools.find_packages(),
    install_requires=['PyMuPDF==1.19.2', 'python-docx==0.8.10'],
    python_requires='>=3.5',
    license="MIT",
    keywords=[
        'pdf extraction',
        'docx extraction',
        'text mining',
    ],
    long_description=open('README.md').read(), # 读取的Readme文档内容
    long_description_content_type="text/markdown")  # 指定包文档格式为markdown

