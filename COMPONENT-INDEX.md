# Index des composants — ElegantFin Cinema Edition v1.4.5

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.4.5.css` — 7976 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 38 | 16 | 444–455, 486–532, 770, 887, 1552–1572, 2176–2209, 2236–2240, 2517–2535, 2571, 6837, 6873–6883, 7119–7138, 7216–7238, 7268–7275, 7439, 7854 |
| `cardScalable` | 31 | 13 | 444–455, 509–532, 833–877, 903–947, 2535, 3615, 3726, 3805, 5971, 6851–6883, 6954, 7119, 7259–7275 |
| `itemDetailPage` | 22 | 13 | 1615, 1701, 1780, 1807, 2036–2072, 2107–2122, 2158–2162, 2272, 2584, 4061–4072, 4744, 5043, 7674–7712 |
| `material-icons` | 17 | 13 | 380–399, 1771, 1869, 1922, 3572, 3731, 3805–3811, 3918, 4076, 4621, 5150, 5184–5194, 5788 |
| `cardImageContainer` | 22 | 12 | 504, 855, 883–912, 947, 1004–1034, 6097–6101, 6181, 6843, 6946–6954, 6994, 7119–7138, 7259 |
| `skinHeader` | 16 | 10 | 293, 4433, 4479–4506, 5979, 6390, 6446–6454, 6520–6545, 6937, 7086, 7783 |
| `nameContainer` | 27 | 9 | 716, 2279–2302, 2343, 2372, 2407–2454, 2491, 2522–2526, 5544–5597, 7674–7712 |
| `cardBox` | 13 | 9 | 444–455, 486–498, 524, 770, 925–929, 1038, 6837, 7119, 7485 |
| `emby-button` | 12 | 9 | 642–659, 686–704, 3211, 3346–3353, 3751, 3786, 3940, 4639, 5366 |
| `js` | 10 | 9 | 327–347, 1687, 1780, 2343, 2949, 3705, 5788, 7038, 7285 |
| `card-hoverable` | 23 | 8 | 532, 843, 903–997, 6101, 6861, 6994–7029, 7119, 7485 |
| `parentName` | 23 | 8 | 716, 2284–2302, 2343, 2372, 2407–2454, 5550–5597, 5670, 7674–7712 |
| `detailLogo` | 21 | 8 | 716, 2046–2072, 2107–2122, 2149–2162, 2272–2302, 2372, 2407–2454, 2522 |
| `listItem` | 19 | 8 | 311, 659, 2539, 4541–4567, 4598–4630, 4675, 4719, 7462–7479 |
| `detailPageWrapperContainer` | 17 | 8 | 716, 1583–1593, 2072, 2245, 2279–2302, 2372, 2407–2454, 2522 |
| `subtitle` | 17 | 8 | 2036–2046, 2158–2162, 2284, 2343, 2463–2473, 2584, 5605–5638, 7674–7712 |
| `backdropCard` | 12 | 8 | 991–997, 1119, 2036–2046, 2188, 2272, 2526–2535, 2562, 2872 |
| `nowPlayingBar` | 8 | 8 | 327, 3135, 6233, 6900, 6988, 7072, 7098, 7444 |
| `loginPage` | 16 | 7 | 3884, 5983–6014, 6054, 6082–6101, 6890, 6933, 7248–7275 |
| `navMenuOption` | 12 | 6 | 659, 755–765, 4126, 4608–4630, 4725–4730, 7161–7172 |
| `emby-tab-button` | 11 | 6 | 659, 726–735, 3863, 6596–6604, 6633–6650, 7795 |
| `paper-icon-button-light` | 11 | 6 | 604–659, 1701, 1771, 1869, 3512–3532, 5450 |
| `verticalSection` | 11 | 6 | 1775, 2774–2779, 5043, 6946, 7038, 7285 |
| `button-link` | 10 | 6 | 659, 686–704, 3085–3094, 3155–3165, 3211, 7636 |
| `headerTop` | 9 | 6 | 2162, 4433, 4479, 6396–6421, 6512–6529, 6556–6560 |
| `person` | 8 | 6 | 2036–2057, 2272, 2526, 2571–2580, 4013, 7669 |
| `mainDrawer` | 7 | 6 | 3099, 4090, 4479, 6890–6900, 7148, 7187 |
| `scss` | 6 | 6 | 293, 798, 1064, 3621, 4132, 7038 |
| `detailImageContainer` | 20 | 5 | 2036–2057, 2176–2240, 2272, 2513–2535, 2562–2580 |
| `osdHeader` | 15 | 5 | 1744–1762, 6385–6454, 6520–6545, 6937, 7444 |
| `sectionTabs` | 11 | 5 | 1838, 3863, 4506, 6426–6431, 6611–6655 |
| `actionSheetMenuItem` | 10 | 5 | 659, 4541–4552, 4598, 4675–4719, 6918 |
| `cardImageIcon` | 8 | 5 | 436–440, 2526–2535, 2598, 3599, 6181 |
| `sectionTitle` | 7 | 5 | 1775, 1848–1855, 4334, 5120–5128, 6049 |
| `emby-scroller-container` | 6 | 5 | 1775–1780, 1818, 2764, 6946, 7038 |
| `portraitCard` | 6 | 5 | 1119, 1203, 1960–1965, 2236, 2872 |
| `appfooter` | 5 | 5 | 327, 2815, 6570, 6977, 7444 |
| `skinHeader-withBackground` | 5 | 5 | 1683, 4061, 5979, 6385, 6435 |
| `btnPlay` | 16 | 4 | 541–565, 604–659, 3815–3857, 3890–3918 |
| `cardOverlayContainer` | 12 | 4 | 965–997, 1042–1064, 1137, 7444–7462 |
| `itemName` | 11 | 4 | 716, 2343, 5550–5597, 5688–5705 |
| `backdropImage` | 10 | 4 | 2663–2691, 2718–2722, 6830, 6954–6962 |
| `upNextContainer` | 10 | 4 | 5212–5231, 5257–5283, 6890–6900, 6926 |
| `emby-scroller` | 9 | 4 | 1780, 1818–1824, 7191–7238, 7423–7439 |
| `backgroundContainer` | 8 | 4 | 2126, 2654, 2696–2714, 2746 |
| `detailRibbon` | 8 | 4 | 1640–1668, 1875, 1960–1972, 7669 |
| `listItemBodyText` | 7 | 4 | 4562–4581, 4621, 4696, 7479 |
| `skip-button` | 7 | 4 | 659, 3868, 5306–5323, 5350–5368 |
| `visualCardBox` | 7 | 4 | 444, 864–877, 903–908, 1038 |
| `button-submit` | 6 | 4 | 3884, 3972, 6082–6090, 7547–7562 |
| `cardText-secondary` | 6 | 4 | 311, 952, 3604–3608, 7016–7024 |
| `detailPagePrimaryContent` | 6 | 4 | 1655–1673, 2478, 5037, 7102 |
| `squareCard` | 6 | 4 | 887, 2526, 2562–2580, 6058–6062 |
| `semiTransparent` | 5 | 4 | 1683, 5979, 6414–6435, 6471 |
| `skinHeader-blurred` | 5 | 4 | 5979, 6414–6421, 7086, 7444 |
| `itemsContainer` | 4 | 4 | 770, 1807, 1842, 5043 |
| `raised` | 4 | 4 | 659, 745, 3751, 3786 |
| `x` | 4 | 4 | 2343, 4132, 5653, 7038 |
| `detailButton` | 13 | 3 | 604–659, 3796–3857, 3914–3918 |
| `itemSelectionPanel` | 9 | 3 | 916–920, 3544, 3572–3615 |
| `pageTitle` | 8 | 3 | 1719–1762, 6446, 6545 |
| `sectionTitleTextButton` | 8 | 3 | 5103–5111, 5138–5150, 5184–5194 |
| `homePage` | 7 | 3 | 4433, 4479–4506, 6672 |
| `playedIndicator` | 7 | 3 | 798–812, 3688, 7119–7143 |
| `check` | 6 | 3 | 3572, 3805, 4675–4719 |
| `detailSectionContent` | 6 | 3 | 3378, 4826–4836, 4916–4926 |
| `emby-checkbox` | 6 | 3 | 3549, 3586–3590, 3639–3651 |
| `actionSheetContent` | 5 | 3 | 4667–4671, 6890–6900, 6926 |
| `cardText-first` | 5 | 3 | 952, 3578–3604, 6162 |
| `dialog` | 5 | 3 | 3428–3438, 6890–6900, 6926 |
| `guideProgramName` | 5 | 3 | 659, 5729–5740, 5783–5788 |
| `noHomeButtonHeader` | 5 | 3 | 1701, 6446, 6596–6604 |
| `overflowBackdropCard` | 5 | 3 | 991–997, 3582, 6157–6162 |
| `secondary` | 5 | 3 | 311, 4571–4581, 4621 |
| `album` | 4 | 3 | 2272, 2531–2535, 2571 |
| `cardPadder` | 4 | 3 | 440, 1038, 3595–3599 |
| `cardText` | 4 | 3 | 952–962, 3604, 7264 |
| `detailPageContent` | 4 | 3 | 1797, 4757, 5030–5037 |
| `dialog-fullscreen` | 4 | 3 | 3438, 6890–6900, 6926 |
| `emby-scrollbuttons` | 4 | 3 | 1860–1865, 7285, 7829 |
| `folder` | 4 | 3 | 1960–1965, 3705, 3769 |
| `formDialogFooter` | 4 | 3 | 3496, 3979, 7496–7520 |
| `infoWrapper` | 4 | 3 | 2215–2220, 2478, 2506 |
| `listItemImage` | 4 | 3 | 2849–2854, 4535, 7479 |
| `musicParentName` | 4 | 3 | 2036, 2584, 5670–5679 |
| `programGuideSection` | 4 | 3 | 2539–2554, 4926, 4953 |
| `toast` | 4 | 3 | 5204, 6890–6900, 6926 |
| `cardFooter` | 3 | 3 | 3615, 6994, 7029 |
| `collectionItems` | 3 | 3 | 1807, 4926, 4962 |
| `defaultCardBackground` | 3 | 3 | 3726, 6177, 6276 |
| `detailPageSecondaryContainer` | 3 | 3 | 1650, 1677, 1797 |
| `emby-input` | 3 | 3 | 5464, 5493, 7562 |
| `formDialogFooterItem` | 3 | 3 | 3496, 3764, 3890 |
| `formDialogHeader` | 3 | 3 | 3979, 7444, 7496 |
| `iconOsd` | 3 | 3 | 5957, 7444, 7496 |
| `live_tv` | 3 | 3 | 2036, 2571, 4013 |
| `myPreferencesMenuPage` | 3 | 3 | 413, 4735, 5051 |
| `page` | 3 | 3 | 1034, 2746, 6946 |
| `playerStats` | 3 | 3 | 5957, 7496, 7532 |
| `sectionTitle-cards` | 3 | 3 | 1775, 5120, 5180 |
| `sectionTitleContainer` | 3 | 3 | 1807, 1865, 4962 |
| `tsx` | 3 | 3 | 1119, 4433, 4510 |
| `itemExternalLinks` | 13 | 2 | 3148–3226, 3378 |
| `checkboxOutline` | 10 | 2 | 3549–3590, 3621–3651 |
| `itemBackdrop` | 9 | 2 | 2002–2057, 2245 |
| `mdl-slider` | 9 | 2 | 2945, 3000–3058 |
| `cardOverlayButton-br` | 8 | 2 | 1050, 1079–1130 |
| `listItemIcon` | 8 | 2 | 4009–4013, 4675–4735 |
| `sliderContainer` | 8 | 2 | 2949, 2977–3042 |
| `detail-clamp-text` | 7 | 2 | 3314–3340, 3366–3370 |
| `divUsers` | 7 | 2 | 6058–6062, 7248–7275 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3586–3590, 3620–3639 |
| `countIndicator` | 6 | 2 | 789–819, 7496–7520 |
| `detailPagePrimaryContainer` | 6 | 2 | 1627–1673, 2478 |
| `detailsGroupItem` | 6 | 2 | 4788, 4856–4893 |
| `headerButton` | 6 | 2 | 579–659, 6538 |
| `headerLeft` | 6 | 2 | 1725–1762, 6759 |
| `selectionCommandsPanel` | 6 | 2 | 3506–3540, 7444 |
| `trackSelections` | 6 | 2 | 4761–4788, 4921–4926 |
| `withBackdrop` | 6 | 2 | 2654, 2696–2714 |
| `detailSection` | 5 | 2 | 4744–4753, 4906–4926 |
| `fullSyncIndicator` | 5 | 2 | 789–812, 7496–7520 |
| `mainDrawer-scrollContainer` | 5 | 2 | 3108, 7161–7178 |
| `mediaInfoItem` | 5 | 2 | 1879–1922, 7038 |
| `overview-expand` | 5 | 2 | 3346–3370, 4826 |
| `scrollX` | 5 | 2 | 1780, 1818–1838 |
| `videoIndicator` | 5 | 2 | 3694–3722, 7496 |
| `withSectionTabs` | 5 | 2 | 2705–2722, 6421 |
| `alphaPickerButton` | 4 | 2 | 659, 4977–4989 |
| `backgroundProgress` | 4 | 2 | 2860–2872, 2902 |
| `emby-select` | 4 | 2 | 5464–5476, 7562 |
| `emby-tab-button-active` | 4 | 2 | 3951, 6641–6655 |
| `mediaSourceIndicator` | 4 | 2 | 789–812, 7496 |
| `play_arrow` | 4 | 2 | 3731–3747, 3918 |
| `playbackProgress` | 4 | 2 | 2860–2872, 2907 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4562–4567, 6270–6276 |
| `programCell` | 4 | 2 | 5720, 5779–5788 |
| `section0` | 4 | 2 | 1004–1034, 6946 |
| `visualLoginForm` | 4 | 2 | 6049–6066, 6107 |
| `cardOverlayButtonIcon` | 3 | 2 | 1050–1062, 1130 |
| `castCollapsible` | 3 | 2 | 855, 3590–3599 |
| `emby-scrollbuttons-button` | 3 | 2 | 1869, 7836–7843 |
| `emby-textarea` | 3 | 2 | 5455–5464, 5493 |
| `guestCastContent` | 3 | 2 | 855, 3590–3599 |
| `guide-channelHeaderCell` | 3 | 2 | 659, 5754–5770 |
| `guide-date-tab-button` | 3 | 2 | 659, 3951–3959 |
| `headerUserButton` | 3 | 2 | 579–592, 5055 |
| `manualLoginForm` | 3 | 2 | 6049–6066, 6107 |
| `overview` | 3 | 2 | 3366–3370, 4836 |
| `add` | 2 | 2 | 1780, 7038 |
| `alphaPicker-fixed-right` | 2 | 2 | 2746, 4989 |
| `backdropImageFadeIn` | 2 | 2 | 2799, 7536 |
| `book` | 2 | 2 | 2036, 2571 |
| `btnDeleteImage` | 2 | 2 | 3751, 3965 |
| `cardContent` | 2 | 2 | 855, 887 |
| `cardOverlayButton` | 2 | 2 | 1064, 1107 |
| `cardOverlayButton-hover` | 2 | 2 | 947, 1079 |
| `chevron_right` | 2 | 2 | 5150, 5194 |
| `classList` | 2 | 2 | 1780, 7038 |
| `collapseContent` | 2 | 2 | 3501, 3977 |
| `collectionItemsContainer` | 2 | 2 | 1807, 4966 |
| `content-primary` | 2 | 2 | 5030, 5086 |
| `editorsChoiceItemOverview` | 2 | 2 | 7758, 7847 |
| `endsAt` | 2 | 2 | 1900, 7038 |
| `fieldDescription` | 2 | 2 | 311, 7562 |
| `formDialogFooter-clear` | 2 | 2 | 3496, 3979 |
| `guide-programNameCaret` | 2 | 2 | 311, 5736 |
| `headroom` | 2 | 2 | 6409, 6446 |
| `indicator` | 2 | 2 | 819, 3683 |
| `mediaInfoOfficialRating` | 2 | 2 | 1900, 7038 |
| `navMenuOption-selected` | 2 | 2 | 4740, 7172 |
| `nowPlayingInfoContainer` | 2 | 2 | 3139, 6207 |
| `org` | 2 | 2 | 3175, 3205 |
| `paperList` | 2 | 2 | 864, 3990 |
| `playlist` | 2 | 2 | 4557, 6185 |
| `programSecondaryTitle` | 2 | 2 | 311, 5788 |
| `queue` | 2 | 2 | 2036, 2571 |
| `reactRoot` | 2 | 2 | 4433, 6765 |
| `readOnlyContent` | 2 | 2 | 4021, 6688 |
| `recordingFields` | 2 | 2 | 4780, 4921 |
| `runtime` | 2 | 2 | 6119, 6147 |
| `sectionTitleContainer-cards` | 2 | 2 | 5115, 5180 |
| `sidebarHeader` | 2 | 2 | 4113, 7178 |
| `tagline` | 2 | 2 | 2645, 4836 |
| `upNextDialog-title` | 2 | 2 | 5236, 5270 |
| `vertical-list` | 2 | 2 | 1842, 7664 |
| `vertical-wrap` | 2 | 2 | 785, 1807 |
| `videoOsdBottom` | 2 | 2 | 3131, 6376 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3131, 6376 |
| `userPreferencesPage` | 12 | 1 | 7547–7643 |
| `checkboxContainer` | 7 | 1 | 3578–3615 |
| `itemDetailsGroup` | 7 | 1 | 4840–4926 |
| `itemProgressBar` | 6 | 1 | 2849–2883 |
| `streaming-lookup-container` | 6 | 1 | 3233–3278 |
| `trackSelectionFieldContainer` | 6 | 1 | 4799–4822 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7803–7843 |
| `innerCardFooter` | 5 | 1 | 3391–3420 |
| `chapterCardImageContainer` | 4 | 1 | 3391–3420 |
| `emby-select-withcolor` | 4 | 1 | 5464–5511 |
| `endTimeText` | 4 | 1 | 6119–6147 |
| `mainDetailButtons` | 4 | 1 | 3914–3928 |
| `overview-controls` | 4 | 1 | 3366–3378 |
| `startTimeText` | 4 | 1 | 6119–6141 |
| `button-flat` | 3 | 1 | 3112–3122 |
| `cardIndicators` | 3 | 1 | 3668–3678 |
| `cardOverlayFab-primary` | 3 | 1 | 1042–1064 |
| `com` | 3 | 1 | 3181–3199 |
| `content` | 3 | 1 | 4862–4893 |
| `discover-card` | 3 | 1 | 7854–7877 |
| `fab` | 3 | 1 | 3773–3786 |
| `listChildrenCollapsible` | 3 | 1 | 4911–4926 |
| `mdl-slider-background-flex` | 3 | 1 | 2969–2982 |
| `mediaInfoCriticRating` | 3 | 1 | 1941–1950 |
| `nextUpSection` | 3 | 1 | 4906–4926 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 6171–6181 |
| `serverInfo` | 3 | 1 | 3994–4003 |
| `transcodingProgress` | 3 | 1 | 2860–2872 |
