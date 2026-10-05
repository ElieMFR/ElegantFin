# Index des composants — ElegantFin Cinema Edition v1.3.15

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.15.css` — 7482 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 36 | 14 | 428–510, 748, 865, 1511–1531, 2121–2154, 2181–2185, 2461–2479, 2515, 6454, 6712–6728, 6806–6828, 6858–6865, 6955, 7360 |
| `cardScalable` | 28 | 13 | 428–439, 487–510, 811–855, 881–919, 2479, 3484, 3595, 3674, 5647, 6468–6478, 6547, 6712, 6849–6865 |
| `itemDetailPage` | 21 | 13 | 1574, 1660, 1739, 1766, 1994–2030, 2065–2080, 2116, 2217, 2528, 3929–3940, 4463, 4750, 7188–7226 |
| `material-icons` | 17 | 13 | 364–383, 1730, 1828, 1880, 3441, 3600, 3674–3680, 3786, 3944, 4347, 4853, 4887–4897, 5465 |
| `cardImageContainer` | 22 | 12 | 482, 833, 861–890, 919, 976–1006, 5772–5776, 5856, 6460, 6539–6547, 6587, 6712–6728, 6849 |
| `skinHeader` | 16 | 10 | 284, 4159, 4205–4232, 5655, 6065, 6121–6129, 6155–6180, 6530, 6679, 7297 |
| `nameContainer` | 27 | 9 | 694, 2224–2247, 2288, 2317, 2352–2398, 2435, 2466–2470, 5222–5274, 7188–7226 |
| `js` | 9 | 9 | 331, 1646, 1739, 2288, 2892, 3574, 5465, 6631, 6875 |
| `card-hoverable` | 23 | 8 | 510, 821, 881–969, 5776, 6478, 6587–6622, 6712, 7001 |
| `parentName` | 23 | 8 | 694, 2229–2247, 2288, 2317, 2352–2398, 5228–5274, 5347, 7188–7226 |
| `detailLogo` | 20 | 8 | 694, 2004–2030, 2065–2080, 2107–2116, 2217–2247, 2317, 2352–2398, 2466 |
| `listItem` | 19 | 8 | 302, 637, 2483, 4267–4293, 4324–4356, 4398, 4438, 6978–6995 |
| `detailPageWrapperContainer` | 17 | 8 | 694, 1542–1552, 2030, 2190, 2224–2247, 2317, 2352–2398, 2466 |
| `subtitle` | 16 | 8 | 1994–2004, 2116, 2229, 2288, 2407–2417, 2528, 5282–5315, 7188–7226 |
| `backdropCard` | 12 | 8 | 963–969, 1084, 1994–2004, 2133, 2217, 2470–2479, 2506, 2815 |
| `cardBox` | 12 | 8 | 428–476, 502, 748, 903, 1010, 6454, 6712, 7001 |
| `emby-button` | 11 | 8 | 620–637, 664–682, 3154, 3215–3222, 3620, 3655, 3808, 4365 |
| `nowPlayingBar` | 8 | 8 | 318, 3078, 5908, 6493, 6581, 6665, 6691, 6960 |
| `loginPage` | 16 | 7 | 3753, 5659–5690, 5729, 5757–5776, 6483, 6526, 6838–6865 |
| `navMenuOption` | 12 | 6 | 637, 733–743, 3994, 4334–4356, 4444–4449, 6751–6762 |
| `paper-icon-button-light` | 11 | 6 | 582–637, 1660, 1730, 1828, 3381–3401, 5141 |
| `verticalSection` | 11 | 6 | 1734, 2717–2722, 4750, 6539, 6631, 6875 |
| `button-link` | 10 | 6 | 637, 664–682, 3028–3037, 3098–3108, 3154, 7151 |
| `person` | 8 | 6 | 1994–2015, 2217, 2470, 2515–2524, 3881, 7183 |
| `mainDrawer` | 7 | 6 | 3042, 3958, 4205, 6483–6493, 6738, 6777 |
| `detailImageContainer` | 20 | 5 | 1994–2015, 2121–2185, 2217, 2457–2479, 2506–2524 |
| `osdHeader` | 15 | 5 | 1703–1721, 6060–6129, 6155–6180, 6530, 6960 |
| `actionSheetMenuItem` | 10 | 5 | 637, 4267–4278, 4324, 4398–4438, 6511 |
| `sectionTabs` | 10 | 5 | 1797, 3732, 4232, 6101–6106, 6246–6272 |
| `cardImageIcon` | 8 | 5 | 420–424, 2470–2479, 2542, 3468, 5856 |
| `headerTop` | 8 | 5 | 4159, 4205, 6071–6096, 6147–6164, 6191–6195 |
| `sectionTitle` | 7 | 5 | 1734, 1807–1814, 4060, 4823–4831, 5724 |
| `emby-scroller-container` | 6 | 5 | 1734–1739, 1777, 2707, 6539, 6631 |
| `portraitCard` | 6 | 5 | 1084, 1162, 1918–1923, 2181, 2815 |
| `scss` | 5 | 5 | 284, 776, 1036, 3490, 6631 |
| `skinHeader-withBackground` | 5 | 5 | 1642, 3929, 5655, 6060, 6110 |
| `btnPlay` | 16 | 4 | 519–543, 582–637, 3684–3726, 3759–3786 |
| `cardOverlayContainer` | 12 | 4 | 937–969, 1014–1036, 1096, 6960–6978 |
| `itemName` | 11 | 4 | 694, 2288, 5228–5274, 5365–5382 |
| `backdropImage` | 10 | 4 | 2607–2634, 2661–2665, 6447, 6547–6555 |
| `emby-tab-button` | 10 | 4 | 637, 704–713, 3732, 6231–6267 |
| `upNextContainer` | 10 | 4 | 4915–4934, 4960–4986, 6483–6493, 6519 |
| `emby-scroller` | 9 | 4 | 1739, 1777–1783, 6781–6828, 6939–6955 |
| `backgroundContainer` | 8 | 4 | 2084, 2598, 2639–2657, 2689 |
| `detailRibbon` | 8 | 4 | 1599–1627, 1833, 1918–1930, 7183 |
| `listItemBodyText` | 7 | 4 | 4288–4307, 4347, 4418, 6995 |
| `visualCardBox` | 7 | 4 | 428, 842–855, 881–886, 1010 |
| `button-submit` | 6 | 4 | 3753, 3840, 5757–5765, 7063–7077 |
| `cardText-secondary` | 6 | 4 | 302, 924, 3473–3477, 6609–6617 |
| `detailPagePrimaryContent` | 6 | 4 | 1614–1632, 2422, 4744, 6695 |
| `skip-button` | 6 | 4 | 637, 3737, 5009–5026, 5053–5059 |
| `squareCard` | 6 | 4 | 865, 2470, 2506–2524, 5733–5737 |
| `skinHeader-blurred` | 5 | 4 | 5655, 6089–6096, 6679, 6960 |
| `appfooter` | 4 | 4 | 2758, 6205, 6570, 6960 |
| `itemsContainer` | 4 | 4 | 748, 1766, 1801, 4750 |
| `raised` | 4 | 4 | 637, 723, 3620, 3655 |
| `detailButton` | 13 | 3 | 582–637, 3665–3726, 3782–3786 |
| `itemSelectionPanel` | 9 | 3 | 894–898, 3413, 3441–3484 |
| `pageTitle` | 8 | 3 | 1678–1721, 6121, 6180 |
| `sectionTitleTextButton` | 8 | 3 | 4806–4814, 4841–4853, 4887–4897 |
| `homePage` | 7 | 3 | 4159, 4205–4232, 6289 |
| `playedIndicator` | 7 | 3 | 776–790, 3557, 6712–6733 |
| `check` | 6 | 3 | 3441, 3674, 4398–4438 |
| `detailSectionContent` | 6 | 3 | 3247, 4545–4555, 4635–4645 |
| `emby-checkbox` | 6 | 3 | 3418, 3455–3459, 3508–3520 |
| `actionSheetContent` | 5 | 3 | 4390–4394, 6483–6493, 6519 |
| `cardText-first` | 5 | 3 | 924, 3447–3473, 5837 |
| `dialog` | 5 | 3 | 3297–3307, 6483–6493, 6519 |
| `guideProgramName` | 5 | 3 | 637, 5406–5417, 5460–5465 |
| `noHomeButtonHeader` | 5 | 3 | 1660, 6121, 6231–6239 |
| `overflowBackdropCard` | 5 | 3 | 963–969, 3451, 5832–5837 |
| `secondary` | 5 | 3 | 302, 4297–4307, 4347 |
| `album` | 4 | 3 | 2217, 2475–2479, 2515 |
| `cardPadder` | 4 | 3 | 424, 1010, 3464–3468 |
| `cardText` | 4 | 3 | 924–934, 3473, 6854 |
| `detailPageContent` | 4 | 3 | 1756, 4476, 4737–4744 |
| `dialog-fullscreen` | 4 | 3 | 3307, 6483–6493, 6519 |
| `emby-scrollbuttons` | 4 | 3 | 1819–1824, 6875, 7335 |
| `folder` | 4 | 3 | 1918–1923, 3574, 3638 |
| `formDialogFooter` | 4 | 3 | 3365, 3847, 7012–7036 |
| `infoWrapper` | 4 | 3 | 2160–2165, 2422, 2450 |
| `listItemImage` | 4 | 3 | 2792–2797, 4261, 6995 |
| `musicParentName` | 4 | 3 | 1994, 2528, 5347–5356 |
| `semiTransparent` | 4 | 3 | 1642, 5655, 6089–6110 |
| `toast` | 4 | 3 | 4907, 6483–6493, 6519 |
| `cardFooter` | 3 | 3 | 3484, 6587, 6622 |
| `defaultCardBackground` | 3 | 3 | 3595, 5852, 5951 |
| `detailPageSecondaryContainer` | 3 | 3 | 1609, 1636, 1756 |
| `formDialogFooterItem` | 3 | 3 | 3365, 3633, 3759 |
| `formDialogHeader` | 3 | 3 | 3847, 6960, 7012 |
| `iconOsd` | 3 | 3 | 5633, 6960, 7012 |
| `live_tv` | 3 | 3 | 1994, 2515, 3881 |
| `myPreferencesMenuPage` | 3 | 3 | 397, 4454, 4758 |
| `page` | 3 | 3 | 1006, 2689, 6539 |
| `playerStats` | 3 | 3 | 5633, 7012, 7048 |
| `sectionTitle-cards` | 3 | 3 | 1734, 4823, 4883 |
| `sectionTitleContainer` | 3 | 3 | 1766, 1824, 4669 |
| `x` | 3 | 3 | 2288, 5330, 6631 |
| `itemExternalLinks` | 13 | 2 | 3091–3169, 3247 |
| `checkboxOutline` | 10 | 2 | 3418–3459, 3490–3520 |
| `itemBackdrop` | 9 | 2 | 1960–2015, 2190 |
| `mdl-slider` | 9 | 2 | 2888, 2943–3001 |
| `listItemIcon` | 8 | 2 | 3877–3881, 4398–4454 |
| `sliderContainer` | 8 | 2 | 2892, 2920–2985 |
| `cardOverlayButton-br` | 7 | 2 | 1022, 1051–1089 |
| `detail-clamp-text` | 7 | 2 | 3183–3209, 3235–3239 |
| `divUsers` | 7 | 2 | 5733–5737, 6838–6865 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3455–3459, 3489–3508 |
| `countIndicator` | 6 | 2 | 767–797, 7012–7036 |
| `detailPagePrimaryContainer` | 6 | 2 | 1586–1632, 2422 |
| `detailsGroupItem` | 6 | 2 | 4507, 4575–4612 |
| `headerButton` | 6 | 2 | 557–637, 6173 |
| `headerLeft` | 6 | 2 | 1684–1721, 6376 |
| `selectionCommandsPanel` | 6 | 2 | 3375–3409, 6960 |
| `trackSelections` | 6 | 2 | 4480–4507, 4640–4645 |
| `withBackdrop` | 6 | 2 | 2598, 2639–2657 |
| `detailSection` | 5 | 2 | 4463–4472, 4625–4645 |
| `fullSyncIndicator` | 5 | 2 | 767–790, 7012–7036 |
| `mainDrawer-scrollContainer` | 5 | 2 | 3051, 6751–6768 |
| `mediaInfoItem` | 5 | 2 | 1837–1880, 6631 |
| `overview-expand` | 5 | 2 | 3215–3239, 4545 |
| `scrollX` | 5 | 2 | 1739, 1777–1797 |
| `videoIndicator` | 5 | 2 | 3563–3591, 7012 |
| `withSectionTabs` | 5 | 2 | 2648–2665, 6096 |
| `alphaPickerButton` | 4 | 2 | 637, 4684–4696 |
| `backgroundProgress` | 4 | 2 | 2803–2815, 2845 |
| `emby-tab-button-active` | 4 | 2 | 3819, 6258–6272 |
| `mediaSourceIndicator` | 4 | 2 | 767–790, 7012 |
| `play_arrow` | 4 | 2 | 3600–3616, 3786 |
| `playbackProgress` | 4 | 2 | 2803–2815, 2850 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4288–4293, 5945–5951 |
| `programCell` | 4 | 2 | 5397, 5456–5465 |
| `programGuideSection` | 4 | 2 | 2483–2498, 4645–4660 |
| `section0` | 4 | 2 | 976–1006, 6539 |
| `visualLoginForm` | 4 | 2 | 5724–5741, 5782 |
| `cardOverlayButtonIcon` | 3 | 2 | 1022–1034, 1089 |
| `castCollapsible` | 3 | 2 | 833, 3459–3468 |
| `collectionItems` | 3 | 2 | 1766, 4645–4669 |
| `emby-input` | 3 | 2 | 5155–5171, 7077 |
| `emby-scrollbuttons-button` | 3 | 2 | 1828, 7342–7349 |
| `guestCastContent` | 3 | 2 | 833, 3459–3468 |
| `guide-channelHeaderCell` | 3 | 2 | 637, 5431–5447 |
| `guide-date-tab-button` | 3 | 2 | 637, 3819–3827 |
| `headerUserButton` | 3 | 2 | 557–570, 4762 |
| `manualLoginForm` | 3 | 2 | 5724–5741, 5782 |
| `overview` | 3 | 2 | 3235–3239, 4555 |
| `add` | 2 | 2 | 1739, 6631 |
| `alphaPicker-fixed-right` | 2 | 2 | 2689, 4696 |
| `backdropImageFadeIn` | 2 | 2 | 2742, 7052 |
| `book` | 2 | 2 | 1994, 2515 |
| `btnDeleteImage` | 2 | 2 | 3620, 3833 |
| `cardContent` | 2 | 2 | 833, 865 |
| `cardOverlayButton` | 2 | 2 | 1036, 1072 |
| `cardOverlayButton-hover` | 2 | 2 | 919, 1051 |
| `chevron_right` | 2 | 2 | 4853, 4897 |
| `classList` | 2 | 2 | 1739, 6631 |
| `collapseContent` | 2 | 2 | 3370, 3845 |
| `collectionItemsContainer` | 2 | 2 | 1766, 4673 |
| `content-primary` | 2 | 2 | 4737, 4789 |
| `editorsChoiceItemOverview` | 2 | 2 | 7272, 7353 |
| `emby-select` | 2 | 2 | 5155, 7077 |
| `endsAt` | 2 | 2 | 1858, 6631 |
| `fieldDescription` | 2 | 2 | 302, 7077 |
| `formDialogFooter-clear` | 2 | 2 | 3365, 3847 |
| `guide-programNameCaret` | 2 | 2 | 302, 5413 |
| `headroom` | 2 | 2 | 6084, 6121 |
| `indicator` | 2 | 2 | 797, 3552 |
| `mediaInfoOfficialRating` | 2 | 2 | 1858, 6631 |
| `navMenuOption-selected` | 2 | 2 | 4459, 6762 |
| `nowPlayingInfoContainer` | 2 | 2 | 3082, 5882 |
| `org` | 2 | 2 | 3118, 3148 |
| `paperList` | 2 | 2 | 842, 3858 |
| `playlist` | 2 | 2 | 4283, 5860 |
| `programSecondaryTitle` | 2 | 2 | 302, 5465 |
| `queue` | 2 | 2 | 1994, 2515 |
| `reactRoot` | 2 | 2 | 4159, 6382 |
| `readOnlyContent` | 2 | 2 | 3889, 6305 |
| `recordingFields` | 2 | 2 | 4499, 4640 |
| `runtime` | 2 | 2 | 5794, 5822 |
| `sectionTitleContainer-cards` | 2 | 2 | 4818, 4883 |
| `sidebarHeader` | 2 | 2 | 3981, 6768 |
| `tagline` | 2 | 2 | 2589, 4555 |
| `tsx` | 2 | 2 | 4159, 4236 |
| `upNextDialog-title` | 2 | 2 | 4939, 4973 |
| `vertical-list` | 2 | 2 | 1801, 7178 |
| `vertical-wrap` | 2 | 2 | 763, 1766 |
| `videoOsdBottom` | 2 | 2 | 3074, 6051 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3074, 6051 |
| `userPreferencesPage` | 12 | 1 | 7063–7158 |
| `checkboxContainer` | 7 | 1 | 3447–3484 |
| `itemDetailsGroup` | 7 | 1 | 4559–4645 |
| `itemProgressBar` | 6 | 1 | 2792–2826 |
| `trackSelectionFieldContainer` | 6 | 1 | 4518–4541 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7309–7349 |
| `innerCardFooter` | 5 | 1 | 3260–3289 |
| `chapterCardImageContainer` | 4 | 1 | 3260–3289 |
| `endTimeText` | 4 | 1 | 5794–5822 |
| `mainDetailButtons` | 4 | 1 | 3782–3796 |
| `overview-controls` | 4 | 1 | 3235–3247 |
| `startTimeText` | 4 | 1 | 5794–5816 |
| `button-flat` | 3 | 1 | 3055–3065 |
| `cardIndicators` | 3 | 1 | 3537–3547 |
| `cardOverlayFab-primary` | 3 | 1 | 1014–1036 |
| `com` | 3 | 1 | 3124–3142 |
| `content` | 3 | 1 | 4581–4612 |
| `discover-card` | 3 | 1 | 7360–7383 |
| `emby-select-withcolor` | 3 | 1 | 5155–5189 |
| `emby-textarea` | 3 | 1 | 5146–5171 |
| `fab` | 3 | 1 | 3642–3655 |
| `listChildrenCollapsible` | 3 | 1 | 4630–4645 |
| `mdl-slider-background-flex` | 3 | 1 | 2912–2925 |
| `mediaInfoCriticRating` | 3 | 1 | 1899–1908 |
| `nextUpSection` | 3 | 1 | 4625–4645 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 5846–5856 |
| `serverInfo` | 3 | 1 | 3862–3871 |
| `transcodingProgress` | 3 | 1 | 2803–2815 |
