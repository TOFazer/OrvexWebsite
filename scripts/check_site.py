#!/usr/bin/env python3
"""Small standard-library smoke checker for generated site files and local links."""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_PAGES = [
    "index.html",
    "discord-bots/index.html",
    "discord-bots/freegamedrop/index.html",
    "install/index.html",
    "docs/index.html",
    "status/index.html",
    "roadmap/index.html",
    "changelog/index.html",
    "support/index.html",
    "privacy/index.html",
    "terms/index.html",
    "legal/index.html",
]


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.links: list[tuple[str, str]] = []
        self.title_depth = 0
        self.title_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(str(values["id"]))
        if tag == "a" and values.get("href") is not None:
            self.links.append((str(values["href"]), "href"))
        if tag in {"script", "img", "source"} and values.get("src"):
            self.links.append((str(values["src"]), "src"))
        if tag == "link" and values.get("href"):
            self.links.append((str(values["href"]), "href"))
        if tag == "title":
            self.title_depth += 1

    def handle_endtag(self, tag: str) -> None:
        if tag == "title" and self.title_depth:
            self.title_depth -= 1

    def handle_data(self, data: str) -> None:
        if self.title_depth:
            self.title_text.append(data)


def main() -> int:
    errors: list[str] = []
    parsed_pages: dict[Path, PageParser] = {}

    for relative in EXPECTED_PAGES:
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"Missing generated page: {relative}")
            continue
        parser = PageParser()
        parser.feed(path.read_text(encoding="utf-8"))
        parsed_pages[path] = parser
        if not " ".join(parser.title_text).strip():
            errors.append(f"Missing <title>: {relative}")
        if "{{ROOT}}" in path.read_text(encoding="utf-8"):
            errors.append(f"Unexpanded root placeholder: {relative}")

    for source, parser in parsed_pages.items():
        for raw_url, attribute in parser.links:
            url = urlsplit(raw_url)
            if url.scheme or url.netloc or raw_url.startswith(("mailto:", "tel:", "javascript:")):
                continue
            target = (source.parent / unquote(url.path)).resolve() if url.path else source
            if not target.exists():
                errors.append(f"Broken local {attribute} in {source.relative_to(ROOT)}: {raw_url}")
                continue
            if url.fragment and target.suffix.lower() in {".html", ".htm"} and target in parsed_pages:
                if unquote(url.fragment) not in parsed_pages[target].ids:
                    errors.append(f"Missing fragment in {source.relative_to(ROOT)}: {raw_url}")

    config = ROOT / "assets/site-config.js"
    config_text = config.read_text(encoding="utf-8") if config.exists() else ""
    if "DISCORD_TOKEN=" in config_text or "DISCORD_CLIENT_SECRET=" in config_text:
        errors.append("A Discord secret appears in the public site configuration")

    if errors:
        print("Site check failed:")
        for error in errors:
            print(f" - {error}")
        return 1

    print(f"Site check passed: {len(parsed_pages)} crawlable pages, local links and fragments verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
