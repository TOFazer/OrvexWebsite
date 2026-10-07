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
      if (event.key === "Escape") {
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
    // Discord Application IDs are public identifiers, not secrets.
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

  const installUrl = getInstallUrl();
  document.querySelectorAll("[data-install-cta]").forEach((link) => {
    if (installUrl) {
      link.href = installUrl;
      link.target = "_blank";
      link.rel = "noopener noreferrer";
      link.removeAttribute("aria-disabled");
      link.removeAttribute("role");
      link.setAttribute("aria-label", "Ajouter FreeGameDrop à un serveur Discord");
      replaceLabel(link, "Ajouter à Discord");
    } else {
      link.href = "#installation";
      link.setAttribute("aria-disabled", "true");
      link.setAttribute("aria-label", "Lien d'installation Discord de FreeGameDrop à configurer");
      link.addEventListener("click", (event) => {
        event.preventDefault();
        if (announcer) announcer.textContent = "Le lien d'installation Discord n'est pas encore configuré. Renseignez l'Application ID publique dans assets/site-config.js.";
      });
      replaceLabel(link, "Lien d'installation à configurer");
    }
  });

  document.querySelectorAll("[data-install-status]").forEach((element) => {
    element.textContent = installUrl
      ? "Invitation Discord configurée. L'ajout se fait sur les serveurs où tu as les permissions nécessaires."
      : "Le lien d'invitation Discord n'a pas encore été communiqué.";
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
