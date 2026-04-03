# ☁️ API Driven Infrastructure : Pilotage EC2 via Lambda
> **Projet de fin de module - Orchestration & Cloud émulé**

---

## 👤 Informations Étudiant
* **Nom** : Jean-Gérard
* **Filière** : Infra ESI_EPSI
* **Année Académique** : 2025-2026
* **Intervenant** : **Boris STOCKER**

---

## 🚀 RÉCAPITULATIF COMPLET DES COMMANDES EXÉCUTÉES

Voici l'intégralité du code et des commandes utilisés pour ce projet.

### 1️⃣ Initialisation de l'Infrastructure (AWS CLI)
Commandes tapées pour configurer l'environnement et créer l'instance :
\`\`\`bash
# Configuration des accès
aws configure
# (test / test / us-east-1)

# Création de l'instance EC2 (avec AMI par défaut LocalStack)
aws --endpoint-url=http://localhost:4566 ec2 run-instances \
    --image-id ami-df5de72bdb3b \
    --count 1 \
    --instance-type t2.micro
# ID obtenu : i-51f8a34f64ad0e1e8
\`\`\`

### 2️⃣ Code Source Complet : lambda_function.py
Ce code gère les requêtes HTTP et communique avec l'API EC2 de LocalStack :
\`\`\`python
import boto3
import os
import json

def lambda_handler(event, context):
    # Gestion du réseau interne pour LocalStack
    localstack_hostname = os.environ.get('LOCALSTACK_HOSTNAME')
    endpoint_url = f"http://{localstack_hostname}:4566" if localstack_hostname else "http://localhost:4566"
    
    ec2 = boto3.client('ec2', endpoint_url=endpoint_url, region_name='us-east-1')
    instance_id = 'i-51f8a34f64ad0e1e8'
    
    # Récupération de l'action via les paramètres d'URL (?action=xxx)
    action = event.get('queryStringParameters', {}).get('action', 'status')
    
    if action == 'start':
        ec2.start_instances(InstanceIds=[instance_id])
        message = "Demarrage envoye"
    elif action == 'stop':
        ec2.stop_instances(InstanceIds=[instance_id])
        message = "Arret envoye"
    else:
        response = ec2.describe_instances(InstanceIds=[instance_id])
        state = response['Reservations'][0]['Instances'][0]['State']['Name']
        message = f"Statut: {state}"

    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({'message': message, 'instance': instance_id})
    }
\`\`\`

### 3️⃣ Automatisation : Makefile Complet
Contenu du fichier Makefile utilisé pour simplifier les opérations :
\`\`\`makefile
deploy:
	zip function.zip lambda_function.py
	aws --endpoint-url=http://localhost:4566 lambda update-function-code \
		--function-name ec2-manager --zip-file fileb://function.zip --region us-east-1

status:
	curl "https://automatic-palm-tree-r4v47xjpq97r3p9rw-4566.app.github.dev/?action=status"
\`\`\`

---

## 🔗 Endpoints Live (Pilotage)
* **🔍 Statut** : [Cliquer ici](https://automatic-palm-tree-r4v47xjpq97r3p9rw-4566.app.github.dev/?action=status)
* **▶️ Démarrer** : [Cliquer ici](https://automatic-palm-tree-r4v47xjpq97r3p9rw-4566.app.github.dev/?action=start)
* **⏹️ Stopper** : [Cliquer ici](https://automatic-palm-tree-r4v47xjpq97r3p9rw-4566.app.github.dev/?action=stop)

---

## 📝 Rapport d'erreurs et Solutions
1. **Erreur d'AMI** : Résolue en switchant sur `ami-df5de72bdb3b`.
2. **Erreur Réseau Lambda** : Résolue via `LOCALSTACK_HOSTNAME` (indispensable pour que la Lambda "sorte" de son container).
3. **Droits Git** : Résolu par la création d'un Fork personnel pour finaliser le push.

---
*Dépôt finalisé et fonctionnel.*
