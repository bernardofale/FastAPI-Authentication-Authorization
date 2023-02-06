# ssa

## Getting Started
```sh
git clone git@github.com:bernardofalle/ssa.git
```

### Prerequisites
- Docker
- Pip
- Python

### Installing
Create a virtual environment and install the requirements
```sh
python3 -m venv venv
pip install -r requirements.txt
```
Run docker compose to get MongoDB and MongoExpress services up
```sh
docker-compose -f compose.yaml up
```
