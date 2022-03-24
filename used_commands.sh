docker-compose up -d --build
docker-compose exec order python -m pytest "tests"
docker-compose exec order python -m pytest "tests" -p no:warnings --cov='application'
