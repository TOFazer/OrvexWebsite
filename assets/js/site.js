(() => {
  "use strict";

  const config = window.OVERX_CONFIG || {};
  const menuButton = document.querySelector("[data-menu-toggle]");
  const nav = document.querySelector("[data-site-nav]");
  const announcer = document.querySelector("[data-site-announcer]");

  if (menuButton && nav) {
    const closeMenu = () => {
      nav.classList.remove("is-open");
      menuButton.setAttribute("aria-expanded", "false");
      menuButton.setAttribute("aria-label", "Ouvrir le menu");
    };

    menuButton.addEventListener("click", () => {
      const isOpen = menuButton.getAttribute("aria-expanded") === "true";
      menuButton.setAttribute("aria-expanded", String(!isOpen));
      menuButton.setAttribute("aria-label", isOpen ? "Ouvrir le menu" : "Fermer le menu");
      nav.classList.toggle("is-open", !isOpen);
    });

    nav.querySelectorAll("a").forEach((link) => link.addEventListener("click", closeMenu));
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && nav.classList.contains("is-open")) {
        closeMenu();
        menuButton.focus();
      }
    });
    document.addEventListener("click", (event) => {
      if (nav.classList.contains("is-open") && !nav.contains(event.target) && !menuButton.contains(event.target)) {
        closeMenu();
      }
    });
  }

  function validDiscordInstallUrl(rawUrl) {
    if (!rawUrl || typeof rawUrl !== "string") return null;
    try {
      const url = new URL(rawUrl);
      if (url.protocol !== "https:" || url.hostname !== "discord.com" || !url.pathname.startsWith("/oauth2/authorize")) return null;
      return url.href;
    } catch {
      return null;
    }
  }

  function getInstallUrl() {
    const suppliedUrl = validDiscordInstallUrl(config.discordInstallUrl);
    if (suppliedUrl) return suppliedUrl;

    const clientId = String(config.discordApplicationId || "").trim();
    // A Discord Application ID is public; bot tokens and OAuth client secrets are not.
    if (!/^\d{17,20}$/.test(clientId)) return null;

    const url = new URL("https://discord.com/oauth2/authorize");
    url.searchParams.set("client_id", clientId);
    url.searchParams.set("permissions", String(config.installPermissions || "268454928"));
    url.searchParams.set("scope", "bot applications.commands");
    return url.href;
  }

  function replaceLabel(element, label) {
    const firstText = Array.from(element.childNodes).find((node) => node.nodeType === Node.TEXT_NODE);
    if (firstText) {
      firstText.nodeValue = `${label} `;
    } else {
      element.prepend(document.createTextNode(`${label} `));
    }
  }

  function enableDiscordLink(element, url) {
    element.href = url;
    element.target = "_blank";
    element.rel = "noopener noreferrer";
    element.removeAttribute("aria-disabled");
    element.removeAttribute("aria-label");
    element.removeAttribute("title");
    element.classList.remove("is-unavailable");
    element.addEventListener("click", () => {
      if (nav?.classList.contains("is-open")) {
        nav.classList.remove("is-open");
        menuButton?.setAttribute("aria-expanded", "false");
      }
    });
  }

  function disableDirectDiscordLink(element) {
    element.href = "#ajouter";
    element.removeAttribute("target");
    element.removeAttribute("rel");
    element.setAttribute("aria-disabled", "true");
    element.setAttribute("aria-label", "Invitation Discord de production à configurer");
    element.setAttribute("title", "Le lien officiel de l'application PROD doit être ajouté par l'équipe OverX.");
    element.classList.add("is-unavailable");
    element.addEventListener("click", (event) => {
      event.preventDefault();
      if (announcer) announcer.textContent = "Le lien d'invitation de production n'est pas encore configuré. Le bouton sera activé dès que l'URL OAuth2 officielle sera ajoutée.";
    });
  }

  const installUrl = getInstallUrl();

  // General install CTAs open Discord directly once the production link is configured.
  // Until then, they lead to a helpful install guide instead of a broken or fake URL.
  document.querySelectorAll("[data-install-cta]").forEach((link) => {
    if (installUrl) {
      enableDiscordLink(link, installUrl);
      link.setAttribute("aria-label", "Ajouter FreeGameDrop à un serveur Discord");
      replaceLabel(link, "Ajouter à Discord");
    } else {
      link.removeAttribute("aria-disabled");
      link.removeAttribute("target");
      link.removeAttribute("rel");
      link.setAttribute("aria-label", "Ouvrir le guide d'installation de FreeGameDrop");
      replaceLabel(link, "Guide d'installation");
    }
  });

  // The prominent button on the install page is the actual OAuth action.
  document.querySelectorAll("[data-discord-install]").forEach((link) => {
    if (installUrl) {
      enableDiscordLink(link, installUrl);
      link.setAttribute("aria-label", "Ajouter FreeGameDrop à un serveur Discord");
      replaceLabel(link, "Ajouter à Discord");
    } else {
      disableDirectDiscordLink(link);
      replaceLabel(link, "Invitation de production à configurer");
    }
  });

  document.querySelectorAll("[data-install-status]").forEach((element) => {
    element.textContent = installUrl
      ? "Le lien officiel d'installation est configuré. Discord te demandera ensuite de choisir le serveur et d'autoriser les permissions."
      : "Le lien OAuth2 de l'application FreeGameDrop PROD n'a pas encore été fourni. Les autres boutons ouvrent ce guide plutôt qu'un lien non vérifié.";
  });

  document.querySelectorAll("[data-copy-admin]").forEach((button) => {
    if (!installUrl) return;
    button.hidden = false;
    button.addEventListener("click", async () => {
      const message = `Peux-tu ajouter FreeGameDrop à notre serveur Discord ? Il faut la permission « Gérer le serveur » pour autoriser l'application. Voici le lien officiel : ${installUrl}`;
      try {
        await navigator.clipboard.writeText(message);
        if (announcer) announcer.textContent = "Message d'installation copié. Tu peux l'envoyer à un administrateur du serveur.";
        button.textContent = "Message copié ✓";
      } catch {
        if (announcer) announcer.textContent = "La copie automatique n'a pas fonctionné. Tu peux partager le lien d'invitation directement.";
      }
    });
  });

  document.querySelectorAll("[data-install-state]").forEach((element) => {
    const textNode = Array.from(element.childNodes).find((node) => node.nodeType === Node.TEXT_NODE);
    if (installUrl) {
      element.classList.remove("status-neutral");
      element.classList.add("status-current");
      if (textNode) textNode.nodeValue = " Invitation prête";
    } else if (textNode) {
      textNode.nodeValue = " Lien de production à configurer";
    }
  });

  document.querySelectorAll("[data-current-year]").forEach((element) => {
    element.textContent = String(new Date().getFullYear());
  });

  const communityUrl = String(config.communityInviteUrl || "").trim();
  if (communityUrl) {
    try {
      const url = new URL(communityUrl);
      if (url.protocol === "https:" && (url.hostname === "discord.gg" || url.hostname === "discord.com")) {
        document.querySelectorAll("[data-community-cta]").forEach((link) => {
          link.href = url.href;
          link.hidden = false;
          link.target = "_blank";
          link.rel = "noopener noreferrer";
        });
      }
    } catch {
      // An invalid public invite stays hidden; never render an untrusted URL.
    }
  }
})();
