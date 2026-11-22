# ElegantFin Cinema Edition — release notes

## [English](#english) | [Francais](#francais)

---

<a name="english"></a>
## English

### Cinema Edition — cinematic modules on top of ElegantFin

This release transforms the ElegantFin theme into a professional, premium streaming experience while keeping full compatibility with desktop, mobile, and TV platforms.

---

#### v1.5.10: TV login focus, Save button, keyboard focus

- TV: the "Sign In" button shows a thick white outline when selected.
- Settings pages: the Save button no longer dims the field above it.
- Keyboard: switches, checkboxes and the slider handle are easier to see when selected.
- Desktop, keyboard: the arrows of a row show up when selected.
- Text fields: the example text is easier to read.
- TV: with reduced motion turned on, a selected card no longer zooms.
- The Skip button no longer keeps its shadow when pressed.

---

#### v1.5.9: Clean-up

- Detail pages: internal clean-up, no visible change.

---

#### v1.5.8: Skip button, Play button focus, contrast

- TV: the Skip button fades out again instead of staying selected while invisible, so pressing OK no longer skips blindly.
- Keyboard (desktop and phone): the Play button shows a clear white ring when selected.
- TV: the outline of text fields and drop-down lists is thicker.
- Home rows no longer flash before sliding in.
- The "watched" tick is easier to read.
- Menus (audio, subtitles…) on older TVs and browsers keep the tick on the selected option.
- Jellyfin 10.11 is no longer supported: the theme targets Jellyfin 12 only.

---

#### v1.5.7: Keyboard focus and contrast

- Desktop, keyboard: the year or episode under a selected card shows, as on hover.
- Desktop, keyboard: the buttons next to Play (favorite, watched, more) turn white when selected.
- Purple links, the Save button of the top bar and the side menu titles are lighter, so they read better on the dark background.
- Login card: now fits older TVs.

---

#### v1.5.6: Media Bar and Home Screen Sections

- The theme no longer styles Media Bar and Home Screen Sections, which it was not tested with, and no longer lists them as supported. Both keep their own look.

---

#### v1.5.5: Keyboard focus on desktop and phone

- The selected card shows a white outline.
- A row title that opens the full list shows a white outline when selected.

---

#### v1.5.4: TV detail pages, Jellyfin 12.4, login title

- TV, detail pages: the audio and subtitle menus sit right under the Play buttons, so the up arrow takes you back to Play.
- Jellyfin 12.4: the "Reset filters" button no longer takes the purple pill of the active library.
- Login page: the title follows the Jellyfin language (French or English). `--loginPageText` still sets your own text.
- The Home and Favorites tab icons and the "more" arrow follow the `--iconPack` option (LG TV tip in the README).

---

#### v1.5.3: TV, Editor's Choice banner

- The up arrow reaches the tabs again from the banner.

---

#### v1.5.2: TV, Editor's Choice banner and top bar

- The banner reaches the top of the screen, with no dark strip above the tabs.
- When you scroll, the top bar gets a dark veil, so the tabs and icons stay readable.

---

#### v1.5.1: TV, lighter home page

- The Editor's Choice banner image stays still, so the TV does much less work on the home page. Desktop and phone keep the effect.
- No more blur under the top bar.

---

#### v1.5.0: TV, much smoother

- TV and other devices: much smoother when Jellyfin shows or hides something on screen. The TV guide scrolls more smoothly.
- Desktop: library names in the top bar no longer wrap onto two lines.
- Phone (Jellyfin 10.11): the Home button also shows on library pages.

---

#### v1.4.5: Card menu button and Jellyfin Enhanced tabs

- Desktop: the ⋮ button is back on cards when you hover them. `--extraCardButtonsVisibility` now only hides the watched and favorite buttons.
- New option `--jeTabsVisibility` (desktop and phone): `none` hides the Jellyfin Enhanced tabs (Seerr recommendations, Requests, Calendar), shown as icons at the top right instead. Default `inline-flex` keeps the tabs.

---

#### v1.4.4: Top bar, room after the library pills

- Top bar (desktop and phone in landscape): a little room after the last library pill, so it no longer crowds the icons next to it.

---

#### v1.4.3: Phones in landscape, library pills

- Phone in landscape: the library links in the top bar get the same pills as on desktop.

---

#### v1.4.2: TV, header tabs and season logo

- TV, home and libraries: the tabs stop before the header icons, so "Requests" no longer hides under the first icon.
- TV, season pages: the logo sits just under the header and is smaller.

---

#### v1.4.1: TV, smoother navigation

- TV: moving around with the remote is lighter.

---

#### v1.4.0: Cards without drop shadow

- TV: the selected card keeps its zoom, white outline and soft white glow, without the dark drop shadow.
- PC: hovering a card zooms it with its lighter border, without a drop shadow.

---

#### v1.3.26: TV focus zoom, PC hover shadow

- TV: the selected card shows its shadow on the picture only, and the thin white glow around the picture and title is gone.
- PC: the hover shadow follows the picture instead of a dark rectangle around the picture and title.

---

#### v1.3.25: Jellyfin Enhanced button, TV focus zoom

- Jellyfin Enhanced: the active streams button in the header is always purple.
- TV: nicer, lighter zoom on the selected card, with its shadow following the picture and its rounded corners.

---

#### v1.3.24: TV, profile picture size

- TV: the header profile picture is back to its usual size.

---

#### v1.3.23: TV, readable header on detail pages

- TV, detail pages: when you scroll down, a navy veil fades in behind the header, so the logo, info and Play button no longer mix with the header icons.

---

#### v1.3.22: Home tab arrows, centered row arrows

- PC, narrow window: when the home tabs no longer fit, arrows replace the thin scrollbar under them.
- PC: row arrows sit at the centre of the posters.

---

#### v1.3.21: Jellyfin Enhanced, Seerr badges

- Search and Jellyseerr sections: the Film, Series and Collection badges on Seerr results use the theme's purple.

---

#### v1.3.20: Drop-down lists, older TVs

- Drop-down lists (audio and subtitle tracks, settings): long names no longer run under the arrow.
- PC, narrow window: on a detail page the Credits and Media panels stack, as on phones, so track names show in full.
- Older TVs (Tizen 4.0 to 6.5): button borders, the Save button, item titles and menu ticks get a fallback these TVs understand.

---

#### v1.3.19: Jellyfin Enhanced "where to watch" bar

- Detail pages: the Jellyfin Enhanced "where to watch" bar gets the theme's look, like the panels below it.

---

#### v1.3.18: TV, Skip button countdown

- TV: the purple countdown of the Skip button shows again.

---

#### v1.3.17: Library pills, theme colors, Play button on phones

- Jellyfin 12, desktop: the libraries in the top bar become pills and the server name becomes a header with a thin divider (style adapted from elegantfin-jf12 by mihaif7, GPL-2.0).
- Jellyfin 12: the interface follows the theme's purple, navy and red instead of Jellyfin's blue and gray. On TV, the selected Skip button, selected drop-down lists and the Up Next countdown turn purple.
- Phones, Jellyfin 12: movie posters get their Play button back.

---

#### v1.3.16: TV, header tabs

- TV, Music and Live TV pages: the header tabs no longer spill over the page title, the bell and the icons, and scroll in their frame.
- The focus pill is never cut, from the first tab to the last.

---

#### v1.3.15: Smoother TV navigation

- TV: the home screen and the live guide respond faster to the remote.

---

#### v1.3.14: Half-screen windows, theme songs

- Jellyfin 12, desktop, half-screen windows: the empty space reserved for the backdrop is gone, so the logo sits under the top bar and the Play button comes up.
- Desktop: detail pages no longer jump when a series theme song starts or stops.

---

#### v1.3.13: Season pages, phones

- Season, episode and album pages keep their backdrop bright at the top, like the series page.
- Jellyfin 12, desktop: no more lighter band behind the top bar on those pages.
- Phones, season, episode and album pages: backdrop at full brightness, logo right under the image, no empty space between the logo and the title.
- Phones: the Play button comes up on film, series, season, episode and album pages.
- TV, season pages in 1080p: the series title no longer overlaps the logo.

---

#### v1.3.12: Alignments, "99+" badge, selection bar

- Long press on a card (select mode): the close button, the counter and the ⋮ button are white again and visible on the navy bar.
- Phones: horizontal rows line up with their title (home, favorites, detail pages, search).
- Detail pages: the "Next up", "Seasons", actor films and artist albums grids line up with their title.
- TV: Live TV rows and the "Suggestions" tab of libraries line up with their title too.
- The "99+" unwatched badge widens into a pill instead of touching its circle.

---

#### v1.3.11: Login page

- Jellyfin 12, desktop: the login page no longer shows a bright strip under the top bar or two scrollbars. The top bar is hidden on the login page only and comes back once signed in.

---

#### v1.3.10: Phones, touch on detail pages

- Jellyfin 12, phones: series, season and movie pages respond to taps again.
- Libraries: the A-Z picker stays on screen while scrolling.

---

#### v1.3.9: Jellyfin Enhanced, Letterboxd and Seerr icons

- Detail pages: the Letterboxd and Seerr icons added by Jellyfin Enhanced look like the IMDb, TVDB and TMDB logos and sit on the same line.

---

#### v1.3.8: Lighter pages

- Thumbnails: the loading animation, which left a faint white veil over images, is removed (the "Skeleton Loading" module is gone). On TV, posters show their true colors again, blacks included.
- Pages take less work to display.

---

#### v1.3.7: Detail pages, aligned rows

- Detail pages: rows (cast, "More like this", Jellyseerr sections) line up with the rest of the page.
- Jellyfin 12: the right scroll arrow of those rows is fully on screen, and the last poster of a row is fully visible.
- Phones and TV with Jellyfin Enhanced: Jellyseerr sections line up with the other rows and no longer widen the page.
- Subtitle preview (Settings › Subtitles): background in the theme's colors.

---

#### v1.3.6: Lighter on TV

- TV: the guide is lighter to navigate, with the same look.

---

#### v1.3.5: Jellyfin 12, the new interface matches 10.11

- Top bar: the same fading cinema header as 10.11, with no shadow when scrolling.
- Home: the Home and Favorites tabs are back under the top bar, and the duplicate Favorites link leaves the desktop top bar.
- Active library link: violet pill with white text.
- "Play all" and "Shuffle": dark text and icons, and the divider between them is no longer blue.
- Display settings page: fields, labels, focus ring, section titles and sticky Save button as in 10.11.
- Every element of the new interface uses the theme's font.
- A-Z picker: dimmed letters, selected letter in white, no gray panel.
- Toggles and checked checkboxes in the theme's violet.
- Resume bars on library cards are white.
- Menus and filter popover: navy rounded surfaces, white keyboard focus, pill-shaped button groups, no more gray panels.
- Phone drawer aligned with the older drawer.
- Section titles in white.
- Library pages: the empty band under the top bar is gone.
- Colors restored everywhere, TV included: white badge digits and watched tick, main and secondary text levels.
- Icon tooltips use the theme's navy glass.
- Hover on buttons, A-Z letters and menu entries is violet instead of gray; the library item count is a dark violet chip.
- Keyboard focus: white pill instead of a gray pulsing circle, violet click ripple.
- Search page: the "Suggestions" title is centered over its list.

---

#### v1.3.4: Tizen 4.0, Home tab

- Tizen 4.0: the Home tab is no longer clipped when the focus moves to Favorites.

---

#### v1.3.3: Tizen 4.0, layouts

- Tizen 4.0: the progress bar of "Continue watching" cards is back at the bottom of the poster.
- Tizen 4.0: the title block and sections of detail pages are in the right place and order, and the TV tabs are centered vertically.

---

#### v1.3.2: Tizen 4.0, focus

- Tizen 4.0: the selection indicators work again (card zoom, Play button, avatar, detail and header buttons, links, tabs, profile ring). A selected button could be invisible.

---

#### v1.3.1: TV, blurs and older sets

- TV: the last permanent blurs (card counters, player stats, dialog footers) and the backdrop fade-in on detail pages are removed, so scrolling is lighter.
- Tizen 4.0 to 7.0: the TV guide frame gets its border, background and rounding back, and the poster shows on Cast, Book and Live TV pages.

---

#### v1.3.0: Phone mini Play button

- Phones: the mini Play button keeps its usual size.

---

#### v1.2.99: Media type badges, player title

- Folders, photo albums, photos and home videos: the corner badge shows its amber, blue or red again.
- Player: a long episode title lays out on two lines instead of spilling out.

---

#### v1.2.98: Phones, a way back to Home

- Phones: the Home button is back in the header on film and series pages.

---

#### v1.2.97: Audit

- Reduced motion now covers every animation (mobile backdrop, loading placeholder).
- TV: the last full-screen blur is removed (it only showed with the Backdrops option on).

---

#### v1.2.96: Phones, backdrop and text

- Phones: on film and series pages, the backdrop no longer paints over the text.

---

#### v1.2.95: Phones, top bar

- Phones: the top bar now stays in place while you scroll, so it can no longer get stuck hidden.

---

#### v1.2.94: Jellyfin 12, credits block

- Jellyfin 12: the credits block (Genres, Director, Writers, Studios) is styled again.

---

#### v1.2.93: Critics rating on phones

- Phones: the critics rating is hidden in the info line under a title. `--criticsRatingVisibility: block` brings it back.

---

#### v1.2.92: Clean-up

- Internal clean-up, no visible change.

---

#### v1.2.91: Logo above the title

- Desktop and mobile: the logo sits above the title and no longer lands on it or under the top bar. The large empty gap is gone.

---

#### v1.2.89: Skip button countdown

- TV: the countdown gauge of the Skip button is back.

---

#### v1.2.88: Icons, Skip button on TV

- Books, photos and photo albums show the right icon, and the outlined "info" icon is no longer filled.
- TV: the Skip Intro button appears in its final colors at once, and selection shows as a white outline.

---

#### v1.2.87: Clean-up

- Internal clean-up, no visible change.

---

#### v1.2.86: Jellyfin 12, top bar

- Jellyfin 12: no more hairline under the top bar.

---

#### v1.2.85: Primary button, profile picture

- Jellyfin 12: the primary action button (for example "Play all") is white and easier to read. Red and green variants keep their colors.
- Profile page: the picture no longer touches the top bar.

---

#### v1.2.84: First pass for Jellyfin 12

- Jellyfin 12: the active tab, profile avatar, library badge and links follow the theme's accent.

---

#### v1.2.83: TV, page transitions

- TV: no more dark band across the background when opening an episode.

---

#### v1.2.82: Firefox, gradients

- Firefox: no more thin horizontal lines across card thumbnails and gradients.

---

#### v1.2.81: Accurate seekbar

- The playback bar is accurate: clicks near the start or end seek on target, the hover preview lines up, and the thumb reaches both ends. The volume slider benefits too.
- Phones: the seekbar thumb stays enlarged.

---

#### v1.2.80: TV, top bar

- TV: the top bar can no longer get stuck hidden.

---

#### v1.2.79: Clean-up

- Internal clean-up, no visible change.

---

#### v1.2.78: Skip button states, slimmer header on mobile

- Skip Intro: the label no longer disappears on mouse hover. Hover and pressed states use the white pill, and the focus halo shows.
- TV: no more hover zoom on the Skip button.
- Phones: less empty space under the header tab row.

---

#### v1.2.77: Editor's Choice logo on small screens

- Editor's Choice: the title logo keeps its proportions on small screens.

---

#### v1.2.76: Slimmer PC header

- Desktop: the header is slimmer, and the Editor's Choice controls sit just under it.

---

#### v1.2.75: Editor's Choice controls in fullscreen

- Desktop, wide windows: the Editor's Choice controls sit clear of the top bar.

---

#### v1.2.74: Skip button, text caret, keyboard focus

- Skip Intro: the button is navy with a white label, and its countdown reads as a violet fill. Focus still turns it white.
- PC: a stray blinking text caret no longer appears on the player's play/pause button.
- PC, keyboard: tabbing through the interface shows the same focus indicators as the TV remote.

---

#### v1.2.73: Editor's Choice controls

- Editor's Choice: the ‹ ❚❚ › controls show as round navy pills under the top bar, at the top right.
- The row arrows of other sections no longer cover the banner.

---

#### v1.2.72: Editor's Choice arrows

- Editor's Choice: second step to free the controls from under the header (completed in v1.2.73).

---

#### v1.2.71: Editor's Choice arrows on desktop

- Desktop: first step to bring back the Editor's Choice banner arrows (completed in v1.2.73).

---

#### v1.2.70: Focus on the Play button and avatar

- TV: the Play button inverts when selected (navy fill, white text, white ring).
- TV: the profile avatar shows a thick white ring when selected.

---

#### v1.2.69: Skip button focus

- TV: the Skip Intro button shows a white outline when selected.

---

#### v1.2.68: Original title

- TV and mobile: the original (Japanese) title is no longer cut on the right.

---

#### v1.2.67: Lighter fonts

- Much lighter fonts with the same look, so first loads are faster.

---

#### v1.2.66: Series title focus

- TV: the selected series title is no longer white on white.

---

#### v1.2.65: Series title

- Season and episode pages: the series title uses the same format as the "Season X - Episode" line, on TV, desktop and mobile, with or without a logo.

---

#### v1.2.64: Version badge

- The version badge at the bottom of the Preferences page is easier to read.

---

#### v1.2.63: Series title on all platforms

- Season and episode pages: the series title matches the "Season X - Episode" line (size and weight) on TV, desktop and mobile, and stays clickable.

---

#### v1.2.62: Series title on season and episode pages

- TV, season and episode pages: the series name shares the format of the line below it and stays clickable.

---

#### v1.2.61: Fixes from the original ElegantFin

- Desktop: the ⋮ menu button is back on card hover and list rows.
- Jellyfin Enhanced: the TMDB reviews no longer overflow the detail page, and external links (Radarr/Sonarr, Letterboxd) get the theme's link style.
- Settings pages: the Save button stays in view.
- Firefox: the seek bar thumb reacts to hover, drag and focus like on Chrome.
- iPhone: the hamburger menu covers the full screen height, and several menu glitches are fixed.
- Icons no longer flash as invisible text while loading.
- Music: track lists and disc headings spacing, cast row closer to its title.
- The icon font is updated to cover newer Jellyfin icons.

---

#### v1.2.60: Lighter file, version tags

- The theme file is lighter to download.
- Each release is tagged, so you can pin a version (for example `@v1.2.60`) in your import URL and roll back.
- Font licences are included.

---


> 🗄️ Versions before v1.2.60 are in [`RELEASE_NOTES_ARCHIVE.md`](./RELEASE_NOTES_ARCHIVE.md).

---

### Compatibility
- Jellyfin **10.11.x** and **12.x** (tested on 12.1, new and legacy interfaces)
- Works on all web browsers (Chrome, Edge, Firefox, Safari), Android app, LG WebOS, Samsung Tizen
- Full `@supports` fallback for browsers without `backdrop-filter`

---

<a name="francais"></a>
## Francais

### Edition Cinema — modules cinematiques par-dessus ElegantFin

Cette version transforme le theme ElegantFin en une experience de streaming professionnelle inspiree des grandes apps de streaming, tout en gardant la compatibilite complete avec bureau, mobile et TV.

---

#### v1.5.10 : Focus de connexion sur TV, bouton Sauvegarder, focus clavier

- TV : le bouton « Se connecter » affiche un contour blanc épais quand il est sélectionné.
- Pages de réglages : le bouton Sauvegarder ne grise plus le champ au-dessus.
- Clavier : les interrupteurs, les cases et la poignée du curseur se voient mieux quand ils sont sélectionnés.
- PC, clavier : les flèches d'une rangée apparaissent quand elles sont sélectionnées.
- Champs de texte : le texte d'exemple se lit mieux.
- TV : avec le mouvement réduit activé, une carte sélectionnée ne zoome plus.
- Le bouton Passer ne garde plus son ombre quand on appuie dessus.

---

#### v1.5.9 : Ménage

- Fiches : nettoyage interne, aucun changement visible.

---

#### v1.5.8 : Bouton Passer, focus du bouton Lire, contraste

- TV : le bouton Passer s'efface de nouveau en fondu au lieu de rester sélectionné sans être visible, donc appuyer sur OK ne fait plus sauter le segment à l'aveugle.
- Clavier (PC et téléphone) : le bouton Lire affiche un anneau blanc net quand il est sélectionné.
- TV : le contour des champs de texte et des listes déroulantes est plus épais.
- Les rangées de l'accueil ne clignotent plus avant d'entrer en glissement.
- La coche « vu » se lit mieux.
- Menus (audio, sous-titres…) sur les anciennes TV et navigateurs : la coche reste sur l'option choisie.
- Jellyfin 10.11 n'est plus pris en charge : le thème vise Jellyfin 12 seulement.

---

#### v1.5.7 : Focus clavier et contraste

- PC, clavier : l'année ou l'épisode sous une carte sélectionnée s'affiche, comme au survol.
- PC, clavier : les boutons à côté de Lire (favori, vu, plus) deviennent blancs quand ils sont sélectionnés.
- Les liens violets, le bouton Sauvegarder de la barre du haut et les titres du menu latéral sont plus clairs, pour mieux se lire sur le fond sombre.
- Carte de connexion : elle convient maintenant aux anciennes TV.

---

#### v1.5.6 : Media Bar et Home Screen Sections

- Le thème n'habille plus Media Bar ni Home Screen Sections, avec lesquels il n'est pas testé, et ne les annonce plus comme pris en charge. Les deux gardent leur propre aspect.

---

#### v1.5.5 : Focus clavier sur PC et téléphone

- La carte sélectionnée affiche un contour blanc.
- Le titre d'une rangée qui ouvre la liste complète affiche un contour blanc quand il est sélectionné.

---

#### v1.5.4 : Fiches TV, Jellyfin 12.4, titre de connexion

- TV, fiches : les menus audio et sous-titres sont juste sous les boutons Lire, donc la flèche haut ramène sur Lire.
- Jellyfin 12.4 : le bouton « Réinitialiser les filtres » ne prend plus la pastille violette de la bibliothèque active.
- Page de connexion : le titre suit la langue de Jellyfin (français ou anglais). `--loginPageText` permet toujours de mettre votre texte.
- Les icônes des onglets Accueil et Favoris et la flèche « plus » suivent l'option `--iconPack` (astuce TV LG du README).

---

#### v1.5.3 : TV, bannière Editor's Choice

- La flèche haut ramène de nouveau aux onglets depuis la bannière.

---

#### v1.5.2 : TV, bannière Editor's Choice et barre du haut

- La bannière va jusqu'en haut de l'écran, sans bande sombre au-dessus des onglets.
- Quand on descend, la barre du haut prend un voile sombre, donc les onglets et les icônes restent lisibles.

---

#### v1.5.1 : TV, accueil plus léger

- L'image de la bannière Editor's Choice reste fixe, donc la TV travaille beaucoup moins sur l'accueil. PC et téléphone gardent l'effet.
- Plus de flou sous la barre du haut.

---

#### v1.5.0 : TV, beaucoup plus fluide

- TV et autres appareils : beaucoup plus fluide quand Jellyfin affiche ou masque un élément à l'écran. Le guide TV défile plus fluidement.
- PC : les noms de bibliothèques de la barre du haut ne passent plus sur deux lignes.
- Téléphone (Jellyfin 10.11) : le bouton Accueil s'affiche aussi sur les pages de bibliothèque.

---

#### v1.4.5 : Bouton menu des cartes et onglets Jellyfin Enhanced

- PC : le bouton ⋮ revient sur les cartes au survol. `--extraCardButtonsVisibility` ne masque plus que les boutons vu et favori.
- Nouvelle option `--jeTabsVisibility` (PC et téléphone) : `none` masque les onglets Jellyfin Enhanced (recommandations Seerr, Requests, Calendar), affichés en icônes en haut à droite. Par défaut `inline-flex` garde les onglets.

---

#### v1.4.4 : Barre du haut, de l'air après les pastilles de bibliothèques

- Barre du haut (PC et téléphone en paysage) : un peu d'espace après la dernière pastille de bibliothèque, qui ne colle plus aux icônes voisines.

---

#### v1.4.3 : Téléphone en paysage, pastilles de bibliothèques

- Téléphone en paysage : les liens de bibliothèques de la barre du haut prennent les mêmes pastilles que sur PC.

---

#### v1.4.2 : TV, onglets et logo des saisons

- TV, accueil et bibliothèques : les onglets s'arrêtent avant les icônes de l'en-tête, donc « Requests » ne se cache plus sous la première icône.
- TV, pages de saison : le logo se place juste sous l'en-tête et il est plus petit.

---

#### v1.4.1 : TV, navigation plus fluide

- TV : se déplacer à la télécommande est plus léger.

---

#### v1.4.0 : Cartes sans ombre portée

- TV : la carte sélectionnée garde son zoom, son contour blanc et sa lueur blanche douce, sans l'ombre portée sombre.
- PC : survoler une carte la zoome avec sa bordure plus claire, sans ombre portée.

---

#### v1.3.26 : Zoom TV, ombre de survol PC

- TV : la carte sélectionnée a son ombre sur l'image seulement, et la fine lueur blanche autour de l'image et du titre a disparu.
- PC : l'ombre au survol suit l'image au lieu d'un rectangle sombre autour de l'image et du titre.

---

#### v1.3.25 : Bouton Jellyfin Enhanced, zoom TV

- Jellyfin Enhanced : le bouton des lectures en cours dans l'en-tête est toujours violet.
- TV : zoom plus joli et plus léger sur la carte sélectionnée, avec une ombre qui suit l'image et ses coins arrondis.

---

#### v1.3.24 : TV, taille de la photo de profil

- TV : la photo de profil de l'en-tête retrouve sa taille habituelle.

---

#### v1.3.23 : TV, en-tête lisible sur les fiches

- TV, fiches : quand on descend, un voile bleu marine apparaît derrière l'en-tête, donc le logo, les infos et le bouton Lire ne se mélangent plus aux icônes de l'en-tête.

---

#### v1.3.22 : Flèches des onglets, flèches de rangée centrées

- PC, fenêtre étroite : quand les onglets de l'accueil ne tiennent plus, des flèches remplacent la fine barre de défilement dessous.
- PC : les flèches des rangées sont au centre des affiches.

---

#### v1.3.21 : Jellyfin Enhanced, badges Seerr

- Recherche et sections Jellyseerr : les badges Film, Série et Collection des résultats Seerr prennent le violet du thème.

---

#### v1.3.20 : Listes déroulantes, anciennes TV

- Listes déroulantes (pistes audio et sous-titres, réglages) : les noms longs ne passent plus sous la flèche.
- PC, fenêtre étroite : sur une fiche, les panneaux Crédits et Média s'empilent, comme sur téléphone, donc les noms de pistes s'affichent en entier.
- Anciennes TV (Tizen 4.0 à 6.5) : les bordures de boutons, le bouton Sauvegarder, les titres d'éléments et les coches des menus prennent un repli que ces TV comprennent.

---

#### v1.3.19 : Bandeau « où regarder » de Jellyfin Enhanced

- Fiches : le bandeau « où regarder » de Jellyfin Enhanced prend l'aspect du thème, comme les panneaux en dessous.

---

#### v1.3.18 : TV, jauge du bouton Passer

- TV : la jauge violette du bouton Passer se voit de nouveau.

---

#### v1.3.17 : Bibliothèques en pastilles, couleurs du thème, bouton Lire au téléphone

- Jellyfin 12, PC : les bibliothèques de la barre du haut deviennent des pastilles et le nom du serveur devient un titre avec un fin séparateur (style adapté de elegantfin-jf12 par mihaif7, GPL-2.0).
- Jellyfin 12 : l'interface suit le violet, le bleu marine et le rouge du thème au lieu du bleu et des gris de Jellyfin. Sur TV, le bouton Passer sélectionné, les listes déroulantes sélectionnées et le compte à rebours « À suivre » deviennent violets.
- Téléphone, Jellyfin 12 : les affiches de films retrouvent leur bouton Lire.

---

#### v1.3.16 : TV, onglets de l'en-tête

- TV, pages Musique et TV en direct : les onglets de l'en-tête ne débordent plus sur le titre de la page, la cloche et les icônes, et défilent dans leur cadre.
- La pastille de focus n'est jamais coupée, du premier onglet au dernier.

---

#### v1.3.15 : Navigation TV plus fluide

- TV : l'accueil et le guide TV répondent plus vite à la télécommande.

---

#### v1.3.14 : Fenêtres en demi-écran, génériques

- Jellyfin 12, PC, fenêtres en demi-écran : l'espace vide réservé à l'image de fond a disparu, donc le logo se place sous la barre du haut et le bouton Lire remonte.
- PC : les fiches ne sautent plus quand le générique d'une série démarre ou s'arrête.

---

#### v1.3.13 : Pages de saison, téléphone

- Les pages de saison, d'épisode et d'album gardent leur image de fond lumineuse en haut, comme la page de série.
- Jellyfin 12, PC : plus de bande plus claire derrière la barre du haut sur ces pages.
- Téléphone, pages de saison, d'épisode et d'album : image de fond à pleine luminosité, logo juste sous l'image, plus d'espace vide entre le logo et le titre.
- Téléphone : le bouton Lire remonte sur les pages de film, de série, de saison, d'épisode et d'album.
- TV, pages de saison en 1080p : le titre de la série ne chevauche plus le logo.

---

#### v1.3.12 : Alignements, pastille « 99+ », barre de sélection

- Appui long sur une carte (mode sélection) : le bouton de fermeture, le compteur et le bouton ⋮ sont de nouveau blancs et visibles sur la barre bleu marine.
- Téléphone : les rangées horizontales s'alignent sur leur titre (accueil, favoris, fiches, recherche).
- Fiches : les grilles « À suivre », « Saisons », films d'acteur et albums d'artiste s'alignent sur leur titre.
- TV : les rangées de TV en direct et l'onglet « Suggestions » des bibliothèques s'alignent aussi sur leur titre.
- La pastille « 99+ » des non-vus s'élargit en gélule au lieu de toucher son cercle.

---

#### v1.3.11 : Page de connexion

- Jellyfin 12, PC : la page de connexion n'affiche plus de bande claire sous la barre du haut ni deux barres de défilement. La barre du haut est masquée sur la page de connexion seulement et revient une fois connecté.

---

#### v1.3.10 : Téléphone, toucher sur les fiches

- Jellyfin 12, téléphone : les pages de série, de saison et de film répondent de nouveau au toucher.
- Bibliothèques : le sélecteur A-Z reste à l'écran pendant le défilement.

---

#### v1.3.9 : Jellyfin Enhanced, icônes Letterboxd et Seerr

- Fiches : les icônes Letterboxd et Seerr ajoutées par Jellyfin Enhanced ressemblent aux logos IMDb, TVDB et TMDB et sont sur la même ligne.

---

#### v1.3.8 : Pages plus légères

- Vignettes : l'animation de chargement, qui laissait un léger voile blanc sur les images, est retirée (le module « Skeleton Loading » disparaît). Sur TV, les affiches retrouvent leurs vraies couleurs, noirs compris.
- Les pages demandent moins de travail à l'affichage.

---

#### v1.3.7 : Fiches, rangées alignées

- Fiches : les rangées (distribution, « Titres similaires », sections Jellyseerr) s'alignent sur le reste de la page.
- Jellyfin 12 : la flèche de défilement de droite de ces rangées est entièrement à l'écran, et la dernière affiche d'une rangée est entièrement visible.
- Téléphone et TV avec Jellyfin Enhanced : les sections Jellyseerr s'alignent sur les autres rangées et n'élargissent plus la page.
- Aperçu des sous-titres (Réglages › Sous-titres) : fond aux couleurs du thème.

---

#### v1.3.6 : Plus léger sur TV

- TV : le guide est plus léger à parcourir, avec le même aspect.

---

#### v1.3.5 : Jellyfin 12, la nouvelle interface rejoint la 10.11

- Barre du haut : le même en-tête cinéma en fondu que la 10.11, sans ombre au défilement.
- Accueil : les onglets Accueil et Favoris reviennent sous la barre du haut, et le lien Favoris en double quitte la barre du haut sur PC.
- Lien de la bibliothèque active : pastille violette à texte blanc.
- « Tout lire » et « Aléatoire » : texte et icônes sombres, et le séparateur entre les deux n'est plus bleu.
- Page des réglages d'affichage : champs, libellés, anneau de focus, titres de section et bouton Sauvegarder fixe comme en 10.11.
- Tous les éléments de la nouvelle interface utilisent la police du thème.
- Sélecteur A-Z : lettres atténuées, lettre choisie en blanc, plus de panneau gris.
- Interrupteurs et cases cochées au violet du thème.
- Les barres de reprise des cartes de bibliothèque sont blanches.
- Menus et fenêtre de filtres : surfaces bleu marine arrondies, focus clavier blanc, groupes de boutons en gélule, plus de panneaux gris.
- Tiroir du téléphone aligné sur l'ancien tiroir.
- Titres de section en blanc.
- Pages de bibliothèque : la bande vide sous la barre du haut a disparu.
- Couleurs rétablies partout, TV comprise : chiffres des badges et coche « vu » en blanc, niveaux du texte principal et secondaire.
- Info-bulles des icônes : verre bleu marine du thème.
- Survol des boutons, lettres A-Z et entrées de menu : violet au lieu de gris ; le nombre d'éléments d'une bibliothèque est une pastille violet foncé.
- Focus clavier : pastille blanche au lieu d'un cercle gris pulsant, ondulation violette au clic.
- Page de recherche : le titre « Suggestions » est centré au-dessus de sa liste.

---

#### v1.3.4 : Tizen 4.0, onglet Accueil

- Tizen 4.0 : l'onglet Accueil n'est plus coupé quand le focus passe sur Favoris.

---

#### v1.3.3 : Tizen 4.0, dispositions

- Tizen 4.0 : la barre de progression des cartes « Continuer à regarder » est de nouveau en bas de l'affiche.
- Tizen 4.0 : le bloc de titre et les sections des fiches sont à la bonne place et dans le bon ordre, et les onglets TV sont centrés verticalement.

---

#### v1.3.2 : Tizen 4.0, focus

- Tizen 4.0 : les indicateurs de sélection fonctionnent de nouveau (zoom des cartes, bouton Lire, avatar, boutons des fiches et de l'en-tête, liens, onglets, anneau des profils). Un bouton sélectionné pouvait être invisible.

---

#### v1.3.1 : TV, flous et anciens téléviseurs

- TV : les derniers flous permanents (compteurs des cartes, statistiques du lecteur, pieds de boîtes de dialogue) et le fondu de l'image de fond des fiches sont retirés, donc le défilement est plus léger.
- Tizen 4.0 à 7.0 : le cadre du guide TV retrouve sa bordure, son fond et ses coins arrondis, et l'affiche s'affiche sur les pages Casting, Livre et TV en direct.

---

#### v1.3.0 : Mini-bouton Lire du téléphone

- Téléphone : le mini-bouton Lire garde sa taille habituelle.

---

#### v1.2.99 : Badges de type de média, titre du lecteur

- Dossiers, albums photo, photos et vidéos personnelles : le badge de coin retrouve son ambre, son bleu ou son rouge.
- Lecteur : un long titre d'épisode s'affiche sur deux lignes au lieu de déborder.

---

#### v1.2.98 : Téléphone, un chemin vers l'accueil

- Téléphone : le bouton Accueil revient dans l'en-tête sur les pages de film et de série.

---

#### v1.2.97 : Audit

- Le mouvement réduit couvre maintenant toutes les animations (image de fond mobile, indicateur de chargement).
- TV : le dernier flou plein écran est retiré (il n'apparaissait qu'avec l'option Arrière-plans activée).

---

#### v1.2.96 : Téléphone, image de fond et texte

- Téléphone : sur les pages de film et de série, l'image de fond ne recouvre plus le texte.

---

#### v1.2.95 : Téléphone, barre du haut

- Téléphone : la barre du haut reste en place au défilement, donc elle ne peut plus rester coincée cachée.

---

#### v1.2.94 : Jellyfin 12, bloc des crédits

- Jellyfin 12 : le bloc des crédits (Genres, Réalisateur, Scénaristes, Studios) retrouve son style.

---

#### v1.2.93 : Note des critiques sur téléphone

- Téléphone : la note des critiques est masquée dans la ligne d'infos sous un titre. `--criticsRatingVisibility: block` la ramène.

---

#### v1.2.92 : Ménage

- Nettoyage interne, aucun changement visible.

---

#### v1.2.91 : Logo au-dessus du titre

- PC et mobile : le logo se place au-dessus du titre et ne tombe plus dessus ni sous la barre du haut. Le grand espace vide a disparu.

---

#### v1.2.89 : Jauge du bouton Passer

- TV : la jauge de compte à rebours du bouton Passer est revenue.

---

#### v1.2.88 : Icônes, bouton Passer sur TV

- Les livres, photos et albums photo affichent la bonne icône, et l'icône « info » en contour n'est plus pleine.
- TV : le bouton Passer l'intro apparaît tout de suite avec ses couleurs définitives, et la sélection se voit par un contour blanc.

---

#### v1.2.87 : Ménage

- Nettoyage interne, aucun changement visible.

---

#### v1.2.86 : Jellyfin 12, barre du haut

- Jellyfin 12 : plus de liseré sous la barre du haut.

---

#### v1.2.85 : Bouton principal, photo de profil

- Jellyfin 12 : le bouton d'action principal (par exemple « Tout lire ») est blanc et se lit mieux. Les variantes rouge et verte gardent leurs couleurs.
- Page de profil : la photo ne touche plus la barre du haut.

---

#### v1.2.84 : Première passe Jellyfin 12

- Jellyfin 12 : l'onglet actif, l'avatar du profil, le badge de bibliothèque et les liens suivent l'accent du thème.

---

#### v1.2.83 : TV, changements de page

- TV : plus de bande sombre en travers du fond à l'ouverture d'un épisode.

---

#### v1.2.82 : Firefox, dégradés

- Firefox : plus de fines lignes horizontales sur les vignettes des cartes et les dégradés.

---

#### v1.2.81 : Barre de lecture précise

- La barre de lecture est précise : un clic près du début ou de la fin se place au bon endroit, l'aperçu au survol est aligné et le curseur atteint les deux bouts. Le curseur de volume en profite aussi.
- Téléphone : le curseur de la barre de lecture reste agrandi.

---

#### v1.2.80 : TV, barre du haut

- TV : la barre du haut ne peut plus rester coincée cachée.

---

#### v1.2.79 : Ménage

- Nettoyage interne, aucun changement visible.

---

#### v1.2.78 : États du bouton Passer, en-tête plus fin sur mobile

- Passer l'intro : le libellé ne disparaît plus au survol de la souris. Les états survol et appui utilisent la pastille blanche, et le halo de focus s'affiche.
- TV : plus de zoom au survol du bouton Passer.
- Téléphone : moins d'espace vide sous la rangée d'onglets de l'en-tête.

---

#### v1.2.77 : Logo Editor's Choice sur petit écran

- Editor's Choice : le logo du titre garde ses proportions sur petit écran.

---

#### v1.2.76 : En-tête PC plus fin

- PC : l'en-tête est plus fin, et les contrôles Editor's Choice se placent juste dessous.

---

#### v1.2.75 : Contrôles Editor's Choice en plein écran

- PC, fenêtres larges : les contrôles Editor's Choice dégagent la barre du haut.

---

#### v1.2.74 : Bouton Passer, curseur de texte, focus clavier

- Passer l'intro : le bouton est bleu marine à libellé blanc, et sa jauge se lit comme un remplissage violet. Le focus le rend toujours blanc.
- PC : un curseur de texte clignotant parasite n'apparaît plus sur le bouton lecture/pause du lecteur.
- PC, clavier : naviguer à la touche Tab affiche les mêmes indicateurs de focus qu'à la télécommande TV.

---

#### v1.2.73 : Contrôles Editor's Choice

- Editor's Choice : les contrôles ‹ ❚❚ › s'affichent en pastilles rondes bleu marine sous la barre du haut, en haut à droite.
- Les flèches de rangée des autres sections ne couvrent plus la bannière.

---

#### v1.2.72 : Flèches Editor's Choice

- Editor's Choice : deuxième étape pour dégager les contrôles de sous l'en-tête (terminée en v1.2.73).

---

#### v1.2.71 : Flèches Editor's Choice sur PC

- PC : première étape pour rendre ses flèches à la bannière Editor's Choice (terminée en v1.2.73).

---

#### v1.2.70 : Focus du bouton Lire et de l'avatar

- TV : le bouton Lire s'inverse quand il est sélectionné (fond bleu marine, texte blanc, anneau blanc).
- TV : l'avatar du profil affiche un épais anneau blanc quand il est sélectionné.

---

#### v1.2.69 : Focus du bouton Passer

- TV : le bouton Passer l'intro affiche un contour blanc quand il est sélectionné.

---

#### v1.2.68 : Titre original

- TV et mobile : le titre original (japonais) n'est plus coupé à droite.

---

#### v1.2.67 : Polices plus légères

- Polices beaucoup plus légères avec le même rendu, donc des premiers chargements plus rapides.

---

#### v1.2.66 : Focus du titre de série

- TV : le titre de série sélectionné n'est plus blanc sur blanc.

---

#### v1.2.65 : Titre de série

- Pages de saison et d'épisode : le titre de série prend le même format que la ligne « Saison X - Épisode », sur TV, PC et mobile, avec ou sans logo.

---

#### v1.2.64 : Badge de version

- Le badge de version en bas de la page Préférences se lit mieux.

---

#### v1.2.63 : Titre de série sur toutes les plateformes

- Pages de saison et d'épisode : le titre de série correspond à la ligne « Saison X - Épisode » (taille et graisse) sur TV, PC et mobile, et reste cliquable.

---

#### v1.2.62 : Titre de série sur les pages de saison et d'épisode

- TV, pages de saison et d'épisode : le nom de la série partage le format de la ligne en dessous et reste cliquable.

---

#### v1.2.61 : Correctifs de l'ElegantFin d'origine

- PC : le bouton de menu ⋮ revient au survol des cartes et sur les lignes de liste.
- Jellyfin Enhanced : les critiques TMDB ne débordent plus de la fiche, et les liens externes (Radarr/Sonarr, Letterboxd) prennent le style de liens du thème.
- Pages de réglages : le bouton Sauvegarder reste visible.
- Firefox : le curseur de la barre de lecture réagit au survol, au glissement et au focus comme sur Chrome.
- iPhone : le menu hamburger couvre toute la hauteur de l'écran, et plusieurs défauts de menus sont corrigés.
- Les icônes ne clignotent plus en texte invisible pendant le chargement.
- Musique : espacement des listes de pistes et des titres de disque, rangée de distribution plus proche de son titre.
- La police d'icônes est mise à jour pour couvrir les icônes Jellyfin plus récentes.

---

#### v1.2.60 : Fichier plus léger, tags de version

- Le fichier du thème est plus léger à télécharger.
- Chaque version est taguée : vous pouvez figer une version (par exemple `@v1.2.60`) dans votre URL d'import et revenir en arrière.
- Les licences des polices sont incluses.

---


> 🗄️ Les versions anterieures a la v1.2.60 sont dans [`RELEASE_NOTES_ARCHIVE.md`](./RELEASE_NOTES_ARCHIVE.md).

---

### Compatibilite
- Jellyfin **10.11.x** et **12.x** (teste sur la 12.1, nouvelle interface et interface legacy)
- Fonctionne sur tous les navigateurs web (Chrome, Edge, Firefox, Safari), application Android, LG WebOS, Samsung Tizen
- Fallback `@supports` complet pour les navigateurs sans `backdrop-filter`
