#! /usr/bin/env python3
# Copyright (c) 2020 Snoop Project <snoopproject@protonmail.com>
"Text_banner_logo_help"

import base64
import json
import locale
import sys
import time
import webbrowser

from colorama import Fore, Style, init
from rich.panel import Panel
from rich.console import Console

locale.setlocale(locale.LC_ALL, '')
init(autoreset=True)
console = Console()


## Логирование ошибок.
def err_all(err_="low"):
    if err_ == "high":
        return "⚠️ [bold red][RU] Внимание! Критическая ошибка, просьба сообщить об этом разработчику.\n" + \
                   "[EN] Attention! Critical error, please report it to the developer.\nhttps://github.com/snooppr/snoop/issues[/bold red]"
    elif err_ == "low":
        return "⚠️ [bold yellow][RU] Ошибка | [EN] Error[/bold yellow]"


## БД.
def DB(db_base):
    try:
        with open(db_base, "r", encoding="utf8") as f_r:
            db = f_r.read()
            db = db.encode("UTF-8")
            db = base64.b64decode(db)
            db = db[::-1]
            db = base64.b64decode(db)
            trinity = json.loads(db.decode("UTF-8"))
            return trinity
    except Exception:
        print(Style.BRIGHT + Fore.RED + "Упс, что-то пошло не так..." + Style.RESET_ALL)
        sys.exit()


## Пожертвование.
def donate():
    print("")
    console.print(Panel(f"""[cyan]
╭donate/Buy:
├──ЮMoney:: [white]4100111364257544[/white]
├──Сберкарта:: [white]4276100015931808[/white]
└──СБП/Банк Юмани (по номеру телефона):: [white]+79004753581[white]

[bold green]Оплатить софт можно по любым реквизитам, но самым предпочтительным способом является — СБП (перевод по номеру тел. без комиссиий с карты любого банка).

Если пользователя заинтересовало ПО [red]Snoop demo version[/red], то он может приобрести [cyan]Snoop full version[/cyan], поддержав развитие IT-проекта[/bold green] [bold cyan]20$[/bold cyan] [bold green]или[/bold green] [bold cyan]1400р.[/bold cyan]
[bold green]При пожертвовании/покупке в сообщении/письме укажите:[/bold green]

    \"\"\"
    [cyan]На развитие Snoop Project: 20$ ваш e-mail
    full version for Windows RU или full version for Linux RU,
    статус пользователя: Физ.лицо; ИП; Юр.лицо (если покупка ПО).[/cyan]
    \"\"\"

[bold green]В ближайшее время на email пользователя придёт чек о покупке и ссылка для скачивания Snoop full version готовой сборки, то есть исполняемого файла, для Windows — это 'snoop_cli.exe', для GNU/Linux — 'snoop_cli.bin'.

Snoop в исполняемом виде (build-версия) предоставляется по лицензии, с которой пользователь должен ознакомиться перед покупкой ПО.
Лицензия для Snoop Project в исполняемом виде находится в rar-архивах демо версий Snoop по ссылке: [/bold green]
[cyan]https://github.com/snooppr/snoop/releases[/cyan][bold green], также лицензия доступна по команде::
'[/bold green][cyan]snoop_cli.bin --version[/cyan][bold green]' или '[/bold green][cyan]snoop_cli.exe --version[/cyan][bold green]' у исполняемого файла.

Если ПО Snoop требуется пользователю для служебных или образовательных задач, напишите письмо на e-mail разработчика в свободной форме.
Студентам ПО Snoop full version предоставляется с 50% скидкой.

Snoop full version:
 * 4400+ Websites;
 * поддержка локальной и онлайн database snoop;
 * подключение к БД snoop (online), которая расширяется/обновляется;
 * доступен автооптимизированный, быстрый и агрессивный режим поиска;
 * доступна пользовательская настройка разгона скорости работы ПО;
 * плагины без ограничений;
 * ru техподдержка от разработчика ПО;
 * отключены всплывающие окна в HTML-отчёте про упоминание snoop demo version.[/bold green]
[bold red]Ограничения Snoop demo version:
 * database Snoop сокращена в > 15 раз;
 * необновляемая database snoop;
 * отключены некоторые опции/плагины.[/bold red]

[bold green]Email:[/bold green] [cyan]snoopproject@protonmail.com[/cyan]
[bold green]Исходный код:[/bold green] [cyan]https://github.com/snooppr/snoop[/cyan]

❗️[bold yellow] Обратите внимание, что из-за цензуры письма с 'mailru' и 'yandex' не доходят до международного почтового сервиса 'protonmail'. Пользователи mailru/yandex пишите запросы на запасную почту.[/bold yellow]
[bold green]Email: [/bold green][cyan]snoopproject@ya.ru[/cyan]
""",
                        title="[bold red]demo: (Публичная оферта)",
                        border_style="bold blue"))

    try:
        webbrowser.open("https://yoomoney.ru/to/4100111364257544")
    except Exception:
        print("\033[31;1mНе удалось открыть браузер\033[0m")

    print(Style.BRIGHT + Fore.RED + "Выход")
    sys.exit()


## Лого.
def logo(text, exit=True):
    if sys.platform != 'win32':
        with console.screen():
            console.print("""[cyan]
 ____                                      
/\  _`\                                    
\ \,\L\_\    ___     ___     ___   _____   
 \/_\__ \  /' _ `\  / __`\  / __`\/\ '__`\\
   /\ \L\ \/\ \/\ \/\ \_\ \/\ \_\ \ \ \L\ \\
   \ `\____\ \_\ \_\ \____/\ \____/\ \ ,__/
    \/_____/\/_/\/_/\/___/  \/___/  \ \ \/ 
                                     \ \_\\
      __                              \/_/ 
     /\ \                              
     \_\ \     __    ___ ___     ___   
     /'_` \  /'__`\/' __` __`\  / __`\\
    /\ \_\ \/\  __//\ \/\ \/\ \/\ \_\ \\
    \ \___,_\ \____\ \_\ \_\ \_\ \____/
     \/__,_ /\/____/\/_/\/_/\/_/\/___/ 
""")
            time.sleep(1.4)
    for i in text:
        time.sleep(0.04)
        print(f"\033[31;1m{i}", end='', flush=True)
    if exit:
        print("\033[31;1m\n\nВыход")
        sys.exit()


# snoop.py Справка Модули 'if mod == 'help'.
def help_module_1():
    print("""\033[32;1m└──[Справка]\033[0m

\033[32;1m========================
| Плагин GEO_IP/domain |
========================\033[0m \033[32m\n
1) Реализует онлайн одиночный поиск цели по IP/url/domain и предоставляет статистическую информацию: IPv4/v6; GEO-координаты/ссылку; локацию.
(Лёгкий ограниченный поиск).

2) Реализует онлайн поиск цели по списку данных: и предоставляет статистическую и визуализированную информацию: IPv4/v6; GEO-координаты/ссылки; страны/города; отчеты в CLI/txt/csv форматах; предоставляет визуализированный отчет на картах OSM.
(Умеренный небыстрый поиск: ограничения запросов:: 15к/час; не предоставляет информацию о провайдерах).

3) Реализует офлайн поиск цели по списку данных, используя БД: и предоставляет статистическую и визуализированную информацию: IPv4/v6; GEO-координаты/ссылки; локации; провайдеры; отчеты в CLI/txt/csv форматах; предоставляет визуализированный отчет на картах OSM.
(Сильный и быстрый поиск).

Результаты по 1 и 2 методу могут отличаться и быть неполными - зависит от персональных настроек DNS/IPv6 пользователя.
Список данных — текстовый файл (в кодировке utf-8), который пользователь указывает в качестве цели, и который содержит ip, domain или url (или их комбинации).

Предназначение плагина — Образование/ИБ.

\033[32;1m============================
| Плагин Reverse Vgeocoder |
============================\033[0m\n
\033[32mОбратный impresionante-геокодер от Snoop Project для визуализации координат на карте OSM и статистическим анализом в html/csv/txt форматах.

Плагин умеет извлекать и обрабатывать координаты из любых зашумлённых текстовых файлов. Плагин реализует оффлайн поиск цели по заданным геокоординатам и предоставляет подробную статистическую и визуализированную информацию (full version).
Особая повышенная точность у объектов в зоне RU; EU; CIS локаций относительно остального мира.

С помощью данного плагина (full version) пользователь способен извлечь, визуализировать и проанализировать информацию о тысячах геокоординатах за секунды.

Предназначение плагина — CTF/Образование.\033[0m

\033[32;1m========================
| Плагин Yandex_parser |
========================\033[0m\n
\033[32mПлагин позволяет получить информацию о пользователях Яндекс-сервисов:
Я_Отзывы; Я_Кью; Я_Маркет; Я_Музыка; Я_Дзен; Я_Диск; E-mail, Name.
И связать полученные данные между собой с высокой скоростью и масштабно.

Плагин разработан на идее и материалах уязвимости, отчёты были отправлены Яндексу в рамках программы «Охота за ошибками» в 2020-2021 гг.
Попал в зал славы, получил дважды финансовое вознаграждение, а Яндекс исправил 'ошибки' по своему усмотрению.

Предназначение плагина — OSINT.

Подробнее о плагинах см. 'Общее руководство Snoop Project.pdf'.\033[0m""")
    console.rule("[bold red]Конец справки")


# snoopplugins.py Справка Модуль Reverse Vgeocoder 'elif Vgeo == "help"'.
def help_vgeocoder_vgeo():
    print("""\033[32;1m└──[Справка]\033[0m
\033[32m
В Snoop Project поддерживается два режима геокодирования:
[*] Метод '\033[32;1mПростой\033[0m\033[32m':: На карте OSM (урезанный HTML-отчет) расставляются маркеры по координатам.
Все маркеры подписаны геометками.
Для данного метода доступны сокращенные отчёты с геометками в html/txt форматах.

[*] Метод '\033[32;1mПодробный\033[0m\033[32m':: На карте OSM (HTML-отчет) расставляются маркеры по координатам.
Все маркеры подписаны геометками; странами; округами и городами. Доступны графики по странам/регионам, статистика и её фильтрация.
Дополнительные отчёты (таблицы) сохраняются с подробностями в [.txt.csv] форматах.
Данный метод точно расставляет маркеры с геометками, подписывает их адресами к ближайшим населенным пунктам или названиями природных объектов.
Особая повышенная точность у объектов в зоне RU; EU; CIS локаций относительно остального мира.

    Например, если пользователь загрузит для обработки координаты, указывающие в километре от г. Выкса на местность возле озера Разодейское, то маркер на карте OSM встанет точно у озера, а подписан он будет примерно так:

\"\"\"\033[36m
🌎 Координаты: 55.342595 42.230801
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Страна: RU
Регион: Nizhny Novgorod Oblast
Округ: Ozero Razodeyskoye\033[0m\033[32m
\"\"\"

Метод работает на основе — 'Евклидово дерево'.

\033[32;1mПлагин Reverse Vgeocoder\033[0m \033[32m- работает в оффлайн режиме и укомплектован специально разработанной гео-БД (некоторые БД предоставляются под свободной лицензией от download.geonames.org/export/dump/).

    Для обработки данных укажите при запросе текстовый файл с координатами в градусах в кодировке utf-8 (с расширением .txt или без расширения). Каждая строчка с геокоординатами (широта, долгота) должна быть записана в файле с новой строки (желательно).
Snoop довольно умён: распознаёт и выбирает геокоординаты через запятую, пробел'ы или делает интеллектуальную выборку, вычищая случайные строки.
    Пример файла с геокоординатами (как может выглядеть файл с координатами, который необходимо указывать):

\"\"\"\033[36m
51.352,   -108.625
55.466,64.776
52.40662,66.77631
53.028 -104.680
54.505/73.773
Москва55.75, 37.62 Калининград54.71, 20.51 Ростов-на-Дону47.23, 39.72
случайная_строка1, которая_будет обработана Казань 55.7734/49.1436
случайная строка2, которая не будет обработана\033[0m\033[32m
\"\"\"

    По окончанию рендеринга откроется web-browser с визуальным результатом.
Все результаты сохраняются в '~/snoop/results/plugins/ReverseVgeocoder/*[.txt.html.csv]'.
Для статистической обработки информации (сортировка по странам/координатам/raw_данным и т.д.) пользователь может изучить отчёт в csv-формате.
Если графики не отображаются в вашем html-отчёте, попробуйте открыть репорт в другом браузере.
    Это удобный плагин, если пользователю необходимо, например, не только обработать геокоординаты, но и найти хаотичные данные, или наоборот.""")


# snoopplugins.py Справка Модуль Reverse Vgeocoder 'elif Ya == "help"'.
def help_yandex_parser():
    print("""\033[32;1m└──[Справка]

Однопользовательский режим\033[0m
\033[32m[*] Логин — левая часть до символа '@', например, bobbimonov@ya.ru, логин
'\033[36mbobbimonov\033[0m\033[32m'.
[*] Публичная ссылка на Яндекс.Диск — это ссылка для скачивания/просмотра материалов, которую пользователь выложил в публичный доступ, например,
'\033[36mhttps://yadi.sk/d/7C6Z9q_Ds1wXkw\033[0m\033[32m' или '\033[36mhttps://disk.yandex.ru/d/7C6Z9q_Ds1wXkw\033[0m\033[32m'.
[*] Идентификатор — хэш, который указан в url на странице пользователя, например, в сервисе Я.Район: 'https://local.yandex.ru/users/tr6r2c8ea4tvdt3xmpy5atuwg0/' идентификатор — '\033[36mtr6r2c8ea4tvdt3xmpy5atuwg0\033[0m\033[32m'.
    По окончанию успешного поиска выводится отчёт в CLI и открываются Яндекс-страницы пользователя в браузере.
    Плагин Yandex_parser выдает меньше информации по идентификатор-у пользователя (в сравнении с другими методами), причина — fix уязвимости от Яндекса.

\033[32;1mМногопользовательский режим\033[0m
\033[32m[*] Файл с именами пользователей — файл (в кодировке UTF-8 с расширением .txt или без него), в котором записаны логины.
Каждый логин в файле должен быть записан с новой строки, например:

\"\"\"
\033[36mbobbimonov
username
username2
username3
случайная строка
bobbimonov@ya.ru
bobbimonov@ya.ru
bobbimonov@ya.ru\033[0m
\033[32m\"\"\"

    При использовании многопользовательского режима по окончанию поиска (быстро) выводится расширенный отчёт в CLI, сохраняется txt-отчёт о Яндекс-пользователях (с расширенными, структурированными данными) и открывается браузер с мини-отчётом (сгруппированные данные).
    Плагин генерирует, но не проверяет 'доступность' персональных страниц пользователей по причине: частая защита страниц Я.капчей.
Все результаты сохраняются в '\033[36m~/snoop/results/plugins/Yandex_parser/*\033[0m\033[32m'\033[0m
    \033[31;1mВ конце ноября 2022 года Яндекс закрыл публичный api, и возможно, данный плагин больше не заработает...\033[0m""")


# snoopplugins.py Справка Модуль GEO_IP/domain 'elif dipbaza'.
def geo_ip_domain():
    print("\033[32;1m└──Справка\033[0m\n")
    print("""\033[32m[*] Режим '\033[32;1mOnline поиск\033[0m\033[32m'. Модуль GEO_IP/domain от Snoop Project использует публичный api и создает статистическую и визуализированную информацию по ip/url/domain цели (массиву данных).
    Ограничения: запросы ~15к/час, невысокая скорость обработки данных, отсутствие информации о провайдерах.
    Преимущества использования 'Online поиска': в качестве входных данных можно использовать не только ip-адреса, но и domain/url.
    Пример файла с данными (список.txt):

\"\"\"
\033[36m1.1.1.1
2606:2800:220:1:248:1893:25c8:1946
google.com
https://example.org/fo/bar/7564
случайная строка\033[0m
\033[32m\"\"\"\033[0m

\033[32m[*] Режим '\033[32;1mOffline поиск\033[0m\033[32m'. Модуль GEO_IP/domain от Snoop Project использует специальные базы данных и создает статистическую и визуализированную информацию по ip цели (массиву данных т.е. по ip-адресам).
Преимущества использования 'Offline поиска': скорость (обработка тысяч ip без задержек), стабильность (отсутствие зависимости от интернет соединения и персональных настроек DNS/IPv6 пользователя), масштабный охват/покрытие (предоставляется информация об интернет-провайдерах).

[*] Режим '\033[32;1mOffline_тихий поиск\033[0m\033[32m'. Тот же режим, что и режим 'Offline', но не выводит на печать в CLI промежуточные таблицы с данными. Режим даёт прирост производительности в несколько раз.
    Пример файла с данными (список.txt):

\"\"\"
\033[36m8.8.8.8
93.184.216.34
2606:2800:220:1:248:1893:25c8:1946
случайная строка\033[0m
\033[32m\"\"\"

    Snoop довольно умён и способен определять и различать во входных данных: IPv4/v6/domain/url, вычищая ошибки и случайные строки.
    По окончанию обработки данных пользователю предоставляются:
статистические отчеты в [txt/csv/html и визуализированные данные на карте OSM]. Если графики не отображаются в вашем html-отчёте, попробуйте открыть репорт в другом браузере.
    Примеры для чего можно использовать модуль GEO_IP/domain от Snoop Project.
Например, если у пользователя имеется список ip адресов от DDoS атаки,
он может проанализировать откуда исходила  max/min атака и от кого (провайдеры).
Решая квесты-CTF, где используются GPS/IPv4/v6.
В конечном итоге использовать плагин в образовательных целях или из естественного любопытства (проверить любые ip-адреса и их принадлежность к провайдеру и местности).\033[0m""")
