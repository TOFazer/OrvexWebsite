/*
 * Public website settings only.
 * Never put DISCORD_TOKEN, DISCORD_CLIENT_SECRET, DATABASE_URL, or other secrets here.
 * Discord Application IDs and invite URLs are public values used for installation links.
 */
window.OVERX_CONFIG = Object.freeze({
  // Set the public Discord Application ID for the production bot to activate install CTAs.
  // Example format: "123456789012345678" — do not use a development app by accident.
  discordApplicationId: "1556443310053130260",

  // Official production install URL supplied by the project owner. It takes precedence over
  // the generated URL below so Discord receives the exact permissions/scopes they selected.
  discordInstallUrl: "https://discord.com/oauth2/authorize?client_id=1556443310053130260&permissions=268528656&integration_type=0&scope=bot+applications.commands",
  installPermissions: "268454928",

  // Optional: public invite to the OverX Discord community; hidden when empty.
  communityInviteUrl: "",

  // Project links (also referenced in page content and README).
  botSourceUrl: "https://github.com/TOFazer/FreeGameDropDev",
  supportUrl: "https://github.com/TOFazer/FreeGameDropDev/issues",
});
