# Index des composants — ElegantFin Cinema Edition v1.3.4

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.4.css` — 6857 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 36 | 14 | 411–493, 731, 834, 1480–1500, 2003–2036, 2063–2067, 2342–2360, 2396, 5904, 6191–6207, 6287–6309, 6339–6346, 6420, 6735 |
| `cardScalable` | 28 | 13 | 411–422, 470–493, 780–824, 850–888, 2360, 3303, 3414, 3493, 5159, 5918–5928, 5997, 6191, 6330–6346 |
| `cardImageContainer` | 23 | 13 | 465, 802, 830–859, 888, 945–975, 5268–5272, 5353, 5910, 5989–5997, 6050, 6191–6207, 6330, 6468 |
| `material-icons` | 15 | 11 | 347–366, 1699, 1758, 1810, 3260, 3419, 3493–3499, 3605, 3950, 4425, 4459–4469 |
| `itemDetailPage` | 16 | 10 | 1543, 1629, 1708, 1929–1954, 1998, 2098, 2409–2414, 4044, 4332, 6563–6601 |
| `nameContainer` | 27 | 9 | 677, 2105–2128, 2169, 2198, 2233–2279, 2316, 2347–2351, 4798–4850, 6563–6601 |
| `backdropCard` | 12 | 9 | 932–938, 1053, 1929, 2015, 2098, 2351–2360, 2387, 2414, 2684 |
| `card-hoverable` | 23 | 8 | 493, 790, 850–938, 5272, 5928, 6078–6097, 6191, 6475 |
| `parentName` | 23 | 8 | 677, 2110–2128, 2169, 2198, 2233–2279, 4804–4850, 4923, 6563–6601 |
| `detailPageWrapperContainer` | 17 | 8 | 677, 1511–1521, 1954, 2072, 2105–2128, 2198, 2233–2279, 2347 |
| `subtitle` | 16 | 8 | 1929, 1998, 2110, 2169, 2288–2298, 2409–2414, 4858–4891, 6563–6601 |
| `cardBox` | 12 | 8 | 411–459, 485, 731, 872, 979, 5904, 6191, 6475 |
| `skinHeader` | 12 | 8 | 275, 5167, 5517, 5573–5581, 5607–5632, 5980, 6159, 6672 |
| `detailLogo` | 17 | 7 | 677, 1943–1954, 1989–1998, 2098–2128, 2198, 2233–2279, 2347 |
| `loginPage` | 15 | 7 | 3572, 5171–5186, 5225, 5253–5272, 5933, 5976, 6319–6346 |
| `emby-button` | 10 | 7 | 603–620, 647–665, 3062–3069, 3439, 3474, 3627, 3968 |
| `js` | 7 | 7 | 314, 1615, 2169, 2761, 3393, 6106, 6356 |
| `listItem` | 17 | 6 | 293, 620, 2364, 3870–3896, 3927–3959, 6443–6460 |
| `navMenuOption` | 12 | 6 | 620, 716–726, 3759, 3937–3959, 4025–4030, 6230–6241 |
| `verticalSection` | 11 | 6 | 1703, 2580–2585, 4332, 5989, 6106, 6356 |
| `nowPlayingBar` | 8 | 6 | 2947, 5405, 5943, 6037, 6140–6171, 6425 |
| `person` | 8 | 6 | 1929–1939, 2098, 2351, 2396–2405, 3700, 6558 |
| `detailImageContainer` | 20 | 5 | 1929–1939, 2003–2067, 2098, 2338–2360, 2387–2414 |
| `osdHeader` | 15 | 5 | 1672–1690, 5512–5581, 5607–5632, 5980, 6425 |
| `actionSheetMenuItem` | 11 | 5 | 620, 3870–3881, 3927, 4005–4021, 5961 |
| `cardImageIcon` | 8 | 5 | 403–407, 2351–2360, 2420, 3287, 5353 |
| `paper-icon-button-light` | 8 | 5 | 565–620, 1629, 1699, 1758, 4717 |
| `emby-scroller-container` | 7 | 5 | 1703–1716, 2570, 2606, 5989, 6106 |
| `mainDrawer` | 6 | 5 | 2911, 3723, 5933–5943, 6217, 6256 |
| `sectionTitle` | 6 | 5 | 1703, 1737–1744, 3796, 4405, 5220 |
| `portraitCard` | 5 | 5 | 1053, 1131, 1848, 2063, 2684 |
| `scss` | 5 | 5 | 275, 759, 1005, 3309, 6106 |
| `btnPlay` | 16 | 4 | 502–526, 565–620, 3503–3545, 3578–3605 |
| `cardOverlayContainer` | 12 | 4 | 906–938, 983–1005, 1065, 6425–6443 |
| `itemName` | 11 | 4 | 677, 2169, 4804–4850, 4941–4958 |
| `backdropImage` | 10 | 4 | 2486–2513, 2540–2544, 5897, 5997–6005 |
| `emby-tab-button` | 10 | 4 | 620, 687–696, 3551, 5683–5719 |
| `upNextContainer` | 10 | 4 | 4487–4506, 4532–4558, 5933–5943, 5969 |
| `sectionTabs` | 9 | 4 | 1727, 3551, 5553–5558, 5698–5724 |
| `button-link` | 8 | 4 | 620, 647–665, 2897–2906, 2967–2977 |
| `detailRibbon` | 7 | 4 | 1568–1596, 1763, 1848–1853, 6558 |
| `listItemBodyText` | 7 | 4 | 3891–3910, 3950, 4009, 6460 |
| `visualCardBox` | 7 | 4 | 411, 811–824, 850–855, 979 |
| `cardText-secondary` | 6 | 4 | 293, 893, 3292–3296, 6084–6092 |
| `detailPagePrimaryContent` | 6 | 4 | 1583–1601, 2303, 4326, 6175 |
| `skip-button` | 6 | 4 | 620, 3556, 4581–4598, 4625–4631 |
| `squareCard` | 6 | 4 | 834, 2351, 2387–2405, 5229–5233 |
| `button-submit` | 5 | 4 | 3572, 3659, 5253–5261, 6533 |
| `skinHeader-blurred` | 5 | 4 | 5167, 5541–5548, 6159, 6425 |
| `appfooter` | 4 | 4 | 2627, 5657, 6020, 6425 |
| `page` | 4 | 4 | 975, 2561, 2606, 5989 |
| `raised` | 4 | 4 | 620, 706, 3439, 3474 |
| `skinHeader-withBackground` | 4 | 4 | 1611, 5167, 5512, 5562 |
| `detailButton` | 13 | 3 | 565–620, 3484–3545, 3601–3605 |
| `emby-scroller` | 9 | 3 | 1708–1722, 6262–6309, 6411–6420 |
| `itemBackdrop` | 9 | 3 | 1895–1939, 2072, 2414 |
| `itemSelectionPanel` | 9 | 3 | 863–867, 3232, 3260–3303 |
| `check` | 8 | 3 | 3260, 3493, 4001–4021 |
| `pageTitle` | 8 | 3 | 1647–1690, 5573, 5632 |
| `playedIndicator` | 7 | 3 | 759–773, 3376, 6191–6212 |
| `countIndicator` | 6 | 3 | 750–773, 6031, 6482–6506 |
| `detailSectionContent` | 6 | 3 | 3094, 4126–4136, 4217–4227 |
| `emby-checkbox` | 6 | 3 | 3237, 3274–3278, 3327–3339 |
| `headerTop` | 6 | 3 | 5523–5548, 5599–5616, 5643–5647 |
| `actionSheetContent` | 5 | 3 | 3993–3997, 5933–5943, 5969 |
| `cardText-first` | 5 | 3 | 893, 3266–3292, 5334 |
| `dialog` | 5 | 3 | 3144–3154, 5933–5943, 5969 |
| `guideProgramName` | 5 | 3 | 620, 4982–4993, 5036–5041 |
| `musicParentName` | 5 | 3 | 1929, 2409–2414, 4923–4932 |
| `noHomeButtonHeader` | 5 | 3 | 1629, 5573, 5683–5691 |
| `overflowBackdropCard` | 5 | 3 | 932–938, 3270, 5329–5334 |
| `secondary` | 5 | 3 | 293, 3900–3910, 3950 |
| `album` | 4 | 3 | 2098, 2356–2360, 2396 |
| `cardPadder` | 4 | 3 | 407, 979, 3283–3287 |
| `cardText` | 4 | 3 | 893–903, 3292, 6335 |
| `dialog-fullscreen` | 4 | 3 | 3154, 5933–5943, 5969 |
| `emby-scrollbuttons` | 4 | 3 | 1749–1754, 6356, 6710 |
| `formDialogFooter` | 4 | 3 | 3212, 3666, 6482–6506 |
| `infoWrapper` | 4 | 3 | 2042–2047, 2303, 2331 |
| `listItemImage` | 4 | 3 | 2661–2666, 3864, 6460 |
| `semiTransparent` | 4 | 3 | 1611, 5167, 5541–5562 |
| `toast` | 4 | 3 | 4479, 5933–5943, 5969 |
| `defaultCardBackground` | 3 | 3 | 3414, 5349, 5448 |
| `folder` | 3 | 3 | 1848, 3393, 3457 |
| `formDialogFooterItem` | 3 | 3 | 3212, 3452, 3578 |
| `formDialogHeader` | 3 | 3 | 3666, 6425, 6482 |
| `iconOsd` | 3 | 3 | 5145, 6425, 6482 |
| `itemsContainer` | 3 | 3 | 731, 1731, 4332 |
| `live_tv` | 3 | 3 | 1929, 2396, 3700 |
| `myPreferencesMenuPage` | 3 | 3 | 380, 4035, 4340 |
| `playerStats` | 3 | 3 | 5145, 6482, 6518 |
| `sectionTitle-cards` | 3 | 3 | 1703, 4405, 4455 |
| `x` | 3 | 3 | 2169, 4906, 6106 |
| `itemExternalLinks` | 11 | 2 | 2960–3017, 3094 |
| `checkboxOutline` | 10 | 2 | 3237–3278, 3309–3339 |
| `mdl-slider` | 9 | 2 | 2757, 2812–2870 |
| `listItemIcon` | 8 | 2 | 3696–3700, 4005–4035 |
| `sectionTitleTextButton` | 8 | 2 | 4388–4425, 4459–4469 |
| `sliderContainer` | 8 | 2 | 2761, 2789–2854 |
| `cardOverlayButton-br` | 7 | 2 | 991, 1020–1058 |
| `detail-clamp-text` | 7 | 2 | 3030–3056, 3082–3086 |
| `divUsers` | 7 | 2 | 5229–5233, 6319–6346 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3274–3278, 3308–3327 |
| `backgroundContainer` | 6 | 2 | 2476, 2518–2536 |
| `detailPagePrimaryContainer` | 6 | 2 | 1555–1601, 2303 |
| `detailsGroupItem` | 6 | 2 | 4088, 4156–4194 |
| `headerButton` | 6 | 2 | 540–620, 5625 |
| `headerLeft` | 6 | 2 | 1653–1690, 5825 |
| `trackSelections` | 6 | 2 | 4061–4088, 4222–4227 |
| `withBackdrop` | 6 | 2 | 2476, 2518–2536 |
| `detailSection` | 5 | 2 | 4044–4053, 4207–4227 |
| `fullSyncIndicator` | 5 | 2 | 750–773, 6482–6506 |
| `mainDrawer-scrollContainer` | 5 | 2 | 2920, 6230–6247 |
| `mediaInfoItem` | 5 | 2 | 1767–1810, 6106 |
| `overview-expand` | 5 | 2 | 3062–3086, 4126 |
| `videoIndicator` | 5 | 2 | 3382–3410, 6482 |
| `withSectionTabs` | 5 | 2 | 2527–2544, 5548 |
| `alphaPickerButton` | 4 | 2 | 620, 4266–4278 |
| `backgroundProgress` | 4 | 2 | 2672–2684, 2714 |
| `emby-tab-button-active` | 4 | 2 | 3638, 5710–5724 |
| `mediaSourceIndicator` | 4 | 2 | 750–773, 6482 |
| `play_arrow` | 4 | 2 | 3419–3435, 3605 |
| `playbackProgress` | 4 | 2 | 2672–2684, 2719 |
| `playlistIndexIndicatorImage` | 4 | 2 | 3891–3896, 5442–5448 |
| `programCell` | 4 | 2 | 4973, 5032–5041 |
| `programGuideSection` | 4 | 2 | 2364–2379, 4227–4242 |
| `section0` | 4 | 2 | 945–975, 5989 |
| `visualLoginForm` | 4 | 2 | 5220–5237, 5278 |
| `cardFooter` | 3 | 2 | 3303, 6078–6097 |
| `cardOverlayButtonIcon` | 3 | 2 | 991–1003, 1058 |
| `castCollapsible` | 3 | 2 | 802, 3278–3287 |
| `detailPageContent` | 3 | 2 | 4057, 4319–4326 |
| `emby-scrollbuttons-button` | 3 | 2 | 1758, 6717–6724 |
| `guestCastContent` | 3 | 2 | 802, 3278–3287 |
| `guide-channelHeaderCell` | 3 | 2 | 620, 5007–5023 |
| `guide-date-tab-button` | 3 | 2 | 620, 3638–3646 |
| `headerUserButton` | 3 | 2 | 540–553, 4344 |
| `manualLoginForm` | 3 | 2 | 5220–5237, 5278 |
| `overview` | 3 | 2 | 3082–3086, 4136 |
| `selectionCommandsPanel` | 3 | 2 | 3222–3228, 6425 |
| `backdropImageFadeIn` | 2 | 2 | 2611, 6522 |
| `blurhash-canvas` | 2 | 2 | 6050, 6468 |
| `book` | 2 | 2 | 1929, 2396 |
| `btnDeleteImage` | 2 | 2 | 3439, 3652 |
| `cardContent` | 2 | 2 | 802, 834 |
| `cardImage` | 2 | 2 | 6050, 6468 |
| `cardOverlayButton` | 2 | 2 | 1005, 1041 |
| `cardOverlayButton-hover` | 2 | 2 | 888, 1020 |
| `chevron_right` | 2 | 2 | 4425, 4469 |
| `collapseContent` | 2 | 2 | 3217, 3664 |
| `content-primary` | 2 | 2 | 4319, 4371 |
| `detailPageSecondaryContainer` | 2 | 2 | 1578, 1605 |
| `editorsChoiceItemOverview` | 2 | 2 | 6647, 6728 |
| `endsAt` | 2 | 2 | 1788, 6106 |
| `formDialogFooter-clear` | 2 | 2 | 3212, 3666 |
| `guide-programNameCaret` | 2 | 2 | 293, 4989 |
| `headroom` | 2 | 2 | 5536, 5573 |
| `mediaInfoOfficialRating` | 2 | 2 | 1788, 6106 |
| `navMenuOption-selected` | 2 | 2 | 4040, 6241 |
| `nowPlayingInfoContainer` | 2 | 2 | 2951, 5379 |
| `org` | 2 | 2 | 2987, 3017 |
| `paperList` | 2 | 2 | 811, 3677 |
| `playlist` | 2 | 2 | 3886, 5357 |
| `queue` | 2 | 2 | 1929, 2396 |
| `readOnlyContent` | 2 | 2 | 3708, 5754 |
| `recordingFields` | 2 | 2 | 4080, 4222 |
| `runtime` | 2 | 2 | 5290, 5319 |
| `sectionTitleContainer` | 2 | 2 | 1754, 4251 |
| `sectionTitleContainer-cards` | 2 | 2 | 4400, 4455 |
| `sidebarHeader` | 2 | 2 | 3746, 6247 |
| `tagline` | 2 | 2 | 2467, 4136 |
| `upNextDialog-title` | 2 | 2 | 4511, 4545 |
| `vertical-list` | 2 | 2 | 1731, 6553 |
| `videoOsdBottom` | 2 | 2 | 2943, 5503 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 2943, 5503 |
| `checkboxContainer` | 7 | 1 | 3266–3303 |
| `itemDetailsGroup` | 7 | 1 | 4140–4227 |
| `itemProgressBar` | 6 | 1 | 2661–2695 |
| `trackSelectionFieldContainer` | 6 | 1 | 4099–4122 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 6684–6724 |
| `innerCardFooter` | 5 | 1 | 3107–3136 |
| `chapterCardImageContainer` | 4 | 1 | 3107–3136 |
| `endTimeText` | 4 | 1 | 5290–5319 |
| `mainDetailButtons` | 4 | 1 | 3601–3615 |
| `overview-controls` | 4 | 1 | 3082–3094 |
| `scrollX` | 4 | 1 | 1708–1727 |
| `startTimeText` | 4 | 1 | 5290–5313 |
| `button-flat` | 3 | 1 | 2924–2934 |
| `cardIndicators` | 3 | 1 | 3356–3366 |
| `cardOverlayFab-primary` | 3 | 1 | 983–1005 |
| `com` | 3 | 1 | 2993–3011 |
| `content` | 3 | 1 | 4163–4194 |
| `discover-card` | 3 | 1 | 6735–6758 |
| `emby-select-withcolor` | 3 | 1 | 4731–4765 |
| `emby-textarea` | 3 | 1 | 4722–4747 |
| `fab` | 3 | 1 | 3461–3474 |
| `listChildrenCollapsible` | 3 | 1 | 4212–4227 |
| `mdl-slider-background-flex` | 3 | 1 | 2781–2794 |
| `mediaInfoCriticRating` | 3 | 1 | 1829–1838 |
| `nextUpSection` | 3 | 1 | 4207–4227 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 5343–5353 |
| `serverInfo` | 3 | 1 | 3681–3690 |
| `transcodingProgress` | 3 | 1 | 2672–2684 |
