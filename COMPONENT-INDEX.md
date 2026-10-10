# Index des composants — ElegantFin Cinema Edition v1.3.19

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.19.css` — 7688 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 36 | 14 | 428–510, 748, 865, 1517–1537, 2127–2160, 2187–2191, 2467–2485, 2521, 6660, 6918–6934, 7012–7034, 7064–7071, 7161, 7566 |
| `cardScalable` | 28 | 13 | 428–439, 487–510, 811–855, 881–919, 2485, 3539, 3650, 3729, 5848, 6674–6684, 6753, 6918, 7055–7071 |
| `itemDetailPage` | 21 | 13 | 1580, 1666, 1745, 1772, 2000–2036, 2071–2086, 2122, 2223, 2534, 3984–3995, 4652, 4939, 7394–7432 |
| `material-icons` | 17 | 13 | 364–383, 1736, 1834, 1886, 3496, 3655, 3729–3735, 3841, 3999, 4532, 5042, 5076–5086, 5666 |
| `cardImageContainer` | 22 | 12 | 482, 833, 861–890, 919, 976–1006, 5973–5977, 6057, 6666, 6745–6753, 6793, 6918–6934, 7055 |
| `skinHeader` | 16 | 10 | 284, 4344, 4390–4417, 5856, 6266, 6322–6330, 6356–6381, 6736, 6885, 7503 |
| `nameContainer` | 27 | 9 | 694, 2230–2253, 2294, 2323, 2358–2404, 2441, 2472–2476, 5423–5475, 7394–7432 |
| `emby-button` | 12 | 9 | 620–637, 664–682, 3160, 3270–3277, 3675, 3710, 3863, 4550, 5258 |
| `js` | 9 | 9 | 331, 1652, 1745, 2294, 2898, 3629, 5666, 6837, 7081 |
| `card-hoverable` | 23 | 8 | 510, 821, 881–969, 5977, 6684, 6793–6828, 6918, 7207 |
| `parentName` | 23 | 8 | 694, 2235–2253, 2294, 2323, 2358–2404, 5429–5475, 5548, 7394–7432 |
| `detailLogo` | 20 | 8 | 694, 2010–2036, 2071–2086, 2113–2122, 2223–2253, 2323, 2358–2404, 2472 |
| `listItem` | 19 | 8 | 302, 637, 2489, 4452–4478, 4509–4541, 4586, 4627, 7184–7201 |
| `detailPageWrapperContainer` | 17 | 8 | 694, 1548–1558, 2036, 2196, 2230–2253, 2323, 2358–2404, 2472 |
| `subtitle` | 16 | 8 | 2000–2010, 2122, 2235, 2294, 2413–2423, 2534, 5483–5516, 7394–7432 |
| `backdropCard` | 12 | 8 | 963–969, 1084, 2000–2010, 2139, 2223, 2476–2485, 2512, 2821 |
| `cardBox` | 12 | 8 | 428–476, 502, 748, 903, 1010, 6660, 6918, 7207 |
| `nowPlayingBar` | 8 | 8 | 318, 3084, 6109, 6699, 6787, 6871, 6897, 7166 |
| `loginPage` | 16 | 7 | 3808, 5860–5891, 5930, 5958–5977, 6689, 6732, 7044–7071 |
| `navMenuOption` | 12 | 6 | 637, 733–743, 4049, 4519–4541, 4633–4638, 6957–6968 |
| `paper-icon-button-light` | 11 | 6 | 582–637, 1666, 1736, 1834, 3436–3456, 5342 |
| `verticalSection` | 11 | 6 | 1740, 2723–2728, 4939, 6745, 6837, 7081 |
| `button-link` | 10 | 6 | 637, 664–682, 3034–3043, 3104–3114, 3160, 7357 |
| `person` | 8 | 6 | 2000–2021, 2223, 2476, 2521–2530, 3936, 7389 |
| `mainDrawer` | 7 | 6 | 3048, 4013, 4390, 6689–6699, 6944, 6983 |
| `scss` | 6 | 6 | 284, 776, 1036, 3545, 4055, 6837 |
| `detailImageContainer` | 20 | 5 | 2000–2021, 2127–2191, 2223, 2463–2485, 2512–2530 |
| `osdHeader` | 15 | 5 | 1709–1727, 6261–6330, 6356–6381, 6736, 7166 |
| `actionSheetMenuItem` | 10 | 5 | 637, 4452–4463, 4509, 4586–4627, 6717 |
| `sectionTabs` | 10 | 5 | 1803, 3787, 4417, 6302–6307, 6447–6478 |
| `cardImageIcon` | 8 | 5 | 420–424, 2476–2485, 2548, 3523, 6057 |
| `headerTop` | 8 | 5 | 4344, 4390, 6272–6297, 6348–6365, 6392–6396 |
| `sectionTitle` | 7 | 5 | 1740, 1813–1820, 4245, 5012–5020, 5925 |
| `emby-scroller-container` | 6 | 5 | 1740–1745, 1783, 2713, 6745, 6837 |
| `portraitCard` | 6 | 5 | 1084, 1168, 1924–1929, 2187, 2821 |
| `skinHeader-withBackground` | 5 | 5 | 1648, 3984, 5856, 6261, 6311 |
| `btnPlay` | 16 | 4 | 519–543, 582–637, 3739–3781, 3814–3841 |
| `cardOverlayContainer` | 12 | 4 | 937–969, 1014–1036, 1102, 7166–7184 |
| `itemName` | 11 | 4 | 694, 2294, 5429–5475, 5566–5583 |
| `backdropImage` | 10 | 4 | 2613–2640, 2667–2671, 6653, 6753–6761 |
| `emby-tab-button` | 10 | 4 | 637, 704–713, 3787, 6432–6473 |
| `upNextContainer` | 10 | 4 | 5104–5123, 5149–5175, 6689–6699, 6725 |
| `emby-scroller` | 9 | 4 | 1745, 1783–1789, 6987–7034, 7145–7161 |
| `backgroundContainer` | 8 | 4 | 2090, 2604, 2645–2663, 2695 |
| `detailRibbon` | 8 | 4 | 1605–1633, 1839, 1924–1936, 7389 |
| `listItemBodyText` | 7 | 4 | 4473–4492, 4532, 4607, 7201 |
| `skip-button` | 7 | 4 | 637, 3792, 5198–5215, 5242–5260 |
| `visualCardBox` | 7 | 4 | 428, 842–855, 881–886, 1010 |
| `button-submit` | 6 | 4 | 3808, 3895, 5958–5966, 7269–7283 |
| `cardText-secondary` | 6 | 4 | 302, 924, 3528–3532, 6815–6823 |
| `detailPagePrimaryContent` | 6 | 4 | 1620–1638, 2428, 4933, 6901 |
| `squareCard` | 6 | 4 | 865, 2476, 2512–2530, 5934–5938 |
| `skinHeader-blurred` | 5 | 4 | 5856, 6290–6297, 6885, 7166 |
| `appfooter` | 4 | 4 | 2764, 6406, 6776, 7166 |
| `itemsContainer` | 4 | 4 | 748, 1772, 1807, 4939 |
| `raised` | 4 | 4 | 637, 723, 3675, 3710 |
| `x` | 4 | 4 | 2294, 4055, 5531, 6837 |
| `detailButton` | 13 | 3 | 582–637, 3720–3781, 3837–3841 |
| `itemSelectionPanel` | 9 | 3 | 894–898, 3468, 3496–3539 |
| `pageTitle` | 8 | 3 | 1684–1727, 6322, 6381 |
| `sectionTitleTextButton` | 8 | 3 | 4995–5003, 5030–5042, 5076–5086 |
| `homePage` | 7 | 3 | 4344, 4390–4417, 6495 |
| `playedIndicator` | 7 | 3 | 776–790, 3612, 6918–6939 |
| `check` | 6 | 3 | 3496, 3729, 4586–4627 |
| `detailSectionContent` | 6 | 3 | 3302, 4734–4744, 4824–4834 |
| `emby-checkbox` | 6 | 3 | 3473, 3510–3514, 3563–3575 |
| `actionSheetContent` | 5 | 3 | 4578–4582, 6689–6699, 6725 |
| `cardText-first` | 5 | 3 | 924, 3502–3528, 6038 |
| `dialog` | 5 | 3 | 3352–3362, 6689–6699, 6725 |
| `guideProgramName` | 5 | 3 | 637, 5607–5618, 5661–5666 |
| `noHomeButtonHeader` | 5 | 3 | 1666, 6322, 6432–6440 |
| `overflowBackdropCard` | 5 | 3 | 963–969, 3506, 6033–6038 |
| `secondary` | 5 | 3 | 302, 4482–4492, 4532 |
| `album` | 4 | 3 | 2223, 2481–2485, 2521 |
| `cardPadder` | 4 | 3 | 424, 1010, 3519–3523 |
| `cardText` | 4 | 3 | 924–934, 3528, 7060 |
| `detailPageContent` | 4 | 3 | 1762, 4665, 4926–4933 |
| `dialog-fullscreen` | 4 | 3 | 3362, 6689–6699, 6725 |
| `emby-scrollbuttons` | 4 | 3 | 1825–1830, 7081, 7541 |
| `folder` | 4 | 3 | 1924–1929, 3629, 3693 |
| `formDialogFooter` | 4 | 3 | 3420, 3902, 7218–7242 |
| `infoWrapper` | 4 | 3 | 2166–2171, 2428, 2456 |
| `listItemImage` | 4 | 3 | 2798–2803, 4446, 7201 |
| `musicParentName` | 4 | 3 | 2000, 2534, 5548–5557 |
| `semiTransparent` | 4 | 3 | 1648, 5856, 6290–6311 |
| `toast` | 4 | 3 | 5096, 6689–6699, 6725 |
| `cardFooter` | 3 | 3 | 3539, 6793, 6828 |
| `defaultCardBackground` | 3 | 3 | 3650, 6053, 6152 |
| `detailPageSecondaryContainer` | 3 | 3 | 1615, 1642, 1762 |
| `formDialogFooterItem` | 3 | 3 | 3420, 3688, 3814 |
| `formDialogHeader` | 3 | 3 | 3902, 7166, 7218 |
| `iconOsd` | 3 | 3 | 5834, 7166, 7218 |
| `live_tv` | 3 | 3 | 2000, 2521, 3936 |
| `myPreferencesMenuPage` | 3 | 3 | 397, 4643, 4947 |
| `page` | 3 | 3 | 1006, 2695, 6745 |
| `playerStats` | 3 | 3 | 5834, 7218, 7254 |
| `sectionTitle-cards` | 3 | 3 | 1740, 5012, 5072 |
| `sectionTitleContainer` | 3 | 3 | 1772, 1830, 4858 |
| `tsx` | 3 | 3 | 1084, 4344, 4421 |
| `itemExternalLinks` | 13 | 2 | 3097–3175, 3302 |
| `checkboxOutline` | 10 | 2 | 3473–3514, 3545–3575 |
| `itemBackdrop` | 9 | 2 | 1966–2021, 2196 |
| `mdl-slider` | 9 | 2 | 2894, 2949–3007 |
| `listItemIcon` | 8 | 2 | 3932–3936, 4586–4643 |
| `sliderContainer` | 8 | 2 | 2898, 2926–2991 |
| `cardOverlayButton-br` | 7 | 2 | 1022, 1051–1095 |
| `detail-clamp-text` | 7 | 2 | 3238–3264, 3290–3294 |
| `divUsers` | 7 | 2 | 5934–5938, 7044–7071 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3510–3514, 3544–3563 |
| `countIndicator` | 6 | 2 | 767–797, 7218–7242 |
| `detailPagePrimaryContainer` | 6 | 2 | 1592–1638, 2428 |
| `detailsGroupItem` | 6 | 2 | 4696, 4764–4801 |
| `headerButton` | 6 | 2 | 557–637, 6374 |
| `headerLeft` | 6 | 2 | 1690–1727, 6582 |
| `selectionCommandsPanel` | 6 | 2 | 3430–3464, 7166 |
| `trackSelections` | 6 | 2 | 4669–4696, 4829–4834 |
| `withBackdrop` | 6 | 2 | 2604, 2645–2663 |
| `detailSection` | 5 | 2 | 4652–4661, 4814–4834 |
| `fullSyncIndicator` | 5 | 2 | 767–790, 7218–7242 |
| `mainDrawer-scrollContainer` | 5 | 2 | 3057, 6957–6974 |
| `mediaInfoItem` | 5 | 2 | 1843–1886, 6837 |
| `overview-expand` | 5 | 2 | 3270–3294, 4734 |
| `scrollX` | 5 | 2 | 1745, 1783–1803 |
| `videoIndicator` | 5 | 2 | 3618–3646, 7218 |
| `withSectionTabs` | 5 | 2 | 2654–2671, 6297 |
| `alphaPickerButton` | 4 | 2 | 637, 4873–4885 |
| `backgroundProgress` | 4 | 2 | 2809–2821, 2851 |
| `emby-tab-button-active` | 4 | 2 | 3874, 6464–6478 |
| `mediaSourceIndicator` | 4 | 2 | 767–790, 7218 |
| `play_arrow` | 4 | 2 | 3655–3671, 3841 |
| `playbackProgress` | 4 | 2 | 2809–2821, 2856 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4473–4478, 6146–6152 |
| `programCell` | 4 | 2 | 5598, 5657–5666 |
| `programGuideSection` | 4 | 2 | 2489–2504, 4834–4849 |
| `section0` | 4 | 2 | 976–1006, 6745 |
| `visualLoginForm` | 4 | 2 | 5925–5942, 5983 |
| `cardOverlayButtonIcon` | 3 | 2 | 1022–1034, 1095 |
| `castCollapsible` | 3 | 2 | 833, 3514–3523 |
| `collectionItems` | 3 | 2 | 1772, 4834–4858 |
| `emby-input` | 3 | 2 | 5356–5372, 7283 |
| `emby-scrollbuttons-button` | 3 | 2 | 1834, 7548–7555 |
| `guestCastContent` | 3 | 2 | 833, 3514–3523 |
| `guide-channelHeaderCell` | 3 | 2 | 637, 5632–5648 |
| `guide-date-tab-button` | 3 | 2 | 637, 3874–3882 |
| `headerUserButton` | 3 | 2 | 557–570, 4951 |
| `manualLoginForm` | 3 | 2 | 5925–5942, 5983 |
| `overview` | 3 | 2 | 3290–3294, 4744 |
| `add` | 2 | 2 | 1745, 6837 |
| `alphaPicker-fixed-right` | 2 | 2 | 2695, 4885 |
| `backdropImageFadeIn` | 2 | 2 | 2748, 7258 |
| `book` | 2 | 2 | 2000, 2521 |
| `btnDeleteImage` | 2 | 2 | 3675, 3888 |
| `cardContent` | 2 | 2 | 833, 865 |
| `cardOverlayButton` | 2 | 2 | 1036, 1072 |
| `cardOverlayButton-hover` | 2 | 2 | 919, 1051 |
| `chevron_right` | 2 | 2 | 5042, 5086 |
| `classList` | 2 | 2 | 1745, 6837 |
| `collapseContent` | 2 | 2 | 3425, 3900 |
| `collectionItemsContainer` | 2 | 2 | 1772, 4862 |
| `content-primary` | 2 | 2 | 4926, 4978 |
| `editorsChoiceItemOverview` | 2 | 2 | 7478, 7559 |
| `emby-select` | 2 | 2 | 5356, 7283 |
| `endsAt` | 2 | 2 | 1864, 6837 |
| `fieldDescription` | 2 | 2 | 302, 7283 |
| `formDialogFooter-clear` | 2 | 2 | 3420, 3902 |
| `guide-programNameCaret` | 2 | 2 | 302, 5614 |
| `headroom` | 2 | 2 | 6285, 6322 |
| `indicator` | 2 | 2 | 797, 3607 |
| `mediaInfoOfficialRating` | 2 | 2 | 1864, 6837 |
| `navMenuOption-selected` | 2 | 2 | 4648, 6968 |
| `nowPlayingInfoContainer` | 2 | 2 | 3088, 6083 |
| `org` | 2 | 2 | 3124, 3154 |
| `paperList` | 2 | 2 | 842, 3913 |
| `playlist` | 2 | 2 | 4468, 6061 |
| `programSecondaryTitle` | 2 | 2 | 302, 5666 |
| `queue` | 2 | 2 | 2000, 2521 |
| `reactRoot` | 2 | 2 | 4344, 6588 |
| `readOnlyContent` | 2 | 2 | 3944, 6511 |
| `recordingFields` | 2 | 2 | 4688, 4829 |
| `runtime` | 2 | 2 | 5995, 6023 |
| `sectionTitleContainer-cards` | 2 | 2 | 5007, 5072 |
| `sidebarHeader` | 2 | 2 | 4036, 6974 |
| `tagline` | 2 | 2 | 2595, 4744 |
| `upNextDialog-title` | 2 | 2 | 5128, 5162 |
| `vertical-list` | 2 | 2 | 1807, 7384 |
| `vertical-wrap` | 2 | 2 | 763, 1772 |
| `videoOsdBottom` | 2 | 2 | 3080, 6252 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3080, 6252 |
| `userPreferencesPage` | 12 | 1 | 7269–7364 |
| `checkboxContainer` | 7 | 1 | 3502–3539 |
| `itemDetailsGroup` | 7 | 1 | 4748–4834 |
| `itemProgressBar` | 6 | 1 | 2798–2832 |
| `streaming-lookup-container` | 6 | 1 | 3182–3227 |
| `trackSelectionFieldContainer` | 6 | 1 | 4707–4730 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7515–7555 |
| `innerCardFooter` | 5 | 1 | 3315–3344 |
| `chapterCardImageContainer` | 4 | 1 | 3315–3344 |
| `endTimeText` | 4 | 1 | 5995–6023 |
| `mainDetailButtons` | 4 | 1 | 3837–3851 |
| `overview-controls` | 4 | 1 | 3290–3302 |
| `startTimeText` | 4 | 1 | 5995–6017 |
| `button-flat` | 3 | 1 | 3061–3071 |
| `cardIndicators` | 3 | 1 | 3592–3602 |
| `cardOverlayFab-primary` | 3 | 1 | 1014–1036 |
| `com` | 3 | 1 | 3130–3148 |
| `content` | 3 | 1 | 4770–4801 |
| `discover-card` | 3 | 1 | 7566–7589 |
| `emby-select-withcolor` | 3 | 1 | 5356–5390 |
| `emby-textarea` | 3 | 1 | 5347–5372 |
| `fab` | 3 | 1 | 3697–3710 |
| `listChildrenCollapsible` | 3 | 1 | 4819–4834 |
| `mdl-slider-background-flex` | 3 | 1 | 2918–2931 |
| `mediaInfoCriticRating` | 3 | 1 | 1905–1914 |
| `nextUpSection` | 3 | 1 | 4814–4834 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 6047–6057 |
| `serverInfo` | 3 | 1 | 3917–3926 |
| `transcodingProgress` | 3 | 1 | 2809–2821 |
