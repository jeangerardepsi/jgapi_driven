# ☁️ API Driven Infrastructure : Pilotage EC2 via Lambda
> **Projet de fin de module - Orchestration & Cloud émulé**

---

## 👤 Informations Étudiant
* **Nom** : Jean-Gérard
* **Filière** : Infra ESI_EPSI
* **Année Académique** : 2025-2026
* **Intervenant** : **Boris STOCKER**

---

## 🎯 Vision du Projet
L'objectif de cet atelier est de démontrer la puissance de l'**Infrastructure-as-Code** et du **Serverless**. Nous avons mis en place une solution capable de piloter des ressources Cloud (EC2) sans aucune interface graphique, en utilisant une architecture robuste : 
`Requête HTTP` ➔ `API Gateway` ➔ `AWS Lambda` ➔ `Boto3` ➔ `EC2 Instance`.

---

## 🛠️ Stack Technique & Architecture
* **Environnement** : GitHub Codespaces
* **Émulation Cloud** : LocalStack (Services : IAM, EC2, Lambda, API Gateway)
* **Runtime** : Python 3.9
* **Automatisation** : Makefile

---

## 🚀 Guide d'Utilisation (Endpoints API)

| Action | Fonctionnalité | Point d'entrée (URL) |
| :--- | :--- | :--- |
| **🔍 MONITOR** | Vérifier le statut | [Consulter le statut](https://automatic-palm-tree-r4v47xjpq97r3p9rw-4566.app.github.dev/?action=status) |
| **▶️ DEPLOY** | Démarrer l'instance | [Lancer l'instance](https://automatic-palm-tree-r4v47xjpq97r3p9rw-4566.app.github.dev/?action=start) |
| **⏹️ TERMINATE** | Arrêter l'instance | [Stopper l'instance](https://automatic-palm-tree-r4v47xjpq97r3p9rw-4566.app.github.dev/?action=stop) |

> **Note :** L'API répond en **JSON**. Une page blanche signifie que la donnée brute a été transmise avec succès.

---

## ⚙️ Automatisation & DevOps (Séquence 4)
Un **Makefile** a été implémenté pour industrialiser le processus :

1. **Déploiement à chaud** : `make deploy` (Zippage et Update Lambda)
2. **Test local** : `make status`

---

## 📝 Processus de Réalisation
1. **Provisioning** : Création de l'instance via LocalStack.
2. **Architecture** : Configuration du réseau interne via `LOCALSTACK_HOSTNAME`.
3. **Validation** : Cycle de tests validé par les codes de retour HTTP 202.
