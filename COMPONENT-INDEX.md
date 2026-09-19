# Index des composants — ElegantFin Cinema Edition v1.3.5

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.5.css` — 7241 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 36 | 14 | 411–493, 731, 834, 1480–1500, 2003–2036, 2063–2067, 2342–2360, 2396, 6193, 6480–6496, 6576–6598, 6628–6635, 6709, 7119 |
| `cardScalable` | 28 | 13 | 411–422, 470–493, 780–824, 850–888, 2360, 3303, 3414, 3493, 5406, 6207–6217, 6286, 6480, 6619–6635 |
| `cardImageContainer` | 23 | 13 | 465, 802, 830–859, 888, 945–975, 5515–5519, 5600, 6199, 6278–6286, 6339, 6480–6496, 6619, 6757 |
| `material-icons` | 16 | 12 | 347–366, 1699, 1758, 1810, 3260, 3419, 3493–3499, 3605, 3763, 4145, 4630, 4664–4674 |
| `itemDetailPage` | 18 | 11 | 1543, 1629, 1708, 1929–1954, 1998, 2098, 2409–2414, 3748–3759, 4239, 4527, 6947–6985 |
| `nameContainer` | 27 | 9 | 677, 2105–2128, 2169, 2198, 2233–2279, 2316, 2347–2351, 5003–5055, 6947–6985 |
| `skinHeader` | 16 | 9 | 275, 3978–4030, 5414, 5803, 5859–5867, 5893–5918, 6269, 6448, 7056 |
| `backdropCard` | 12 | 9 | 932–938, 1053, 1929, 2015, 2098, 2351–2360, 2387, 2414, 2684 |
| `card-hoverable` | 23 | 8 | 493, 790, 850–938, 5519, 6217, 6367–6386, 6480, 6764 |
| `parentName` | 23 | 8 | 677, 2110–2128, 2169, 2198, 2233–2279, 5009–5055, 5128, 6947–6985 |
| `detailPageWrapperContainer` | 17 | 8 | 677, 1511–1521, 1954, 2072, 2105–2128, 2198, 2233–2279, 2347 |
| `subtitle` | 16 | 8 | 1929, 1998, 2110, 2169, 2288–2298, 2409–2414, 5063–5096, 6947–6985 |
| `cardBox` | 12 | 8 | 411–459, 485, 731, 872, 979, 6193, 6480, 6764 |
| `detailLogo` | 17 | 7 | 677, 1943–1954, 1989–1998, 2098–2128, 2198, 2233–2279, 2347 |
| `loginPage` | 15 | 7 | 3572, 5418–5433, 5472, 5500–5519, 6222, 6265, 6608–6635 |
| `emby-button` | 10 | 7 | 603–620, 647–665, 3062–3069, 3439, 3474, 3627, 4163 |
| `js` | 7 | 7 | 314, 1615, 2169, 2761, 3393, 6395, 6645 |
| `listItem` | 17 | 6 | 293, 620, 2364, 4065–4091, 4122–4154, 6732–6749 |
| `navMenuOption` | 12 | 6 | 620, 716–726, 3813, 4132–4154, 4220–4225, 6519–6530 |
| `verticalSection` | 11 | 6 | 1703, 2580–2585, 4527, 6278, 6395, 6645 |
| `nowPlayingBar` | 8 | 6 | 2947, 5652, 6232, 6326, 6429–6460, 6714 |
| `person` | 8 | 6 | 1929–1939, 2098, 2351, 2396–2405, 3700, 6942 |
| `mainDrawer` | 7 | 6 | 2911, 3777, 4003, 6222–6232, 6506, 6545 |
| `detailImageContainer` | 20 | 5 | 1929–1939, 2003–2067, 2098, 2338–2360, 2387–2414 |
| `osdHeader` | 15 | 5 | 1672–1690, 5798–5867, 5893–5918, 6269, 6714 |
| `actionSheetMenuItem` | 11 | 5 | 620, 4065–4076, 4122, 4200–4216, 6250 |
| `sectionTabs` | 10 | 5 | 1727, 3551, 4030, 5839–5844, 5984–6010 |
| `button-link` | 9 | 5 | 620, 647–665, 2897–2906, 2967–2977, 6910 |
| `cardImageIcon` | 8 | 5 | 403–407, 2351–2360, 2420, 3287, 5600 |
| `paper-icon-button-light` | 8 | 5 | 565–620, 1629, 1699, 1758, 4922 |
| `emby-scroller-container` | 7 | 5 | 1703–1716, 2570, 2606, 6278, 6395 |
| `sectionTitle` | 7 | 5 | 1703, 1737–1744, 3879, 4600–4608, 5467 |
| `portraitCard` | 5 | 5 | 1053, 1131, 1848, 2063, 2684 |
| `scss` | 5 | 5 | 275, 759, 1005, 3309, 6395 |
| `skinHeader-withBackground` | 5 | 5 | 1611, 3748, 5414, 5798, 5848 |
| `btnPlay` | 16 | 4 | 502–526, 565–620, 3503–3545, 3578–3605 |
| `cardOverlayContainer` | 12 | 4 | 906–938, 983–1005, 1065, 6714–6732 |
| `itemName` | 11 | 4 | 677, 2169, 5009–5055, 5146–5163 |
| `backdropImage` | 10 | 4 | 2486–2513, 2540–2544, 6186, 6286–6294 |
| `emby-tab-button` | 10 | 4 | 620, 687–696, 3551, 5969–6005 |
| `upNextContainer` | 10 | 4 | 4692–4711, 4737–4763, 6222–6232, 6258 |
| `headerTop` | 8 | 4 | 3978–4003, 5809–5834, 5885–5902, 5929–5933 |
| `detailRibbon` | 7 | 4 | 1568–1596, 1763, 1848–1853, 6942 |
| `listItemBodyText` | 7 | 4 | 4086–4105, 4145, 4204, 6749 |
| `visualCardBox` | 7 | 4 | 411, 811–824, 850–855, 979 |
| `button-submit` | 6 | 4 | 3572, 3659, 5500–5508, 6822–6836 |
| `cardText-secondary` | 6 | 4 | 293, 893, 3292–3296, 6373–6381 |
| `detailPagePrimaryContent` | 6 | 4 | 1583–1601, 2303, 4521, 6464 |
| `skip-button` | 6 | 4 | 620, 3556, 4786–4803, 4830–4836 |
| `squareCard` | 6 | 4 | 834, 2351, 2387–2405, 5476–5480 |
| `skinHeader-blurred` | 5 | 4 | 5414, 5827–5834, 6448, 6714 |
| `appfooter` | 4 | 4 | 2627, 5943, 6309, 6714 |
| `page` | 4 | 4 | 975, 2561, 2606, 6278 |
| `raised` | 4 | 4 | 620, 706, 3439, 3474 |
| `detailButton` | 13 | 3 | 565–620, 3484–3545, 3601–3605 |
| `emby-scroller` | 9 | 3 | 1708–1722, 6551–6598, 6700–6709 |
| `itemBackdrop` | 9 | 3 | 1895–1939, 2072, 2414 |
| `itemSelectionPanel` | 9 | 3 | 863–867, 3232, 3260–3303 |
| `check` | 8 | 3 | 3260, 3493, 4196–4216 |
| `pageTitle` | 8 | 3 | 1647–1690, 5859, 5918 |
| `sectionTitleTextButton` | 8 | 3 | 4583–4591, 4618–4630, 4664–4674 |
| `playedIndicator` | 7 | 3 | 759–773, 3376, 6480–6501 |
| `countIndicator` | 6 | 3 | 750–773, 6320, 6771–6795 |
| `detailSectionContent` | 6 | 3 | 3094, 4321–4331, 4412–4422 |
| `emby-checkbox` | 6 | 3 | 3237, 3274–3278, 3327–3339 |
| `actionSheetContent` | 5 | 3 | 4188–4192, 6222–6232, 6258 |
| `cardText-first` | 5 | 3 | 893, 3266–3292, 5581 |
| `dialog` | 5 | 3 | 3144–3154, 6222–6232, 6258 |
| `guideProgramName` | 5 | 3 | 620, 5187–5198, 5241–5246 |
| `musicParentName` | 5 | 3 | 1929, 2409–2414, 5128–5137 |
| `noHomeButtonHeader` | 5 | 3 | 1629, 5859, 5969–5977 |
| `overflowBackdropCard` | 5 | 3 | 932–938, 3270, 5576–5581 |
| `secondary` | 5 | 3 | 293, 4095–4105, 4145 |
| `album` | 4 | 3 | 2098, 2356–2360, 2396 |
| `cardPadder` | 4 | 3 | 407, 979, 3283–3287 |
| `cardText` | 4 | 3 | 893–903, 3292, 6624 |
| `dialog-fullscreen` | 4 | 3 | 3154, 6222–6232, 6258 |
| `emby-scrollbuttons` | 4 | 3 | 1749–1754, 6645, 7094 |
| `formDialogFooter` | 4 | 3 | 3212, 3666, 6771–6795 |
| `infoWrapper` | 4 | 3 | 2042–2047, 2303, 2331 |
| `listItemImage` | 4 | 3 | 2661–2666, 4059, 6749 |
| `semiTransparent` | 4 | 3 | 1611, 5414, 5827–5848 |
| `toast` | 4 | 3 | 4684, 6222–6232, 6258 |
| `defaultCardBackground` | 3 | 3 | 3414, 5596, 5695 |
| `folder` | 3 | 3 | 1848, 3393, 3457 |
| `formDialogFooterItem` | 3 | 3 | 3212, 3452, 3578 |
| `formDialogHeader` | 3 | 3 | 3666, 6714, 6771 |
| `iconOsd` | 3 | 3 | 5392, 6714, 6771 |
| `itemsContainer` | 3 | 3 | 731, 1731, 4527 |
| `live_tv` | 3 | 3 | 1929, 2396, 3700 |
| `myPreferencesMenuPage` | 3 | 3 | 380, 4230, 4535 |
| `playerStats` | 3 | 3 | 5392, 6771, 6807 |
| `sectionTitle-cards` | 3 | 3 | 1703, 4600, 4660 |
| `x` | 3 | 3 | 2169, 5111, 6395 |
| `itemExternalLinks` | 11 | 2 | 2960–3017, 3094 |
| `checkboxOutline` | 10 | 2 | 3237–3278, 3309–3339 |
| `mdl-slider` | 9 | 2 | 2757, 2812–2870 |
| `listItemIcon` | 8 | 2 | 3696–3700, 4200–4230 |
| `sliderContainer` | 8 | 2 | 2761, 2789–2854 |
| `cardOverlayButton-br` | 7 | 2 | 991, 1020–1058 |
| `detail-clamp-text` | 7 | 2 | 3030–3056, 3082–3086 |
| `divUsers` | 7 | 2 | 5476–5480, 6608–6635 |
| `homePage` | 7 | 2 | 3978–4030, 6027 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3274–3278, 3308–3327 |
| `backgroundContainer` | 6 | 2 | 2476, 2518–2536 |
| `detailPagePrimaryContainer` | 6 | 2 | 1555–1601, 2303 |
| `detailsGroupItem` | 6 | 2 | 4283, 4351–4389 |
| `headerButton` | 6 | 2 | 540–620, 5911 |
| `headerLeft` | 6 | 2 | 1653–1690, 6114 |
| `trackSelections` | 6 | 2 | 4256–4283, 4417–4422 |
| `withBackdrop` | 6 | 2 | 2476, 2518–2536 |
| `detailSection` | 5 | 2 | 4239–4248, 4402–4422 |
| `fullSyncIndicator` | 5 | 2 | 750–773, 6771–6795 |
| `mainDrawer-scrollContainer` | 5 | 2 | 2920, 6519–6536 |
| `mediaInfoItem` | 5 | 2 | 1767–1810, 6395 |
| `overview-expand` | 5 | 2 | 3062–3086, 4321 |
| `videoIndicator` | 5 | 2 | 3382–3410, 6771 |
| `withSectionTabs` | 5 | 2 | 2527–2544, 5834 |
| `alphaPickerButton` | 4 | 2 | 620, 4461–4473 |
| `backgroundProgress` | 4 | 2 | 2672–2684, 2714 |
| `emby-tab-button-active` | 4 | 2 | 3638, 5996–6010 |
| `mediaSourceIndicator` | 4 | 2 | 750–773, 6771 |
| `play_arrow` | 4 | 2 | 3419–3435, 3605 |
| `playbackProgress` | 4 | 2 | 2672–2684, 2719 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4086–4091, 5689–5695 |
| `programCell` | 4 | 2 | 5178, 5237–5246 |
| `programGuideSection` | 4 | 2 | 2364–2379, 4422–4437 |
| `section0` | 4 | 2 | 945–975, 6278 |
| `visualLoginForm` | 4 | 2 | 5467–5484, 5525 |
| `cardFooter` | 3 | 2 | 3303, 6367–6386 |
| `cardOverlayButtonIcon` | 3 | 2 | 991–1003, 1058 |
| `castCollapsible` | 3 | 2 | 802, 3278–3287 |
| `detailPageContent` | 3 | 2 | 4252, 4514–4521 |
| `emby-input` | 3 | 2 | 4936–4952, 6836 |
| `emby-scrollbuttons-button` | 3 | 2 | 1758, 7101–7108 |
| `guestCastContent` | 3 | 2 | 802, 3278–3287 |
| `guide-channelHeaderCell` | 3 | 2 | 620, 5212–5228 |
| `guide-date-tab-button` | 3 | 2 | 620, 3638–3646 |
| `headerUserButton` | 3 | 2 | 540–553, 4539 |
| `manualLoginForm` | 3 | 2 | 5467–5484, 5525 |
| `overview` | 3 | 2 | 3082–3086, 4331 |
| `selectionCommandsPanel` | 3 | 2 | 3222–3228, 6714 |
| `backdropImageFadeIn` | 2 | 2 | 2611, 6811 |
| `blurhash-canvas` | 2 | 2 | 6339, 6757 |
| `book` | 2 | 2 | 1929, 2396 |
| `btnDeleteImage` | 2 | 2 | 3439, 3652 |
| `cardContent` | 2 | 2 | 802, 834 |
| `cardImage` | 2 | 2 | 6339, 6757 |
| `cardOverlayButton` | 2 | 2 | 1005, 1041 |
| `cardOverlayButton-hover` | 2 | 2 | 888, 1020 |
| `chevron_right` | 2 | 2 | 4630, 4674 |
| `collapseContent` | 2 | 2 | 3217, 3664 |
| `content-primary` | 2 | 2 | 4514, 4566 |
| `detailPageSecondaryContainer` | 2 | 2 | 1578, 1605 |
| `editorsChoiceItemOverview` | 2 | 2 | 7031, 7112 |
| `emby-select` | 2 | 2 | 4936, 6836 |
| `endsAt` | 2 | 2 | 1788, 6395 |
| `fieldDescription` | 2 | 2 | 293, 6836 |
| `formDialogFooter-clear` | 2 | 2 | 3212, 3666 |
| `guide-programNameCaret` | 2 | 2 | 293, 5194 |
| `headroom` | 2 | 2 | 5822, 5859 |
| `mediaInfoOfficialRating` | 2 | 2 | 1788, 6395 |
| `navMenuOption-selected` | 2 | 2 | 4235, 6530 |
| `nowPlayingInfoContainer` | 2 | 2 | 2951, 5626 |
| `org` | 2 | 2 | 2987, 3017 |
| `paperList` | 2 | 2 | 811, 3677 |
| `playlist` | 2 | 2 | 4081, 5604 |
| `queue` | 2 | 2 | 1929, 2396 |
| `readOnlyContent` | 2 | 2 | 3708, 6043 |
| `recordingFields` | 2 | 2 | 4275, 4417 |
| `runtime` | 2 | 2 | 5537, 5566 |
| `sectionTitleContainer` | 2 | 2 | 1754, 4446 |
| `sectionTitleContainer-cards` | 2 | 2 | 4595, 4660 |
| `sidebarHeader` | 2 | 2 | 3800, 6536 |
| `tagline` | 2 | 2 | 2467, 4331 |
| `tsx` | 2 | 2 | 3978, 4034 |
| `upNextDialog-title` | 2 | 2 | 4716, 4750 |
| `vertical-list` | 2 | 2 | 1731, 6937 |
| `videoOsdBottom` | 2 | 2 | 2943, 5789 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 2943, 5789 |
| `userPreferencesPage` | 12 | 1 | 6822–6917 |
| `checkboxContainer` | 7 | 1 | 3266–3303 |
| `itemDetailsGroup` | 7 | 1 | 4335–4422 |
| `itemProgressBar` | 6 | 1 | 2661–2695 |
| `trackSelectionFieldContainer` | 6 | 1 | 4294–4317 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7068–7108 |
| `innerCardFooter` | 5 | 1 | 3107–3136 |
| `chapterCardImageContainer` | 4 | 1 | 3107–3136 |
| `endTimeText` | 4 | 1 | 5537–5566 |
| `mainDetailButtons` | 4 | 1 | 3601–3615 |
| `overview-controls` | 4 | 1 | 3082–3094 |
| `scrollX` | 4 | 1 | 1708–1727 |
| `startTimeText` | 4 | 1 | 5537–5560 |
| `button-flat` | 3 | 1 | 2924–2934 |
| `cardIndicators` | 3 | 1 | 3356–3366 |
| `cardOverlayFab-primary` | 3 | 1 | 983–1005 |
| `com` | 3 | 1 | 2993–3011 |
| `content` | 3 | 1 | 4358–4389 |
| `discover-card` | 3 | 1 | 7119–7142 |
| `emby-select-withcolor` | 3 | 1 | 4936–4970 |
| `emby-textarea` | 3 | 1 | 4927–4952 |
| `fab` | 3 | 1 | 3461–3474 |
| `listChildrenCollapsible` | 3 | 1 | 4407–4422 |
| `mdl-slider-background-flex` | 3 | 1 | 2781–2794 |
| `mediaInfoCriticRating` | 3 | 1 | 1829–1838 |
| `nextUpSection` | 3 | 1 | 4402–4422 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 5590–5600 |
| `serverInfo` | 3 | 1 | 3681–3690 |
| `transcodingProgress` | 3 | 1 | 2672–2684 |
