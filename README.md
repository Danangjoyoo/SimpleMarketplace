# Simple Marketplace Application
Simple Marketplace

---

## Entity Relationship Diagram (ERD)
Database Schema is presented by the image below

![alt text](https://github.com/Danangjoyoo/SimpleMarketplace/blob/develop/docs/erd.png?raw=true)

---

## Docker Environment Details
- Database : MySQL
- Backend : Ubuntu:20.04 (simulated as an AWS EC2 ubuntu)
- Frontend : Ubuntu:20.04 (simulated as an AWS EC2 ubuntu)
- Storage : Ubuntu:20.04 (simulated as an AWS EC2 ubuntu)

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
- This application is provided with `openapi` or `swagger` API documentation Powered by [Flask-Toolkits](https://pypi.org/project/flask-toolkits) (I'm the author, kindly check [this](https://github.com/Danangjoyoo/flask-toolkits) repo also)
- You can access http://localhost:9000/docs

    ![alt text](https://github.com/Danangjoyoo/SimpleMarketplace/blob/develop/docs/apidocs.png?raw=true)


## Automation Testing
1. setup a virtualenv
    ```
    python3 -m virtualenv venv
    ```
2. Activate
    ```
    . venv/bin/activate
    ```
3. Install dependencies
    ```
    pip install --upgrade pip && pip install -r ./backend/requirements.txt
    ```
4. Go to backend directory
    ```
    cd ./backend
    ```
5. run pytest
    ```
    pytest
    ```

---

## Web Pages Sneak Peek
### Home Page
<img alt="" width="800" src="https://github.com/Danangjoyoo/SimpleMarketplace/blob/develop/docs/home.png?raw=true"/>

### Product Detail Page
<img alt="" width="800" src="https://github.com/Danangjoyoo/SimpleMarketplace/blob/develop/docs/product_detail.png?raw=true"/>

### Create Product Page
<img alt="" width="800" src="https://github.com/Danangjoyoo/SimpleMarketplace/blob/develop/docs/create_prodct.png?raw=true"/>

### Update Product Page
<img alt="" width="800" src="https://github.com/Danangjoyoo/SimpleMarketplace/blob/develop/docs/update_product.png?raw=true"/>
<img alt="" width="800" src="https://github.com/Danangjoyoo/SimpleMarketplace/blob/develop/docs/update_product2.png?raw=true"/>

### Variant Detail
<img alt="" width="800" src="https://github.com/Danangjoyoo/SimpleMarketplace/blob/develop/docs/variant_detail.png?raw=true"/>