# URL Shortener
## Frontend

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.


## Backend

### Run with Docker
```bash
# build docker image 
cd server
docker build -t url_shortener_flask:v1 .

# run app 
docker run -p 127.0.0.1:8000:8000 url_shortener_flask:v1
```


### Run without docker
```bash
# create python virtual environment: 
python3 -m venv venv

# activate virtual environment: 
source venv/bin/activate

# install flask and db librarires:
pip3 install Flask \
psycopg2-binary \
flask_sqlalchemy \
flask-cors \
```

```bash
# to enable debugger (ignore if not)
export FLASK_ENV=development

# run app
flask run 
```