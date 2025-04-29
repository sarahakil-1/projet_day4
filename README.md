#  Advanced CLI Task Manager

Un outil en ligne de commande (CLI) pour gérer vos tâches avec prise en charge des sous-commandes, fichiers JSON, logs, variables d’environnement et tests unitaires.

---

##  Fonctionnalités

-  Ajouter, lister et supprimer des tâches
-  Stockage dans un fichier JSON
-  Sous-commandes CLI (`add`, `list`, `delete`) via `argparse`
-  Chemin de fichier configurable avec une variable d’environnement (`TASKS_FILE_PATH`)
-  Tests unitaires avec `unittest`
-  Journalisation des actions dans `logs/task_manager.log`

---

##  Installation

1. Clone le dépôt :
   ```bash
   git clone <url_du_repo>
   cd advanced_cli_task_manager
    ```

2. Active ton environnement Python (optionnel mais recommandé) :

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Installe les dépendances :

    ```bash
    pip install -r requirements.txt
    ```

##  Utilisation

1. Définir le fichier des tâches (optionnel)
Par défaut, les tâches sont stockées dans tasks.json.
Tu peux changer ce fichier avec la variable d’environnement :

    ```bash
    export TASKS_FILE_PATH=mon_fichier.json
    ```

2. Commandes disponibles

    ```bash
    python -m task_manager.cli add "Faire les courses" 2
    ```

    ```bash
    python -m task_manager.cli list
    ```

    ```bash
    python -m task_manager.cli delete 1
    ```

4. Tests
Les tests unitaires couvrent les fonctions d’ajout et de suppression de tâches.

    ```bash
    python -m unittest discover tests
    ```
