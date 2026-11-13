# Index des composants — ElegantFin Cinema Edition v1.5.8

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.5.8.css` — 8079 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 38 | 16 | 457–487, 518–553, 791, 904, 1565–1585, 2199–2232, 2259–2263, 2540–2558, 2594, 6986, 7022–7032, 7172, 7272–7291, 7369–7391, 7421–7428, 7592 |
| `cardScalable` | 29 | 14 | 457, 487, 541–553, 854–894, 920–964, 2558, 3639, 3751, 3829, 6050, 7000–7032, 7102, 7272, 7412–7428 |
| `cardImageContainer` | 21 | 13 | 468, 536, 872, 900–929, 964, 1022–1046, 6206–6210, 6290, 6992, 7102, 7142, 7272–7291, 7412 |
| `material-icons` | 17 | 13 | 393–412, 1790, 1888, 1941, 3596, 3756, 3829–3835, 3950, 4112, 4666, 5206, 5240–5250, 5867 |
| `itemDetailPage` | 20 | 12 | 1628, 1714, 1799, 1826, 2055–2095, 2130–2145, 2181–2185, 2295, 2607, 4793, 5099, 7846–7884 |
| `skinHeader` | 20 | 12 | 296, 1714, 4092–4108, 4478, 4524–4551, 6058–6062, 6499, 6555–6563, 6633–6658, 7086, 7239, 7917 |
| `js` | 13 | 12 | 330, 360, 1700–1714, 1799, 2366, 2973, 3400, 3730, 5867, 6864, 7191, 7438 |
| `emby-button` | 13 | 10 | 663–680, 707–725, 3234, 3368–3375, 3776, 3810, 3972, 4684, 5384, 5437 |
| `nameContainer` | 27 | 9 | 737, 2302–2325, 2366, 2395, 2430–2477, 2514, 2545–2549, 5623–5676, 7846–7884 |
| `parentName` | 23 | 8 | 737, 2307–2325, 2366, 2395, 2430–2477, 5629–5676, 5749, 7846–7884 |
| `detailLogo` | 20 | 8 | 737, 2084–2095, 2130–2145, 2172–2185, 2295–2325, 2395, 2430–2477, 2545 |
| `detailPageWrapperContainer` | 17 | 8 | 737, 1596–1606, 2095, 2268, 2302–2325, 2395, 2430–2477, 2545 |
| `subtitle` | 17 | 8 | 2055–2065, 2181–2185, 2307, 2366, 2486–2496, 2607, 5684–5717, 7846–7884 |
| `cardBox` | 13 | 8 | 457–487, 518–542, 791, 942–946, 1051, 6986, 7272, 7657 |
| `backdropCard` | 12 | 8 | 1009–1015, 1132, 2055–2065, 2211, 2295, 2549–2558, 2585, 2896 |
| `nowPlayingBar` | 8 | 8 | 330, 3158, 6342, 7049, 7136, 7225, 7251, 7597 |
| `card-hoverable` | 22 | 7 | 553, 920–1015, 6210, 7010, 7142–7181, 7272, 7657 |
| `listItem` | 18 | 7 | 314, 680, 2562, 4586–4612, 4643–4675, 4720, 7634–7651 |
| `loginPage` | 18 | 7 | 3916, 6062–6096, 6136–6155, 6191–6210, 7039, 7082, 7401–7428 |
| `paper-icon-button-light` | 12 | 7 | 625–680, 1714, 1790, 1888, 3536–3556, 5384, 5521 |
| `navMenuOption` | 12 | 6 | 680, 776–786, 4161, 4653–4675, 4774–4779, 7314–7325 |
| `emby-tab-button` | 11 | 6 | 680, 747–756, 3891, 6709–6720, 6748–6765, 7929 |
| `verticalSection` | 11 | 6 | 1794, 2798–2803, 5099, 7095, 7191, 7438 |
| `button-link` | 10 | 6 | 680, 707–725, 3109–3118, 3178–3188, 3234, 7808 |
| `headerTop` | 9 | 6 | 2185, 4478, 4524, 6505–6530, 6625–6642, 6669–6673 |
| `person` | 8 | 6 | 2055–2080, 2295, 2549, 2594–2603, 4044, 7841 |
| `mainDrawer` | 7 | 6 | 3123, 4126, 4524, 7039–7049, 7301, 7340 |
| `scss` | 6 | 6 | 296, 819, 1077, 3645, 4167, 7191 |
| `detailImageContainer` | 20 | 5 | 2055–2080, 2199–2263, 2295, 2536–2558, 2585–2603 |
| `btnPlay` | 19 | 5 | 562–586, 625–680, 3839–3890, 3922–3950, 5384 |
| `osdHeader` | 15 | 5 | 1763–1781, 6494–6563, 6633–6658, 7086, 7597 |
| `cardOverlayContainer` | 12 | 5 | 983–1015, 1055–1077, 1150, 7597, 7634 |
| `sectionTabs` | 11 | 5 | 1857, 3891, 4551, 6535–6540, 6726–6770 |
| `cardImageIcon` | 8 | 5 | 449–453, 2549–2558, 2621, 3623, 6290 |
| `sectionTitle` | 7 | 5 | 1794, 1867–1874, 4379, 5176–5184, 6131 |
| `semiTransparent` | 7 | 5 | 1696, 4092–4108, 6058, 6523–6544, 6580 |
| `emby-scroller-container` | 6 | 5 | 1794–1799, 1837, 2786, 7095, 7191 |
| `portraitCard` | 6 | 5 | 1132, 1216, 1979–1984, 2259, 2896 |
| `appfooter` | 5 | 5 | 330, 2839, 6683, 7125, 7597 |
| `skinHeader-withBackground` | 5 | 5 | 1696, 4092, 6058, 6494, 6544 |
| `detailButton` | 15 | 4 | 625–680, 3820–3890, 3946–3950, 5384 |
| `itemName` | 11 | 4 | 737, 2366, 5629–5676, 5767–5784 |
| `backdropImage` | 10 | 4 | 2685–2713, 2740–2744, 6979, 7102–7110 |
| `upNextContainer` | 10 | 4 | 5267–5285, 5311–5337, 7039–7049, 7075 |
| `emby-scroller` | 9 | 4 | 1799, 1837–1843, 7344–7391, 7576–7592 |
| `sectionTitleTextButton` | 9 | 4 | 479, 5159–5167, 5194–5206, 5240–5250 |
| `skip-button` | 9 | 4 | 680, 3900, 5360–5394, 5421–5439 |
| `backgroundContainer` | 8 | 4 | 2149, 2677, 2718–2736, 2768 |
| `detailRibbon` | 8 | 4 | 1653–1681, 1894, 1979–1991, 7841 |
| `visualCardBox` | 7 | 4 | 457, 881–894, 920–925, 1051 |
| `actionSheetMenuItem` | 6 | 4 | 680, 4586–4597, 4643, 7067 |
| `button-submit` | 6 | 4 | 3916, 4003, 6191–6199, 7719–7734 |
| `cardText-secondary` | 6 | 4 | 314, 969, 3628–3632, 7164–7172 |
| `detailPagePrimaryContent` | 6 | 4 | 1668–1686, 2501, 5093, 7255 |
| `skinHeader-blurred` | 6 | 4 | 6058, 6523–6530, 7239, 7597–7616 |
| `squareCard` | 6 | 4 | 904, 2549, 2585–2603, 6160–6164 |
| `itemsContainer` | 4 | 4 | 791, 1826, 1861, 5099 |
| `raised` | 4 | 4 | 680, 766, 3776, 3810 |
| `tsx` | 4 | 4 | 1132, 1714, 4478, 4555 |
| `x` | 4 | 4 | 2366, 4167, 5732, 7191 |
| `itemSelectionPanel` | 9 | 3 | 933–937, 3568, 3596–3639 |
| `pageTitle` | 8 | 3 | 1738–1781, 6555, 6658 |
| `headerButton` | 7 | 3 | 600–680, 5384, 6651 |
| `homePage` | 7 | 3 | 4478, 4524–4551, 6787 |
| `playedIndicator` | 7 | 3 | 819–833, 3712, 7272–7296 |
| `detailSectionContent` | 6 | 3 | 3400, 4879–4889, 4972–4982 |
| `emby-checkbox` | 6 | 3 | 3573, 3610–3614, 3663–3675 |
| `listItemBodyText` | 6 | 3 | 4607–4626, 4666, 7651 |
| `actionSheetContent` | 5 | 3 | 4712–4716, 7039–7049, 7075 |
| `cardText-first` | 5 | 3 | 969, 3602–3628, 6271 |
| `dialog` | 5 | 3 | 3452–3462, 7039–7049, 7075 |
| `guideProgramName` | 5 | 3 | 680, 5808–5819, 5862–5867 |
| `noHomeButtonHeader` | 5 | 3 | 1714, 6555, 6709–6720 |
| `overflowBackdropCard` | 5 | 3 | 1009–1015, 3606, 6266–6271 |
| `secondary` | 5 | 3 | 314, 4616–4626, 4666 |
| `album` | 4 | 3 | 2295, 2554–2558, 2594 |
| `cardPadder` | 4 | 3 | 453, 1051, 3619–3623 |
| `cardText` | 4 | 3 | 969–979, 3628, 7417 |
| `detailPageContent` | 4 | 3 | 1816, 4806, 5086–5093 |
| `dialog-fullscreen` | 4 | 3 | 3462, 7039–7049, 7075 |
| `emby-input` | 4 | 3 | 5535, 5564–5582, 7734 |
| `emby-scrollbuttons` | 4 | 3 | 1879–1884, 7438, 7963 |
| `folder` | 4 | 3 | 1979–1984, 3730, 3793 |
| `formDialogFooter` | 4 | 3 | 3520, 4010, 7668–7692 |
| `infoWrapper` | 4 | 3 | 2238–2243, 2501, 2529 |
| `listItemIcon` | 4 | 3 | 4040–4044, 4720, 4784 |
| `listItemImage` | 4 | 3 | 2873–2878, 4580, 7651 |
| `musicParentName` | 4 | 3 | 2055, 2607, 5749–5758 |
| `programGuideSection` | 4 | 3 | 2562–2577, 4982, 5009 |
| `toast` | 4 | 3 | 5260, 7039–7049, 7075 |
| `cardFooter` | 3 | 3 | 3639, 7142, 7181 |
| `check` | 3 | 3 | 3596, 3829, 4720 |
| `collectionItems` | 3 | 3 | 1826, 4982, 5018 |
| `defaultCardBackground` | 3 | 3 | 3751, 6286, 6385 |
| `detailPageSecondaryContainer` | 3 | 3 | 1663, 1690, 1816 |
| `formDialogFooterItem` | 3 | 3 | 3520, 3788, 3922 |
| `formDialogHeader` | 3 | 3 | 4010, 7597, 7668 |
| `iconOsd` | 3 | 3 | 6036, 7597, 7668 |
| `live_tv` | 3 | 3 | 2055, 2594, 4044 |
| `myPreferencesMenuPage` | 3 | 3 | 426, 4784, 5107 |
| `playerStats` | 3 | 3 | 6036, 7668, 7704 |
| `readOnlyContent` | 3 | 3 | 4052, 6149, 6803 |
| `sectionTitle-cards` | 3 | 3 | 1794, 5176, 5236 |
| `sectionTitleContainer` | 3 | 3 | 1826, 1884, 5018 |
| `itemExternalLinks` | 13 | 2 | 3171–3249, 3400 |
| `checkboxOutline` | 10 | 2 | 3573–3614, 3645–3675 |
| `itemBackdrop` | 9 | 2 | 2021–2080, 2268 |
| `mdl-slider` | 9 | 2 | 2969, 3024–3082 |
| `cardOverlayButton-br` | 8 | 2 | 1063, 1092–1143 |
| `sliderContainer` | 8 | 2 | 2973, 3001–3066 |
| `detail-clamp-text` | 7 | 2 | 3336–3362, 3388–3392 |
| `divUsers` | 7 | 2 | 6160–6164, 7401–7428 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3610–3614, 3644–3663 |
| `countIndicator` | 6 | 2 | 810–840, 7668–7692 |
| `detailPagePrimaryContainer` | 6 | 2 | 1640–1686, 2501 |
| `detailsGroupItem` | 6 | 2 | 4841, 4912–4949 |
| `headerLeft` | 6 | 2 | 1744–1781, 6908 |
| `selectionCommandsPanel` | 6 | 2 | 3530–3564, 7597 |
| `trackSelections` | 6 | 2 | 4810–4841, 4977–4982 |
| `withBackdrop` | 6 | 2 | 2677, 2718–2736 |
| `detailSection` | 5 | 2 | 4793–4802, 4962–4982 |
| `fullSyncIndicator` | 5 | 2 | 810–833, 7668–7692 |
| `mainDrawer-scrollContainer` | 5 | 2 | 3131, 7314–7331 |
| `manualLoginForm` | 5 | 2 | 6131–6175, 6216 |
| `mediaInfoItem` | 5 | 2 | 1898–1941, 7191 |
| `overview-expand` | 5 | 2 | 3368–3392, 4879 |
| `scrollX` | 5 | 2 | 1799, 1837–1857 |
| `videoIndicator` | 5 | 2 | 3719–3747, 7668 |
| `visualLoginForm` | 5 | 2 | 6131–6175, 6216 |
| `withSectionTabs` | 5 | 2 | 2727–2744, 6530 |
| `alphaPickerButton` | 4 | 2 | 680, 5033–5045 |
| `backgroundProgress` | 4 | 2 | 2884–2896, 2926 |
| `emby-select` | 4 | 2 | 5535–5547, 7734 |
| `emby-tab-button-active` | 4 | 2 | 3983, 6756–6770 |
| `emby-textarea` | 4 | 2 | 5526–5535, 5564–5582 |
| `mediaSourceIndicator` | 4 | 2 | 810–833, 7668 |
| `play_arrow` | 4 | 2 | 3756–3772, 3950 |
| `playbackProgress` | 4 | 2 | 2884–2896, 2931 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4607–4612, 6379–6385 |
| `programCell` | 4 | 2 | 5799, 5858–5867 |
| `cardOverlayButtonIcon` | 3 | 2 | 1063–1075, 1143 |
| `castCollapsible` | 3 | 2 | 872, 3614–3623 |
| `emby-scrollbuttons-button` | 3 | 2 | 1888, 7970–7977 |
| `guestCastContent` | 3 | 2 | 872, 3614–3623 |
| `guide-channelHeaderCell` | 3 | 2 | 680, 5833–5849 |
| `guide-date-tab-button` | 3 | 2 | 680, 3983–3991 |
| `headerUserButton` | 3 | 2 | 600–613, 5111 |
| `noHeaderRight` | 3 | 2 | 1714, 6058–6062 |
| `overview` | 3 | 2 | 3388–3392, 4889 |
| `add` | 2 | 2 | 1799, 7191 |
| `alphaPicker-fixed-right` | 2 | 2 | 2768, 5045 |
| `backdropImageFadeIn` | 2 | 2 | 2823, 7708 |
| `book` | 2 | 2 | 2055, 2594 |
| `btnDeleteImage` | 2 | 2 | 3776, 3997 |
| `cardContent` | 2 | 2 | 872, 904 |
| `cardOverlayButton` | 2 | 2 | 1077, 1120 |
| `cardOverlayButton-hover` | 2 | 2 | 964, 1092 |
| `chevron_right` | 2 | 2 | 5206, 5250 |
| `classList` | 2 | 2 | 1799, 7191 |
| `collapseContent` | 2 | 2 | 3525, 4008 |
| `collectionItemsContainer` | 2 | 2 | 1826, 5022 |
| `content-primary` | 2 | 2 | 5086, 5142 |
| `editorsChoiceContainer` | 2 | 2 | 6864, 7888 |
| `editorsChoiceItemBanner` | 2 | 2 | 6864, 7616 |
| `editorsChoiceItemOverview` | 2 | 2 | 7888, 7981 |
| `endsAt` | 2 | 2 | 1919, 7191 |
| `f5f5f5` | 2 | 2 | 5360, 5399 |
| `fieldDescription` | 2 | 2 | 314, 7734 |
| `formDialogFooter-clear` | 2 | 2 | 3520, 4010 |
| `guide-programNameCaret` | 2 | 2 | 314, 5815 |
| `headroom` | 2 | 2 | 6518, 6555 |
| `indicator` | 2 | 2 | 840, 3707 |
| `mc-row` | 2 | 2 | 468, 7508 |
| `mediaInfoOfficialRating` | 2 | 2 | 1919, 7191 |
| `navMenuOption-selected` | 2 | 2 | 4789, 7325 |
| `nowPlayingInfoContainer` | 2 | 2 | 3162, 6316 |
| `org` | 2 | 2 | 3198, 3228 |
| `page` | 2 | 2 | 2768, 7095 |
| `paperList` | 2 | 2 | 881, 4021 |
| `playlist` | 2 | 2 | 4602, 6294 |
| `programSecondaryTitle` | 2 | 2 | 314, 5867 |
| `queue` | 2 | 2 | 2055, 2594 |
| `reactRoot` | 2 | 2 | 4478, 6914 |
| `recordingFields` | 2 | 2 | 4833, 4977 |
| `runtime` | 2 | 2 | 6228, 6256 |
| `sectionTitleContainer-cards` | 2 | 2 | 5171, 5236 |
| `sidebarHeader` | 2 | 2 | 4148, 7331 |
| `splide` | 2 | 2 | 6864, 7937 |
| `tagline` | 2 | 2 | 2668, 4889 |
| `upNextDialog-title` | 2 | 2 | 5290, 5324 |
| `vertical-list` | 2 | 2 | 1861, 7836 |
| `vertical-wrap` | 2 | 2 | 806, 1826 |
| `videoOsdBottom` | 2 | 2 | 3154, 6485 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3154, 6485 |
| `userPreferencesPage` | 12 | 1 | 7719–7815 |
| `checkboxContainer` | 7 | 1 | 3602–3639 |
| `itemDetailsGroup` | 7 | 1 | 4896–4982 |
| `itemProgressBar` | 6 | 1 | 2873–2907 |
| `streaming-lookup-container` | 6 | 1 | 3256–3301 |
| `trackSelectionFieldContainer` | 6 | 1 | 4852–4875 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7937–7977 |
| `emby-select-withcolor` | 5 | 1 | 5535–5590 |
| `innerCardFooter` | 5 | 1 | 3415–3444 |
| `chapterCardImageContainer` | 4 | 1 | 3415–3444 |
| `endTimeText` | 4 | 1 | 6228–6256 |
| `mainDetailButtons` | 4 | 1 | 3946–3960 |
| `overview-controls` | 4 | 1 | 3388–3400 |
| `startTimeText` | 4 | 1 | 6228–6250 |
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
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 6280–6290 |
| `serverInfo` | 3 | 1 | 4025–4034 |
| `transcodingProgress` | 3 | 1 | 2884–2896 |
