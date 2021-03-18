import datetime, re, os, os.path, random

work_dir = os.path.dirname(__file__) # Путь к папке со скриптом
users_files_path = "\\Users\\"
users_files_full_path = work_dir + users_files_path
old_files_full_path = users_files_full_path + "Old\\"

# Перемещение старых файлов (если их больше 15 в папке) в папку Old

if os.path.exists(old_files_full_path) == False:
    os.makedirs(old_files_full_path)

files = os.listdir(path=users_files_full_path)

if len(files) >= 15:
    for i in files:
        if i.find("html") != -1:
            os.renames(users_files_full_path + i, old_files_full_path + i)

# Словарь для транслитерации

letters = { "А": ["A"], "а": ["a"],
            "Б": ["B"], "б": ["b"],
            "В": ["V"], "в": ["v"],
            "Г": ["G"], "г": ["g"],
            "Ґ": ["G"], "ґ": ["g"],
            "Д": ["D"], "д": ["d"],
            "Е": ["E"], "е": ["e"],
            "Є": ["Ye"], "є": ["e"],
            "Ё": ["E"], "ё": ["e"],
            "Ж": ["Zh"], "ж": ["zh"],
            "З": ["Z"], "з": ["z"],
            "И": ["I"], "и": ["i"],
            "І": ["I"], "і": ["i"],
            "Ї": ["Yi"], "ї": ["i"],
            "Й": ["Y"], "й": ["y"],
            "К": ["K"], "к": ["k"],
            "Л": ["L"], "л": ["l"],
            "М": ["M"], "м": ["m"],
            "Н": ["N"], "н": ["n"],
            "О": ["O"], "о": ["o"],
            "П": ["P"], "п": ["p"],
            "Р": ["R"], "р": ["r"],
            "С": ["S"], "с": ["s"],
            "Т": ["T"], "т": ["t"],
            "У": ["U"], "у": ["u"],
            "Ф": ["F"], "ф": ["f"],
            "Х": ["Kh"], "х": ["kh"],
            "Ц": ["Ts"], "ц": ["ts"],
            "Ч": ["Ch"], "ч": ["ch"],
            "Ш": ["Sh"], "ш": ["sh"],
            "Щ": ["Shch"], "щ": ["shch"],
            "Ъ": [""], "ъ": [""],
            "Ы": ["Y"], "ы": ["y"],
            "Ь": [""], "ь": [""],
            "Э": ["E"], "э": ["e"],
            "Ю": ["Yu"], "ю": ["yu"],
            "Я": ["Ya"], "я": ["ya"],
            " ": [" "]}

# Функция для транслитерации имени
def translit(name):
    result_str = ""
    i = 0
    while i < len(name):
        result_str += letters[name[i][0]][0]
        i += 1
    return result_str

# Генерация и проверка пароля
def gen_pwd(length = 8, strength = "alphaNumeric", pwd = ""):
    if strength == "alpha":
        comb = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    elif strength == "alphaNumeric":
        comb = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    elif strength == "alphaNumSpecial":
        comb = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*()_-+={}[]:;\"'<>,.?"

    if length == 0:
        return pwd
    pwd += random.choice(comb)
    return gen_pwd(length-1, strength, pwd)

def check_pwd(pwd, strength):
    if strength == "alpha":
        if re.search(r"[a-z]+", pwd) and re.search(r"[A-Z]+", pwd):
            return True
    elif strength == "alphaNumeric":
        if re.search(r"[a-z]+", pwd) and re.search(r"[A-Z]+", pwd) and re.search(r"[0-9]+", pwd):
            return True
    elif strength == "alphaNumSpecial":
        if re.search(r"[a-z]+", pwd) and re.search(r"[A-Z]+", pwd) and re.search(r"[0-9]+", pwd) and re.search(r"[~!@#$%^&*()_\-\+={}\[\]:;\"'<>,.?]+", pwd):
            return True
    return False


# Формирование конечных данных

name_ru = input("Имя на русском: ")

name_en = translit(name_ru)

# Создание логина и пароля для AD
if name_en.find(" ") != -1:
    login = name_en[:name_en.find(" ")+2].replace(" ", "_")
    # ad_password = name_en[name_en.find(" ")+1:] + str(datetime.date.today())[:4] + "!@"
else:
    login = name_en
    # ad_password = login + str(datetime.date.today())[:4] + "!@"

# Поштовый адрес
mail = login + "@budpostach.com.ua"

while 1:
    mail_password = gen_pwd(9, "alphaNumeric")
    if check_pwd(mail_password, "alphaNumeric"):
        break


login_info = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="Windows utf-8">
    <title>%s</title>
    <style>
        * {
            margin: 0;
            padding: 0;
        }
        .container {
            margin: 20px;
        }
        p {
            font: bold 11pt Calibri, sans-serif;
        }
        .red {
            color: red;
            text-decoration: underline;
        }
        .black, a {
            font-style: italic;
        }
        a {
            color: blue;
        }
        em {
            font-weight: normal;
        }
    </style>
</head>
<body>
    <div class="container">
        %s
        <div class="mail">
            <p><span class="red">Почтовый ящик (e-mail):</span> <a href="#">%s</a></p>
            <p><span class="red">Логин:</span><span class="black"> %s</span></p>
            <p><span class="red">Пароль:</span><span class="black"> %s</span></p>
        </div>
        <br>
        <div class="AD">
            <p><span class="red">Вход в домен (компьютер, БММ, сервер):</span></p>
            <p><span class="red">Логин:</span><span class="black"> %s</span></p>
            <p><span class="red">Пароль:</span><span class="black"> Qwerty1</span></p>
            <p><span class="black">(После ввода пароля, система потребует его сменить. Пароль должен быть не менее восьми символов, содержать большие и маленькие буквы, цифры и символы)</span></p>
        </div>
    </div>
</body>
</html>""" % (name_ru, name_ru, mail, login, mail_password, login)

# Запись в файл
with open(users_files_full_path + name_ru + ".html", "w") as f:
    f.write(login_info)

# print(login_info)