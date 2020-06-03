# MailAutoSender

Установка
-------------------------
Понадобятся Python 3.7, pip и аккаунт на Яндекс.Почте. Рекомендуется все делать в отдельном venv'е.
1. Установить зависимости
`pip install -r ./requirements.txt`
2. Скачать [chromedriver](https://chromedriver.chromium.org/) (можно поместить в папку MailAutoSender)
3. Готово! Можно запускать.

![til](https://github.com/RomanBaggins/MailAutoSender/blob/master/example.gif)

:rocket: Запуск
-------------------------
Перед началом рабоыт прописать креды отправителя и получателя сообщений в credential.py
### Команды запуска
#### :black_medium_square: Фишинг
```
pytest -s -v --language=en  .\test_send_phishing.py
```
#### :black_medium_square: Спам
```
pytest -s -v --language=en  .\test_send_spam.py
```
#### :black_medium_square: Массмэйл
```
pytest -s -v --language=en  .\test_send_massmail.py
```
#### :black_medium_square: Аттачи
```
pytest --language=en --attach_type=<Путь до папки без пробелов начиная с “\sources”> --file_extension=<расширение файла> .\test_send_attach.py
```
##### :black_medium_small_square: Executable files
```
pytest --language=en --attach_type=FormatExecutableFiles --file_extension=exe .\test_send_attach.py
```
##### :black_medium_small_square: Data
###### :black_small_square: Documents
```
pytest --language=en --attach_type=FormatDataDocuments --file_extension=doc .\test_send_attach.py
```
```
pytest --language=en --attach_type=FormatDataDocuments --file_extension=docx .\test_send_attach.py
```
```
pytest --language=en --attach_type=FormatDataDocuments --file_extension=odt .\test_send_attach.py`
```
##### :black_small_square: Spreadsheets
```
pytest --language=en --attach_type=FormatDataSpreadsheets --file_extension=ods .\test_send_attach.py
```
```
pytest --language=en --attach_type=FormatDataSpreadsheets --file_extension=xls .\test_send_attach.py
```
```
pytest --language=en --attach_type=FormatDataSpreadsheets --file_extension=xlt .\test_send_attach.py
```
##### :black_small_square: Presentations
```
pytest --language=en --attach_type=FormatDataPresentations --file_extension=pptx .\test_send_attach.py
```
##### :black_small_square: Specialized
```
pytest --language=en --attach_type=FormatDataSpecialized --file_extension=pub .\test_send_attach.py
```
:pensive: Известные ограничения 
-------------------------
* Если к учетной записи не прикреплен телефонный номер, то тесты могут падать на шаге авторизации (не обрабатывается окно с вводом номера телефона).
* Тесты не обноалялись для Beta- версии почты.
