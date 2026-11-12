# Index des composants — ElegantFin Cinema Edition v1.5.7

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.5.7.css` — 8070 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 38 | 16 | 457–487, 518–553, 791, 904, 1565–1585, 2199–2232, 2259–2263, 2540–2558, 2594, 6977, 7013–7023, 7163, 7263–7282, 7360–7382, 7412–7419, 7583 |
| `cardScalable` | 29 | 14 | 457, 487, 541–553, 854–894, 920–964, 2558, 3639, 3751, 3829, 6041, 6991–7023, 7093, 7263, 7403–7419 |
| `cardImageContainer` | 21 | 13 | 468, 536, 872, 900–929, 964, 1022–1046, 6197–6201, 6281, 6983, 7093, 7133, 7263–7282, 7403 |
| `material-icons` | 17 | 13 | 393–412, 1790, 1888, 1941, 3596, 3756, 3829–3835, 3950, 4112, 4666, 5206, 5240–5250, 5858 |
| `itemDetailPage` | 20 | 12 | 1628, 1714, 1799, 1826, 2055–2095, 2130–2145, 2181–2185, 2295, 2607, 4793, 5099, 7837–7875 |
| `skinHeader` | 20 | 12 | 296, 1714, 4092–4108, 4478, 4524–4551, 6049–6053, 6490, 6546–6554, 6624–6649, 7077, 7230, 7908 |
| `js` | 13 | 12 | 330, 360, 1700–1714, 1799, 2366, 2973, 3400, 3730, 5858, 6855, 7182, 7429 |
| `nameContainer` | 27 | 9 | 737, 2302–2325, 2366, 2395, 2430–2477, 2514, 2545–2549, 5614–5667, 7837–7875 |
| `emby-button` | 12 | 9 | 663–680, 707–725, 3234, 3368–3375, 3776, 3810, 3972, 4684, 5428 |
| `parentName` | 23 | 8 | 737, 2307–2325, 2366, 2395, 2430–2477, 5620–5667, 5740, 7837–7875 |
| `detailLogo` | 20 | 8 | 737, 2084–2095, 2130–2145, 2172–2185, 2295–2325, 2395, 2430–2477, 2545 |
| `detailPageWrapperContainer` | 17 | 8 | 737, 1596–1606, 2095, 2268, 2302–2325, 2395, 2430–2477, 2545 |
| `subtitle` | 17 | 8 | 2055–2065, 2181–2185, 2307, 2366, 2486–2496, 2607, 5675–5708, 7837–7875 |
| `cardBox` | 13 | 8 | 457–487, 518–542, 791, 942–946, 1051, 6977, 7263, 7648 |
| `backdropCard` | 12 | 8 | 1009–1015, 1132, 2055–2065, 2211, 2295, 2549–2558, 2585, 2896 |
| `nowPlayingBar` | 8 | 8 | 330, 3158, 6333, 7040, 7127, 7216, 7242, 7588 |
| `card-hoverable` | 22 | 7 | 553, 920–1015, 6201, 7001, 7133–7172, 7263, 7648 |
| `listItem` | 18 | 7 | 314, 680, 2562, 4586–4612, 4643–4675, 4720, 7625–7642 |
| `loginPage` | 18 | 7 | 3916, 6053–6087, 6127–6146, 6182–6201, 7030, 7073, 7392–7419 |
| `navMenuOption` | 12 | 6 | 680, 776–786, 4161, 4653–4675, 4774–4779, 7305–7316 |
| `emby-tab-button` | 11 | 6 | 680, 747–756, 3891, 6700–6711, 6739–6756, 7920 |
| `paper-icon-button-light` | 11 | 6 | 625–680, 1714, 1790, 1888, 3536–3556, 5512 |
| `verticalSection` | 11 | 6 | 1794, 2798–2803, 5099, 7086, 7182, 7429 |
| `button-link` | 10 | 6 | 680, 707–725, 3109–3118, 3178–3188, 3234, 7799 |
| `headerTop` | 9 | 6 | 2185, 4478, 4524, 6496–6521, 6616–6633, 6660–6664 |
| `person` | 8 | 6 | 2055–2080, 2295, 2549, 2594–2603, 4044, 7832 |
| `mainDrawer` | 7 | 6 | 3123, 4126, 4524, 7030–7040, 7292, 7331 |
| `scss` | 6 | 6 | 296, 819, 1077, 3645, 4167, 7182 |
| `detailImageContainer` | 20 | 5 | 2055–2080, 2199–2263, 2295, 2536–2558, 2585–2603 |
| `osdHeader` | 15 | 5 | 1763–1781, 6485–6554, 6624–6649, 7077, 7588 |
| `cardOverlayContainer` | 12 | 5 | 983–1015, 1055–1077, 1150, 7588, 7625 |
| `sectionTabs` | 11 | 5 | 1857, 3891, 4551, 6526–6531, 6717–6761 |
| `cardImageIcon` | 8 | 5 | 449–453, 2549–2558, 2621, 3623, 6281 |
| `sectionTitle` | 7 | 5 | 1794, 1867–1874, 4379, 5176–5184, 6122 |
| `semiTransparent` | 7 | 5 | 1696, 4092–4108, 6049, 6514–6535, 6571 |
| `emby-scroller-container` | 6 | 5 | 1794–1799, 1837, 2786, 7086, 7182 |
| `portraitCard` | 6 | 5 | 1132, 1216, 1979–1984, 2259, 2896 |
| `appfooter` | 5 | 5 | 330, 2839, 6674, 7116, 7588 |
| `skinHeader-withBackground` | 5 | 5 | 1696, 4092, 6049, 6485, 6535 |
| `btnPlay` | 18 | 4 | 562–586, 625–680, 3839–3890, 3922–3950 |
| `itemName` | 11 | 4 | 737, 2366, 5620–5667, 5758–5775 |
| `backdropImage` | 10 | 4 | 2685–2713, 2740–2744, 6970, 7093–7101 |
| `upNextContainer` | 10 | 4 | 5267–5285, 5311–5337, 7030–7040, 7066 |
| `emby-scroller` | 9 | 4 | 1799, 1837–1843, 7335–7382, 7567–7583 |
| `sectionTitleTextButton` | 9 | 4 | 479, 5159–5167, 5194–5206, 5240–5250 |
| `backgroundContainer` | 8 | 4 | 2149, 2677, 2718–2736, 2768 |
| `detailRibbon` | 8 | 4 | 1653–1681, 1894, 1979–1991, 7832 |
| `skip-button` | 8 | 4 | 680, 3900, 5360–5385, 5412–5430 |
| `visualCardBox` | 7 | 4 | 457, 881–894, 920–925, 1051 |
| `actionSheetMenuItem` | 6 | 4 | 680, 4586–4597, 4643, 7058 |
| `button-submit` | 6 | 4 | 3916, 4003, 6182–6190, 7710–7725 |
| `cardText-secondary` | 6 | 4 | 314, 969, 3628–3632, 7155–7163 |
| `detailPagePrimaryContent` | 6 | 4 | 1668–1686, 2501, 5093, 7246 |
| `skinHeader-blurred` | 6 | 4 | 6049, 6514–6521, 7230, 7588–7607 |
| `squareCard` | 6 | 4 | 904, 2549, 2585–2603, 6151–6155 |
| `itemsContainer` | 4 | 4 | 791, 1826, 1861, 5099 |
| `raised` | 4 | 4 | 680, 766, 3776, 3810 |
| `tsx` | 4 | 4 | 1132, 1714, 4478, 4555 |
| `x` | 4 | 4 | 2366, 4167, 5723, 7182 |
| `detailButton` | 14 | 3 | 625–680, 3820–3890, 3946–3950 |
| `itemSelectionPanel` | 9 | 3 | 933–937, 3568, 3596–3639 |
| `pageTitle` | 8 | 3 | 1738–1781, 6546, 6649 |
| `homePage` | 7 | 3 | 4478, 4524–4551, 6778 |
| `playedIndicator` | 7 | 3 | 819–833, 3712, 7263–7287 |
| `detailSectionContent` | 6 | 3 | 3400, 4879–4889, 4972–4982 |
| `emby-checkbox` | 6 | 3 | 3573, 3610–3614, 3663–3675 |
| `listItemBodyText` | 6 | 3 | 4607–4626, 4666, 7642 |
| `actionSheetContent` | 5 | 3 | 4712–4716, 7030–7040, 7066 |
| `cardText-first` | 5 | 3 | 969, 3602–3628, 6262 |
| `dialog` | 5 | 3 | 3452–3462, 7030–7040, 7066 |
| `guideProgramName` | 5 | 3 | 680, 5799–5810, 5853–5858 |
| `noHomeButtonHeader` | 5 | 3 | 1714, 6546, 6700–6711 |
| `overflowBackdropCard` | 5 | 3 | 1009–1015, 3606, 6257–6262 |
| `secondary` | 5 | 3 | 314, 4616–4626, 4666 |
| `album` | 4 | 3 | 2295, 2554–2558, 2594 |
| `cardPadder` | 4 | 3 | 453, 1051, 3619–3623 |
| `cardText` | 4 | 3 | 969–979, 3628, 7408 |
| `detailPageContent` | 4 | 3 | 1816, 4806, 5086–5093 |
| `dialog-fullscreen` | 4 | 3 | 3462, 7030–7040, 7066 |
| `emby-input` | 4 | 3 | 5526, 5555–5573, 7725 |
| `emby-scrollbuttons` | 4 | 3 | 1879–1884, 7429, 7954 |
| `folder` | 4 | 3 | 1979–1984, 3730, 3793 |
| `formDialogFooter` | 4 | 3 | 3520, 4010, 7659–7683 |
| `infoWrapper` | 4 | 3 | 2238–2243, 2501, 2529 |
| `listItemIcon` | 4 | 3 | 4040–4044, 4720, 4784 |
| `listItemImage` | 4 | 3 | 2873–2878, 4580, 7642 |
| `musicParentName` | 4 | 3 | 2055, 2607, 5740–5749 |
| `programGuideSection` | 4 | 3 | 2562–2577, 4982, 5009 |
| `toast` | 4 | 3 | 5260, 7030–7040, 7066 |
| `cardFooter` | 3 | 3 | 3639, 7133, 7172 |
| `check` | 3 | 3 | 3596, 3829, 4720 |
| `collectionItems` | 3 | 3 | 1826, 4982, 5018 |
| `defaultCardBackground` | 3 | 3 | 3751, 6277, 6376 |
| `detailPageSecondaryContainer` | 3 | 3 | 1663, 1690, 1816 |
| `formDialogFooterItem` | 3 | 3 | 3520, 3788, 3922 |
| `formDialogHeader` | 3 | 3 | 4010, 7588, 7659 |
| `iconOsd` | 3 | 3 | 6027, 7588, 7659 |
| `live_tv` | 3 | 3 | 2055, 2594, 4044 |
| `myPreferencesMenuPage` | 3 | 3 | 426, 4784, 5107 |
| `playerStats` | 3 | 3 | 6027, 7659, 7695 |
| `readOnlyContent` | 3 | 3 | 4052, 6140, 6794 |
| `sectionTitle-cards` | 3 | 3 | 1794, 5176, 5236 |
| `sectionTitleContainer` | 3 | 3 | 1826, 1884, 5018 |
| `itemExternalLinks` | 13 | 2 | 3171–3249, 3400 |
| `checkboxOutline` | 10 | 2 | 3573–3614, 3645–3675 |
| `itemBackdrop` | 9 | 2 | 2021–2080, 2268 |
| `mdl-slider` | 9 | 2 | 2969, 3024–3082 |
| `cardOverlayButton-br` | 8 | 2 | 1063, 1092–1143 |
| `sliderContainer` | 8 | 2 | 2973, 3001–3066 |
| `detail-clamp-text` | 7 | 2 | 3336–3362, 3388–3392 |
| `divUsers` | 7 | 2 | 6151–6155, 7392–7419 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3610–3614, 3644–3663 |
| `countIndicator` | 6 | 2 | 810–840, 7659–7683 |
| `detailPagePrimaryContainer` | 6 | 2 | 1640–1686, 2501 |
| `detailsGroupItem` | 6 | 2 | 4841, 4912–4949 |
| `headerButton` | 6 | 2 | 600–680, 6642 |
| `headerLeft` | 6 | 2 | 1744–1781, 6899 |
| `selectionCommandsPanel` | 6 | 2 | 3530–3564, 7588 |
| `trackSelections` | 6 | 2 | 4810–4841, 4977–4982 |
| `withBackdrop` | 6 | 2 | 2677, 2718–2736 |
| `detailSection` | 5 | 2 | 4793–4802, 4962–4982 |
| `fullSyncIndicator` | 5 | 2 | 810–833, 7659–7683 |
| `mainDrawer-scrollContainer` | 5 | 2 | 3131, 7305–7322 |
| `manualLoginForm` | 5 | 2 | 6122–6166, 6207 |
| `mediaInfoItem` | 5 | 2 | 1898–1941, 7182 |
| `overview-expand` | 5 | 2 | 3368–3392, 4879 |
| `scrollX` | 5 | 2 | 1799, 1837–1857 |
| `videoIndicator` | 5 | 2 | 3719–3747, 7659 |
| `visualLoginForm` | 5 | 2 | 6122–6166, 6207 |
| `withSectionTabs` | 5 | 2 | 2727–2744, 6521 |
| `alphaPickerButton` | 4 | 2 | 680, 5033–5045 |
| `backgroundProgress` | 4 | 2 | 2884–2896, 2926 |
| `emby-select` | 4 | 2 | 5526–5538, 7725 |
| `emby-tab-button-active` | 4 | 2 | 3983, 6747–6761 |
| `emby-textarea` | 4 | 2 | 5517–5526, 5555–5573 |
| `mediaSourceIndicator` | 4 | 2 | 810–833, 7659 |
| `play_arrow` | 4 | 2 | 3756–3772, 3950 |
| `playbackProgress` | 4 | 2 | 2884–2896, 2931 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4607–4612, 6370–6376 |
| `programCell` | 4 | 2 | 5790, 5849–5858 |
| `cardOverlayButtonIcon` | 3 | 2 | 1063–1075, 1143 |
| `castCollapsible` | 3 | 2 | 872, 3614–3623 |
| `emby-scrollbuttons-button` | 3 | 2 | 1888, 7961–7968 |
| `guestCastContent` | 3 | 2 | 872, 3614–3623 |
| `guide-channelHeaderCell` | 3 | 2 | 680, 5824–5840 |
| `guide-date-tab-button` | 3 | 2 | 680, 3983–3991 |
| `headerUserButton` | 3 | 2 | 600–613, 5111 |
| `noHeaderRight` | 3 | 2 | 1714, 6049–6053 |
| `overview` | 3 | 2 | 3388–3392, 4889 |
| `add` | 2 | 2 | 1799, 7182 |
| `alphaPicker-fixed-right` | 2 | 2 | 2768, 5045 |
| `backdropImageFadeIn` | 2 | 2 | 2823, 7699 |
| `book` | 2 | 2 | 2055, 2594 |
| `btnDeleteImage` | 2 | 2 | 3776, 3997 |
| `cardContent` | 2 | 2 | 872, 904 |
| `cardOverlayButton` | 2 | 2 | 1077, 1120 |
| `cardOverlayButton-hover` | 2 | 2 | 964, 1092 |
| `chevron_right` | 2 | 2 | 5206, 5250 |
| `classList` | 2 | 2 | 1799, 7182 |
| `collapseContent` | 2 | 2 | 3525, 4008 |
| `collectionItemsContainer` | 2 | 2 | 1826, 5022 |
| `content-primary` | 2 | 2 | 5086, 5142 |
| `editorsChoiceContainer` | 2 | 2 | 6855, 7879 |
| `editorsChoiceItemBanner` | 2 | 2 | 6855, 7607 |
| `editorsChoiceItemOverview` | 2 | 2 | 7879, 7972 |
| `endsAt` | 2 | 2 | 1919, 7182 |
| `f5f5f5` | 2 | 2 | 5360, 5390 |
| `fieldDescription` | 2 | 2 | 314, 7725 |
| `formDialogFooter-clear` | 2 | 2 | 3520, 4010 |
| `guide-programNameCaret` | 2 | 2 | 314, 5806 |
| `headroom` | 2 | 2 | 6509, 6546 |
| `indicator` | 2 | 2 | 840, 3707 |
| `mc-row` | 2 | 2 | 468, 7499 |
| `mediaInfoOfficialRating` | 2 | 2 | 1919, 7182 |
| `navMenuOption-selected` | 2 | 2 | 4789, 7316 |
| `nowPlayingInfoContainer` | 2 | 2 | 3162, 6307 |
| `org` | 2 | 2 | 3198, 3228 |
| `page` | 2 | 2 | 2768, 7086 |
| `paperList` | 2 | 2 | 881, 4021 |
| `playlist` | 2 | 2 | 4602, 6285 |
| `programSecondaryTitle` | 2 | 2 | 314, 5858 |
| `queue` | 2 | 2 | 2055, 2594 |
| `reactRoot` | 2 | 2 | 4478, 6905 |
| `recordingFields` | 2 | 2 | 4833, 4977 |
| `runtime` | 2 | 2 | 6219, 6247 |
| `sectionTitleContainer-cards` | 2 | 2 | 5171, 5236 |
| `sidebarHeader` | 2 | 2 | 4148, 7322 |
| `splide` | 2 | 2 | 6855, 7928 |
| `tagline` | 2 | 2 | 2668, 4889 |
| `upNextDialog-title` | 2 | 2 | 5290, 5324 |
| `vertical-list` | 2 | 2 | 1861, 7827 |
| `vertical-wrap` | 2 | 2 | 806, 1826 |
| `videoOsdBottom` | 2 | 2 | 3154, 6476 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3154, 6476 |
| `userPreferencesPage` | 12 | 1 | 7710–7806 |
| `checkboxContainer` | 7 | 1 | 3602–3639 |
| `itemDetailsGroup` | 7 | 1 | 4896–4982 |
| `itemProgressBar` | 6 | 1 | 2873–2907 |
| `streaming-lookup-container` | 6 | 1 | 3256–3301 |
| `trackSelectionFieldContainer` | 6 | 1 | 4852–4875 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7928–7968 |
| `emby-select-withcolor` | 5 | 1 | 5526–5581 |
| `innerCardFooter` | 5 | 1 | 3415–3444 |
| `chapterCardImageContainer` | 4 | 1 | 3415–3444 |
| `endTimeText` | 4 | 1 | 6219–6247 |
| `mainDetailButtons` | 4 | 1 | 3946–3960 |
| `overview-controls` | 4 | 1 | 3388–3400 |
| `startTimeText` | 4 | 1 | 6219–6241 |
| `button-flat` | 3 | 1 | 3135–3145 |
| `cardIndicators` | 3 | 1 | 3692–3702 |
| `cardOverlayFab-primary` | 3 | 1 | 1055–1077 |
| `com` | 3 | 1 | 3204–3222 |
| `content` | 3 | 1 | 4918–4949 |
| `fab` | 3 | 1 | 3797–3810 |
| `listChildrenCollapsible` | 3 | 1 | 4967–4982 |
| `mdl-slider-background-flex` | 3 | 1 | 2993–3006 |
| `mediaInfoCriticRating` | 3 | 1 | 1960–1969 |
| `nextUpSection` | 3 | 1 | 4962–4982 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 6271–6281 |
| `serverInfo` | 3 | 1 | 4025–4034 |
| `transcodingProgress` | 3 | 1 | 2884–2896 |
