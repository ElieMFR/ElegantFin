<!-- Image banniere -->
<img src="Theme/assets/img/banner.png" alt="ElegantFin Cinema Edition - Banner">

<div align="center">

# ElegantFin Cinema Edition

**A cinematic fork of [ElegantFin](https://github.com/lscambo13/ElegantFin) — streaming-inspired Jellyfin theme**

[![Version](https://img.shields.io/badge/Cinema%20Edition-v1.2.98-red?style=flat&logo=github)](https://github.com/peterdu1109/ElegantFin/releases)
[![Based on](https://img.shields.io/badge/Based%20on-ElegantFin%20v26.06.06-blue?style=flat&logo=github)](https://github.com/lscambo13/ElegantFin)
[![Jellyfin](https://img.shields.io/badge/Jellyfin-10.11.x-00A4DC?style=flat&logo=jellyfin&logoColor=white)](https://jellyfin.org)
[![Platform](https://img.shields.io/badge/Platform-Desktop%20%7C%20Mobile%20%7C%20TV-green?style=flat)]()
[![jsDelivr](https://img.shields.io/jsdelivr/gh/hm/peterdu1109/ElegantFin?style=flat&label=CDN&color=orange)](https://www.jsdelivr.com/package/gh/peterdu1109/ElegantFin)

</div>

---

<div align="center">

## [English](#english) | [Français](#francais)

</div>

---

<a name="english"></a>

## English

### What is this?

This is a **Cinema Edition** of the ElegantFin theme by [lscambo13](https://github.com/lscambo13), enhanced with **cinematic modules** that transform your Jellyfin into a professional streaming experience inspired by the major streaming platforms.

Everything works on **desktop, mobile and TV** with a single CSS import.

---

### What's new compared to the original?

| Module | Description |
|--------|-------------|
| **Glassmorphism Login** | Frosted glass login card with smooth entrance animation |
| **Page Transitions** | Fade-in and slide-up animations on every page load |
| **Cascade Sections** | Staggered delays for a streaming-style reveal effect |
| **Shimmer Effect** | Subtle light sweep on the first row of cards (desktop) |
| **Cinema Backdrop** | Deeper transparent header gradient, softer backdrop |
| **Cinema Cards** | Pop zoom (1.06x), glowing borders, text highlight on hover |
| **White Progress Bars** | Clean white progress bars replacing colored ones |
| **Premium Badges** | Blurred glass indicators for count, resolution, watched |
| **Cinema Detail Page** | Ultra-light titles (weight 100), italic tagline, white Play button |
| **Modern OSD Player** | Soft gradient, reactive slider, glass footer |
| **Section Titles** | Bolder (700), hidden chevrons, overflow ellipsis |
| **Glass Dialogs** | Backdrop blur on dialogs, menus, drawer, toast, upNext |
| **Navigation Tabs** | Violet active tab, white-pill focus, subtle inactive tabs |
| **TV Focus System** | White-pill focus on every control (buttons, rows, tabs, links) — readable from the couch |
| **Deferred TV Effects** | Card pop + row spotlight fire only at rest — fast scrolling stays smooth |
| **Opaque TV Panels** | Menus and dialogs stay readable over bright video |
| **Who's Watching** | Round centered profile avatars on the login screen |
| **Row Scroll-Snap** | Rows settle aligned on a card (desktop and mobile) |
| **Full-Height Scroll Arrows** | Streaming-style gradient arrows on desktop rows |
| **Typography Hierarchy** | Refined weights for body text, episode titles, subtitles |
| **Long Titles Fix** | Responsive line-clamp (2 desktop, 3 mobile), word-break |
| **Thin Scrollbars** | 4px cross-browser scrollbars, transparent track |
| **OSD Header Glass** | Blurred dark header during video playback |
| **Alpha Picker** | Smooth transition on library A-Z picker |
| **TV Optimizations** | No blur, no shadows, no animations for low-end TVs |
| **Mobile Optimizations** | Reduced blur intensity for better performance |
| **Skeleton Loading** | Animated pulse placeholder while card images load |
| **Hover Preview Info** | Secondary text and gradient reveal on card hover (desktop) |
| **Now Playing Glass** | Glassmorphism on the Now Playing bar |
| **Watched Overlay** | Subtle dark overlay on already-watched items |
| **Sidebar Glass** | Enhanced sidebar with glass effect, styled nav items |

---

### Installation

**Paste the following in your Custom CSS field:**

```
@import url("https://cdn.jsdelivr.net/gh/peterdu1109/ElegantFin@main/Theme/ElegantFin-jellyfin-theme-build-latest-minified.css");
```

> 📌 `@main` always follows the latest version. To pin a release (and upgrade on your own schedule), replace `@main` with a version tag, e.g. `@v1.2.98` — see [Releases](https://github.com/peterdu1109/ElegantFin/releases).

<details>
<summary><b>Server-side installation</b></summary>

1. Open the **Dashboard** from the Administration tab in Settings
2. In the sidebar, select **Branding** (Jellyfin 10.11.x) or **General** (older versions)
3. Scroll down to the **Custom CSS** field
4. Paste the CSS import above
5. Click **Save**
</details>

<details>
<summary><b>Client-side installation</b></summary>

1. Open the **Display** tab in Settings
2. Scroll down to the **Custom CSS** field
3. Paste the CSS import above
4. Click **Save**
</details>

---

### Customization

All original ElegantFin customization options are preserved. Add these overrides **after** the import line:

<details>
<summary><b>Available options</b></summary>

| Option | Variable | Values |
|--------|----------|--------|
| Login background | `--loginPageBgUrl` | `url("your-server/Branding/Splashscreen...")` |
| Play button position | `--overlayPlayButtonPosition` | `50%` (center) / `-999em` (hidden) |
| Card hover effect | `--cardHoverEffect` | `""` (enabled) / `none` (disabled) |
| Library labels | `--libraryLabelVisibility` | `block` / `none` |
| Extra card buttons | `--extraCardButtonsVisibility` | `block` / `none` |
| App bar style | `--appBarHeight` | `5em` (fading) / `4.6em` (solid) |
| Original title | `--itemOriginalTitleVisibility` | `block` / `none` |
| Clear logo | `--clearLogoVisibility` | `block` / `none` |
| Critics rating on phones | `--criticsRatingVisibility` | `none` (hidden) / `block` |
| Icon pack (LG TV fix) | `--iconPack` | `'Material Icons'` (old) |
| Color themes | See [Playground](https://github.com/lscambo13/ElegantFin/discussions/221) | Various |

</details>

---

### Compatibility

| Platform | Status |
|----------|--------|
| Jellyfin Server 10.11.x | Fully supported |
| Jellyfin Server 12.0 (preview) | Works — see note below |
| Web browsers (Chrome, Edge, Firefox, Safari) | Fully supported |
| Jellyfin Android App | Fully supported |
| LG WebOS | Supported (may need icon pack fix) |
| Samsung Tizen (Jellyfin community) | Supported (extensively field-tested; graceful degrade on older models) |
| Android TV native app | Not supported (no CSS support) |
| Jellyfin Media Player (Qt 5.x) | Partial (outdated web engine) |

> **Jellyfin 12 (preview).** Jellyfin 12 splits the web app in two: **TV keeps the current app**, so the theme applies there unchanged. Desktop and mobile default to a new React shell, where the theme already covers cards, detail pages, the player and menus — and its accent colour is applied to the new top bar. That shell is still evolving, so compatibility will be re-checked when 12.0 is released.

---

### Accessibility

- `prefers-reduced-motion` is respected: all animations are disabled when the user has this preference enabled
- TV layouts disable all blur, shadows and animations for performance
- Mobile layouts use reduced blur intensity

---

### 🔌 Supported plugins

Cinema Edition has dedicated styling for these popular Jellyfin plugins:

| Plugin | What it does | Cinema styling |
|--------|--------------|----------------|
| [**Editor's Choice**](https://github.com/lachlandcp/jellyfin-editors-choice-plugin) | Curated editorial picks on home page | Banner spacing fix, button/section collision resolved, 3-line description on desktop, working scroll/pause controls as navy pills below the header, aspect-ratio-safe title logo |
| [**Media Bar**](https://github.com/IAmParadox27/jellyfin-plugin-media-bar) | Auto-cycling slideshow at top of home | Glassmorphism overlay, gradient backdrop, polished button states |
| [**Home Screen Sections**](https://github.com/IAmParadox27/jellyfin-plugin-home-sections) | Extra curated rows on the home page | Readable Top 10 rank numbers (they were near-black on near-black), Discover badges in the theme accent and in French |

If a plugin isn't in this list, the theme just doesn't add overrides for it — it'll work with default styling.

---

### What's new?

📋 See the [**latest GitHub Releases**](https://github.com/peterdu1109/ElegantFin/releases) for a curated, bilingual changelog of all major updates with installation URLs.

🗂️ The full technical changelog (every version) is in [`RELEASE_NOTES.md`](./RELEASE_NOTES.md).

---

### Credits

- **Original theme:** [ElegantFin](https://github.com/lscambo13/ElegantFin) by [lscambo13](https://github.com/lscambo13)
- **Cinema Edition:** Enhanced by [ElieMFR](https://github.com/ElieMFR)

---

<a name="francais"></a>

## Français

### C'est quoi ?

C'est une **Édition Cinéma** du thème ElegantFin par [lscambo13](https://github.com/lscambo13), enrichie de **modules cinématiques** qui transforment votre Jellyfin en une expérience de streaming professionnelle, inspirée des grandes plateformes.

Tout fonctionne sur **PC, mobile et TV** avec un seul import CSS.

---

### Quoi de neuf par rapport à l'original ?

| Module | Description |
|--------|-------------|
| **Connexion en verre dépoli** | Carte de connexion translucide avec animation d'entrée |
| **Transitions de pages** | Fondu et glissement vers le haut à chaque chargement |
| **Sections en cascade** | Délais décalés pour une révélation façon streaming |
| **Effet de balayage** | Reflet lumineux sur la première rangée de cartes (PC) |
| **Arrière-plan Cinéma** | Dégradé transparent plus profond, arrière-plan plus doux |
| **Cartes Cinéma** | Zoom au survol (1,06×), bordures lumineuses, titre mis en avant |
| **Barres de progression blanches** | Barres épurées à la place des barres colorées |
| **Badges Premium** | Pastilles en verre flouté pour le nombre, la résolution, les éléments vus |
| **Page de détail Cinéma** | Titres ultra-fins, accroche en italique, bouton Lire blanc |
| **Lecteur modernisé** | Dégradé doux, curseur réactif, pied de page en verre |
| **Titres de sections** | Plus gras, chevrons masqués, coupure par ellipse |
| **Fenêtres en verre** | Flou d'arrière-plan sur les dialogues, menus, menu latéral, notifications et « À suivre » |
| **Onglets de navigation** | Onglet actif violet, pastille blanche au focus, inactifs discrets |
| **Système de focus TV** | Pastille blanche sur chaque contrôle — boutons, rangées, onglets, liens — lisible depuis le canapé |
| **Effets TV différés** | Le zoom des cartes et la mise en avant de la rangée n'arrivent qu'à l'arrêt : le défilement rapide reste fluide |
| **Panneaux TV opaques** | Menus et dialogues lisibles par-dessus la vidéo |
| **Qui regarde ?** | Avatars de profil ronds et centrés à la connexion |
| **Aimantation des rangées** | Les rangées se posent alignées sur une carte (PC et mobile) |
| **Flèches pleine hauteur** | Flèches en dégradé façon streaming sur les rangées PC |
| **Hiérarchie typographique** | Graisses affinées pour le texte, les titres d'épisodes et les sous-titres |
| **Titres longs** | Nombre de lignes limité selon l'écran (2 sur PC, 3 sur mobile), césure des mots |
| **Barres de défilement fines** | 4 px, compatibles tous navigateurs, piste transparente |
| **En-tête du lecteur en verre** | Bandeau sombre flouté pendant la lecture |
| **Sélecteur A-Z** | Transition fluide sur le sélecteur alphabétique des bibliothèques |
| **Optimisations TV** | Ni flou, ni ombres, ni animations, pour les téléviseurs peu puissants |
| **Optimisations mobile** | Intensité de flou réduite pour de meilleures performances |
| **Chargement en silhouette** | Forme animée le temps que l'image de la carte arrive |
| **Aperçu au survol** | Texte secondaire et dégradé révélés au survol des cartes (PC) |
| **Lecture en cours en verre** | Effet verre dépoli sur la barre de lecture |
| **Voile sur les éléments vus** | Voile sombre discret sur ce qui est déjà visionné |
| **Menu latéral en verre** | Menu latéral en verre dépoli, entrées de navigation habillées |

---

### Installation

**Collez le code suivant dans le champ CSS personnalisé :**

```
@import url("https://cdn.jsdelivr.net/gh/peterdu1109/ElegantFin@main/Theme/ElegantFin-jellyfin-theme-build-latest-minified.css");
```

> 📌 `@main` suit toujours la dernière version. Pour figer une version et mettre à jour quand VOUS le décidez, remplacez `@main` par un tag, par exemple `@v1.2.98` — voir les [Releases](https://github.com/peterdu1109/ElegantFin/releases).

<details>
<summary><b>Installation côté serveur</b></summary>

1. Ouvrez le **Tableau de bord** depuis l'onglet Administration dans les Paramètres
2. Dans la barre latérale, sélectionnez **Marque** (Jellyfin 10.11.x) ou **Général** (versions plus anciennes)
3. Descendez jusqu'au champ **CSS personnalisé**
4. Collez l'import ci-dessus
5. Cliquez sur **Enregistrer**
</details>

<details>
<summary><b>Installation côté client</b></summary>

1. Ouvrez l'onglet **Affichage** dans les Paramètres
2. Descendez jusqu'au champ **CSS personnalisé**
3. Collez l'import ci-dessus
4. Cliquez sur **Enregistrer**
</details>

---

### Personnalisation

Toutes les options de personnalisation d'ElegantFin sont préservées. Ajoutez ces surcharges **après** la ligne d'import :

<details>
<summary><b>Options disponibles</b></summary>

| Option | Variable | Valeurs |
|--------|----------|---------|
| Fond de l'écran de connexion | `--loginPageBgUrl` | `url("votre-serveur/Branding/Splashscreen...")` |
| Position du bouton de lecture | `--overlayPlayButtonPosition` | `50%` (centré) / `-999em` (masqué) |
| Effet au survol des cartes | `--cardHoverEffect` | `""` (activé) / `none` (désactivé) |
| Étiquettes des bibliothèques | `--libraryLabelVisibility` | `block` / `none` |
| Boutons supplémentaires des cartes | `--extraCardButtonsVisibility` | `block` / `none` |
| Style de la barre du haut | `--appBarHeight` | `5em` (fondue) / `4.6em` (pleine) |
| Titre original | `--itemOriginalTitleVisibility` | `block` / `none` |
| Logo du titre | `--clearLogoVisibility` | `block` / `none` |
| Note des critiques sur téléphone | `--criticsRatingVisibility` | `none` (masquée) / `block` |
| Jeu d'icônes (correctif LG TV) | `--iconPack` | `'Material Icons'` (anciennes) |
| Thèmes de couleurs | Voir le [Playground](https://github.com/lscambo13/ElegantFin/discussions/221) | Divers |

</details>

---

### Compatibilité

| Plateforme | Statut |
|------------|--------|
| Jellyfin Server 10.11.x | Entièrement pris en charge |
| Jellyfin Server 12.0 (préversion) | Fonctionne — voir la note ci-dessous |
| Navigateurs web (Chrome, Edge, Firefox, Safari) | Entièrement pris en charge |
| Application Android Jellyfin | Entièrement prise en charge |
| LG WebOS | Pris en charge (peut nécessiter le correctif d'icônes) |
| Samsung Tizen (communauté Jellyfin) | Pris en charge, éprouvé sur matériel réel ; dégradation progressive sur les modèles anciens |
| Application native Android TV | Non prise en charge (elle n'accepte pas de CSS) |
| Jellyfin Media Player (Qt 5.x) | Partiel (moteur web obsolète) |

> **Jellyfin 12 (préversion).** Jellyfin 12 scinde l'application web en deux : la **TV reste sur l'application actuelle**, le thème s'y applique donc à l'identique. PC et mobile passent par défaut sur une nouvelle coque React, où le thème couvre déjà les cartes, les pages de détail, le lecteur et les menus — et où sa couleur d'accent habille la nouvelle barre du haut. Cette coque évolue encore : la compatibilité sera revalidée à la sortie de la 12.0.

---

### Accessibilité

- `prefers-reduced-motion` est respecté : toutes les animations sont désactivées si l'utilisateur a exprimé cette préférence
- Les dispositions TV désactivent tous les flous, ombres et animations, pour la fluidité
- Les dispositions mobiles utilisent une intensité de flou réduite

---

### 🔌 Plugins pris en charge

L'Édition Cinéma habille spécifiquement ces plugins Jellyfin :

| Plugin | Ce qu'il fait | Habillage Cinéma |
|--------|---------------|------------------|
| [**Editor's Choice**](https://github.com/lachlandcp/jellyfin-editors-choice-plugin) | Sélection éditoriale sur la page d'accueil | Espacement de la bannière corrigé, collision bouton/section résolue, description sur trois lignes sur PC, contrôles de défilement et de pause fonctionnels en pastilles sombres sous la barre du haut, logo de titre au ratio préservé |
| [**Media Bar**](https://github.com/IAmParadox27/jellyfin-plugin-media-bar) | Diaporama défilant en haut de la page d'accueil | Voile en verre dépoli, dégradé d'arrière-plan, états des boutons soignés |
| [**Home Screen Sections**](https://github.com/IAmParadox27/jellyfin-plugin-home-sections) | Rangées éditoriales supplémentaires sur la page d'accueil | Numéros du Top 10 rendus lisibles — ils étaient quasi noirs sur fond quasi noir — et badges Découvrir à la couleur du thème, en français |

Si un plugin ne figure pas dans cette liste, le thème ne lui applique aucune surcharge : il s'affiche avec son habillage d'origine.

---

### Quoi de neuf ?

📋 Voir les [**dernières Releases GitHub**](https://github.com/peterdu1109/ElegantFin/releases) pour un journal des versions sélectif et bilingue, avec les URLs d'installation.

🗂️ Le journal technique complet, version par version, est dans [`RELEASE_NOTES.md`](./RELEASE_NOTES.md).

---

### Crédits

- **Thème original :** [ElegantFin](https://github.com/lscambo13/ElegantFin) par [lscambo13](https://github.com/lscambo13)
- **Édition Cinéma :** enrichie par [ElieMFR](https://github.com/ElieMFR)
