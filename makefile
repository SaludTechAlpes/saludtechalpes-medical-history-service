activate:
	if [ -d "venv" ]; then \
        echo "Python 🐍 environment was activated"; \
    else \
        echo "The folder environment doesn't exist"; \
		python3 -m venv venv; \
        echo "The environment folder was created and the python 🐍 environment was activated"; \
    fi
	. ./venv/bin/activate

install:
	pip3 install -r requirements.txt

run:
	@if [ -z "$(strip $(PORT))" ]; then \
		flask --app ./src run; \
	else \
		flask --app ./src run -p $(PORT); \
	fi

run-docker:
ifeq ($(strip $(PORT)),)
	flask --app ./src run -h 0.0.0.0
else
	flask --app ./src run -p $(PORT) -h 0.0.0.0
endif

run-tests:
	PYTHONPATH=/src
	FLASK_ENV=test python3 -m unittest discover -s tests -p '*Test.py' -v

run-tests-coverage:
	 PYTHONPATH=/src
	 FLASK_ENV=test coverage run -m unittest discover -s tests -p '*Test.py' -v
	 coverage report -m
	 coverage html
	 coverage report --fail-under=80

docker-up:
	docker compose up --build

docker-down:
	docker compose down

docker-local-up:
	docker compose -f=docker-compose.local.yaml up --build

docker-local-down:
	docker compose -f=docker-compose.local.yaml down

kubernetes-local-up:
	kubectl apply -f kubernetes/local/k8s-configMap.yaml
	kubectl apply -f kubernetes/local/k8s-secrets.yaml
	kubectl apply -f kubernetes/local/k8s-postgres.yaml
	kubectl apply -f kubernetes/local/k8s-deployment.yaml
	kubectl apply -f kubernetes/local/k8s-hpa.yaml
	kubectl apply -f kubernetes/local/k8s-ingress.yaml
	sleep 5
	minikube tunnel

kubernetes-local-down:
	kubectl delete configMap/medical-history-configmap
	kubectl delete secrets/medical-history-secrets
	kubectl delete deploy/postgres-db
	kubectl delete deploy/saludtechalpes-medical-history-service
	kubectl delete ingress/saludtechalpes-medical-history-service-ingress