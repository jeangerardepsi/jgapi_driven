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

Voici l'historique technique de mon travail, incluant la résolution des erreurs rencontrées.

### 1️⃣ Initialisation et Configuration AWS
J'ai configuré les identifiants locaux pour communiquer avec LocalStack :
\`\`\`bash
aws configure
# Access Key: test | Secret Key: test | Region: us-east-1
\`\`\`

### 2️⃣ Création de l'instance EC2 (Gestion de l'erreur d'AMI)
Au début, j'ai eu une erreur d'AMI non trouvée. J'ai dû identifier l'AMI par défaut de LocalStack pour réussir le provisioning :
\`\`\`bash
# Commande réussie pour créer l'instance :
aws --endpoint-url=http://localhost:4566 ec2 run-instances --image-id ami-df5de72bdb3b --count 1 --instance-type t2.micro
# Instance ID obtenue : i-51f8a34f64ad0e1e8
\`\`\`

### 3️⃣ Développement de la Lambda (Correction du Réseau)
Ma première version du code Python échouait car elle pointait sur \`localhost\`. J'ai dû modifier le code pour utiliser le réseau interne de LocalStack :
\`\`\`python
import boto3
import os
import json

def lambda_handler(event, context):
    # Correction de l'endpoint pour le réseau interne LocalStack
    localstack_hostname = os.environ.get('LOCALSTACK_HOSTNAME')
    endpoint_url = f"http://{localstack_hostname}:4566" if localstack_hostname else "http://localhost:4566"
    
    ec2 = boto3.client('ec2', endpoint_url=endpoint_url, region_name='us-east-1')
    instance_id = 'i-51f8a34f64ad0e1e8'
    
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
        'body': json.dumps({'message': message, 'instance': instance_id})
    }
\`\`\`

### 4️⃣ Déploiement et Automatisation (Makefile)
Pour automatiser la mise à jour, j'ai créé un **Makefile** :
\`\`\`makefile
deploy:
	zip function.zip lambda_function.py
	aws --endpoint-url=http://localhost:4566 lambda update-function-code --function-name ec2-manager --zip-file fileb://function.zip --region us-east-1
\`\`\`
**Commande lancée :** \`make deploy\`

### 5️⃣ Tests de l'API (Endpoints Live)
L'API est exposée via le tunnel GitHub Codespaces :
* **Vérifier le Statut** : [Lien Statut](https://automatic-palm-tree-r4v47xjpq97r3p9rw-4566.app.github.dev/?action=status)
* **Démarrer** : [Lien Start](https://automatic-palm-tree-r4v47xjpq97r3p9rw-4566.app.github.dev/?action=start)
* **Arrêter** : [Lien Stop](https://automatic-palm-tree-r4v47xjpq97r3p9rw-4566.app.github.dev/?action=stop)

---

## 📝 Analyse des Erreurs & Solutions
1. **Erreur d'accès Git** : Résolution en créant un **Fork** sur mon compte personnel pour obtenir les droits d'écriture.
2. **Page Blanche Navigateur** : Confirmation que le JSON brut ne génère pas de visuel, mais transmet bien la donnée.
3. **Erreur 502** : Résolue en paramétrant la visibilité des ports du Codespace en **Public**.

---
*Projet réalisé et documenté avec succès par Jean-Gérard pour Boris STOCKER.*
