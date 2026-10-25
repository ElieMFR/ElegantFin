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
  <b>A streaming-inspired Jellyfin theme, on PC, mobile and TV.</b><br>
  <i>Un thème Jellyfin inspiré du streaming, sur PC, téléphone et TV.</i>
</p>

---

<p align="center">
  <b>🌐 Language / Langue</b><br>
  <a href="#english">English</a> | <a href="#français">Français</a>
</p>

---

<a name="english"></a>
# English

ElegantFin Cinema Edition is a Jellyfin theme inspired by streaming platforms, based on [ElegantFin](https://github.com/lscambo13/ElegantFin) by [lscambo13](https://github.com/lscambo13). One line of CSS on the server, and every device gets it: PC, phone and TV.

> 📖 **Version history:** see [GitHub Releases](https://github.com/peterdu1109/ElegantFin/releases) for what's new in each version, and [`RELEASE_NOTES.md`](./RELEASE_NOTES.md) for every detail.

## 📑 Table of Contents

- [✨ Key Features](#-key-features)
- [📦 Installation](#-installation)
- [⚙️ Customization](#️-customization)
- [📱 Compatibility](#-compatibility)
- [🔌 Supported Plugins](#-supported-plugins)
- [❓ Troubleshooting](#-troubleshooting)
- [🔔 Recommended Plugin](#-recommended-plugin)
- [👥 Authors & Credits](#-authors--credits)

## ✨ Key Features

*   **Made for Jellyfin 12**: the new PC and phone interface gets the full look, with library pills in the top bar and the theme's purple instead of Jellyfin blue.
*   **Detail pages**: full-screen backdrops, title logos, a white Play button, media info in clean panels.
*   **Cards**: rounded posters, a light zoom on hover, glass badges, a soft veil on what you've already watched.
*   **TV**: a clear white focus on every control. The zoom waits until you stop moving, so fast scrolling stays smooth. The home tabs never slide under the header icons.
*   **Light on TV**: no blur, no drop shadows, no looping animations. Every TV change is measured on a Samsung TV and an Android TV box.
*   **Phones**: rows that stop on a card, readable in portrait and landscape, and the same top bar as on PC when the phone is turned sideways.
*   **Details**: glass dialogs and menus, a modern player bar, thin scrollbars, drop-down lists whose text never hides under the arrow.
*   **Plugins**: dedicated styling for Jellyfin Enhanced, Media Carousel, Editor's Choice, Media Bar and Home Screen Sections.
*   **Fonts included**: Inter and Material Icons ship with the theme, nothing is loaded from Google. The theme file is about 150 KB.
*   **Older devices**: recent effects have a fallback, so an old TV or browser keeps a clean interface.
*   **Accessible**: animations switch off when the system asks for reduced motion.

## 📦 Installation

> [!IMPORTANT]
> **Requirements:**
> * Jellyfin **12.x**
> * Jellyfin **10.11.x**
>
> Installed on the server, the theme reaches every client, TV apps included.

### Steps
1.  Open the **Dashboard** from the avatar menu, top right (Jellyfin 10.11: Settings → Administration).
2.  Go to **Branding** and scroll down to **Custom CSS code**.
3.  Paste this line, then click **Save**:
    ```css
    @import url("https://cdn.jsdelivr.net/gh/peterdu1109/ElegantFin@main/Theme/ElegantFin-jellyfin-theme-build-latest-minified.css");
    ```
4.  Reload the page (`Ctrl+F5`). On a TV, close and reopen the Jellyfin app.

**For your account only:** paste the same line in **Settings → Display → Custom CSS code**.

### 📌 Pin a version

`@main` always follows the latest version. To update when you choose, replace `@main` with a version number:

```css
@import url("https://cdn.jsdelivr.net/gh/peterdu1109/ElegantFin@v1.5.1/Theme/ElegantFin-jellyfin-theme-build-latest-minified.css");
```

A pinned version never changes. It is also the fastest way to update a TV app that keeps the old file in cache.

### 🗑️ Uninstall

Delete the `@import` line, click **Save**, then reload (`Ctrl+F5`, or reopen the app on a TV).

## ⚙️ Customization

Most of these options come from the original ElegantFin. Add them **after** the import line:

```css
:root {
    --clearLogoVisibility: none;
}
```

| Option | Variable | Values |
|--------|----------|--------|
| **Login background** | `--loginPageBgUrl` | `url("your-server/Branding/Splashscreen...")` |
| **Play button on cards** | `--overlayPlayButtonPosition` | `50%` (center) / `-999em` (hidden) |
| **Card hover effect** | `--cardHoverEffect` | `""` (on) / `none` (off) |
| **Library labels** | `--libraryLabelVisibility` | `block` / `none` |
| **Watched and favorite buttons on cards (PC)** | `--extraCardButtonsVisibility` | `none` (hidden) / `block` |
| **Top bar height (TV and Jellyfin 10.11)** | `--appBarHeight` | `5em` (default) or another height |
| **Original title** | `--itemOriginalTitleVisibility` | `block` / `none` |
| **Title logo** | `--clearLogoVisibility` | `block` / `none` |
| **Critics rating on phones** | `--criticsRatingVisibility` | `none` (hidden) / `block` |
| **Icons (LG TV)** | `--iconPack` | `'Material Icons'` |
| **Jellyfin Enhanced tabs (PC and phone)** | `--jeTabsVisibility` | `inline-flex` (tabs under the bar) / `none` (icons at the top right) |
| **Color themes** | See the [Playground](https://github.com/lscambo13/ElegantFin/discussions/221) | Partly: backgrounds and borders change, the purple stays |

## 📱 Compatibility

| Platform | Status |
|----------|--------|
| **Jellyfin 12** | Main target |
| **Jellyfin 10.11** | Supported |
| **Chrome, Edge, Firefox** | Supported |
| **Safari** | Should work, not tested |
| **Jellyfin Android app** | Supported |
| **Samsung Tizen** (community app) | Supported, tested on a real TV |
| **Android TV apps based on the Jellyfin web interface** | Supported, tested on an Android TV box |
| **LG webOS** | Should work, not tested (may need the icon option) |
| **Jellyfin Media Player** | Not tested |
| **Native Android TV app** | Not supported: it doesn't load custom CSS |

## 🔌 Supported Plugins

| Plugin | What it does | Theme styling |
|--------|--------------|---------------|
| [**Jellyfin Enhanced**](https://github.com/n00bcodr/Jellyfin-Enhanced) | Shortcuts, Jellyseerr requests, reviews, extra links | Letterboxd and Seerr icons in line, "where to watch" bar, badges and active streams button in the theme's colours |
| [**Media Carousel**](https://github.com/peterdu1109/MediaCarousel) | Home rows: server Top 10, worldwide Top 10, Seerr requests | Row arrows centred on the posters |
| [**Editor's Choice**](https://github.com/lachlandcp/jellyfin-editors-choice-plugin) | Curated picks on the home page | Banner spacing, readable description, working controls |
| [**Media Bar**](https://github.com/IAmParadox27/jellyfin-plugin-media-bar) | Slideshow at the top of home | Gradient, readable synopsis, buttons |
| [**Home Screen Sections**](https://github.com/IAmParadox27/jellyfin-plugin-home-sections) | Extra rows on the home page | Readable Top 10 numbers, badges in the theme's colour |

Other plugins keep their own look.

## ❓ Troubleshooting

| Issue | Solution |
|-------|----------|
| **The theme doesn't show** | The `@import` line must be the **first** line of the field. Click **Save**, then `Ctrl+F5`. |
| **A TV still shows the old version** | Close and reopen the app. If it persists, [pin a version](#-pin-a-version). |
| **`@main` hasn't updated yet** | The CDN can take a few hours (up to 12 h). Pin the new version to get it right away. |
| **Square icons on an LG TV** | Add `--iconPack: 'Material Icons';` in a `:root { }` block after the import. |
| **No arrows on the home tabs in Firefox** | Normal: these arrows need a recent Chrome or Edge. Firefox keeps a thin scrollbar. |
| **A plugin doesn't match the rest** | Only the [plugins listed above](#-supported-plugins) are styled. Open an issue to suggest one. |

## 🔔 Recommended Plugin

ElegantFin Cinema Edition goes well with [**NotifySync**](https://github.com/peterdu1109/NotifySync), a notification bell for Jellyfin in the theme's colours. Both work together on PC, mobile and TV.

## 👥 Authors & Credits

- **Original theme:** [ElegantFin](https://github.com/lscambo13/ElegantFin) by [lscambo13](https://github.com/lscambo13)
- **Cinema Edition:** [ElieMFR](https://github.com/ElieMFR)

Bug reports and suggestions are welcome on [GitHub](https://github.com/peterdu1109/ElegantFin/issues).

Released under the [GPL-2.0 License](./LICENSE), like the original theme.

---

<a name="français"></a>
# Français

ElegantFin Cinema Edition est un thème Jellyfin inspiré des plateformes de streaming, basé sur [ElegantFin](https://github.com/lscambo13/ElegantFin) de [lscambo13](https://github.com/lscambo13). Une ligne de CSS sur le serveur, et tous les appareils en profitent : PC, téléphone et TV.

> 📖 **Historique des versions :** voir les [Releases GitHub](https://github.com/peterdu1109/ElegantFin/releases) pour les nouveautés de chaque version, et [`RELEASE_NOTES.md`](./RELEASE_NOTES.md) pour tous les détails.

## 📑 Sommaire

- [✨ Fonctionnalités](#-fonctionnalités)
- [📦 Installation](#-installation-1)
- [⚙️ Personnalisation](#️-personnalisation)
- [📱 Compatibilité](#-compatibilité)
- [🔌 Plugins pris en charge](#-plugins-pris-en-charge)
- [❓ Dépannage](#-dépannage)
- [🔔 Plugin recommandé](#-plugin-recommandé)
- [👥 Auteurs & Crédits](#-auteurs--crédits)

## ✨ Fonctionnalités

*   **Pensé pour Jellyfin 12** : la nouvelle interface PC et mobile prend tout le style, avec les pastilles de bibliothèques dans la barre du haut et le violet du thème au lieu du bleu Jellyfin.
*   **Fiches** : images de fond en plein écran, logos des titres, bouton Lire blanc, infos média dans des panneaux nets.
*   **Cartes** : affiches arrondies, léger zoom au survol, pastilles en verre, voile discret sur ce que vous avez déjà vu.
*   **TV** : un focus blanc bien visible sur chaque élément. Le zoom attend que vous vous arrêtiez, le défilement rapide reste donc fluide. Les onglets de l'accueil ne passent jamais sous les icônes.
*   **Léger sur TV** : ni flou, ni ombre portée, ni animation en boucle. Chaque changement TV est mesuré sur une TV Samsung et une box Android TV.
*   **Téléphone** : rangées qui s'arrêtent sur une carte, lisible en portrait comme en paysage, et la même barre du haut que sur PC quand le téléphone est tourné.
*   **Détails** : fenêtres et menus en verre, barre du lecteur moderne, barres de défilement fines, listes déroulantes dont le texte ne passe jamais sous la flèche.
*   **Plugins** : un habillage dédié pour Jellyfin Enhanced, Media Carousel, Editor's Choice, Media Bar et Home Screen Sections.
*   **Polices incluses** : Inter et Material Icons sont livrées avec le thème, rien n'est chargé depuis Google. Le fichier du thème pèse environ 150 Ko.
*   **Anciens appareils** : les effets récents ont un repli, une ancienne TV ou un vieux navigateur garde une interface propre.
*   **Accessible** : les animations se coupent quand le système demande moins de mouvement.

## 📦 Installation

> [!IMPORTANT]
> **Prérequis :**
> * Jellyfin **12.x**
> * Jellyfin **10.11.x**
>
> Installé sur le serveur, le thème atteint tous les clients, applis TV comprises.

### Étapes
1.  Ouvrez le **Tableau de bord** depuis le menu de l'avatar, en haut à droite (Jellyfin 10.11 : Paramètres → Administration).
2.  Allez dans **Slogan** (c'est le nom de la page Branding en français), puis descendez jusqu'à **Code CSS personnalisé**.
3.  Collez cette ligne, puis cliquez sur **Sauvegarder** :
    ```css
    @import url("https://cdn.jsdelivr.net/gh/peterdu1109/ElegantFin@main/Theme/ElegantFin-jellyfin-theme-build-latest-minified.css");
    ```
4.  Rechargez la page (`Ctrl+F5`). Sur une TV, fermez puis rouvrez l'appli Jellyfin.

**Pour votre compte seulement :** collez la même ligne dans **Paramètres → Affichage → Code CSS personnalisé**.

### 📌 Figer une version

`@main` suit toujours la dernière version. Pour mettre à jour quand vous le décidez, remplacez `@main` par un numéro de version :

```css
@import url("https://cdn.jsdelivr.net/gh/peterdu1109/ElegantFin@v1.5.1/Theme/ElegantFin-jellyfin-theme-build-latest-minified.css");
```

Une version figée ne change jamais. C'est aussi le moyen le plus rapide de mettre à jour une appli TV qui garde l'ancien fichier en cache.

### 🗑️ Désinstaller

Supprimez la ligne `@import`, cliquez sur **Sauvegarder**, puis rechargez (`Ctrl+F5`, ou rouvrez l'appli sur une TV).

## ⚙️ Personnalisation

La plupart de ces options viennent d'ElegantFin d'origine. Ajoutez-les **après** la ligne d'import :

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
| **Boutons vu et favori sur les cartes (PC)** | `--extraCardButtonsVisibility` | `none` (masqués) / `block` |
| **Hauteur de la barre du haut (TV et Jellyfin 10.11)** | `--appBarHeight` | `5em` (par défaut) ou une autre hauteur |
| **Titre original** | `--itemOriginalTitleVisibility` | `block` / `none` |
| **Logo du titre** | `--clearLogoVisibility` | `block` / `none` |
| **Note critique sur téléphone** | `--criticsRatingVisibility` | `none` (masquée) / `block` |
| **Icônes (TV LG)** | `--iconPack` | `'Material Icons'` |
| **Onglets Jellyfin Enhanced (PC et téléphone)** | `--jeTabsVisibility` | `inline-flex` (onglets sous la barre) / `none` (icônes en haut à droite) |
| **Thèmes de couleurs** | Voir le [Playground](https://github.com/lscambo13/ElegantFin/discussions/221) | En partie : fonds et bordures changent, le violet reste |

## 📱 Compatibilité

| Plateforme | État |
|------------|------|
| **Jellyfin 12** | Cible principale |
| **Jellyfin 10.11** | Pris en charge |
| **Chrome, Edge, Firefox** | Pris en charge |
| **Safari** | Devrait fonctionner, non testé |
| **Appli Android Jellyfin** | Prise en charge |
| **Samsung Tizen** (appli communautaire) | Prise en charge, testée sur une vraie TV |
| **Applis Android TV basées sur l'interface web de Jellyfin** | Prises en charge, testées sur une box Android TV |
| **LG webOS** | Devrait fonctionner, non testé (l'option icônes peut être nécessaire) |
| **Jellyfin Media Player** | Non testé |
| **Appli native Android TV** | Non prise en charge : elle ne charge pas de CSS personnalisé |

## 🔌 Plugins pris en charge

| Plugin | Ce qu'il fait | Habillage du thème |
|--------|---------------|--------------------|
| [**Jellyfin Enhanced**](https://github.com/n00bcodr/Jellyfin-Enhanced) | Raccourcis, demandes Jellyseerr, avis, liens supplémentaires | Icônes Letterboxd et Seerr alignées, bandeau « où regarder », badges et bouton des lectures en cours aux couleurs du thème |
| [**Media Carousel**](https://github.com/peterdu1109/MediaCarousel) | Rangées d'accueil : Top 10 du serveur, Top 10 mondial, demandes Seerr | Flèches des rangées centrées sur les affiches |
| [**Editor's Choice**](https://github.com/lachlandcp/jellyfin-editors-choice-plugin) | Sélection éditoriale sur l'accueil | Espacement de la bannière, résumé lisible, contrôles fonctionnels |
| [**Media Bar**](https://github.com/IAmParadox27/jellyfin-plugin-media-bar) | Diaporama en haut de l'accueil | Dégradé, résumé lisible, boutons |
| [**Home Screen Sections**](https://github.com/IAmParadox27/jellyfin-plugin-home-sections) | Rangées supplémentaires sur l'accueil | Numéros du Top 10 lisibles, badges à la couleur du thème |

Les autres plugins gardent leur propre apparence.

## ❓ Dépannage

| Problème | Solution |
|----------|----------|
| **Le thème ne s'affiche pas** | La ligne `@import` doit être la **première** du champ. Cliquez sur **Sauvegarder**, puis `Ctrl+F5`. |
| **Une TV affiche encore l'ancienne version** | Fermez puis rouvrez l'appli. Si ça persiste, [figez une version](#-figer-une-version). |
| **`@main` n'est pas encore à jour** | Le CDN peut mettre quelques heures (jusqu'à 12 h). Figez la nouvelle version pour l'avoir tout de suite. |
| **Icônes carrées sur une TV LG** | Ajoutez `--iconPack: 'Material Icons';` dans un bloc `:root { }` après l'import. |
| **Pas de flèches sur les onglets de l'accueil dans Firefox** | Normal : ces flèches demandent un Chrome ou un Edge récent. Firefox garde une fine barre de défilement. |
| **Un plugin ne ressemble pas au reste** | Seuls les [plugins listés plus haut](#-plugins-pris-en-charge) sont habillés. Ouvrez une issue pour en proposer un. |

## 🔔 Plugin recommandé

ElegantFin Cinema Edition va bien avec [**NotifySync**](https://github.com/peterdu1109/NotifySync), une cloche de notifications pour Jellyfin aux couleurs du thème. Les deux fonctionnent ensemble sur PC, mobile et TV.

## 👥 Auteurs & Crédits

- **Thème original :** [ElegantFin](https://github.com/lscambo13/ElegantFin) de [lscambo13](https://github.com/lscambo13)
- **Édition Cinéma :** [ElieMFR](https://github.com/ElieMFR)

Signalements de bugs et suggestions bienvenus sur [GitHub](https://github.com/peterdu1109/ElegantFin/issues).

Distribué sous [licence GPL-2.0](./LICENSE), comme le thème d'origine.
