# Variables
ENDPOINT = --endpoint-url=http://localhost:4566
REGION = --region us-east-1

deploy:
	@echo "--- Compression de la Lambda ---"
	zip function.zip lambda_function.py
	@echo "--- Mise à jour du code dans LocalStack ---"
	aws $(ENDPOINT) lambda update-function-code --function-name ec2-manager --zip-file fileb://function.zip $(REGION)

status:
	@echo "--- Statut de l'instance ---"
	curl "http://localhost:4566/restapis/kj1ybinxjm/test/_user_request_/?action=status"

start:
	@echo "--- Demarrage de l'instance ---"
	curl "http://localhost:4566/restapis/kj1ybinxjm/test/_user_request_/?action=start"

stop:
	@echo "--- Arret de l'instance ---"
	curl "http://localhost:4566/restapis/kj1ybinxjm/test/_user_request_/?action=stop"