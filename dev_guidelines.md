# Directives de développement pour TFM

Ce document a pour objectif d'assurer une cohérence dans la manière dont nous développons, modifions et étendons TFM.
Il ne s'agit pas d'un ensemble de règles strictes mais de bonnes pratiques pour que le projet reste clair, lisible et évolutif.

## 1. Philosophie du projet
TFM est un outil en ligne de commande visant à simplifier la génération et l'importation de données dans des bases SQL. Il doit rester :

- **Simple à utiliser** (pas de commandes inutilement longues)
- **Prévisible** (les comportements doivent être cohérents entre `generate` et `parse`)
- **Documenté** (chaque fonctionnalité doit être compréhensible par quelqu'un qui découvre le projet)
- **Évolutif** (ne pas verrouiller des décisions trop tôt si une extension est probable)

## 2. Structure du code
- Toute nouvelle fonctionnalité doit être réfléchie pour s'intégrer dans la structure CLI existante.
- Préférer **des fonctions claires et courtes** plutôt que des blocs longs et complexes.
- Quand une fonction commence à "faire trop de choses", la découper.
- Les valeurs par défaut doivent rester synchronisées avec `config.json`.

## 3. Gestion de la configuration
- Ne jamais changer la structure du `config.json` sans mettre à jour la documentation.
- Si une nouvelle valeur est ajoutée, vérifier :
  - Comment elle s'intègre dans `tfm config`
  - Comment elle s'insère dans l'exécution de `generate` ou `parse`
  - Si elle doit être héritée depuis rollback

## 4. Style de développement
- Garder le code **lisible**, même si cela demande quelques lignes supplémentaires.
- Ajouter des **commentaires courts** uniquement lorsque la logique n'est pas évidente.
- Nommer les variables de façon explicite.

## 5. Interface utilisateur
- Les messages affichés doivent être informatifs, mais garder le ton du projet :
  - pas trop formel
  - pas condescendant
  - un peu d'humour sec est autorisé

## 6. Ajout d'un nouveau format (`format_value`)
Lorsqu'un nouveau type de donnée générable est ajouté :

1. L'ajouter dans le module qui gère la génération.
2. Vérifier qu'il fonctionne avec et sans `--optimized`.
3. Ajouter un exemple dans la documentation.

## 7. Tests
- Quand vous ajoutez une fonctionnalité, testez-la sur un table vide *et* une table existante.
- Tester dans un environnement avec config + sans config.

## 8. Contributeurs
Si vous modifiez ou ajoutez quelque chose :

- Notez-le dans le changelog (si présent)
- Prévenez les autres contributeurs des changements impactant

---
Merci d'aider à améliorer cet outil.
Même si ça a commencé comme un "projet bordélique", il devient utilisable parce qu'on le construit **ensemble**.

## 9. Mentalité UX de TFM
Le but de TFM est d'accélérer le prototypage de bases de données. Même si la documentation couvre des sujets plus larges (ex : installation de MariaDB/MySQL), l'outil n'a pas vocation à être "parfait".

Si quelque chose échoue à cause d'un mauvais usage, **c'est l'utilisateur qui s'est trompé**. Utilisez le système d'erreurs avec `rich` pour afficher des messages clairs et (légèrement) accusateurs.

## 10. Performance
Ne surchargez pas TFM avec des optimisations étranges, complexes ou illisibles.

TFM est développé en Python **parce que** il privilégie la richesse fonctionnelle plutôt que la vitesse.

Les optimisations légères sont bienvenues (simplification logique, mémoïsation, etc.), mais n’essayez pas de transformer TFM en machine de guerre ultra-performante.

## 11. Développement des commandes
Ne tentez **pas** de créer une commande entière de TFM seul si elle est complexe (comme `generate` qui requiert un parseur de format dédié).

Travail en binôme recommandé.

## 12. Contribution
Toute contribution compte.
Même corriger une annotation de type ou améliorer un commentaire est valide.

## 13. Tests et style
Utilisez le dossier `Tests/`.
Privilégiez la programmation fonctionnelle quand possible.
L'annotation de types simplifie énormément la maintenance.

---

### Dernier Mot
> *C'EST PAS COMME SI C'ÉTAIT UN OUTIL QUI ALLAIT SURVIVRE AU CIMETIÈRE DE GITHUB. DÉTENDS-TOI. AMUSE-TOI.*

Fin du document.

