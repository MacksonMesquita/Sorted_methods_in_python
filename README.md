# Sorted methods - ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
Neste repositório você encontrará algoritimos de ordenação em Python, utilizando juntamente, testes unitários


### Unittest
O unittest é um framework muito utilizado para testes de implementações em python (principalmente).
<br />
Sua principal característica é gerir com segurança e ponticidade os testes e seus respectivos resultados a serem esperados. 

#### Sua estrutura base segue o padrão: 
     import unittest

    class TestStringMethods(unittest.TestCase):

     def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

     def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    if __name__ == '__main__':
    unittest.main()


Onde cada def realiza um teste, ordenado por uma função com a extensão *unittest.TestCase* de testes de caixa!
<br />
Para saber mais sobre o unittest framework, acesse a doc:

> [Documentação do Unittest](https://docs.python.org/3/library/unittest.html)


<br />

### Detalhes:
O repositório contem todos os tipos de algoritimos de ordenação ccada um com duas versões exemplificativas 
* Utilizando o método sort do python
* Utilizando um algoritimo de ordenação escolhido (sem o sort metodo nativo do py)

<br />

### Estrutura das pastas 📁 : 

#### 
    Pasta Root: My test { 
    
    Dentro da pasta root, há pastas com nomes dos algoritimos de sort utilizado {
    
       Ao selecionar sua opção, dentro de cada uma, há mais duas subpasta, as quais divide os algoritimos em questão de acordo com a utilização do método nativo sort ou sem sua utilização (with sort ou without sort) {
       
           Dentro de cada subpasta temos dois arquivos, os quais são respectivamente os arquivos de teste e implementação do algoritimo
           
           }
        }
    }

<br />

**Se você gostou do conteúdo, compartilhe!**

![Reddit](https://img.shields.io/badge/Reddit-%23FF4500.svg?style=for-the-badge&logo=Reddit&logoColor=white)
![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)
![Facebook](https://img.shields.io/badge/Facebook-%231877F2.svg?style=for-the-badge&logo=Facebook&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)
![Twitter](https://img.shields.io/badge/Twitter-%231DA1F2.svg?style=for-the-badge&logo=Twitter&logoColor=white)
  
<br />

![](https://i.imgur.com/waxVImv.png)

<br />

In this repository you will find sorting algorithms in Python, with unit tests .

### Unittest
Unittest is a framework widely used for testing Python implementations (mainly).
<br />
Its main characteristic is to safely and promptly manage the tests and their respective expected results.

#### Its base structure follows the standard:
     import unittest

    class TestStringMethods(unittest.TestCase):

     def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

     def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    if __name__ == '__main__':
    unittest.main()


Where each def performs a test, ordered by a function with the *unittest.TestCase* extension of box tests!
<br />
To learn more about the unittest framework, access the doc:

> [Unittest documentation](https://docs.python.org/3/library/unittest.html)

<br />

### Details:
The repository contains two example versions,
* Using python's sort method
* Using a sorting algorithm (without py's native sorting method)
  
<br />

### Folders structures 📁 :

####
    Root folder: My test {
    
    Inside the root folder, there are folders named after the sort algorithm used {
    
       Within each one, there are two more subfolders, which divides the algorithms in question, according to whether sort method is used or not (with sort or without sort) {
       
           Within each subfolder we have two files, which are respectively the test and implementation files of the algorithm
           
           }
        }
    }

<br />

***Warning:*** *The content was written in portuguese(Brazil), and do not support for other languages - (variables and functions name)*

<br />

**If you liked this content, share it!**

![Reddit](https://img.shields.io/badge/Reddit-%23FF4500.svg?style=for-the-badge&logo=Reddit&logoColor=white)
![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)
![Facebook](https://img.shields.io/badge/Facebook-%231877F2.svg?style=for-the-badge&logo=Facebook&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)
![Twitter](https://img.shields.io/badge/Twitter-%231DA1F2.svg?style=for-the-badge&logo=Twitter&logoColor=white)
