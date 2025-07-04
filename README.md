# URL Shortener
## Frontend

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

### Setup .env to talk to backend
Create `.env` file under `./client` and put: 
```
REACT_APP_API_URL=http://localhost:8000
```
Change localhost to your host name if needed


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
Create `.env` file under `./server` and put your db credentials: 
```
POSTGRES_USER=youruser
POSTGRES_PASSWORD=yourpassword
POSTGRES_DB=url_map
DATABASE_URL=postgresql://youruser:yourpassword@postgres:5432/url_map
```

Run flask app and postgres together with docker-compose:
Use the `--build` flag if you need to rebuild the flask image
```bash
docker-compose up --build
```

To rebuild container/volume/network (note: will wipe out all data in volumes!) 
```bash
docker-compose down -v
```