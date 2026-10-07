/*
 * Public website settings only.
 * Never put DISCORD_TOKEN, DISCORD_CLIENT_SECRET, DATABASE_URL, or other secrets here.
 * Discord Application IDs and invite URLs are public values used for installation links.
 */
window.OVERX_CONFIG = Object.freeze({
  // Set the public Discord Application ID for the production bot to activate install CTAs.
  // Example format: "123456789012345678" — do not use a development app by accident.
  discordApplicationId: "",

  // Optional: supply a complete HTTPS Discord OAuth install URL instead of building one.
  discordInstallUrl: "",
  installPermissions: "268454928",

  // Optional: public invite to the OverX Discord community; hidden when empty.
  communityInviteUrl: "",

  // Project links (also referenced in page content and README).
  botSourceUrl: "https://github.com/TOFazer/FreeGameDropDev",
  supportUrl: "https://github.com/TOFazer/FreeGameDropDev/issues",
});
