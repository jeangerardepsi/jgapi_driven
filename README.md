# 🚀 Projet : API Driven Infrastructure (EC2 Manager)

> **Étudiant :** Jean-Gérard  
> **Environnement :** GitHub Codespaces + LocalStack  
> **Objectif :** Piloter une instance EC2 via une architecture Serverless (Lambda + API Gateway).

---

### 🛠️ Étape 1 : Initialisation de l'Infrastructure
J'ai commencé par simuler l'environnement AWS en local pour créer les ressources de base :
* **IAM Role** : Création d'un rôle `lambda-role` avec les permissions EC2.
* **Instance EC2** : Lancement d'une instance cible (ID: `i-51f8a34f64ad0e1e8`) basée sur l'AMI `ami-df5de72bdb3b`.

### 💻 Étape 2 : Développement de la Logique (Lambda)
Le cœur de la solution est un script **Python 3.9** utilisant `boto3`. 
* **Réseau interne** : Utilisation de `LOCALSTACK_HOSTNAME` pour permettre à la Lambda de communiquer avec l'API EC2 sans erreur de connexion.
* **Flexibilité** : Le script analyse les paramètres d'URL (`queryStringParameters`) pour différencier les actions.

---

### 🔗 Liens de Pilotage (Live)
*Cliquez sur les liens pour tester l'API en direct :*

| Action | URL du Point d'Entrée |
| :--- | :--- |
| **🔍 Statut** | [Vérifier l'état](https://automatic-palm-tree-r4v47xjpq97r3p9rw-4566.app.github.dev/?action=status) |
| **▶️ Start** | [Démarrer l'EC2](https://automatic-palm-tree-r4v47xjpq97r3p9rw-4566.app.github.dev/?action=start) |
| **⏹️ Stop** | [Stopper l'EC2](https://automatic-palm-tree-r4v47xjpq97r3p9rw-4566.app.github.dev/?action=stop) |

> **💡 Note Pédagogique :** Si le navigateur affiche une page blanche, c'est normal ! L'API renvoie du **JSON brut**, format standard pour la communication entre applications.

---

### 🤖 Automatisation (Séquence 4)
Pour répondre aux exigences de propreté du projet, j'ai intégré un **Makefile** qui automatise le cycle de vie :
* `make deploy` : Re-zippe et met à jour la fonction Lambda.
* `make status` : Teste l'API directement depuis le terminal.

### 📂 Fichiers présents dans le Repository :
* `lambda_function.py` : Code source Python.
* `Makefile` : Scripts d'automatisation.
* `README.md` : Documentation complète.
* `function.zip` : Package de déploiement.
