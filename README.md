<h1 align="center">🎬 ElegantFin Cinema Edition</h1>

<p align="center">
  <img src="https://img.shields.io/github/v/release/peterdu1109/ElegantFin?label=version&color=red&cacheSeconds=3600" alt="Version">
  <img src="https://img.shields.io/badge/Jellyfin-12.x%20%7C%2010.11.x-blueviolet" alt="Jellyfin">
  <img src="https://img.shields.io/badge/platform-Desktop%20%7C%20Mobile%20%7C%20TV-green" alt="Platforms">
  <a href="https://github.com/lscambo13/ElegantFin"><img src="https://img.shields.io/badge/based%20on-ElegantFin%20v26.09.05-blue" alt="Based on ElegantFin"></a>
  <img src="https://img.shields.io/badge/license-GPL--2.0-green" alt="License">
  <a href="https://www.jsdelivr.com/package/gh/peterdu1109/ElegantFin"><img src="https://img.shields.io/jsdelivr/gh/hm/peterdu1109/ElegantFin?label=CDN%20hits&color=orange" alt="jsDelivr"></a>
  <img src="https://img.shields.io/github/release-date/peterdu1109/ElegantFin?color=orange&cacheSeconds=3600" alt="Last release">
</p>

<p align="center">
  <b>A cinematic, streaming-inspired theme for Jellyfin — on desktop, mobile and TV.</b><br>
  <i>Un thème Jellyfin cinématique, inspiré du streaming — sur PC, téléphone et TV.</i>
</p>

---

<p align="center">
  <b>🌐 Language / Langue</b><br>
  <a href="#english">English</a> | <a href="#français">Français</a>
</p>

---

<a name="english"></a>
# English

ElegantFin Cinema Edition is a fork of [ElegantFin](https://github.com/lscambo13/ElegantFin) by [lscambo13](https://github.com/lscambo13), reworked into a full streaming-style experience: cinematic detail pages, polished cards, a remote-friendly TV interface and dedicated styling for popular plugins. One line of CSS, and every device connected to your server gets it.

> 📖 **Changelog & version history:** see [GitHub Releases](https://github.com/peterdu1109/ElegantFin/releases) for what's new in each version, and [`RELEASE_NOTES.md`](./RELEASE_NOTES.md) for every detail.

## 📑 Table of Contents

- [🚀 Quick Start](#-quick-start)
- [✨ Key Features](#-key-features)
- [📦 Installation](#-installation)
- [⚙️ Customization](#️-customization)
- [📱 Compatibility](#-compatibility)
- [🔌 Supported Plugins](#-supported-plugins)
- [❓ Troubleshooting](#-troubleshooting)
- [🔔 Recommended Plugin](#-recommended-plugin)
- [👥 Authors & Credits](#-authors--credits)

## 🚀 Quick Start

1. Open **Dashboard → Branding**.
2. Paste this line into **Custom CSS code**, then **Save**:
   ```css
   @import url("https://cdn.jsdelivr.net/gh/peterdu1109/ElegantFin@main/Theme/ElegantFin-jellyfin-theme-build-latest-minified.css");
   ```
3. Reload the page (`Ctrl+F5`). On a TV, close and reopen the Jellyfin app.

That's it — every browser, phone and TV connected to your server now uses the theme.

## ✨ Key Features

*   **Made for Jellyfin 12** — The new desktop and mobile interface gets the full cinema look: library pills in the top bar, the theme's purple instead of Jellyfin blue, every page and plugin restyled. Jellyfin 10.11 is still supported.
*   **Cinematic detail pages** — Full-bleed backdrops, title logos, light typography, a white Play button, and media info laid out in clean panels.
*   **Streaming-style cards** — Rounded posters, a gentle zoom and light border on hover, glass badges for counts and quality, a soft veil on what you've already watched.
*   **Built for the couch** — On TV, every control gets a clear white focus. Card zoom and row dimming wait until you stop moving, so fast scrolling stays smooth. Menus stay readable over bright video, and the header gets a navy veil as you scroll a detail page, and the home tabs never slide under the header icons.
*   **Light on TVs** — No blur, no drop shadows, no looping animations on TV layouts. Every TV change is measured on a real Samsung TV (Tizen) and an Android TV box before release.
*   **Phones too** — Rows that settle on a card, a readable layout in portrait and landscape, and the same top bar as on desktop when the phone is turned sideways.
*   **Polished everyday details** — Glass dialogs and menus, a modern video player bar, thin scrollbars, drop-down lists that never hide their text under the arrow, round "Who's watching?" avatars on the login screen.
*   **Plugin-aware** — Dedicated styling for Jellyfin Enhanced, Media Carousel, Editor's Choice, Media Bar and Home Screen Sections, so they look like part of the theme.
*   **Self-hosted fonts** — Inter and Material Icons ship with the theme. Nothing is loaded from Google, and the theme file itself is about 150 KB.
*   **Graceful on older devices** — Modern effects come with fallbacks: an older TV or browser keeps a clean, working interface instead of a broken one.
*   **Accessible** — `prefers-reduced-motion` is respected: animations switch off when the system asks for it.

## 📦 Installation

> [!IMPORTANT]
> **Prerequisites:**
> * Jellyfin **12.x** (10.11.x is still supported)
> * Server-side installation reaches **every client**, TV apps included. Client-side installation only applies to your own account.

### Server-side (recommended)

1.  Open the **Dashboard** from the avatar menu, top right (on Jellyfin 10.11: Settings → Administration).
2.  Go to **Branding** and scroll down to **Custom CSS code**.
3.  Paste the import line from [Quick Start](#-quick-start) and click **Save**.
4.  Reload your browser (`Ctrl+F5`). On TVs, close and reopen the Jellyfin app.

### Client-side

1.  Open **Settings → Display**.
2.  Scroll down to **Custom CSS code**, paste the import line, and click **Save**.

### 📌 Pin a version

`@main` always follows the latest version. To update on your own schedule, replace `@main` with a version tag, for example:

```css
@import url("https://cdn.jsdelivr.net/gh/peterdu1109/ElegantFin@v1.4.4/Theme/ElegantFin-jellyfin-theme-build-latest-minified.css");
```

A pinned version never changes, so it is also the fastest way to get an update on a TV app that keeps the previous file in cache. Versions follow `X.Y.Z`: the last number for fixes, the middle one when a batch of work closes.

### 🗑️ Uninstall

Delete the `@import` line from **Custom CSS code** and click **Save**: Jellyfin goes back to its original look on the next reload (`Ctrl+F5`, or reopen the app on a TV).

## ⚙️ Customization

These options come from the original ElegantFin. Add your overrides **after** the import line:

```css
:root {
    --clearLogoVisibility: none;
}
```

| Option | Variable | Values |
|--------|----------|--------|
| **Login background** | `--loginPageBgUrl` | `url("your-server/Branding/Splashscreen...")` |
| **Play button on cards** | `--overlayPlayButtonPosition` | `50%` (center) / `-999em` (hidden) |
| **Card hover effect** | `--cardHoverEffect` | `""` (enabled) / `none` (disabled) |
| **Library labels** | `--libraryLabelVisibility` | `block` / `none` |
| **Extra card buttons** | `--extraCardButtonsVisibility` | `block` / `none` |
| **App bar style (TV and Jellyfin 10.11)** | `--appBarHeight` | `5em` (fading) / `4.6em` (solid) |
| **Original title** | `--itemOriginalTitleVisibility` | `block` / `none` |
| **Title logo** | `--clearLogoVisibility` | `block` / `none` |
| **Critics rating on phones** | `--criticsRatingVisibility` | `none` (hidden) / `block` |
| **Icon pack (LG TV fix)** | `--iconPack` | `'Material Icons'` |
| **Color themes** | See the [Playground](https://github.com/lscambo13/ElegantFin/discussions/221) | Partly: backgrounds and borders change, the theme's purple accent stays |

## 📱 Compatibility

| Platform | Status |
|----------|--------|
| **Jellyfin Server 12** | Fully supported — main target |
| **Jellyfin Server 10.11** | Supported |
| **Web browsers** (Chrome, Edge, Firefox) | Fully supported |
| **Safari** | Should work, not tested |
| **Jellyfin Android app** | Fully supported |
| **Samsung Tizen** (Jellyfin community app) | Supported, field-tested; older models fall back gracefully |
| **Android TV apps based on the Jellyfin web interface** | Supported, field-tested on an Android TV box |
| **LG webOS** | Should work, not tested (may need the icon pack option) |
| **Jellyfin Media Player** (older web engine) | Not tested, may look simpler |
| **Android TV native app** | Not supported (it doesn't load custom CSS) |

## 🔌 Supported Plugins

The theme adds dedicated styling for these plugins:

| Plugin | What it does | Cinema styling |
|--------|--------------|----------------|
| [**Jellyfin Enhanced**](https://github.com/n00bcodr/Jellyfin-Enhanced) | Shortcuts, Jellyseerr requests, reviews, extra links | Letterboxd and Seerr icons in line with the other logos, "where to watch" bar, Seerr badges and active streams button in the theme's colours, reviews that stay inside the page |
| [**Media Carousel**](https://github.com/peterdu1109/MediaCarousel) | Streaming-style home rows: server Top 10, worldwide Top 10, Seerr requests | Row arrows centred on the posters, like the other rows |
| [**Editor's Choice**](https://github.com/lachlandcp/jellyfin-editors-choice-plugin) | Curated picks on the home page | Banner spacing, readable description, working scroll and pause controls, aspect-safe title logo |
| [**Media Bar**](https://github.com/IAmParadox27/jellyfin-plugin-media-bar) | Auto-cycling slideshow at the top of home | Gradient overlay, readable synopsis, polished buttons |
| [**Home Screen Sections**](https://github.com/IAmParadox27/jellyfin-plugin-home-sections) | Extra curated rows on the home page | Readable Top 10 numbers, Discover badges in the theme accent |

A plugin that isn't listed works with its own styling — the theme just doesn't add anything to it.

## ❓ Troubleshooting

| Issue | Solution |
|-------|----------|
| **The theme doesn't show** | Check that the `@import` line is the **first** line of the Custom CSS field, click **Save**, then `Ctrl+F5`. |
| **A TV still shows the previous version** | Close and reopen the Jellyfin app. If it persists, [pin a version](#-pin-a-version): a new URL can't come from the cache. |
| **`@main` hasn't updated yet** | The CDN can take a few hours (up to 12 h) to refresh `@main`. Pin the new version tag to get it right away. |
| **Square icons on an LG TV** | Add `--iconPack: 'Material Icons';` in a `:root { }` block after the import. |
| **No arrows on the home tabs in Firefox** | Expected: those arrows need a recent Chrome or Edge. Firefox keeps a thin scrollbar under the tabs. |
| **Something looks off on an old TV or in Jellyfin Media Player** | Their web engine is older; the theme falls back to a simpler look there. Open an issue with a screenshot if something is actually broken. |
| **A plugin doesn't look like the rest** | Only the [plugins listed above](#-supported-plugins) are styled. Open an issue to suggest another one. |

## 🔔 Recommended Plugin

ElegantFin Cinema Edition pairs with [**NotifySync**](https://github.com/peterdu1109/NotifySync), a real-time notification bell for Jellyfin: the latest additions in a glass dropdown that follows the theme's colours.

> ⭐ Install both for a complete streaming-style Jellyfin, with new content announced as soon as it arrives.

## 👥 Authors & Credits

- **Original theme:** [ElegantFin](https://github.com/lscambo13/ElegantFin) by [lscambo13](https://github.com/lscambo13)
- **Cinema Edition:** [ElieMFR](https://github.com/ElieMFR)

Bug reports and suggestions are welcome on [GitHub](https://github.com/peterdu1109/ElegantFin/issues).

Released under the [GPL-2.0 License](./LICENSE), like the original theme.

---

<a name="français"></a>
# Français

ElegantFin Cinema Edition est une déclinaison d'[ElegantFin](https://github.com/lscambo13/ElegantFin) de [lscambo13](https://github.com/lscambo13), retravaillée en une vraie expérience façon streaming : fiches cinématiques, cartes soignées, une interface TV pensée pour la télécommande et un habillage dédié aux plugins populaires. Une ligne de CSS, et tous les appareils connectés à votre serveur en profitent.

> 📖 **Nouveautés & historique :** voir les [Releases GitHub](https://github.com/peterdu1109/ElegantFin/releases) pour ce qu'apporte chaque version, et [`RELEASE_NOTES.md`](./RELEASE_NOTES.md) pour tous les détails.

## 📑 Sommaire

- [🚀 Démarrage rapide](#-démarrage-rapide)
- [✨ Fonctionnalités](#-fonctionnalités)
- [📦 Installation](#-installation-1)
- [⚙️ Personnalisation](#️-personnalisation)
- [📱 Compatibilité](#-compatibilité)
- [🔌 Plugins pris en charge](#-plugins-pris-en-charge)
- [❓ Dépannage](#-dépannage)
- [🔔 Plugin recommandé](#-plugin-recommandé)
- [👥 Auteurs & Crédits](#-auteurs--crédits)

## 🚀 Démarrage rapide

1. Ouvrez **Tableau de bord → Slogan** (la page Branding porte ce nom dans Jellyfin en français).
2. Collez cette ligne dans **Code CSS personnalisé**, puis **Sauvegarder** :
   ```css
   @import url("https://cdn.jsdelivr.net/gh/peterdu1109/ElegantFin@main/Theme/ElegantFin-jellyfin-theme-build-latest-minified.css");
   ```
3. Rechargez la page (`Ctrl+F5`). Sur une TV, fermez puis rouvrez l'appli Jellyfin.

C'est tout : tous les navigateurs, téléphones et TV connectés à votre serveur utilisent désormais le thème.

## ✨ Fonctionnalités

*   **Pensé pour Jellyfin 12** — La nouvelle interface PC et mobile prend tout le style cinéma : pastilles de bibliothèques dans la barre du haut, violet du thème au lieu du bleu Jellyfin, chaque page et chaque plugin rhabillés. Jellyfin 10.11 reste pris en charge.
*   **Fiches cinématiques** — Images de fond en pleine page, logos des titres, typographie légère, bouton Lire blanc, et infos média rangées dans des panneaux nets.
*   **Cartes façon streaming** — Affiches arrondies, léger zoom et liseré éclairci au survol, pastilles en verre pour le nombre d'épisodes et la qualité, voile discret sur ce que vous avez déjà vu.
*   **Pensé pour le canapé** — Sur TV, chaque élément a un focus blanc bien visible. Le zoom des cartes et l'atténuation de la rangée attendent que vous vous arrêtiez : le défilement rapide reste fluide. Les menus restent lisibles sur une vidéo claire, et l'en-tête prend un voile bleu nuit quand on descend dans une fiche, et les onglets de l'accueil ne passent jamais sous les icônes.
*   **Léger sur TV** — Ni flou, ni ombre portée, ni animation en boucle en disposition TV. Chaque changement TV est mesuré sur une vraie TV Samsung (Tizen) et une box Android TV avant publication.
*   **Aussi sur téléphone** — Rangées qui s'arrêtent sur une carte, mise en page lisible en portrait comme en paysage, et la même barre du haut que sur PC quand le téléphone est tourné.
*   **Les détails du quotidien** — Fenêtres et menus en verre, barre du lecteur vidéo moderne, barres de défilement fines, listes déroulantes dont le texte ne passe jamais sous la flèche, avatars ronds « Qui regarde ? » à la connexion.
*   **Attentif aux plugins** — Un habillage dédié pour Jellyfin Enhanced, Media Carousel, Editor's Choice, Media Bar et Home Screen Sections, pour qu'ils fassent partie du thème.
*   **Polices intégrées** — Inter et Material Icons sont livrées avec le thème. Rien n'est chargé depuis Google, et le fichier du thème pèse environ 150 Ko.
*   **Sans casse sur les anciens appareils** — Les effets récents ont un repli : une ancienne TV ou un vieux navigateur garde une interface propre et fonctionnelle.
*   **Accessible** — `prefers-reduced-motion` est respecté : les animations se coupent quand le système le demande.

## 📦 Installation

> [!IMPORTANT]
> **Prérequis :**
> * Jellyfin **12.x** (10.11.x reste pris en charge)
> * L'installation côté serveur atteint **tous les clients**, applis TV comprises. L'installation côté client ne vaut que pour votre compte.

### Côté serveur (recommandé)

1.  Ouvrez le **Tableau de bord** depuis le menu de l'avatar, en haut à droite (sur Jellyfin 10.11 : Paramètres → Administration).
2.  Allez dans **Slogan** (Branding), puis descendez jusqu'à **Code CSS personnalisé**.
3.  Collez la ligne d'import du [Démarrage rapide](#-démarrage-rapide) et cliquez sur **Sauvegarder**.
4.  Rechargez le navigateur (`Ctrl+F5`). Sur les TV, fermez puis rouvrez l'appli Jellyfin.

### Côté client

1.  Ouvrez **Paramètres → Affichage**.
2.  Descendez jusqu'à **Code CSS personnalisé**, collez la ligne d'import et cliquez sur **Sauvegarder**.

### 📌 Figer une version

`@main` suit toujours la dernière version. Pour mettre à jour quand vous le décidez, remplacez `@main` par un numéro de version, par exemple :

```css
@import url("https://cdn.jsdelivr.net/gh/peterdu1109/ElegantFin@v1.4.4/Theme/ElegantFin-jellyfin-theme-build-latest-minified.css");
```

Une version figée ne change jamais : c'est aussi le moyen le plus rapide de faire passer une mise à jour sur une appli TV qui garde l'ancien fichier en cache. Les versions suivent `X.Y.Z` : le dernier chiffre pour les correctifs, celui du milieu quand un ensemble de travaux se referme.

### 🗑️ Désinstaller

Supprimez la ligne `@import` du **Code CSS personnalisé** et cliquez sur **Sauvegarder** : Jellyfin retrouve son apparence d'origine au prochain rechargement (`Ctrl+F5`, ou en rouvrant l'appli sur une TV).

## ⚙️ Personnalisation

Ces options viennent d'ElegantFin d'origine. Ajoutez vos réglages **après** la ligne d'import :

```css
:root {
    --clearLogoVisibility: none;
}
```

| Option | Variable | Valeurs |
|--------|----------|---------|
| **Fond de la page de connexion** | `--loginPageBgUrl` | `url("votre-serveur/Branding/Splashscreen...")` |
| **Bouton Lire sur les cartes** | `--overlayPlayButtonPosition` | `50%` (centré) / `-999em` (masqué) |
| **Effet au survol des cartes** | `--cardHoverEffect` | `""` (activé) / `none` (désactivé) |
| **Noms des bibliothèques** | `--libraryLabelVisibility` | `block` / `none` |
| **Boutons supplémentaires des cartes** | `--extraCardButtonsVisibility` | `block` / `none` |
| **Style de la barre du haut (TV et Jellyfin 10.11)** | `--appBarHeight` | `5em` (en fondu) / `4.6em` (pleine) |
| **Titre original** | `--itemOriginalTitleVisibility` | `block` / `none` |
| **Logo du titre** | `--clearLogoVisibility` | `block` / `none` |
| **Note critique sur téléphone** | `--criticsRatingVisibility` | `none` (masquée) / `block` |
| **Pack d'icônes (TV LG)** | `--iconPack` | `'Material Icons'` |
| **Thèmes de couleurs** | Voir le [Playground](https://github.com/lscambo13/ElegantFin/discussions/221) | En partie : fonds et bordures changent, le violet du thème reste |

## 📱 Compatibilité

| Plateforme | État |
|------------|------|
| **Serveur Jellyfin 12** | Entièrement pris en charge — cible principale |
| **Serveur Jellyfin 10.11** | Pris en charge |
| **Navigateurs web** (Chrome, Edge, Firefox) | Entièrement pris en charge |
| **Safari** | Devrait fonctionner, non testé |
| **Appli Android Jellyfin** | Entièrement prise en charge |
| **Samsung Tizen** (appli communautaire Jellyfin) | Prise en charge, éprouvée sur matériel réel ; repli propre sur les anciens modèles |
| **Applis Android TV basées sur l'interface web de Jellyfin** | Prises en charge, testées sur une box Android TV |
| **LG webOS** | Devrait fonctionner, non testé (l'option pack d'icônes peut être nécessaire) |
| **Jellyfin Media Player** (moteur web plus ancien) | Non testé, rendu possiblement plus simple |
| **Appli native Android TV** | Non prise en charge (elle ne charge pas de CSS personnalisé) |

## 🔌 Plugins pris en charge

Le thème ajoute un habillage dédié à ces plugins :

| Plugin | Ce qu'il fait | Habillage Cinema |
|--------|---------------|------------------|
| [**Jellyfin Enhanced**](https://github.com/n00bcodr/Jellyfin-Enhanced) | Raccourcis, demandes Jellyseerr, avis, liens supplémentaires | Icônes Letterboxd et Seerr alignées sur les autres logos, bandeau « où regarder », badges Seerr et bouton des lectures en cours aux couleurs du thème, avis qui restent dans la page |
| [**Media Carousel**](https://github.com/peterdu1109/MediaCarousel) | Rangées d'accueil façon streaming : Top 10 du serveur, Top 10 mondial, demandes Seerr | Flèches des rangées centrées sur les affiches, comme les autres rangées |
| [**Editor's Choice**](https://github.com/lachlandcp/jellyfin-editors-choice-plugin) | Sélection éditoriale sur l'accueil | Espacement de la bannière, résumé lisible, contrôles de défilement et de pause fonctionnels, logo de titre au ratio préservé |
| [**Media Bar**](https://github.com/IAmParadox27/jellyfin-plugin-media-bar) | Diaporama défilant en haut de l'accueil | Dégradé d'arrière-plan, résumé lisible, boutons soignés |
| [**Home Screen Sections**](https://github.com/IAmParadox27/jellyfin-plugin-home-sections) | Rangées éditoriales supplémentaires sur l'accueil | Numéros du Top 10 lisibles, badges Découvrir à la couleur du thème |

Un plugin absent de la liste fonctionne avec son propre habillage : le thème ne lui ajoute simplement rien.

## ❓ Dépannage

| Problème | Solution |
|----------|----------|
| **Le thème ne s'affiche pas** | Vérifiez que la ligne `@import` est la **première** ligne du champ CSS personnalisé, cliquez sur **Sauvegarder**, puis `Ctrl+F5`. |
| **Une TV affiche encore l'ancienne version** | Fermez puis rouvrez l'appli Jellyfin. Si ça persiste, [figez une version](#-figer-une-version) : une nouvelle adresse ne peut pas venir du cache. |
| **`@main` n'est pas encore à jour** | Le CDN peut mettre quelques heures (jusqu'à 12 h) à rafraîchir `@main`. Figez le nouveau numéro de version pour l'avoir tout de suite. |
| **Icônes carrées sur une TV LG** | Ajoutez `--iconPack: 'Material Icons';` dans un bloc `:root { }` après l'import. |
| **Pas de flèches sur les onglets de l'accueil dans Firefox** | Normal : ces flèches demandent un Chrome ou un Edge récent. Firefox garde une fine barre de défilement sous les onglets. |
| **Un détail cloche sur une ancienne TV ou dans Jellyfin Media Player** | Leur moteur web est plus ancien ; le thème y passe à un rendu plus simple. Ouvrez une issue avec une capture si quelque chose est vraiment cassé. |
| **Un plugin ne ressemble pas au reste** | Seuls les [plugins listés plus haut](#-plugins-pris-en-charge) sont habillés. Ouvrez une issue pour en proposer un autre. |

## 🔔 Plugin recommandé

ElegantFin Cinema Edition va de pair avec [**NotifySync**](https://github.com/peterdu1109/NotifySync), une cloche de notifications en temps réel pour Jellyfin : les derniers ajouts dans un menu en verre aux couleurs du thème.

> ⭐ Installez les deux pour un Jellyfin complet façon streaming, avec les nouveautés annoncées dès leur arrivée.

## 👥 Auteurs & Crédits

- **Thème original :** [ElegantFin](https://github.com/lscambo13/ElegantFin) par [lscambo13](https://github.com/lscambo13)
- **Édition Cinéma :** [ElieMFR](https://github.com/ElieMFR)

Signalements de bugs et suggestions bienvenus sur [GitHub](https://github.com/peterdu1109/ElegantFin/issues).

Distribué sous [licence GPL-2.0](./LICENSE), comme le thème d'origine.
