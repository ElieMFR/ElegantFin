# Index des composants — ElegantFin Cinema Edition v1.3.15

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.15.css` — 7469 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 36 | 14 | 428–510, 748, 865, 1511–1531, 2121–2154, 2181–2185, 2461–2479, 2515, 6441, 6699–6715, 6793–6815, 6845–6852, 6942, 7347 |
| `cardScalable` | 28 | 13 | 428–439, 487–510, 811–855, 881–919, 2479, 3484, 3595, 3674, 5634, 6455–6465, 6534, 6699, 6836–6852 |
| `itemDetailPage` | 21 | 13 | 1574, 1660, 1739, 1766, 1994–2030, 2065–2080, 2116, 2217, 2528, 3929–3940, 4450, 4737, 7175–7213 |
| `material-icons` | 17 | 13 | 364–383, 1730, 1828, 1880, 3441, 3600, 3674–3680, 3786, 3944, 4334, 4840, 4874–4884, 5452 |
| `cardImageContainer` | 22 | 12 | 482, 833, 861–890, 919, 976–1006, 5759–5763, 5843, 6447, 6526–6534, 6574, 6699–6715, 6836 |
| `skinHeader` | 16 | 10 | 284, 4159, 4192–4219, 5642, 6052, 6108–6116, 6142–6167, 6517, 6666, 7284 |
| `nameContainer` | 27 | 9 | 694, 2224–2247, 2288, 2317, 2352–2398, 2435, 2466–2470, 5209–5261, 7175–7213 |
| `js` | 9 | 9 | 331, 1646, 1739, 2288, 2892, 3574, 5452, 6618, 6862 |
| `card-hoverable` | 23 | 8 | 510, 821, 881–969, 5763, 6465, 6574–6609, 6699, 6988 |
| `parentName` | 23 | 8 | 694, 2229–2247, 2288, 2317, 2352–2398, 5215–5261, 5334, 7175–7213 |
| `detailLogo` | 20 | 8 | 694, 2004–2030, 2065–2080, 2107–2116, 2217–2247, 2317, 2352–2398, 2466 |
| `listItem` | 19 | 8 | 302, 637, 2483, 4254–4280, 4311–4343, 4385, 4425, 6965–6982 |
| `detailPageWrapperContainer` | 17 | 8 | 694, 1542–1552, 2030, 2190, 2224–2247, 2317, 2352–2398, 2466 |
| `subtitle` | 16 | 8 | 1994–2004, 2116, 2229, 2288, 2407–2417, 2528, 5269–5302, 7175–7213 |
| `backdropCard` | 12 | 8 | 963–969, 1084, 1994–2004, 2133, 2217, 2470–2479, 2506, 2815 |
| `cardBox` | 12 | 8 | 428–476, 502, 748, 903, 1010, 6441, 6699, 6988 |
| `emby-button` | 11 | 8 | 620–637, 664–682, 3154, 3215–3222, 3620, 3655, 3808, 4352 |
| `nowPlayingBar` | 8 | 8 | 318, 3078, 5895, 6480, 6568, 6652, 6678, 6947 |
| `loginPage` | 16 | 7 | 3753, 5646–5677, 5716, 5744–5763, 6470, 6513, 6825–6852 |
| `navMenuOption` | 12 | 6 | 637, 733–743, 3994, 4321–4343, 4431–4436, 6738–6749 |
| `paper-icon-button-light` | 11 | 6 | 582–637, 1660, 1730, 1828, 3381–3401, 5128 |
| `verticalSection` | 11 | 6 | 1734, 2717–2722, 4737, 6526, 6618, 6862 |
| `button-link` | 10 | 6 | 637, 664–682, 3028–3037, 3098–3108, 3154, 7138 |
| `person` | 8 | 6 | 1994–2015, 2217, 2470, 2515–2524, 3881, 7170 |
| `mainDrawer` | 7 | 6 | 3042, 3958, 4192, 6470–6480, 6725, 6764 |
| `detailImageContainer` | 20 | 5 | 1994–2015, 2121–2185, 2217, 2457–2479, 2506–2524 |
| `osdHeader` | 15 | 5 | 1703–1721, 6047–6116, 6142–6167, 6517, 6947 |
| `actionSheetMenuItem` | 10 | 5 | 637, 4254–4265, 4311, 4385–4425, 6498 |
| `sectionTabs` | 10 | 5 | 1797, 3732, 4219, 6088–6093, 6233–6259 |
| `cardImageIcon` | 8 | 5 | 420–424, 2470–2479, 2542, 3468, 5843 |
| `headerTop` | 8 | 5 | 4159, 4192, 6058–6083, 6134–6151, 6178–6182 |
| `sectionTitle` | 7 | 5 | 1734, 1807–1814, 4060, 4810–4818, 5711 |
| `emby-scroller-container` | 6 | 5 | 1734–1739, 1777, 2707, 6526, 6618 |
| `portraitCard` | 6 | 5 | 1084, 1162, 1918–1923, 2181, 2815 |
| `scss` | 5 | 5 | 284, 776, 1036, 3490, 6618 |
| `skinHeader-withBackground` | 5 | 5 | 1642, 3929, 5642, 6047, 6097 |
| `btnPlay` | 16 | 4 | 519–543, 582–637, 3684–3726, 3759–3786 |
| `cardOverlayContainer` | 12 | 4 | 937–969, 1014–1036, 1096, 6947–6965 |
| `itemName` | 11 | 4 | 694, 2288, 5215–5261, 5352–5369 |
| `backdropImage` | 10 | 4 | 2607–2634, 2661–2665, 6434, 6534–6542 |
| `emby-tab-button` | 10 | 4 | 637, 704–713, 3732, 6218–6254 |
| `upNextContainer` | 10 | 4 | 4902–4921, 4947–4973, 6470–6480, 6506 |
| `emby-scroller` | 9 | 4 | 1739, 1777–1783, 6768–6815, 6926–6942 |
| `backgroundContainer` | 8 | 4 | 2084, 2598, 2639–2657, 2689 |
| `detailRibbon` | 8 | 4 | 1599–1627, 1833, 1918–1930, 7170 |
| `listItemBodyText` | 7 | 4 | 4275–4294, 4334, 4405, 6982 |
| `visualCardBox` | 7 | 4 | 428, 842–855, 881–886, 1010 |
| `button-submit` | 6 | 4 | 3753, 3840, 5744–5752, 7050–7064 |
| `cardText-secondary` | 6 | 4 | 302, 924, 3473–3477, 6596–6604 |
| `detailPagePrimaryContent` | 6 | 4 | 1614–1632, 2422, 4731, 6682 |
| `skip-button` | 6 | 4 | 637, 3737, 4996–5013, 5040–5046 |
| `squareCard` | 6 | 4 | 865, 2470, 2506–2524, 5720–5724 |
| `skinHeader-blurred` | 5 | 4 | 5642, 6076–6083, 6666, 6947 |
| `appfooter` | 4 | 4 | 2758, 6192, 6557, 6947 |
| `itemsContainer` | 4 | 4 | 748, 1766, 1801, 4737 |
| `raised` | 4 | 4 | 637, 723, 3620, 3655 |
| `detailButton` | 13 | 3 | 582–637, 3665–3726, 3782–3786 |
| `itemSelectionPanel` | 9 | 3 | 894–898, 3413, 3441–3484 |
| `pageTitle` | 8 | 3 | 1678–1721, 6108, 6167 |
| `sectionTitleTextButton` | 8 | 3 | 4793–4801, 4828–4840, 4874–4884 |
| `homePage` | 7 | 3 | 4159, 4192–4219, 6276 |
| `playedIndicator` | 7 | 3 | 776–790, 3557, 6699–6720 |
| `check` | 6 | 3 | 3441, 3674, 4385–4425 |
| `detailSectionContent` | 6 | 3 | 3247, 4532–4542, 4622–4632 |
| `emby-checkbox` | 6 | 3 | 3418, 3455–3459, 3508–3520 |
| `actionSheetContent` | 5 | 3 | 4377–4381, 6470–6480, 6506 |
| `cardText-first` | 5 | 3 | 924, 3447–3473, 5824 |
| `dialog` | 5 | 3 | 3297–3307, 6470–6480, 6506 |
| `guideProgramName` | 5 | 3 | 637, 5393–5404, 5447–5452 |
| `noHomeButtonHeader` | 5 | 3 | 1660, 6108, 6218–6226 |
| `overflowBackdropCard` | 5 | 3 | 963–969, 3451, 5819–5824 |
| `secondary` | 5 | 3 | 302, 4284–4294, 4334 |
| `album` | 4 | 3 | 2217, 2475–2479, 2515 |
| `cardPadder` | 4 | 3 | 424, 1010, 3464–3468 |
| `cardText` | 4 | 3 | 924–934, 3473, 6841 |
| `detailPageContent` | 4 | 3 | 1756, 4463, 4724–4731 |
| `dialog-fullscreen` | 4 | 3 | 3307, 6470–6480, 6506 |
| `emby-scrollbuttons` | 4 | 3 | 1819–1824, 6862, 7322 |
| `folder` | 4 | 3 | 1918–1923, 3574, 3638 |
| `formDialogFooter` | 4 | 3 | 3365, 3847, 6999–7023 |
| `infoWrapper` | 4 | 3 | 2160–2165, 2422, 2450 |
| `listItemImage` | 4 | 3 | 2792–2797, 4248, 6982 |
| `musicParentName` | 4 | 3 | 1994, 2528, 5334–5343 |
| `semiTransparent` | 4 | 3 | 1642, 5642, 6076–6097 |
| `toast` | 4 | 3 | 4894, 6470–6480, 6506 |
| `cardFooter` | 3 | 3 | 3484, 6574, 6609 |
| `defaultCardBackground` | 3 | 3 | 3595, 5839, 5938 |
| `detailPageSecondaryContainer` | 3 | 3 | 1609, 1636, 1756 |
| `formDialogFooterItem` | 3 | 3 | 3365, 3633, 3759 |
| `formDialogHeader` | 3 | 3 | 3847, 6947, 6999 |
| `iconOsd` | 3 | 3 | 5620, 6947, 6999 |
| `live_tv` | 3 | 3 | 1994, 2515, 3881 |
| `myPreferencesMenuPage` | 3 | 3 | 397, 4441, 4745 |
| `page` | 3 | 3 | 1006, 2689, 6526 |
| `playerStats` | 3 | 3 | 5620, 6999, 7035 |
| `sectionTitle-cards` | 3 | 3 | 1734, 4810, 4870 |
| `sectionTitleContainer` | 3 | 3 | 1766, 1824, 4656 |
| `x` | 3 | 3 | 2288, 5317, 6618 |
| `itemExternalLinks` | 13 | 2 | 3091–3169, 3247 |
| `checkboxOutline` | 10 | 2 | 3418–3459, 3490–3520 |
| `itemBackdrop` | 9 | 2 | 1960–2015, 2190 |
| `mdl-slider` | 9 | 2 | 2888, 2943–3001 |
| `listItemIcon` | 8 | 2 | 3877–3881, 4385–4441 |
| `sliderContainer` | 8 | 2 | 2892, 2920–2985 |
| `cardOverlayButton-br` | 7 | 2 | 1022, 1051–1089 |
| `detail-clamp-text` | 7 | 2 | 3183–3209, 3235–3239 |
| `divUsers` | 7 | 2 | 5720–5724, 6825–6852 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3455–3459, 3489–3508 |
| `countIndicator` | 6 | 2 | 767–797, 6999–7023 |
| `detailPagePrimaryContainer` | 6 | 2 | 1586–1632, 2422 |
| `detailsGroupItem` | 6 | 2 | 4494, 4562–4599 |
| `headerButton` | 6 | 2 | 557–637, 6160 |
| `headerLeft` | 6 | 2 | 1684–1721, 6363 |
| `selectionCommandsPanel` | 6 | 2 | 3375–3409, 6947 |
| `trackSelections` | 6 | 2 | 4467–4494, 4627–4632 |
| `withBackdrop` | 6 | 2 | 2598, 2639–2657 |
| `detailSection` | 5 | 2 | 4450–4459, 4612–4632 |
| `fullSyncIndicator` | 5 | 2 | 767–790, 6999–7023 |
| `mainDrawer-scrollContainer` | 5 | 2 | 3051, 6738–6755 |
| `mediaInfoItem` | 5 | 2 | 1837–1880, 6618 |
| `overview-expand` | 5 | 2 | 3215–3239, 4532 |
| `scrollX` | 5 | 2 | 1739, 1777–1797 |
| `videoIndicator` | 5 | 2 | 3563–3591, 6999 |
| `withSectionTabs` | 5 | 2 | 2648–2665, 6083 |
| `alphaPickerButton` | 4 | 2 | 637, 4671–4683 |
| `backgroundProgress` | 4 | 2 | 2803–2815, 2845 |
| `emby-tab-button-active` | 4 | 2 | 3819, 6245–6259 |
| `mediaSourceIndicator` | 4 | 2 | 767–790, 6999 |
| `play_arrow` | 4 | 2 | 3600–3616, 3786 |
| `playbackProgress` | 4 | 2 | 2803–2815, 2850 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4275–4280, 5932–5938 |
| `programCell` | 4 | 2 | 5384, 5443–5452 |
| `programGuideSection` | 4 | 2 | 2483–2498, 4632–4647 |
| `section0` | 4 | 2 | 976–1006, 6526 |
| `visualLoginForm` | 4 | 2 | 5711–5728, 5769 |
| `cardOverlayButtonIcon` | 3 | 2 | 1022–1034, 1089 |
| `castCollapsible` | 3 | 2 | 833, 3459–3468 |
| `collectionItems` | 3 | 2 | 1766, 4632–4656 |
| `emby-input` | 3 | 2 | 5142–5158, 7064 |
| `emby-scrollbuttons-button` | 3 | 2 | 1828, 7329–7336 |
| `guestCastContent` | 3 | 2 | 833, 3459–3468 |
| `guide-channelHeaderCell` | 3 | 2 | 637, 5418–5434 |
| `guide-date-tab-button` | 3 | 2 | 637, 3819–3827 |
| `headerUserButton` | 3 | 2 | 557–570, 4749 |
| `manualLoginForm` | 3 | 2 | 5711–5728, 5769 |
| `overview` | 3 | 2 | 3235–3239, 4542 |
| `add` | 2 | 2 | 1739, 6618 |
| `alphaPicker-fixed-right` | 2 | 2 | 2689, 4683 |
| `backdropImageFadeIn` | 2 | 2 | 2742, 7039 |
| `book` | 2 | 2 | 1994, 2515 |
| `btnDeleteImage` | 2 | 2 | 3620, 3833 |
| `cardContent` | 2 | 2 | 833, 865 |
| `cardOverlayButton` | 2 | 2 | 1036, 1072 |
| `cardOverlayButton-hover` | 2 | 2 | 919, 1051 |
| `chevron_right` | 2 | 2 | 4840, 4884 |
| `classList` | 2 | 2 | 1739, 6618 |
| `collapseContent` | 2 | 2 | 3370, 3845 |
| `collectionItemsContainer` | 2 | 2 | 1766, 4660 |
| `content-primary` | 2 | 2 | 4724, 4776 |
| `editorsChoiceItemOverview` | 2 | 2 | 7259, 7340 |
| `emby-select` | 2 | 2 | 5142, 7064 |
| `endsAt` | 2 | 2 | 1858, 6618 |
| `fieldDescription` | 2 | 2 | 302, 7064 |
| `formDialogFooter-clear` | 2 | 2 | 3365, 3847 |
| `guide-programNameCaret` | 2 | 2 | 302, 5400 |
| `headroom` | 2 | 2 | 6071, 6108 |
| `indicator` | 2 | 2 | 797, 3552 |
| `mediaInfoOfficialRating` | 2 | 2 | 1858, 6618 |
| `navMenuOption-selected` | 2 | 2 | 4446, 6749 |
| `nowPlayingInfoContainer` | 2 | 2 | 3082, 5869 |
| `org` | 2 | 2 | 3118, 3148 |
| `paperList` | 2 | 2 | 842, 3858 |
| `playlist` | 2 | 2 | 4270, 5847 |
| `programSecondaryTitle` | 2 | 2 | 302, 5452 |
| `queue` | 2 | 2 | 1994, 2515 |
| `readOnlyContent` | 2 | 2 | 3889, 6292 |
| `recordingFields` | 2 | 2 | 4486, 4627 |
| `runtime` | 2 | 2 | 5781, 5809 |
| `sectionTitleContainer-cards` | 2 | 2 | 4805, 4870 |
| `sidebarHeader` | 2 | 2 | 3981, 6755 |
| `tagline` | 2 | 2 | 2589, 4542 |
| `tsx` | 2 | 2 | 4159, 4223 |
| `upNextDialog-title` | 2 | 2 | 4926, 4960 |
| `vertical-list` | 2 | 2 | 1801, 7165 |
| `vertical-wrap` | 2 | 2 | 763, 1766 |
| `videoOsdBottom` | 2 | 2 | 3074, 6038 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3074, 6038 |
| `userPreferencesPage` | 12 | 1 | 7050–7145 |
| `checkboxContainer` | 7 | 1 | 3447–3484 |
| `itemDetailsGroup` | 7 | 1 | 4546–4632 |
| `itemProgressBar` | 6 | 1 | 2792–2826 |
| `trackSelectionFieldContainer` | 6 | 1 | 4505–4528 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7296–7336 |
| `innerCardFooter` | 5 | 1 | 3260–3289 |
| `chapterCardImageContainer` | 4 | 1 | 3260–3289 |
| `endTimeText` | 4 | 1 | 5781–5809 |
| `mainDetailButtons` | 4 | 1 | 3782–3796 |
| `overview-controls` | 4 | 1 | 3235–3247 |
| `startTimeText` | 4 | 1 | 5781–5803 |
| `button-flat` | 3 | 1 | 3055–3065 |
| `cardIndicators` | 3 | 1 | 3537–3547 |
| `cardOverlayFab-primary` | 3 | 1 | 1014–1036 |
| `com` | 3 | 1 | 3124–3142 |
| `content` | 3 | 1 | 4568–4599 |
| `discover-card` | 3 | 1 | 7347–7370 |
| `emby-select-withcolor` | 3 | 1 | 5142–5176 |
| `emby-textarea` | 3 | 1 | 5133–5158 |
| `fab` | 3 | 1 | 3642–3655 |
| `listChildrenCollapsible` | 3 | 1 | 4617–4632 |
| `mdl-slider-background-flex` | 3 | 1 | 2912–2925 |
| `mediaInfoCriticRating` | 3 | 1 | 1899–1908 |
| `nextUpSection` | 3 | 1 | 4612–4632 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 5833–5843 |
| `serverInfo` | 3 | 1 | 3862–3871 |
| `transcodingProgress` | 3 | 1 | 2803–2815 |
