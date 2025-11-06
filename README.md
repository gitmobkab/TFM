# TFM
--- MANUEL CONCEPTUEL TFM POUR LA RÉDACTION DE DOCUMENTATION ---

Exemples rapides de commandes :

* `tfm generate name|telephone|address` ou `tfm generate "name telephone address"`
* `tfm parse ~/MariaDb/students.csv` ou `tfm parse ~/MySuperDatabase/companies.xlsx`
* `tfm config`
* `tfm full-config` [Toujours en développement, disponible dans la prochaine mise à jour]

Note : la commande `tfm` est un alias pour `python3 tfm.py` généré automatiquement par `setup.sh`.
Si vous ne souhaitez pas exécuter `setup.sh` ou que vous rencontrez des problèmes ([link_to_troubleshout_page]facing issues[/]), remplacez `tfm` par `python3 tfm.py`.

[DEPENDANCES]

* `Typer` (pour l'interface CLI et le parsing des arguments) — statut : externe, vital
* `rich` (pour l'affichage des tableaux générés) — statut : externe, vital
* `mysql-connector-python` (pour les requêtes et opérations sur la base de données) — statut : externe, vital
* `pandas` (support de parsing pour fichiers CSV et Excel) — statut : externe, vital
* `os` (manipulation de fichiers et gestion des chemins) — statut : intégré

Note : `os` fournit des outils pour la manipulation de chemins et fichiers ; cependant après les [link_to_related_topic_page]tests finaux[/], il pourrait être retiré au profit d'une intégration plus poussée via l'interface Typer.

--- PRINCIPES / RÈGLES ---

`tfm` nécessite toujours au moins un fichier JSON de configuration lors de son exécution (nom d'utilisateur, nom de la base, nom de la table, etc.).
Cependant `tfm` ne prend pas encore en charge un chemin personnalisé pour le fichier de configuration ; cela signifie que l'utilisateur devra utiliser les chemins préconfigurés jusqu'à ce qu'une mise à jour permette ce comportement.

Le fichier de configuration utilisateur se trouve toujours à `~/.config/tfm/config.json`.

Selon que vous ayez exécuté ou non `setup.sh`, la configuration de secours (rollback) par défaut change :

* **Sans `setup.sh`**
  --> `/the/tfm/folder/path/rollback.json`

* **Avec `setup.sh`**
  --> `/etc/tfm/rollback.json`

--- DOCUMENTATION DÉTAILLÉE DES COMMANDES TFM ---

`tfm` comporte pour l'instant trois sous-commandes :
`generate`, `parse` et `config`.

* `tfm generate`

SYNTAXE :
`tfm generate <format> [--optimized] [--user] [--password] [--database] [--table] [--config] [--rows]`

* `<format>` est l'unique argument requis.
  C'est une chaîne contenant les `format_value` séparés par `|` ou par un espace. Le but du format est d'indiquer à `tfm` quoi générer et dans quel ordre.

Exemples :

* `tfm generate name|telephone` produira des lignes du type :

  > `'Adaline Reichel','02789324'`
  > `'Dr. Santa Prosacco DVM','44-865'`

* `tfm generate first_name|last_name|age` produira des lignes du type :

  > `'Mob','Francis',19`
  > `'Tom','Mark',23`

:: Ne prenez pas la première ligne trop au sérieux.

Options importantes :

* `--optimized` : flag booléen, valeur par défaut `false`.
  Si `true`, la génération est plus rapide mais les données sont moins réalistes (désactive les pondérations pour les choix).

* `--user` : nom d'utilisateur pour la connexion à la base.

* `--password` : mot de passe de l'utilisateur courant.

* `--database` : nom de la base de données à utiliser.

* `--table` : table qui doit être remplie ou étendue par `tfm`.

Règles concernant la configuration :

* Si l'une des quatre valeurs précédentes n'est pas fournie, `tfm` utilisera le fichier de configuration utilisateur.

* Si le fichier de configuration utilisateur n'existe pas, `tfm` tentera alors le fichier de rollback selon les règles `setup.sh` exposées ci-dessus.

* IMPORTANT : si une valeur lue depuis le config est une chaîne vide `""`, vous serez invité à entrer la valeur manquante. Ceci est capital à garder en tête lors de l'écriture de scripts, car ce comportement se manifeste en shell non interactif et peut bloquer l'exécution.

* `--config` : chemin du fichier de configuration à utiliser.
  Si le fichier n'est pas trouvé, **il n'y aura PAS de parsing de rollback** et `tfm` quittera immédiatement.

* `--rows` : nombre de lignes à générer (50 par défaut — modifiable dans le fichier de config).

- `tfm parse`

SYNTAXE :
`tfm parse <path> [--ext] [--user] [--password] [--database] [--table] [--rows] [--config]`

* `<path>` : chemin du fichier (ou dossier) à parser pour remplir la table.
* `--ext` : si `<path>` est un dossier, par défaut `tfm` prendra le premier fichier `.csv` ou `.xls/.xlsx` trouvé.
  Pour éviter cela, fournissez `--ext` avec la valeur `csv` (pour .csv) ou `xl` (pour .xls/.xlsx) et `tfm` ne touchera que le premier fichier correspondant à cette extension.

Le reste des options fonctionne de la même manière que pour `tfm generate` (utilisation du config, rollback, prompts si valeurs vides, etc.).

* `tfm config`

SYNTAXE :
`tfm config`

* `tfm config` sert à aider l'utilisateur à générer et remplir tous les champs possibles du `config.json`.
* Attention : si `config.json` existe déjà, il sera **écrasé**. Un sous-commande `tfm update_conf` est en cours de développement pour permettre la modification ou l'ajout de valeurs sans écrasement.

Architecture minimale du `config.json` :

```json
{
  "user":{
      "name":"",
      "password":"",
      "database":"",
      "table":""
  },

  "gen_settings":{
     "optimized":false,
     "rows": 50
  }
}
```

Merci d'avoir lu et d'utiliser ce shithole — je ne sais même pas pourquoi j'ai construit ça mais peu importe.

Dans les futures mises à jour, `format_values` pourra probablement accepter des fonctions comme `int(n,m)` si je parviens à le faire... 🥀🥀🥀
