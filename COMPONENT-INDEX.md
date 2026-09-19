# Index des composants — ElegantFin Cinema Edition v1.3.6

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.6.css` — 7247 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 36 | 14 | 411–493, 731, 834, 1480–1500, 2003–2036, 2063–2067, 2342–2360, 2396, 6208, 6488–6504, 6582–6604, 6634–6641, 6715, 7125 |
| `cardScalable` | 28 | 13 | 411–422, 470–493, 780–824, 850–888, 2360, 3298, 3409, 3488, 5416, 6222–6232, 6301, 6488, 6625–6641 |
| `cardImageContainer` | 23 | 13 | 465, 802, 830–859, 888, 945–975, 5525–5529, 5609, 6214, 6293–6301, 6352, 6488–6504, 6625, 6763 |
| `material-icons` | 17 | 13 | 347–366, 1699, 1758, 1810, 3255, 3414, 3488–3494, 3600, 3758, 4140, 4624, 4658–4668, 5240 |
| `itemDetailPage` | 18 | 11 | 1543, 1629, 1708, 1929–1954, 1998, 2098, 2409–2414, 3743–3754, 4234, 4521, 6953–6991 |
| `nameContainer` | 27 | 9 | 677, 2105–2128, 2169, 2198, 2233–2279, 2316, 2347–2351, 4997–5049, 6953–6991 |
| `skinHeader` | 16 | 9 | 275, 3973–4025, 5424, 5818, 5874–5882, 5908–5933, 6284, 6456, 7062 |
| `backdropCard` | 12 | 9 | 932–938, 1053, 1929, 2015, 2098, 2351–2360, 2387, 2414, 2679 |
| `card-hoverable` | 23 | 8 | 493, 790, 850–938, 5529, 6232, 6380–6399, 6488, 6770 |
| `parentName` | 23 | 8 | 677, 2110–2128, 2169, 2198, 2233–2279, 5003–5049, 5122, 6953–6991 |
| `detailPageWrapperContainer` | 17 | 8 | 677, 1511–1521, 1954, 2072, 2105–2128, 2198, 2233–2279, 2347 |
| `subtitle` | 16 | 8 | 1929, 1998, 2110, 2169, 2288–2298, 2409–2414, 5057–5090, 6953–6991 |
| `cardBox` | 12 | 8 | 411–459, 485, 731, 872, 979, 6208, 6488, 6770 |
| `js` | 8 | 8 | 314, 1615, 2169, 2756, 3388, 5240, 6408, 6651 |
| `detailLogo` | 17 | 7 | 677, 1943–1954, 1989–1998, 2098–2128, 2198, 2233–2279, 2347 |
| `loginPage` | 15 | 7 | 3567, 5428–5443, 5482, 5510–5529, 6237, 6280, 6614–6641 |
| `emby-button` | 10 | 7 | 603–620, 647–665, 3057–3064, 3434, 3469, 3622, 4158 |
| `nowPlayingBar` | 7 | 7 | 2942, 5661, 6247, 6335, 6442, 6468, 6720 |
| `listItem` | 17 | 6 | 293, 620, 2364, 4060–4086, 4117–4149, 6738–6755 |
| `navMenuOption` | 12 | 6 | 620, 716–726, 3808, 4127–4149, 4215–4220, 6527–6538 |
| `verticalSection` | 11 | 6 | 1703, 2580–2585, 4521, 6293, 6408, 6651 |
| `person` | 8 | 6 | 1929–1939, 2098, 2351, 2396–2405, 3695, 6948 |
| `mainDrawer` | 7 | 6 | 2906, 3772, 3998, 6237–6247, 6514, 6553 |
| `detailImageContainer` | 20 | 5 | 1929–1939, 2003–2067, 2098, 2338–2360, 2387–2414 |
| `osdHeader` | 15 | 5 | 1672–1690, 5813–5882, 5908–5933, 6284, 6720 |
| `actionSheetMenuItem` | 11 | 5 | 620, 4060–4071, 4117, 4195–4211, 6265 |
| `sectionTabs` | 10 | 5 | 1727, 3546, 4025, 5854–5859, 5999–6025 |
| `button-link` | 9 | 5 | 620, 647–665, 2892–2901, 2962–2972, 6916 |
| `cardImageIcon` | 8 | 5 | 403–407, 2351–2360, 2420, 3282, 5609 |
| `paper-icon-button-light` | 8 | 5 | 565–620, 1629, 1699, 1758, 4916 |
| `sectionTitle` | 7 | 5 | 1703, 1737–1744, 3874, 4594–4602, 5477 |
| `portraitCard` | 5 | 5 | 1053, 1131, 1848, 2063, 2679 |
| `scss` | 5 | 5 | 275, 759, 1005, 3304, 6408 |
| `skinHeader-withBackground` | 5 | 5 | 1611, 3743, 5424, 5813, 5863 |
| `btnPlay` | 16 | 4 | 502–526, 565–620, 3498–3540, 3573–3600 |
| `cardOverlayContainer` | 12 | 4 | 906–938, 983–1005, 1065, 6720–6738 |
| `itemName` | 11 | 4 | 677, 2169, 5003–5049, 5140–5157 |
| `backdropImage` | 10 | 4 | 2486–2513, 2540–2544, 6201, 6301–6309 |
| `emby-tab-button` | 10 | 4 | 620, 687–696, 3546, 5984–6020 |
| `upNextContainer` | 10 | 4 | 4686–4705, 4731–4757, 6237–6247, 6273 |
| `headerTop` | 8 | 4 | 3973–3998, 5824–5849, 5900–5917, 5944–5948 |
| `detailRibbon` | 7 | 4 | 1568–1596, 1763, 1848–1853, 6948 |
| `listItemBodyText` | 7 | 4 | 4081–4100, 4140, 4199, 6755 |
| `visualCardBox` | 7 | 4 | 411, 811–824, 850–855, 979 |
| `button-submit` | 6 | 4 | 3567, 3654, 5510–5518, 6828–6842 |
| `cardText-secondary` | 6 | 4 | 293, 893, 3287–3291, 6386–6394 |
| `detailPagePrimaryContent` | 6 | 4 | 1583–1601, 2303, 4515, 6472 |
| `emby-scroller-container` | 6 | 4 | 1703–1716, 2570, 6293, 6408 |
| `skip-button` | 6 | 4 | 620, 3551, 4780–4797, 4824–4830 |
| `squareCard` | 6 | 4 | 834, 2351, 2387–2405, 5486–5490 |
| `skinHeader-blurred` | 5 | 4 | 5424, 5842–5849, 6456, 6720 |
| `appfooter` | 4 | 4 | 2622, 5958, 6324, 6720 |
| `raised` | 4 | 4 | 620, 706, 3434, 3469 |
| `detailButton` | 13 | 3 | 565–620, 3479–3540, 3596–3600 |
| `emby-scroller` | 9 | 3 | 1708–1722, 6557–6604, 6706–6715 |
| `itemBackdrop` | 9 | 3 | 1895–1939, 2072, 2414 |
| `itemSelectionPanel` | 9 | 3 | 863–867, 3227, 3255–3298 |
| `check` | 8 | 3 | 3255, 3488, 4191–4211 |
| `pageTitle` | 8 | 3 | 1647–1690, 5874, 5933 |
| `sectionTitleTextButton` | 8 | 3 | 4577–4585, 4612–4624, 4658–4668 |
| `playedIndicator` | 7 | 3 | 759–773, 3371, 6488–6509 |
| `detailSectionContent` | 6 | 3 | 3089, 4316–4326, 4406–4416 |
| `emby-checkbox` | 6 | 3 | 3232, 3269–3273, 3322–3334 |
| `actionSheetContent` | 5 | 3 | 4183–4187, 6237–6247, 6273 |
| `cardText-first` | 5 | 3 | 893, 3261–3287, 5590 |
| `dialog` | 5 | 3 | 3139–3149, 6237–6247, 6273 |
| `guideProgramName` | 5 | 3 | 620, 5181–5192, 5235–5240 |
| `musicParentName` | 5 | 3 | 1929, 2409–2414, 5122–5131 |
| `noHomeButtonHeader` | 5 | 3 | 1629, 5874, 5984–5992 |
| `overflowBackdropCard` | 5 | 3 | 932–938, 3265, 5585–5590 |
| `secondary` | 5 | 3 | 293, 4090–4100, 4140 |
| `album` | 4 | 3 | 2098, 2356–2360, 2396 |
| `cardPadder` | 4 | 3 | 407, 979, 3278–3282 |
| `cardText` | 4 | 3 | 893–903, 3287, 6630 |
| `dialog-fullscreen` | 4 | 3 | 3149, 6237–6247, 6273 |
| `emby-scrollbuttons` | 4 | 3 | 1749–1754, 6651, 7100 |
| `formDialogFooter` | 4 | 3 | 3207, 3661, 6777–6801 |
| `infoWrapper` | 4 | 3 | 2042–2047, 2303, 2331 |
| `listItemImage` | 4 | 3 | 2656–2661, 4054, 6755 |
| `semiTransparent` | 4 | 3 | 1611, 5424, 5842–5863 |
| `toast` | 4 | 3 | 4678, 6237–6247, 6273 |
| `defaultCardBackground` | 3 | 3 | 3409, 5605, 5704 |
| `folder` | 3 | 3 | 1848, 3388, 3452 |
| `formDialogFooterItem` | 3 | 3 | 3207, 3447, 3573 |
| `formDialogHeader` | 3 | 3 | 3661, 6720, 6777 |
| `iconOsd` | 3 | 3 | 5402, 6720, 6777 |
| `itemsContainer` | 3 | 3 | 731, 1731, 4521 |
| `live_tv` | 3 | 3 | 1929, 2396, 3695 |
| `myPreferencesMenuPage` | 3 | 3 | 380, 4225, 4529 |
| `page` | 3 | 3 | 975, 2561, 6293 |
| `playerStats` | 3 | 3 | 5402, 6777, 6813 |
| `sectionTitle-cards` | 3 | 3 | 1703, 4594, 4654 |
| `x` | 3 | 3 | 2169, 5105, 6408 |
| `itemExternalLinks` | 11 | 2 | 2955–3012, 3089 |
| `checkboxOutline` | 10 | 2 | 3232–3273, 3304–3334 |
| `mdl-slider` | 9 | 2 | 2752, 2807–2865 |
| `listItemIcon` | 8 | 2 | 3691–3695, 4195–4225 |
| `sliderContainer` | 8 | 2 | 2756, 2784–2849 |
| `cardOverlayButton-br` | 7 | 2 | 991, 1020–1058 |
| `detail-clamp-text` | 7 | 2 | 3025–3051, 3077–3081 |
| `divUsers` | 7 | 2 | 5486–5490, 6614–6641 |
| `homePage` | 7 | 2 | 3973–4025, 6042 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3269–3273, 3303–3322 |
| `backgroundContainer` | 6 | 2 | 2476, 2518–2536 |
| `detailPagePrimaryContainer` | 6 | 2 | 1555–1601, 2303 |
| `detailsGroupItem` | 6 | 2 | 4278, 4346–4383 |
| `headerButton` | 6 | 2 | 540–620, 5926 |
| `headerLeft` | 6 | 2 | 1653–1690, 6129 |
| `trackSelections` | 6 | 2 | 4251–4278, 4411–4416 |
| `withBackdrop` | 6 | 2 | 2476, 2518–2536 |
| `countIndicator` | 5 | 2 | 750–773, 6777–6801 |
| `detailSection` | 5 | 2 | 4234–4243, 4396–4416 |
| `fullSyncIndicator` | 5 | 2 | 750–773, 6777–6801 |
| `mainDrawer-scrollContainer` | 5 | 2 | 2915, 6527–6544 |
| `mediaInfoItem` | 5 | 2 | 1767–1810, 6408 |
| `overview-expand` | 5 | 2 | 3057–3081, 4316 |
| `videoIndicator` | 5 | 2 | 3377–3405, 6777 |
| `withSectionTabs` | 5 | 2 | 2527–2544, 5849 |
| `alphaPickerButton` | 4 | 2 | 620, 4455–4467 |
| `backgroundProgress` | 4 | 2 | 2667–2679, 2709 |
| `emby-tab-button-active` | 4 | 2 | 3633, 6011–6025 |
| `mediaSourceIndicator` | 4 | 2 | 750–773, 6777 |
| `play_arrow` | 4 | 2 | 3414–3430, 3600 |
| `playbackProgress` | 4 | 2 | 2667–2679, 2714 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4081–4086, 5698–5704 |
| `programCell` | 4 | 2 | 5172, 5231–5240 |
| `programGuideSection` | 4 | 2 | 2364–2379, 4416–4431 |
| `section0` | 4 | 2 | 945–975, 6293 |
| `visualLoginForm` | 4 | 2 | 5477–5494, 5535 |
| `cardFooter` | 3 | 2 | 3298, 6380–6399 |
| `cardOverlayButtonIcon` | 3 | 2 | 991–1003, 1058 |
| `castCollapsible` | 3 | 2 | 802, 3273–3282 |
| `detailPageContent` | 3 | 2 | 4247, 4508–4515 |
| `emby-input` | 3 | 2 | 4930–4946, 6842 |
| `emby-scrollbuttons-button` | 3 | 2 | 1758, 7107–7114 |
| `guestCastContent` | 3 | 2 | 802, 3273–3282 |
| `guide-channelHeaderCell` | 3 | 2 | 620, 5206–5222 |
| `guide-date-tab-button` | 3 | 2 | 620, 3633–3641 |
| `headerUserButton` | 3 | 2 | 540–553, 4533 |
| `manualLoginForm` | 3 | 2 | 5477–5494, 5535 |
| `overview` | 3 | 2 | 3077–3081, 4326 |
| `selectionCommandsPanel` | 3 | 2 | 3217–3223, 6720 |
| `backdropImageFadeIn` | 2 | 2 | 2606, 6817 |
| `blurhash-canvas` | 2 | 2 | 6352, 6763 |
| `book` | 2 | 2 | 1929, 2396 |
| `btnDeleteImage` | 2 | 2 | 3434, 3647 |
| `cardContent` | 2 | 2 | 802, 834 |
| `cardImage` | 2 | 2 | 6352, 6763 |
| `cardOverlayButton` | 2 | 2 | 1005, 1041 |
| `cardOverlayButton-hover` | 2 | 2 | 888, 1020 |
| `chevron_right` | 2 | 2 | 4624, 4668 |
| `collapseContent` | 2 | 2 | 3212, 3659 |
| `content-primary` | 2 | 2 | 4508, 4560 |
| `detailPageSecondaryContainer` | 2 | 2 | 1578, 1605 |
| `editorsChoiceItemOverview` | 2 | 2 | 7037, 7118 |
| `emby-select` | 2 | 2 | 4930, 6842 |
| `endsAt` | 2 | 2 | 1788, 6408 |
| `fieldDescription` | 2 | 2 | 293, 6842 |
| `formDialogFooter-clear` | 2 | 2 | 3207, 3661 |
| `guide-programNameCaret` | 2 | 2 | 293, 5188 |
| `headroom` | 2 | 2 | 5837, 5874 |
| `mediaInfoOfficialRating` | 2 | 2 | 1788, 6408 |
| `navMenuOption-selected` | 2 | 2 | 4230, 6538 |
| `nowPlayingInfoContainer` | 2 | 2 | 2946, 5635 |
| `org` | 2 | 2 | 2982, 3012 |
| `paperList` | 2 | 2 | 811, 3672 |
| `playlist` | 2 | 2 | 4076, 5613 |
| `programSecondaryTitle` | 2 | 2 | 293, 5240 |
| `queue` | 2 | 2 | 1929, 2396 |
| `readOnlyContent` | 2 | 2 | 3703, 6058 |
| `recordingFields` | 2 | 2 | 4270, 4411 |
| `runtime` | 2 | 2 | 5547, 5575 |
| `sectionTitleContainer` | 2 | 2 | 1754, 4440 |
| `sectionTitleContainer-cards` | 2 | 2 | 4589, 4654 |
| `sidebarHeader` | 2 | 2 | 3795, 6544 |
| `tagline` | 2 | 2 | 2467, 4326 |
| `tsx` | 2 | 2 | 3973, 4029 |
| `upNextDialog-title` | 2 | 2 | 4710, 4744 |
| `vertical-list` | 2 | 2 | 1731, 6943 |
| `videoOsdBottom` | 2 | 2 | 2938, 5804 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 2938, 5804 |
| `userPreferencesPage` | 12 | 1 | 6828–6923 |
| `checkboxContainer` | 7 | 1 | 3261–3298 |
| `itemDetailsGroup` | 7 | 1 | 4330–4416 |
| `itemProgressBar` | 6 | 1 | 2656–2690 |
| `trackSelectionFieldContainer` | 6 | 1 | 4289–4312 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7074–7114 |
| `innerCardFooter` | 5 | 1 | 3102–3131 |
| `chapterCardImageContainer` | 4 | 1 | 3102–3131 |
| `endTimeText` | 4 | 1 | 5547–5575 |
| `mainDetailButtons` | 4 | 1 | 3596–3610 |
| `overview-controls` | 4 | 1 | 3077–3089 |
| `scrollX` | 4 | 1 | 1708–1727 |
| `startTimeText` | 4 | 1 | 5547–5569 |
| `button-flat` | 3 | 1 | 2919–2929 |
| `cardIndicators` | 3 | 1 | 3351–3361 |
| `cardOverlayFab-primary` | 3 | 1 | 983–1005 |
| `com` | 3 | 1 | 2988–3006 |
| `content` | 3 | 1 | 4352–4383 |
| `discover-card` | 3 | 1 | 7125–7148 |
| `emby-select-withcolor` | 3 | 1 | 4930–4964 |
| `emby-textarea` | 3 | 1 | 4921–4946 |
| `fab` | 3 | 1 | 3456–3469 |
| `listChildrenCollapsible` | 3 | 1 | 4401–4416 |
| `mdl-slider-background-flex` | 3 | 1 | 2776–2789 |
| `mediaInfoCriticRating` | 3 | 1 | 1829–1838 |
| `nextUpSection` | 3 | 1 | 4396–4416 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 5599–5609 |
| `serverInfo` | 3 | 1 | 3676–3685 |
| `transcodingProgress` | 3 | 1 | 2667–2679 |
