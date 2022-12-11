# Simple Marketplace Application
Simple Marketplace

---

## Entity Relationship Diagram (ERD)
Database Schema is presented by the image below

![alt text](https://github.com/Danangjoyoo/SimpleMarketplace/blob/develop/docs/erd.png?raw=true)

---

## How to serve
1. Make sure you have docker installed in your machine
2. Make sure your docker has docker-compose plugin
3. open terminal, go to this project directory
4. Build without cache, to make sure this projects run succesfully in your machine. Please build first with `--no-cache` option to avoid any errors while serving up `docker-compose` due to your machine's docker cache.
    ```bash
    docker-compose build --no-cache
    ```
4. Run
    ```bash
    docker-compose up
    ```
5. Access to http://localhost:3000 to the web page

---

## API Documentation
- This application is provided with `openapi` or `swagger` API documentation (Powered by [Flask-Toolkits](https://pypi.org/project/flask-toolkits)).
- You can access http://localhost:9000/docs

    ![alt text](https://github.com/Danangjoyoo/SimpleMarketplace/blob/develop/docs/apidocs.png?raw=true)


## Automation Testing
1. Unit Testing
2. Behavior Testing