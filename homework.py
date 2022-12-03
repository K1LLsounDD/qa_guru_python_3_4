#Сделайте функцию, которая будет печатать читаемое имя переданной ей функции и значений аргументов.

#Вызовите ее внутри функций, описанных ниже

#Например, вызов следующей функции должен преобразовать имя функции в более читаемый вариант

# (заменить символ подчеркивания на пробел, сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:

#open_browser(browser_name="Chrome")

#"Open Browser Chrome" или "Open Browser [Chrome]" – на ваш выбор.

#Подсказка: Имя функции можно получить с помощью func.__name__



def print_func_name(name, *args):
    name = name.__name__.title().replace('_', ' ')
    print(name, *args)

def open_browser(browser_name):
    print_func_name(open_browser, browser_name)



def go_to_companyname_homepage(page_url):
    print_func_name(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    print_func_name(find_registration_button_on_login_page, page_url, button_text)


open_browser('Chrome')
go_to_companyname_homepage('https://www.youtube.com/')
find_registration_button_on_login_page('https://qiwi.com/', 'Создать кошелек')