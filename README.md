# Todo-Python
A web application for creating and managing to do Lists in categories using Flask and SqlAlchemy.

## Getting Started

This repository includes python files used to interract with a postgreQL database:

- python version 3.10.4
- pip version 22.0.4
- install psycopg2 binary ``pip install psycopg2-binary``
- install postgresQL
- run `python3 demo.py`
- install flask ``pip install flask``
- install flask sqlalchemy ``pip install flask-sqlalchemy``
- run migrations ``python3 -m flask db upgrade`` after creating the database and editing the connection in ``app.config['SQLALCHEMY_DATABASE_URI'] ``
- run ``FLASK_APP=flash-hello-app.py FLASK_DEBUG=true python3 -m flask run`` or ``FLASK_APP=app.py FLASK_DEBUG=true flask run`` or ``python3 app.py``to start the app
**Important note: create a database ``todoapp`` and add the name and credentials to psycopg2.connect('dbname=`dbname` password=`password` host=localhost')**


## Author

👤 **Cyril Iyadi**

- GitHub:[@see-why](https://github.com/see-why)
- Twitter: [@4_see_why](https://twitter.com/4_see_why?s=08)
- LinkedIn: [C.Iyadi](https://www.linkedin.com/in/cyril-iyadi/)


## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues/).

## Show your support

Give a ⭐️ if you like this project!

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
- etc

## 📝 License

This project is [MIT](./MIT.md) licensed.
