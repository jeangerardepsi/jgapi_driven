# ☁️ API Driven Infrastructure : EC2 Manager v1.0
> **Projet de fin de module : Orchestration & Cloud émulé**

![AWS](https://img.shields.io/badge/AWS-LocalStack-FF9900?style=for-the-badge&logo=amazon-aws)
![Python](https://img.shields.io/badge/Python-3.9-3776AB?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Functional-brightgreen?style=for-the-badge)

---

## 👤 Informations Étudiant
> [!IMPORTANT]
> **Nom :** Jean-Gérard  
> **Filière :** Infra ESI_EPSI  
> **Année Académique :** 2025-2026  
> **Intervenant :** **Boris STOCKER**

---

## 🎯 Présentation du Projet
Ce projet démontre la mise en place d'une architecture **Serverless** permettant de piloter des instances EC2 via des requêtes HTTP. L'infrastructure est entièrement émulée via **LocalStack**.

### ⛓️ Chaîne de liaison
`Requête HTTP` ➔ `API Gateway` ➔ `Lambda (Boto3)` ➔ `EC2 Instance`

---

## 🚀 RÉCAPITULATIF TECHNIQUE (LES 3 POINTS CLÉS)

### 1️⃣ Initialisation & Provisioning (AWS CLI)
Configuration des accès et création de l'instance cible avec gestion de l'erreur d'AMI :
\`\`\`bash
# Configuration des accès locaux
aws configure # (test / test / us-east-1)

# Lancement de l'instance avec l'AMI par défaut de LocalStack
aws --endpoint-url=http://localhost:4566 ec2 run-instances \
    --image-id ami-df5de72bdb3b \
    --count 1 --instance-type t2.micro
# ID Instance obtenu : i-51f8a34f64ad0e1e8
\`\`\`

### 2️⃣ CODE FINAL : lambda_function.py
Ce script est le cœur de l'automatisation. Il gère la communication interne et les actions de pilotage :
\`\`\`python
import boto3
import os
import json

def lambda_handler(event, context):
    # Correction réseau : Utilisation du hostname dynamique de LocalStack
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
        # Action par défaut : Status
        response = ec2.describe_instances(InstanceIds=[instance_id])
        state = response['Reservations'][0]['Instances'][0]['State']['Name']
        message = f"Statut: {state}"

    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({'message': message, 'instance': instance_id})
    }
\`\`\`

### 3️⃣ CODE FINAL : Makefile
Automatisation du cycle de vie du projet :
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

| Action | Description | Lien de contrôle |
| :--- | :--- | :--- |
| 🔍 **MONITOR** | Consulter l'état actuel | [Vérifier le statut ➔](https://automatic-palm-tree-r4v47xjpq97r3p9rw-4566.app.github.dev/?action=status) |
| ▶️ **START** | Démarrer l'instance | [Lancer l'instance ➔](https://automatic-palm-tree-r4v47xjpq97r3p9rw-4566.app.github.dev/?action=start) |
| ⏹️ **STOP** | Arrêter l'instance | [Stopper l'instance ➔](https://automatic-palm-tree-r4v47xjpq97r3p9rw-4566.app.github.dev/?action=stop) |

---

## 💡 Résolution de Problèmes (Post-Mortem)
* **Réseau :** L'erreur `ConnectionRefused` a été corrigée via `LOCALSTACK_HOSTNAME`.
* **Git :** Un **Fork** a été réalisé sur `jeangerardepsi/jgapi_driven` pour finaliser le push.
* **Affichage :** Les réponses sont au format **JSON**, confirmées par la donnée brute en navigateur.

---
*Dépôt finalisé et archivé pour évaluation finale.*

*git add README.md Makefile lambda_function.py*
*git commit -m "Final submission: Including full code in README"*
*git push*


