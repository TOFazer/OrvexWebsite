#!/usr/bin/env python3
"""Build OverX's dependency-free, crawlable static website."""
from __future__ import annotations

from html import escape
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]

PAGES: list[dict[str, str]] = [
    {
        "path": "index.html",
        "title": "OverX — des bots Discord conçus pour simplifier vos serveurs",
        "description": "Découvrez FreeGameDrop, le premier bot de l'écosystème OverX : alertes de jeux gratuits, documentation claire et aucune statistique inventée.",
        "active": "home",
        "body": r"""
<main id="main-content">
  <section class="hero container">
    <div class="hero-copy">
      <p class="eyebrow"><span class="eyebrow-dot"></span> DES OUTILS DISCORD, SANS COMPLEXITÉ</p>
      <h1>Des bots Discord<br><span>qui simplifient</span><br>vos serveurs.</h1>
      <p class="hero-lead">OverX rassemble des outils utiles, simples à prendre en main et pensés pour les communautés Discord. Le premier : <strong>FreeGameDrop</strong>, pour ne plus passer à côté des jeux gratuits.</p>
      <div class="hero-actions">
        <a class="button button-primary" href="{{ROOT}}discord-bots/index.html">Découvrir les bots <span aria-hidden="true">↗</span></a>
        <a class="button button-secondary" data-install-cta href="{{ROOT}}install/index.html#ajouter">Guide d'installation <span aria-hidden="true">↗</span></a>
      </div>
      <div class="hero-caption"><span class="caption-check" aria-hidden="true">✓</span> Un seul bot présenté aujourd'hui. Les suivants arriveront quand ils seront prêts.</div>
    </div>
    <div class="hero-visual" aria-label="Aperçu illustratif d'une annonce de jeu dans Discord">
      <div class="visual-grid" aria-hidden="true"></div>
      <div class="visual-orbit orbit-one" aria-hidden="true"></div>
      <div class="visual-orbit orbit-two" aria-hidden="true"></div>
      <div class="orbit-node node-one" aria-hidden="true">✦</div>
      <div class="orbit-node node-two" aria-hidden="true">⌘</div>
      <div class="orbit-node node-three" aria-hidden="true">↗</div>
      <div class="floating-label label-top"><span class="mini-spark">✦</span> Un écosystème, plusieurs outils</div>
      <div class="discord-preview">
        <div class="preview-topbar"><div class="window-controls"><i></i><i></i><i></i></div><span>APERÇU ILLUSTRATIF</span><span class="preview-menu">•••</span></div>
        <div class="preview-channel"><span class="hash">#</span> jeux-gratuits <span class="channel-lock">⌑</span></div>
        <div class="preview-message">
          <div class="preview-avatar">FG</div>
          <div class="preview-message-body">
            <div class="preview-author">FreeGameDrop <span class="bot-tag">BOT</span><time>exemple</time></div>
            <div class="preview-embed">
              <div class="embed-kicker"><span class="embed-dot"></span> NOUVELLE OFFRE À DÉCOUVRIR</div>
              <h2>Un jeu gratuit, sans rien manquer.</h2>
              <p>Une alerte claire, la plateforme concernée et le lien vers l'offre — directement dans votre serveur.</p>
              <div class="embed-meta"><span>🎮 Plateformes suivies</span><span>⏱ Vérification périodique</span></div>
              <div class="embed-button">Voir les offres <span aria-hidden="true">↗</span></div>
            </div>
          </div>
        </div>
        <div class="preview-foot"><span class="tiny-pulse"></span> Illustration d'interface · aucune offre en temps réel affichée</div>
      </div>
      <div class="floating-label label-bottom"><span class="label-mark">O</span> OVERX <span class="label-divider"></span> DISCORD TOOLS</div>
    </div>
  </section>

  <section class="truth-band" aria-label="Engagement de transparence">
    <div class="container truth-band-inner">
      <div class="truth-icon" aria-hidden="true">✓</div>
      <div><p class="truth-title">Des chiffres réels, ou pas de chiffres.</p><p class="truth-copy">Les statistiques publiques apparaîtront une fois reliées aux données du bot. Pas de compteurs inventés.</p></div>
      <a class="text-link" href="{{ROOT}}status/index.html">Voir le statut des services <span aria-hidden="true">→</span></a>
    </div>
  </section>

  <section class="section container" id="bots">
    <div class="section-heading section-heading-split">
      <div><p class="eyebrow">LA COLLECTION OVERX</p><h2>Un premier bot.<br><span>Le début de l'écosystème.</span></h2></div>
      <p class="section-intro">Chaque application aura sa fiche, sa documentation et son état de disponibilité. Les projets futurs resteront clairement indiqués comme tels.</p>
    </div>
    <article class="featured-bot-card">
      <div class="bot-card-main">
        <div class="bot-card-topline"><span class="product-mark" aria-hidden="true">FG<span>D</span></span><span class="status-pill status-neutral"><span></span> Disponibilité publique à confirmer</span></div>
        <p class="eyebrow bot-category">JEUX GRATUITS · DISCORD</p>
        <h3>FreeGameDrop</h3>
        <p class="bot-description">Les jeux gratuits annoncés automatiquement sur Discord. Des alertes par plateforme, un catalogue consultable et des préférences personnalisées.</p>
        <div class="chip-row"><span class="chip">Epic Games Store</span><span class="chip">GamerPower</span><span class="chip">Favoris & alertes</span></div>
        <div class="card-actions">
          <a class="button button-primary" href="{{ROOT}}discord-bots/freegamedrop/index.html">Voir FreeGameDrop <span aria-hidden="true">↗</span></a>
<a class="button button-outline" data-install-cta href="{{ROOT}}install/index.html#ajouter">Guide d'installation <span aria-hidden="true">↗</span></a>
        </div>
        <p class="micro-note" data-install-status>Le lien d'invitation Discord n'a pas encore été communiqué.</p>
      </div>
      <div class="bot-card-art" aria-hidden="true">
        <div class="art-halo"></div>
        <div class="art-symbol">FG<span>D</span></div>
        <div class="art-caption"><span class="art-caption-dot"></span> FREEGAMEDROP <small>BOT · 01</small></div>
        <div class="art-line line-a"></div><div class="art-line line-b"></div>
        <div class="art-orbit-dot"></div>
      </div>
    </article>
    <div class="coming-soon-row"><span class="coming-icon" aria-hidden="true">＋</span><div><strong>Les prochains bots ?</strong><p>Ils seront ajoutés ici quand leur développement et leur disponibilité seront confirmés.</p></div><span class="coming-badge">À VENIR</span></div>
  </section>

  <section class="section section-alt">
    <div class="container">
      <div class="section-heading"><p class="eyebrow">CONÇU AVEC INTENTION</p><h2>Utile d'abord.<br><span>Impressionnant ensuite.</span></h2><p class="section-intro">OverX avance par étapes : une expérience fiable, de la documentation compréhensible, puis les intégrations qui apportent une vraie valeur.</p></div>
      <div class="principles-grid">
        <article class="principle-card"><div class="principle-index">01</div><div class="principle-icon icon-violet">◎</div><h3>Clair à configurer</h3><p>Des commandes et des guides qui expliquent quoi faire, sans jargon inutile.</p></article>
        <article class="principle-card"><div class="principle-index">02</div><div class="principle-icon icon-cyan">⌁</div><h3>Transparent par défaut</h3><p>État de service, chiffres et fonctionnalités ne sont publiés que s'ils sont vérifiables.</p></article>
        <article class="principle-card"><div class="principle-index">03</div><div class="principle-icon icon-lime">↗</div><h3>Construit pour évoluer</h3><p>Une page dédiée par bot, puis un dashboard et plusieurs applications quand ce sera prêt.</p></article>
      </div>
    </div>
  </section>

  <section class="section container">
    <div class="cta-panel">
      <div class="cta-glow" aria-hidden="true"></div>
      <div><p class="eyebrow">DÉCOUVRIR LE PREMIER BOT</p><h2>Les jeux gratuits.<br><span>Directement sur Discord.</span></h2><p>Explore les fonctionnalités confirmées de FreeGameDrop et suis son développement.</p></div>
      <div class="cta-actions"><a class="button button-light" href="{{ROOT}}discord-bots/freegamedrop/index.html">Découvrir FreeGameDrop <span aria-hidden="true">→</span></a><a class="text-link" href="https://github.com/TOFazer/FreeGameDropDev" target="_blank" rel="noopener noreferrer">Voir le dépôt GitHub <span aria-hidden="true">↗</span></a></div>
    </div>
  </section>
</main>
""",
    },
    {
        "path": "discord-bots/index.html",
        "title": "Bots Discord — OverX",
        "description": "Parcourez le catalogue OverX. Découvrez FreeGameDrop et les prochaines applications Discord lorsqu'elles seront prêtes.",
        "active": "bots",
        "body": r"""
<main id="main-content">
  <section class="page-hero container">
    <p class="eyebrow"><a href="{{ROOT}}index.html">OVERX</a> <span class="crumb-slash">/</span> CATALOGUE</p>
    <h1>Des bots utiles.<br><span>Pas une liste de promesses.</span></h1>
    <p class="hero-lead narrow">Voici les applications réellement documentées aujourd'hui. Les prochains bots seront annoncés quand ils auront un nom, des fonctionnalités et une disponibilité confirmés.</p>
    <div class="catalogue-meta"><span class="catalogue-dot"></span> 1 bot présenté <span class="meta-divider"></span> Catalogue en construction</div>
  </section>

  <section class="section container section-compact">
    <article class="catalogue-card">
      <div class="catalogue-visual"><div class="catalogue-visual-grid"></div><div class="catalogue-logo">FG<span>D</span></div><div class="catalogue-stamp">FREE<br>GAME<br>DROP</div><div class="catalogue-orbit"></div><span class="catalogue-tag">01 · GAMING</span></div>
      <div class="catalogue-content">
        <div class="catalogue-top"><span class="eyebrow">JEUX GRATUITS · ALERTES DISCORD</span><span class="status-pill status-neutral"><span></span> Instance publique à confirmer</span></div>
        <h2>FreeGameDrop</h2>
        <p>Repère les jeux gratuits à partir de sources comme GamerPower et l'Epic Games Store, puis aide chaque membre à suivre les plateformes et offres qui l'intéressent.</p>
        <ul class="check-list"><li>Surveillance périodique des offres</li><li>Préférences par plateforme et type d'offre</li><li>Favoris, recherche et rappels</li></ul>
        <div class="catalogue-actions"><a class="button button-primary" href="{{ROOT}}discord-bots/freegamedrop/index.html">Voir la fiche complète <span aria-hidden="true">↗</span></a><a class="button button-outline" data-install-cta href="{{ROOT}}install/index.html#ajouter">Guide d'installation <span aria-hidden="true">↗</span></a></div>
        <p class="micro-note" data-install-status>Application ID / invitation publique à renseigner dans la configuration du site.</p>
      </div>
    </article>

    <div class="future-panel"><div class="future-lock" aria-hidden="true">⌑</div><div><p class="eyebrow">LA SUITE DE L'ÉCOSYSTÈME</p><h2>Les autres bots arrivent<br><span>quand ils seront prêts.</span></h2><p>Aucun bot fictif ni compteur de lancement : cette page s'enrichira au fil des projets réellement publiés.</p></div><a class="text-link" href="{{ROOT}}roadmap/index.html">Voir la feuille de route <span aria-hidden="true">→</span></a></div>
  </section>
</main>
""",
    },
    {
        "path": "discord-bots/freegamedrop/index.html",
        "title": "FreeGameDrop — bot Discord de jeux gratuits | OverX",
        "description": "FreeGameDrop annonce les offres de jeux gratuits sur Discord : sources GamerPower et Epic Games Store, alertes personnalisées, favoris, recherche et rappels.",
        "active": "bots",
        "body": r"""
<main id="main-content">
  <section class="product-hero container" id="installation">
    <div class="product-copy">
      <p class="eyebrow"><a href="{{ROOT}}discord-bots/index.html">BOTS</a> <span class="crumb-slash">/</span> FREEGAMEDROP</p>
      <div class="product-heading"><span class="product-mark product-mark-large" aria-hidden="true">FG<span>D</span></span><span class="status-pill status-neutral"><span></span> Disponibilité publique à confirmer</span></div>
      <h1>Ne rate plus<br><span>les jeux gratuits.</span></h1>
      <p class="hero-lead">FreeGameDrop surveille des offres de jeux et les annonce dans ton serveur Discord. Chaque membre peut ensuite choisir ses plateformes, filtrer le catalogue et garder ses offres favorites.</p>
      <div class="hero-actions">
        <a class="button button-primary" data-install-cta href="{{ROOT}}install/index.html#ajouter">Guide d'installation <span aria-hidden="true">↗</span></a>
        <a class="button button-secondary" href="https://github.com/TOFazer/FreeGameDropDev" target="_blank" rel="noopener noreferrer">Voir le code source</a>
      </div>
      <p class="micro-note" data-install-status>L'invitation publique n'est pas encore renseignée. Le bouton d'installation restera inactif jusque-là.</p>
    </div>
    <div class="product-preview-card" aria-label="Exemple illustratif du panneau d'offres FreeGameDrop">
      <div class="product-preview-top"><span class="preview-led"></span><span>FREEGAMEDROP</span><span class="preview-top-right">APERÇU</span></div>
      <div class="product-preview-body">
        <div class="offer-type"><span>✦</span> EXEMPLE D'ANNONCE</div>
        <h2>Les offres qui comptent,<br>au bon endroit.</h2>
        <p>Plateforme, durée restante et lien vers la boutique — dans un message lisible sur ton serveur.</p>
        <div class="offer-platforms"><span class="platform-icon platform-epic">E</span><span>Epic Games Store</span><span class="platform-separator">·</span><span>et autres plateformes suivies</span></div>
        <div class="preview-cta-line"><span>Découvrir les offres</span><span aria-hidden="true">→</span></div>
      </div>
      <div class="preview-disclaimer">Maquette de présentation · pas une annonce en direct</div>
    </div>
  </section>

  <section class="section section-alt">
    <div class="container">
      <div class="section-heading"><p class="eyebrow">FONCTIONNALITÉS DOCUMENTÉES</p><h2>Tout ce qu'il faut<br><span>pour trouver sa prochaine offre.</span></h2><p class="section-intro">Les fonctionnalités ci-dessous sont tirées de la documentation du dépôt FreeGameDropDev. L'état de l'instance publique n'est pas vérifié par ce site.</p></div>
      <div class="feature-grid">
        <article class="feature-card"><div class="feature-icon icon-violet">⌁</div><h3>Offres agrégées</h3><p>Le code documente GamerPower et l'API officielle de l'Epic Games Store comme sources d'offres.</p><span class="feature-index">01</span></article>
        <article class="feature-card"><div class="feature-icon icon-cyan">◉</div><h3>Alertes par plateforme</h3><p>Configuration de rôles et salons dédiés; les membres choisissent les plateformes qui les intéressent.</p><span class="feature-index">02</span></article>
        <article class="feature-card"><div class="feature-icon icon-lime">♡</div><h3>Favoris & rappels</h3><p>Enregistre des offres, active des alertes personnelles et rappelle les fins d'offre proches.</p><span class="feature-index">03</span></article>
        <article class="feature-card"><div class="feature-icon icon-orange">⌕</div><h3>Recherche & historique</h3><p>Parcours les offres connues, recherche par mot-clé et retrouve les offres récentes.</p><span class="feature-index">04</span></article>
        <article class="feature-card"><div class="feature-icon icon-pink">⚙</div><h3>Réglages personnels</h3><p>Filtre par plateforme, type d'offre, valeur minimale et genre, selon les options disponibles.</p><span class="feature-index">05</span></article>
        <article class="feature-card"><div class="feature-icon icon-blue">⌁</div><h3>Santé & statistiques</h3><p>Le bot documente les commandes <code>/stats</code> et <code>/sante</code>. Les chiffres publics doivent venir de mesures réelles.</p><span class="feature-index">06</span></article>
      </div>
    </div>
  </section>

  <section class="section container">
    <div class="section-heading section-heading-split"><div><p class="eyebrow">PREMIÈRE CONFIGURATION</p><h2>Du serveur au<br><span>premier salon de jeux.</span></h2></div><p class="section-intro">Une fois l'application invitée et les permissions accordées, les administrateurs peuvent lancer l'assistant depuis Discord.</p></div>
    <div class="setup-steps">
      <article class="setup-step"><span class="step-number">01</span><div><h3>Ajouter le bot</h3><p>Le lien public d'installation doit d'abord être configuré par l'équipe OverX. L'ajout nécessite une permission de gestion du serveur.</p></div><span class="step-state">LIEN À CONFIGURER</span></article>
      <article class="setup-step"><span class="step-number">02</span><div><h3>Lancer <code>/setup-auto</code></h3><p>Choisis les plateformes à suivre. La commande crée ou répare la catégorie, les rôles, les salons et le panneau de sélection.</p></div><span class="step-state">COMMANDE DOCUMENTÉE</span></article>
      <article class="setup-step"><span class="step-number">03</span><div><h3>Personnaliser les alertes</h3><p>Les membres peuvent ensuite parcourir <code>/free</code>, gérer leurs favoris, alertes et préférences.</p></div><span class="step-state">GUIDE DISPONIBLE</span></article>
    </div>
  </section>

  <section class="section section-alt">
    <div class="container two-column-section">
      <div><p class="eyebrow">COMMANDES RAPIDES</p><h2>À portée<br><span>de slash.</span></h2><p class="section-intro">FreeGameDrop utilise des commandes d'application Discord. Les commandes de configuration sont réservées aux administrateurs.</p><a class="text-link" href="{{ROOT}}docs/index.html#commandes">Toutes les commandes <span aria-hidden="true">→</span></a></div>
      <div class="command-pills"><span><code>/free</code><small>parcourir les offres</small></span><span><code>/favoris</code><small>gérer ses jeux favoris</small></span><span><code>/recherche</code><small>chercher une offre</small></span><span><code>/preferences</code><small>personnaliser le catalogue</small></span><span><code>/alertes</code><small>gérer ses notifications</small></span><span><code>/sante</code><small>vérifier l'état mesuré</small></span></div>
    </div>
  </section>

  <section class="section container">
    <div class="privacy-callout"><div class="callout-icon" aria-hidden="true">⌑</div><div><p class="eyebrow">DONNÉES & CONFIDENTIALITÉ</p><h2>Pas de collecte de messages.</h2><p>La documentation du bot indique qu'il ne stocke pas le contenu des messages. Il conserve toutefois certaines données de configuration et de préférences nécessaires au service. Consulte la politique de confidentialité provisoire pour le détail.</p><a class="text-link" href="{{ROOT}}privacy/index.html">Lire la politique de confidentialité <span aria-hidden="true">→</span></a></div></div>
  </section>
</main>
""",
    },
    {
        "path": "install/index.html",
        "title": "Installer FreeGameDrop sur Discord — OverX",
        "description": "Guide pas à pas pour ajouter FreeGameDrop à un serveur Discord : autoriser l'application, sélectionner son serveur et lancer la configuration.",
        "active": "install",
        "body": r"""
<main id="main-content">
  <section class="install-hero container">
    <div class="install-copy">
      <p class="eyebrow"><a href="{{ROOT}}discord-bots/freegamedrop/index.html">FREEGAMEDROP</a> <span class="crumb-slash">/</span> INSTALLATION</p>
      <span class="status-pill status-neutral install-state" data-install-state><span></span> Lien de production à configurer</span>
      <h1>Sur ton serveur.<br><span>En quelques étapes.</span></h1>
      <p class="hero-lead">Le parcours est celui de Discord : autoriser le bot, choisir un serveur, puis lancer son assistant de configuration. Pas de compte OverX à créer.</p>
      <div class="install-copy-actions"><a class="button button-primary install-main-cta" data-discord-install href="#ajouter" aria-disabled="true">Invitation Discord à configurer <span aria-hidden="true">↗</span></a><button class="button button-secondary copy-admin-button" data-copy-admin type="button" hidden>Copier un message pour mon admin</button></div>
      <p class="install-live-note" data-install-status>Le lien officiel de l'application PROD n'a pas encore été renseigné.</p>
    </div>
    <div class="install-flow-card" aria-label="Les trois étapes de l'installation">
      <div class="install-flow-header"><span class="flow-logo">FG<span>D</span></span><div><strong>Installation FreeGameDrop</strong><small>Parcours dans Discord</small></div><span class="flow-lock" aria-hidden="true">⌑</span></div>
      <div class="flow-step"><span class="flow-number">01</span><span class="flow-icon">↗</span><div><strong>Autoriser l'application</strong><small>Discord affiche les permissions demandées</small></div><span class="flow-check">✓</span></div>
      <div class="flow-connector"></div>
      <div class="flow-step"><span class="flow-number">02</span><span class="flow-icon icon-cyan">⌂</span><div><strong>Choisir ton serveur</strong><small>Il faut pouvoir gérer le serveur</small></div><span class="flow-check">✓</span></div>
      <div class="flow-connector"></div>
      <div class="flow-step"><span class="flow-number">03</span><span class="flow-icon icon-lime">⚙</span><div><strong>Lancer <code>/setup-auto</code></strong><small>Choisis les plateformes à suivre</small></div><span class="flow-check">✓</span></div>
      <div class="install-flow-footer"><span class="tiny-pulse"></span> Tu restes sur le parcours officiel Discord</div>
    </div>
  </section>

  <section class="section section-alt" id="ajouter">
    <div class="container">
      <div class="section-heading"><p class="eyebrow">INSTALLATION, PAS À PAS</p><h2>Tu sais déjà utiliser Discord ?<br><span>Tu peux installer le bot.</span></h2><p class="section-intro">Suis ces étapes dans l'ordre. Si tu bloques à l'étape 2, ce n'est probablement pas toi : Discord réserve l'ajout d'applications aux membres qui peuvent gérer le serveur.</p></div>
      <div class="install-steps-grid">
        <article class="install-step-card"><span class="install-step-index">ÉTAPE 01</span><div class="install-step-icon">↗</div><h3>Clique sur Ajouter à Discord</h3><p>Le bouton ouvre la page d'autorisation officielle de Discord. Connecte-toi au compte qui gère ton serveur si Discord te le demande.</p></article>
        <article class="install-step-card"><span class="install-step-index">ÉTAPE 02</span><div class="install-step-icon icon-cyan">⌂</div><h3>Sélectionne ton serveur</h3><p>Choisis le serveur dans la liste. Il faut la permission <strong>Gérer le serveur</strong> ou <strong>Administrateur</strong>. Si le serveur n'apparaît pas, demande à un admin de faire l'installation.</p></article>
        <article class="install-step-card"><span class="install-step-index">ÉTAPE 03</span><div class="install-step-icon icon-lime">✓</div><h3>Autorise puis configure</h3><p>Vérifie les permissions affichées par Discord, clique sur <strong>Autoriser</strong>, puis lance <code>/setup-auto</code> dans le serveur pour créer les salons de jeux.</p></article>
      </div>
    </div>
  </section>

  <section class="section container">
    <div class="install-permissions-layout">
      <div><p class="eyebrow">PERMISSIONS AFFICHÉES PAR DISCORD</p><h2>Le minimum utile<br><span>pour faire fonctionner le bot.</span></h2><p class="section-intro">FreeGameDrop doit pouvoir créer les espaces de jeux et publier les offres. Discord t'affichera la demande avant l'ajout.</p></div>
      <div class="install-permissions-card"><div class="permission-heading"><span class="permission-discord-icon">◉</span><div><strong>Permissions du serveur</strong><small>Demandées lors de l'ajout</small></div></div><div class="permission-check-row"><span>✓</span> Gérer les salons</div><div class="permission-check-row"><span>✓</span> Gérer les rôles de plateforme</div><div class="permission-check-row"><span>✓</span> Voir les salons</div><div class="permission-check-row"><span>✓</span> Envoyer des messages et intégrer des liens</div><p class="permission-footnote">Ces permissions correspondent à l'invitation documentée dans le dépôt fourni. Discord reste l'écran de confirmation officiel.</p></div>
    </div>
  </section>

  <section class="section section-alt">
    <div class="container install-help-layout">
      <div><p class="eyebrow">ÇA NE MARCHE PAS ?</p><h2>Les blocages<br><span>les plus fréquents.</span></h2><p class="section-intro">Une aide directe plutôt qu'un écran d'erreur incompréhensible.</p></div>
      <div class="install-help-list">
        <details class="faq-item"><summary>Mon serveur n'apparaît pas dans Discord.</summary><p>Ton compte n'a probablement pas la permission de gérer ce serveur. Demande à un administrateur ou à un membre ayant « Gérer le serveur » de lancer l'invitation.</p></details>
        <details class="faq-item"><summary>Le bot est ajouté, mais aucun salon n'a été créé.</summary><p>L'installation ajoute l'application au serveur; la configuration des salons se lance ensuite avec <code>/setup-auto</code>. Le bot doit être en ligne et conserver les permissions nécessaires.</p></details>
        <details class="faq-item"><summary>Discord refuse une permission ou l'invitation semble incorrecte.</summary><p>Ne tente pas d'utiliser l'application de développement. L'équipe doit renseigner ici le lien OAuth2 de production vérifié. Tant qu'il n'est pas configuré, le bouton reste désactivé.</p></details>
        <details class="faq-item"><summary>Je suis sur téléphone.</summary><p>Le même bouton ouvre Discord ou son navigateur. Connecte-toi au bon compte, choisis le serveur, puis confirme l'autorisation. Si tu ne peux pas gérer le serveur, demande à son administrateur.</p></details>
      </div>
    </div>
  </section>

  <section class="section container">
    <div class="install-bottom-cta"><div><p class="eyebrow">BESOIN D'UN COUP DE MAIN ?</p><h2>On t'accompagne.</h2><p>Consulte le guide complet ou signale un problème dans le dépôt du bot. Ne publie jamais de token Discord.</p></div><div class="install-bottom-actions"><a class="button button-primary" href="{{ROOT}}docs/index.html#installation">Lire le guide complet <span aria-hidden="true">→</span></a><a class="text-link" href="{{ROOT}}support/index.html">Contacter le support <span aria-hidden="true">→</span></a></div></div>
  </section>
</main>
""",
    },
    {
        "path": "docs/index.html",
        "title": "Documentation FreeGameDrop — OverX",
        "description": "Guide d'installation, de configuration et de commandes pour FreeGameDrop, le bot Discord de jeux gratuits d'OverX.",
        "active": "docs",
        "body": r"""
<main id="main-content">
  <section class="page-hero container docs-hero">
    <p class="eyebrow">GUIDES OVERX <span class="crumb-slash">/</span> FREEGAMEDROP</p>
    <h1>La documentation<br><span>sans chercher partout.</span></h1>
    <p class="hero-lead narrow">Les étapes ci-dessous suivent les commandes et comportements décrits dans le dépôt FreeGameDropDev. Le lien d'invitation public reste à configurer.</p>
    <div class="docs-search-note"><span aria-hidden="true">⌕</span><span>Une question précise ? Utilise la recherche de ton navigateur avec <kbd>Ctrl</kbd> <span>+</span> <kbd>F</kbd>.</span></div>
  </section>

  <section class="section container docs-layout">
    <aside class="docs-toc"><p class="eyebrow">DANS CE GUIDE</p><a href="#installation">Installation</a><a href="#configuration">Configuration</a><a href="#commandes">Commandes</a><a href="#permissions">Permissions</a><a href="#faq">FAQ</a><a href="#auto-hebergement">Auto-hébergement</a></aside>
    <div class="docs-content">
      <section class="doc-section" id="installation"><p class="eyebrow">01 · DÉMARRER</p><h2>Installer le bot</h2><ol class="numbered-steps"><li><strong>Ajoute FreeGameDrop à ton serveur.</strong><p>L'invitation publique n'est pas encore configurée sur ce site. Elle sera activée dès que l'Application ID de l'instance sera fourni.</p></li><li><strong>Choisis un serveur où tu peux gérer les applications.</strong><p>Discord demande la permission de gérer le serveur pour autoriser l'installation d'un bot.</p></li><li><strong>Vérifie les permissions puis autorise.</strong><p>Le bot a besoin des permissions documentées ci-dessous pour créer les salons, rôles et annonces.</p></li><li><strong>Lance <code>/setup-auto</code> dans ton serveur.</strong><p>Sélectionne les plateformes souhaitées, puis valide la création ou la mise à jour de la configuration.</p></li></ol><div class="notice notice-warn"><strong>À savoir</strong><p>La disponibilité de l'instance et son URL d'invitation ne sont pas encore connectées au site. Le code source reste consultable sur GitHub.</p><a class="text-link" href="https://github.com/TOFazer/FreeGameDropDev" target="_blank" rel="noopener noreferrer">Ouvrir FreeGameDropDev <span aria-hidden="true">↗</span></a></div></section>

      <section class="doc-section" id="configuration"><p class="eyebrow">02 · CONFIGURATION</p><h2>Configurer les notifications</h2><p><code>/setup-auto</code> crée ou met à jour la catégorie de jeux, les rôles de plateforme, les salons dédiés et le panneau de sélection. Les membres peuvent cliquer sur les boutons pour obtenir ou retirer un rôle de plateforme.</p><ul class="doc-bullets"><li>Les salons de jeux sont organisés par plateforme et configurés en lecture seule pour les membres.</li><li>Les commandes <code>/config</code> et <code>/acces-salon-roles</code> permettent aux administrateurs d'ajuster la configuration décrite par le bot.</li><li><code>/rappel-salon</code> permet de choisir le salon qui reçoit les rappels de fin d'offre.</li><li>Le bot est documenté comme vérifiant les offres toutes les heures; l'état réel de l'instance doit être vérifié avec <code>/sante</code>.</li></ul></section>

      <section class="doc-section" id="commandes"><p class="eyebrow">03 · RÉFÉRENCE</p><h2>Commandes principales</h2><div class="table-wrap"><table class="command-table"><thead><tr><th>Commande</th><th>Accès</th><th>À quoi elle sert</th></tr></thead><tbody>
        <tr><td><code>/setup-auto</code></td><td>Admin</td><td>Crée ou répare salons, rôles et panneau de sélection.</td></tr>
        <tr><td><code>/config</code></td><td>Admin</td><td>Rouvre le panneau de configuration.</td></tr>
        <tr><td><code>/free</code></td><td>Membres</td><td>Parcourt les offres disponibles avec des filtres.</td></tr>
        <tr><td><code>/favoris</code></td><td>Membres</td><td>Consulte et gère les offres favorites.</td></tr>
        <tr><td><code>/historique</code></td><td>Membres</td><td>Parcourt les dernières offres connues.</td></tr>
        <tr><td><code>/recherche</code></td><td>Membres</td><td>Recherche une offre par titre ou description.</td></tr>
        <tr><td><code>/preferences</code></td><td>Membres</td><td>Filtre par plateforme, type, valeur minimale et genre.</td></tr>
        <tr><td><code>/alertes</code></td><td>Membres</td><td>Active ou désactive des alertes privées.</td></tr>
        <tr><td><code>/rappel-salon</code></td><td>Admin</td><td>Choisit le salon des rappels de fin d'offre.</td></tr>
        <tr><td><code>/stats</code></td><td>Membres</td><td>Affiche les chiffres mesurés par le bot.</td></tr>
        <tr><td><code>/sante</code></td><td>Membres</td><td>Affiche l'état mesuré du bot, des sources et de la base.</td></tr>
        <tr><td><code>/mes-donnees</code></td><td>Membres</td><td>Demande la suppression des favoris associés au compte.</td></tr>
        <tr><td><code>/info</code> · <code>/ping</code></td><td>Membres</td><td>Informations sur le bot et test de réponse.</td></tr>
        <tr><td><code>/test-jeux</code> · <code>/reset-jeux</code></td><td>Admin</td><td>Actions de test et de réannonce décrites dans le README.</td></tr>
      </tbody></table></div><p class="fine-print">La liste complète des commandes, leurs options exactes et les notes de version sont maintenues dans le dépôt du bot.</p></section>

      <section class="doc-section" id="permissions"><p class="eyebrow">04 · AUTORISATIONS</p><h2>Permissions nécessaires</h2><p>La documentation du dépôt recommande les permissions Discord utiles à la création des espaces de jeux et à l'envoi des annonces :</p><div class="permission-grid"><span>Gérer les salons</span><span>Gérer les rôles</span><span>Voir les salons</span><span>Envoyer des messages</span><span>Intégrer des liens</span></div><div class="notice"><strong>Rôles de plateforme</strong><p>Place le rôle du bot au-dessus des rôles qu'il doit attribuer. Discord empêchera sinon le bot de les gérer.</p></div></section>

      <section class="doc-section" id="faq"><p class="eyebrow">05 · QUESTIONS FRÉQUENTES</p><h2>FAQ</h2><details class="faq-item"><summary>Le site peut-il configurer mon serveur ?</summary><p>Non. Cette version du site est statique : aucune connexion Discord, aucun dashboard ni aucune API OverX n'y sont activés. La configuration se fait avec les commandes du bot.</p></details><details class="faq-item"><summary>Où trouver les statistiques réelles ?</summary><p>La commande <code>/stats</code> est documentée dans le bot et ne doit afficher que des valeurs mesurées. La page Statut du site indique explicitement qu'aucune source live n'est encore raccordée.</p></details><details class="faq-item"><summary>Le bot est-il actuellement en ligne ?</summary><p>Ce site ne peut pas le confirmer sans endpoint de santé public. Si le bot est présent sur ton serveur, la commande <code>/sante</code> donne son état mesuré selon le code du projet.</p></details><details class="faq-item"><summary>Comment demander de l'aide ?</summary><p>Utilise le suivi de bugs et les discussions du dépôt GitHub FreeGameDropDev. Une invitation Discord de support sera ajoutée si elle est fournie.</p><a class="text-link" href="{{ROOT}}support/index.html">Ouvrir la page Support <span aria-hidden="true">→</span></a></details></section>

      <section class="doc-section" id="auto-hebergement"><p class="eyebrow">06 · POUR LES DÉVELOPPEURS</p><h2>Auto-hébergement</h2><p>Le dépôt FreeGameDropDev contient les instructions détaillées sur Python, Docker, les variables d'environnement, les environnements DEV/PROD et les tests. Les secrets doivent rester côté serveur, jamais dans le site.</p><a class="button button-secondary" href="https://github.com/TOFazer/FreeGameDropDev" target="_blank" rel="noopener noreferrer">Lire le README du bot <span aria-hidden="true">↗</span></a></section>
    </div>
  </section>
</main>
""",
    },
    {
        "path": "status/index.html",
        "title": "Statut des services — OverX",
        "description": "État de transparence OverX : aucune sonde publique de disponibilité n'est connectée pour le moment.",
        "active": "status",
        "body": r"""
<main id="main-content">
  <section class="page-hero container status-hero">
    <p class="eyebrow">OVERX <span class="crumb-slash">/</span> STATUS</p>
    <h1>Un statut clair.<br><span>Même quand il manque des données.</span></h1>
    <p class="hero-lead narrow">Nous n'affichons pas de pastilles vertes sans vérification. Aucune sonde publique de disponibilité n'est encore raccordée à cette page.</p>
  </section>
  <section class="section container section-compact">
    <div class="status-summary"><div class="status-summary-icon">—</div><div><p class="eyebrow">ÉTAT ACTUEL DE LA PAGE</p><h2>Non mesuré en temps réel</h2><p>Dernière vérification automatique : <strong>aucune sonde configurée</strong>.</p></div><span class="status-pill status-neutral"><span></span> Données non connectées</span></div>
    <div class="service-list">
      <article class="service-row"><div class="service-indicator indicator-unknown">?</div><div><h3>FreeGameDrop · bot Discord</h3><p>Aucun endpoint public de santé n'a été fourni. Sur un serveur où le bot est installé, <code>/sante</code> est la commande documentée pour vérifier ses composants.</p></div><span class="service-state">NON MESURÉ</span></article>
      <article class="service-row"><div class="service-indicator indicator-unknown">?</div><div><h3>Site OverX</h3><p>Page de statut statique. Elle n'effectue pas de contrôle de disponibilité de l'hébergement.</p></div><span class="service-state">NON MESURÉ</span></article>
      <article class="service-row"><div class="service-indicator indicator-muted">—</div><div><h3>Dashboard & API OverX</h3><p>Non inclus dans cette première version du site; prévus comme pistes d'évolution.</p></div><span class="service-state">NON DÉPLOYÉS DANS CETTE V1</span></article>
    </div>
    <div class="notice notice-warn status-note"><strong>Pourquoi pas d'uptime ?</strong><p>Un pourcentage comme « 99,9 % » doit venir d'une mesure horodatée et reproductible. Il sera affiché lorsqu'une sonde et une source de données auront été mises en place.</p></div>
    <div class="status-links"><a class="text-link" href="https://github.com/TOFazer/FreeGameDropDev" target="_blank" rel="noopener noreferrer">Dépôt FreeGameDropDev <span aria-hidden="true">↗</span></a><a class="text-link" href="{{ROOT}}support/index.html">Signaler un problème <span aria-hidden="true">→</span></a></div>
  </section>
</main>
""",
    },
    {
        "path": "changelog/index.html",
        "title": "Changelog — OverX",
        "description": "Notes de version et évolutions des bots OverX.",
        "active": "changelog",
        "body": r"""
<main id="main-content">
  <section class="page-hero container">
    <p class="eyebrow">OVERX <span class="crumb-slash">/</span> CHANGELOG</p>
    <h1>Ce qui change.<br><span>Quand ça change vraiment.</span></h1>
    <p class="hero-lead narrow">Les versions et changements publics seront consignés ici. Aucune version ni date de lancement n'a été inventée pour remplir la page.</p>
  </section>
  <section class="section container section-compact">
    <div class="empty-state"><div class="empty-orbit" aria-hidden="true"><span>✦</span></div><p class="eyebrow">JOURNAL DES VERSIONS</p><h2>Aucune note de version publiée pour le moment.</h2><p>Le code et les évolutions de FreeGameDrop sont consultables dans son dépôt GitHub. Les prochaines notes visibles ici devront correspondre à des changements réellement publiés.</p><a class="button button-primary" href="https://github.com/TOFazer/FreeGameDropDev" target="_blank" rel="noopener noreferrer">Suivre le dépôt du bot <span aria-hidden="true">↗</span></a></div>
    <div class="changelog-how"><span class="timeline-mark"></span><div><p class="eyebrow">À VENIR</p><h3>Notes de version OverX</h3><p>Cette page pourra accueillir les nouvelles fonctionnalités, améliorations et corrections, avec leur date et leur version vérifiées.</p></div></div>
  </section>
</main>
""",
    },
    {
        "path": "roadmap/index.html",
        "title": "Feuille de route — OverX",
        "description": "Les étapes prévues pour faire évoluer OverX : FreeGameDrop, le site, la connexion Discord et l'écosystème de bots.",
        "active": "roadmap",
        "body": r"""
<main id="main-content">
  <section class="page-hero container">
    <p class="eyebrow">OVERX <span class="crumb-slash">/</span> ROADMAP</p>
    <h1>Une étape à la fois.<br><span>Sans brûler les étapes.</span></h1>
    <p class="hero-lead narrow">La priorité est de rendre le premier bot compréhensible, testable et transparent avant de multiplier les applications ou de créer un dashboard.</p>
  </section>
  <section class="section container section-compact">
    <div class="roadmap-list">
      <article class="roadmap-item roadmap-now"><div class="roadmap-marker"><span>01</span></div><div class="roadmap-copy"><div class="roadmap-top"><span class="eyebrow">FONDATIONS</span><span class="status-pill status-current"><span></span> PRIORITÉ</span></div><h2>FreeGameDrop & OverX v1</h2><p>Documenter les fonctionnalités réelles du bot, proposer un catalogue lisible et préparer les pages d'installation, de support, de statut et de confidentialité.</p><div class="roadmap-tags"><span>Site responsive</span><span>Documentation</span><span>Transparence</span><span>Installation à configurer</span></div></div></article>
      <article class="roadmap-item"><div class="roadmap-marker"><span>02</span></div><div class="roadmap-copy"><div class="roadmap-top"><span class="eyebrow">APRÈS VALIDATION</span><span class="status-pill status-neutral"><span></span> À PLANIFIER</span></div><h2>Connexion Discord & dashboard</h2><p>Étudier OAuth2, la liste des serveurs gérables et la configuration web de FreeGameDrop. Cette étape nécessitera un backend, une base de données, des secrets serveur et une politique de confidentialité finalisée.</p><div class="roadmap-tags"><span>OAuth2</span><span>Sessions sécurisées</span><span>API</span><span>Configuration de serveur</span></div></div></article>
      <article class="roadmap-item"><div class="roadmap-marker"><span>03</span></div><div class="roadmap-copy"><div class="roadmap-top"><span class="eyebrow">ENSUITE</span><span class="status-pill status-neutral"><span></span> À EXPLORER</span></div><h2>Communauté & croissance</h2><p>Connecter des statistiques réelles, un statut mesuré, un changelog, puis préparer l'internationalisation et la découverte dans Discord.</p><div class="roadmap-tags"><span>Statistiques vérifiées</span><span>Anglais</span><span>App Directory</span><span>Suggestions</span></div></div></article>
      <article class="roadmap-item"><div class="roadmap-marker"><span>04</span></div><div class="roadmap-copy"><div class="roadmap-top"><span class="eyebrow">LONG TERME</span><span class="status-pill status-neutral"><span></span> NON ANNONCÉ</span></div><h2>Écosystème multi-bots</h2><p>De nouveaux bots, une API commune et un compte OverX ne seront ajoutés que lorsque des produits concrets et des besoins validés le justifieront.</p><div class="roadmap-tags"><span>Pas de noms fictifs</span><span>Pas de dates promises</span></div></div></article>
    </div>
    <div class="notice"><strong>La roadmap peut évoluer.</strong><p>Les idées ne sont pas des engagements de livraison. Les changements réellement publiés apparaîtront dans le <a class="inline-link" href="{{ROOT}}changelog/index.html">changelog</a>.</p></div>
  </section>
</main>
""",
    },
    {
        "path": "support/index.html",
        "title": "Support — OverX & FreeGameDrop",
        "description": "Besoin d'aide avec FreeGameDrop ? Consultez la documentation ou signalez un problème dans le dépôt officiel.",
        "active": "support",
        "body": r"""
<main id="main-content">
  <section class="page-hero container">
    <p class="eyebrow">OVERX <span class="crumb-slash">/</span> SUPPORT</p>
    <h1>On peut t'aider.<br><span>Voici le bon endroit.</span></h1>
    <p class="hero-lead narrow">La communauté Discord OverX n'a pas encore de lien public renseigné. En attendant, le dépôt du bot permet de consulter le code et de signaler un problème.</p>
  </section>
  <section class="section container section-compact">
    <div class="support-grid">
      <article class="support-card support-card-primary"><div class="support-icon">?</div><p class="eyebrow">UNE QUESTION OU UN BUG ?</p><h2>Ouvrir une discussion GitHub</h2><p>Décris le problème, la commande concernée et ce que tu as essayé. Ne publie jamais de token, mot de passe ou donnée privée.</p><a class="button button-primary" href="https://github.com/TOFazer/FreeGameDropDev/issues" target="_blank" rel="noopener noreferrer">Aller au support FreeGameDrop <span aria-hidden="true">↗</span></a></article>
      <article class="support-card"><div class="support-icon icon-cyan">⌕</div><p class="eyebrow">AVANT DE SIGNALER</p><h2>Vérifier le guide</h2><p>Les étapes de configuration, les commandes principales et les permissions nécessaires sont regroupées dans la documentation OverX.</p><a class="text-link" href="{{ROOT}}docs/index.html">Ouvrir la documentation <span aria-hidden="true">→</span></a></article>
      <article class="support-card"><div class="support-icon icon-lime">⌘</div><p class="eyebrow">CODE & CONTRIBUTIONS</p><h2>Explorer le projet</h2><p>Le dépôt fourni pour FreeGameDrop est un dépôt de développement. Consulte son README pour les consignes d'installation, d'environnement et de contribution.</p><a class="text-link" href="https://github.com/TOFazer/FreeGameDropDev" target="_blank" rel="noopener noreferrer">Voir le dépôt GitHub <span aria-hidden="true">↗</span></a></article>
    </div>
    <div class="notice notice-warn"><strong>Discord support</strong><p>Un lien d'invitation au serveur de communauté n'a pas été fourni. Il pourra être ajouté dans <code>assets/site-config.js</code> dès qu'il existera.</p></div>
  </section>
</main>
""",
    },
    {
        "path": "privacy/index.html",
        "title": "Politique de confidentialité — OverX",
        "description": "Politique de confidentialité provisoire du site OverX et informations documentées sur les données utilisées par FreeGameDrop.",
        "active": "legal",
        "body": r"""
<main id="main-content">
  <section class="page-hero container legal-hero">
    <p class="eyebrow">INFORMATIONS LÉGALES <span class="crumb-slash">/</span> CONFIDENTIALITÉ</p>
    <h1>Ta vie privée<br><span>n'est pas une option.</span></h1>
    <p class="hero-lead narrow">Cette page décrit la version statique actuelle du site et les données mentionnées dans la documentation de FreeGameDrop.</p>
  </section>
  <section class="section container legal-layout">
    <div class="draft-warning"><span aria-hidden="true">!</span><div><strong>Brouillon à compléter avant publication publique</strong><p>L'identité légale de l'éditeur, l'adresse de contact, l'hébergeur et certaines durées de conservation n'ont pas été communiqués. Ne présente pas ce texte comme une politique finalisée sans validation.</p></div></div>
    <article class="legal-content">
      <p class="legal-updated">État : version de travail · 7 octobre 2026</p>
      <h2>1. Responsable du traitement</h2><p>Éditeur / responsable du traitement : <strong>[À COMPLÉTER : nom ou raison sociale, adresse et moyen de contact]</strong>. Les coordonnées du responsable ne sont pas encore fournies.</p>
      <h2>2. Le site OverX</h2><p>Dans cette première version, le site est constitué de pages statiques. Il ne propose ni connexion Discord, ni formulaire, ni compte, ni dashboard, ni outil d'analyse d'audience; aucun cookie non essentiel n'est installé par le code du site.</p><p>Comme pour tout site hébergé, l'hébergeur peut traiter des données techniques de requête (par exemple adresse IP, date, navigateur) dans ses journaux. L'hébergeur et ses durées de conservation devront être précisés lorsque le déploiement sera choisi.</p>
      <h2>3. Bot FreeGameDrop</h2><p>Le bot Discord est un service séparé du site. Selon le README du dépôt <a href="https://github.com/TOFazer/FreeGameDropDev" target="_blank" rel="noopener noreferrer">FreeGameDropDev</a>, son fonctionnement peut enregistrer dans SQLite des identifiants de serveurs, salons et rôles, des informations d'offres publiques, des favoris associés à un identifiant Discord, des préférences et réglages d'alertes, ainsi qu'un historique minimal d'alertes. Le dépôt indique que le bot ne stocke pas le contenu des messages ni la preuve qu'un jeu a été réclamé.</p><p>Le README précise que les offres publiques non favorites sont retirées du catalogue après 90 jours sans nouvelle observation; les favoris restent jusqu'à leur retrait ou à la suppression des données. Les autres durées doivent être confirmées par l'exploitant. Les paramètres d'une éventuelle connexion web décrits dans le dépôt ne sont pas activés par ce site.</p>
      <h2>4. Suppression et droits</h2><p>Le dépôt documente la commande <code>/mes-donnees</code> pour demander la suppression des favoris associés au compte. Sa documentation précise que cette commande ne supprime pas les réglages du serveur ni toutes les préférences et alertes personnelles. La procédure complète de contact et d'exercice des droits doit être confirmée par le responsable du traitement.</p><p>Contact pour les demandes relatives aux données : <strong>[À COMPLÉTER : adresse de contact du responsable]</strong>.</p>
      <h2>5. Services tiers</h2><p>Les liens vers Discord et GitHub conduisent vers des services externes soumis à leurs propres conditions et politiques de confidentialité. Le site ne contrôle pas leurs traitements.</p>
      <h2>6. Mise à jour</h2><p>Cette politique devra être complétée et mise à jour si un compte Discord, des statistiques, une API, des formulaires, des cookies ou un dashboard sont ajoutés. Dernière révision du brouillon : 7 octobre 2026.</p>
    </article>
  </section>
</main>
""",
    },
    {
        "path": "terms/index.html",
        "title": "Conditions d'utilisation — OverX",
        "description": "Conditions d'utilisation provisoires du site OverX et des informations relatives à FreeGameDrop.",
        "active": "legal",
        "body": r"""
<main id="main-content">
  <section class="page-hero container legal-hero">
    <p class="eyebrow">INFORMATIONS LÉGALES <span class="crumb-slash">/</span> CONDITIONS</p>
    <h1>Des règles simples.<br><span>À finaliser avant lancement.</span></h1>
    <p class="hero-lead narrow">Projet de conditions pour le site OverX et les liens vers ses bots Discord.</p>
  </section>
  <section class="section container legal-layout">
    <div class="draft-warning"><span aria-hidden="true">!</span><div><strong>Document de travail</strong><p>Le nom et les coordonnées de l'éditeur, les modalités de support et le droit applicable doivent être validés avant publication. Ceci n'est pas un avis juridique.</p></div></div>
    <article class="legal-content">
      <p class="legal-updated">État : version de travail · 7 octobre 2026</p>
      <h2>1. Éditeur et champ d'application</h2><p>Le site OverX est édité par <strong>[À COMPLÉTER : identité légale et coordonnées]</strong>. Les présentes conditions sont un brouillon couvrant la consultation des pages et les liens vers les applications Discord.</p>
      <h2>2. Site et disponibilité</h2><p>Le site fournit des informations sur les projets OverX. Il est actuellement statique et ne fournit ni compte utilisateur, ni dashboard, ni API de configuration. Le statut des bots n'est pas vérifié en temps réel depuis ces pages; aucune disponibilité permanente n'est promise.</p>
      <h2>3. Utilisation du bot</h2><p>FreeGameDrop est une application distincte opérant sur Discord. Son utilisation dépend des règles de Discord, des permissions accordées au bot et de la disponibilité des sources d'offres. Les utilisateurs et administrateurs doivent respecter les règles de leur serveur et celles de Discord.</p>
      <h2>4. Informations et services tiers</h2><p>Les offres de jeux proviennent de sources tierces et peuvent évoluer. Les liens vers Discord, GitHub, les boutiques et les fournisseurs de données sont soumis aux conditions de ces services. Les informations du site ne garantissent pas qu'une offre soit encore disponible au moment où elle est consultée.</p>
      <h2>5. Propriété intellectuelle</h2><p>Les droits sur les éléments du site et des bots appartiennent à leurs titulaires respectifs. La licence et les modalités de réutilisation du code sont indiquées dans le dépôt du projet lorsqu'elles sont applicables.</p>
      <h2>6. Contact et modifications</h2><p>Contact de l'éditeur : <strong>[À COMPLÉTER : adresse de contact]</strong>. Ces conditions devront être complétées et révisées avant l'ouverture publique du service. Le droit applicable et la juridiction compétente restent à valider par l'éditeur.</p>
    </article>
  </section>
</main>
""",
    },
    {
        "path": "legal/index.html",
        "title": "Mentions légales — OverX",
        "description": "Mentions légales provisoires du site OverX. Les informations de l'éditeur et de l'hébergeur restent à renseigner.",
        "active": "legal",
        "body": r"""
<main id="main-content">
  <section class="page-hero container legal-hero">
    <p class="eyebrow">INFORMATIONS LÉGALES <span class="crumb-slash">/</span> MENTIONS LÉGALES</p>
    <h1>Qui édite ce site ?<br><span>Informations à renseigner.</span></h1>
    <p class="hero-lead narrow">Les coordonnées légales n'ont pas été fournies. Cette page est volontairement marquée comme incomplète afin de ne pas inventer l'identité de l'éditeur.</p>
  </section>
  <section class="section container legal-layout">
    <div class="draft-warning"><span aria-hidden="true">!</span><div><strong>À compléter avant la mise en ligne publique</strong><p>Renseigne l'identité de l'éditeur et les informations de l'hébergeur avec des données exactes. Fais vérifier les obligations applicables à ton statut.</p></div></div>
    <article class="legal-content">
      <h2>Éditeur du site</h2><ul class="legal-fields"><li><strong>Nom / raison sociale</strong><span>[À COMPLÉTER]</span></li><li><strong>Forme juridique</strong><span>[À COMPLÉTER, le cas échéant]</span></li><li><strong>Adresse</strong><span>[À COMPLÉTER]</span></li><li><strong>Adresse e-mail ou contact</strong><span>[À COMPLÉTER]</span></li><li><strong>Numéro d'immatriculation</strong><span>[À COMPLÉTER si applicable]</span></li><li><strong>Directeur de publication</strong><span>[À COMPLÉTER]</span></li></ul>
      <h2>Hébergement</h2><ul class="legal-fields"><li><strong>Nom de l'hébergeur</strong><span>[À COMPLÉTER après choix du déploiement]</span></li><li><strong>Adresse et contact de l'hébergeur</strong><span>[À COMPLÉTER]</span></li></ul>
      <h2>Propriété intellectuelle</h2><p>Les informations de licence et de réutilisation du code du bot sont à consulter dans le dépôt <a href="https://github.com/TOFazer/FreeGameDropDev" target="_blank" rel="noopener noreferrer">FreeGameDropDev</a>. Les marques, logos et contenus tiers restent la propriété de leurs titulaires.</p>
      <h2>Contact</h2><p>Pour une demande relative au site : <strong>[À COMPLÉTER : moyen de contact vérifié]</strong>.</p>
    </article>
  </section>
</main>
""",
    },
]

NAV_ITEMS = [
    ("Accueil", "index.html", "home"),
    ("Bots", "discord-bots/index.html", "bots"),
    ("Documentation", "docs/index.html", "docs"),
    ("Statut", "status/index.html", "status"),
    ("Roadmap", "roadmap/index.html", "roadmap"),
]


def asset_root(path: str) -> str:
    depth = len(PurePosixPath(path).parent.parts)
    return "../" * depth


def render_nav(root: str, active: str) -> str:
    links = []
    for label, target, key in NAV_ITEMS:
        current = ' aria-current="page"' if key == active else ""
        links.append(f'<a href="{root}{target}"{current}>{label}</a>')
    return "\n        ".join(links)


def render_footer(root: str) -> str:
    return f"""
  <footer class="site-footer">
    <div class="container footer-main">
      <div class="footer-brand-block"><a class="brand" href="{root}index.html" aria-label="OverX — accueil"><img src="{root}assets/brand-mark.svg" alt="" width="34" height="34"><span class="brand-word">OVER<span>X</span><small>DISCORD TOOLS</small></span></a><p>Des outils Discord conçus pour simplifier vos serveurs.</p><a class="footer-github" href="https://github.com/TOFazer/OrvexWebsite" target="_blank" rel="noopener noreferrer">Projet du site sur GitHub <span aria-hidden="true">↗</span></a></div>
      <div class="footer-links"><div><p class="footer-label">EXPLORER</p><a href="{root}discord-bots/index.html">Nos bots</a><a href="{root}install/index.html">Installer FreeGameDrop</a><a href="{root}docs/index.html">Documentation</a><a href="{root}status/index.html">Statut des services</a><a href="{root}changelog/index.html">Changelog</a></div><div><p class="footer-label">COMMUNAUTÉ</p><a href="{root}support/index.html">Support</a><a href="{root}roadmap/index.html">Roadmap</a><a href="https://github.com/TOFazer/FreeGameDropDev" target="_blank" rel="noopener noreferrer">FreeGameDropDev ↗</a></div><div><p class="footer-label">LÉGAL</p><a href="{root}privacy/index.html">Confidentialité</a><a href="{root}terms/index.html">Conditions</a><a href="{root}legal/index.html">Mentions légales</a></div></div>
    </div>
    <div class="container footer-bottom"><span>© <span data-current-year>2026</span> OverX · Projet indépendant</span><span class="footer-transparency"><span class="footer-dot"></span> Pas de statistiques non vérifiées</span></div>
  </footer>
  <div class="sr-only" role="status" aria-live="polite" data-site-announcer></div>
"""


def render_page(page: dict[str, str]) -> str:
    path = page["path"]
    root = asset_root(path)
    title = escape(page["title"], quote=True)
    description = escape(page["description"], quote=True)
    robots = '<meta name="robots" content="noindex,follow">' if path in {"privacy/index.html", "terms/index.html", "legal/index.html"} else ""
    body = page["body"].replace("{{ROOT}}", root).strip()
    nav = render_nav(root, page["active"])
    footer = render_footer(root)
    return f"""<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#090a11">
{robots}
  <meta name="description" content="{description}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="OverX">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <title>{title}</title>
  <link rel="icon" type="image/svg+xml" href="{root}assets/brand-mark.svg">
  <link rel="stylesheet" href="{root}assets/css/site.css">
  <script src="{root}assets/site-config.js" defer></script>
  <script src="{root}assets/js/site.js" defer></script>
</head>
<body>
  <a class="skip-link" href="#main-content">Aller au contenu</a>
  <header class="site-header">
    <div class="container header-inner">
      <a class="brand" href="{root}index.html" aria-label="OverX — accueil"><img src="{root}assets/brand-mark.svg" alt="" width="36" height="36"><span class="brand-word">OVER<span>X</span><small>DISCORD TOOLS</small></span></a>
      <nav class="site-nav" id="primary-nav" data-site-nav aria-label="Navigation principale">
        {nav}
        <a class="mobile-nav-cta" data-install-cta href="{root}install/index.html#ajouter">Guide d'installation</a>
      </nav>
      <div class="header-actions"><a class="button button-header" data-install-cta href="{root}install/index.html#ajouter">Installer FreeGameDrop <span aria-hidden="true">↗</span></a><button class="menu-toggle" type="button" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="primary-nav" data-menu-toggle><span></span><span></span><span></span></button></div>
    </div>
  </header>
{body}
{footer}
</body>
</html>
"""


def main() -> None:
    for page in PAGES:
        destination = ROOT / page["path"]
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(render_page(page), encoding="utf-8")
        print(f"generated {destination.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
