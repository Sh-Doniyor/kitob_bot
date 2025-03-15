from aiogram import Dispatcher

TOKEN = "7843853662:AAFGlOASLlLuxWrq6HRndP1KdBN73_4oJM8"
dp = Dispatcher()




#githubgayuklash
#
# 1:repository ga kirib yangi repository ochamiz , nom berib , public qilib create ni bosamiz
# 2:git init # git papka ochib beradi
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/Sh-Doniyor/Bot-template.git
# git push -u origin main
#
# 1:har bittasini pycharm terminalida ishlatamiz
# git init qilgandan keyin  ".gitignore" fayl ochamiz
#
# 2:gitignore file ichiga yuklamaydigan fayllar nomini yozamiz , ".venv, .env , .idea , .migrations/versions/*  "
#
# 3:keyin terminalga pip freeze deb yozamiz kutubxonalar chiqadi , bu kutubxonalarni terminalda  "pip freeze > requirements.txt " deb buyruq bersak , o'zi filega yozib beradi
#
# 4:git add . deymiz , git status desak nimalarni qoshganini bilib olsak boladi
#
# 5:git commit -m "first commit"
#
# 6:git branch -M main
#
# 7:git remote add origin https://github.com/Sh-Doniyor/Bot-template.git
#
# 8:git push -u origin main qilgandan keyin token olish kerak , uni githubdan olamiz , settingsga kirib , developer settings va davom etamiz
#
# 9:tokenni olib kiritamiz va git hubga joylanadi











#
# alembic qilayotganda:
#
#
# https://medium.com/@johnidouglasmarangon/using-migrations-in-python-sqlalchemy-with-alembic-docker-solution-bd79b219d6a saytga kiramiz va aytilgan narsalarni install qilib olamiz:
#
# 1:pip install psycopg2-binary sqlalchemy
# 2:pip install alembic
# 3:alembic init migrations
# 4:sqlalchemy.url = postgresql+psycopg2://myuser:mypassword@0.0.0.0:5432/mydb shu joyga ozimiznikini kiritamiz yani :
# "sqlalchemy.url = postgresql+psycopg2://postgres:1@localhost/chat_bot_db"
# 5:models.py ichiga metadata=Base.metadata deb yozamiz
# 6:env.py ichidagi :target_metadata = none " qiymatni target_metadata = metadata qilib ozgartiramiz
# 7:MAkefileni ichiga :
# mig :
#   alembic revision --autogenerate -m "Create a baseline migrations"
# #migratsiya faylini yaratadi
# head:
#   alembic upgrade head
# upgrade:
#   alembic upgrade head
# downgrade:
#   alembic downgrade head
