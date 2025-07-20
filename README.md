# URL Shortener
## Frontend
Please cd into directory `/client` to execute commands. 

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
Please cd into directory `/server` to execute commands. 

### Implementation Summary
The shortened URL will be the base 62 encoded id of the original URL stored in the database. 

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

Connect to the postgresSQL through terminal-based frontend: 
```bash
docker exec -it <db_container_id> psql -U <username> -d <db name>
```
### Test flask backend
```
docker-compose run --rm web pytest
```

## TODOs
- (optional) logging detect anomaly? 
- seperate dev and prod config (e.g. .env.dev)
- tag local version as a release
- deploy to aws

## Completed TODOs
- Save original url with https://
- Duplicate original url should produce the same shortened url
- Write tests