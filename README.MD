# Project Deployment
You can run the project here: https://wow-production-7f90.up.railway.app/

## Project Deployment locally
```bash
pip install -r requirements.txt
python main.py
```
### Deploying with Docker
```bash
docker build -t unit-logbook .
docker run -p 8000:8000 unit-logbook
```

## API documentation
- Route docs: https://wow-production-7f90.up.railway.app/docs