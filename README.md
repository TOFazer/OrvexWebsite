# OverX Website

Site statique, responsive et indexable pour l'écosystème OverX. Le dépôt contenait uniquement ce README : cette première version ajoute l'accueil, le catalogue, la fiche FreeGameDrop, la documentation, le statut, la roadmap, le support, le changelog et les pages légales.

> Le nom affiché est **OverX**, conformément au brief. Le dépôt et le README du bot FreeGameDrop mentionnent encore **Orvex** : harmoniser ce nom dans les dépôts avant une annonce publique.

## Stack

- HTML statique généré par `scripts/build_site.py` (Python standard, aucune dépendance à installer)
- CSS responsive, sans framework ni ressource CDN
- JavaScript limité au menu mobile et à l'activation facultative du lien Discord
- Contenu HTML présent dans chaque page générée pour rester lisible sans JavaScript et indexable

## Prévisualiser en local

```bash
python3 scripts/build_site.py
python3 -m http.server 4173 --bind 0.0.0.0
```

Puis ouvre `http://localhost:4173`.

Pour vérifier les fichiers générés et les liens locaux :

```bash
python3 scripts/check_site.py
```

## Pages

| URL du dépôt | Contenu |
| --- | --- |
| `/` | Présentation OverX et FreeGameDrop |
| `/discord-bots/` | Catalogue des bots |
| `/discord-bots/freegamedrop/` | Fonctionnalités et configuration du bot |
| `/install/` | Parcours guidé d'installation Discord, permissions et dépannage |
| `/docs/` | Installation, permissions, commandes et FAQ |
| `/status/` | État de disponibilité, sans faux indicateurs verts |
| `/roadmap/` | Étapes prévues, sans dates promises |
| `/changelog/` | Notes de version publiées |
| `/support/` | Documentation et issues GitHub |
| `/privacy/`, `/terms/`, `/legal/` | Brouillons de pages légales à finaliser |

## Configurer l'installation Discord

Le parcours d'installation est guidé, mais le bouton qui ouvre réellement Discord reste désactivé tant que l'invitation de l'application de production n'est pas renseignée. Les autres CTA renvoient vers le guide au lieu d'un lien cassé. Modifie `assets/site-config.js` :

```js
window.OVERX_CONFIG = Object.freeze({
  discordApplicationId: "IDENTIFIANT_PUBLIC_DE_L_APPLICATION_PROD",
  discordInstallUrl: "",
  installPermissions: "268454928",
  communityInviteUrl: "",
  // ...
});
```

Le site construit alors l'URL OAuth2 Discord avec les scopes `bot applications.commands`. Il est aussi possible de fournir une URL complète `https://discord.com/oauth2/authorize?...` dans `discordInstallUrl`.

- **Application ID / Client ID** : identifiant public, utilisable dans le frontend.
- **DISCORD_TOKEN, DISCORD_CLIENT_SECRET, SECRET_KEY, DATABASE_URL** : secrets; ne jamais les mettre dans ce dépôt ni dans un fichier servi au navigateur.
- N'active le lien qu'après avoir vérifié qu'il cible l'application de production, et non l'application DEV.

`communityInviteUrl` peut recevoir l'invitation publique du serveur OverX. Le bouton communautaire reste absent tant que l'URL n'est pas renseignée. En attendant, la page support renvoie vers les issues du dépôt fourni.

## Données et affirmations publiques

Aucun endpoint de statistiques, de disponibilité ou d'uptime n'a été fourni. Les compteurs sont donc représentés par « — » et la page Statut indique « non mesuré ». L'aperçu Discord de la page d'accueil est explicitement une illustration, pas une offre en direct.

La fiche FreeGameDrop s'appuie sur le README du dépôt `TOFazer/FreeGameDropDev`. Elle distingue les sources d'offres documentées, les commandes et les fonctionnalités du code de la disponibilité effective de l'instance publique. Les chiffres et l'état en ligne ne sont jamais déduits du seul code source.

## Publication

Le site est déployable comme site statique depuis la racine de ce dépôt (par exemple GitHub Pages). Aucun backend, OAuth, base de données, analytics ou cookie non essentiel n'est ajouté dans cette V1.

Une fois le domaine et l'hébergeur choisis :

1. ajouter l'URL publique dans les métadonnées canonical et le sitemap;
2. renseigner l'hébergeur dans les mentions légales et la politique de confidentialité;
3. compléter l'identité et le contact de l'éditeur dans `legal/`, `privacy/` et `terms/`;
4. faire vérifier les textes légaux avant publication;
5. renseigner l'Application ID de production et l'invitation du Discord communautaire, s'ils existent;
6. ne publier des métriques qu'après connexion à une source mesurée et documentée.

Les pages légales portent un avertissement visible et doivent être complétées avant d'être présentées comme définitives.
