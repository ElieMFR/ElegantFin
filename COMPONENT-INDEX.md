# Index des composants — ElegantFin Cinema Edition v1.3.14

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.14.css` — 7451 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 36 | 14 | 428–510, 748, 865, 1511–1531, 2121–2154, 2181–2185, 2461–2479, 2515, 6423, 6681–6697, 6775–6797, 6827–6834, 6924, 7329 |
| `cardScalable` | 28 | 13 | 428–439, 487–510, 811–855, 881–919, 2479, 3484, 3595, 3674, 5616, 6437–6447, 6516, 6681, 6818–6834 |
| `itemDetailPage` | 21 | 13 | 1574, 1660, 1739, 1766, 1994–2030, 2065–2080, 2116, 2217, 2528, 3929–3940, 4428, 4715, 7157–7195 |
| `material-icons` | 17 | 13 | 364–383, 1730, 1828, 1880, 3441, 3600, 3674–3680, 3786, 3944, 4334, 4818, 4852–4862, 5434 |
| `cardImageContainer` | 22 | 12 | 482, 833, 861–890, 919, 976–1006, 5741–5745, 5825, 6429, 6508–6516, 6556, 6681–6697, 6818 |
| `skinHeader` | 16 | 10 | 284, 4159, 4192–4219, 5624, 6034, 6090–6098, 6124–6149, 6499, 6648, 7266 |
| `nameContainer` | 27 | 9 | 694, 2224–2247, 2288, 2317, 2352–2398, 2435, 2466–2470, 5191–5243, 7157–7195 |
| `js` | 9 | 9 | 331, 1646, 1739, 2288, 2892, 3574, 5434, 6600, 6844 |
| `card-hoverable` | 23 | 8 | 510, 821, 881–969, 5745, 6447, 6556–6591, 6681, 6970 |
| `parentName` | 23 | 8 | 694, 2229–2247, 2288, 2317, 2352–2398, 5197–5243, 5316, 7157–7195 |
| `detailLogo` | 20 | 8 | 694, 2004–2030, 2065–2080, 2107–2116, 2217–2247, 2317, 2352–2398, 2466 |
| `detailPageWrapperContainer` | 17 | 8 | 694, 1542–1552, 2030, 2190, 2224–2247, 2317, 2352–2398, 2466 |
| `subtitle` | 16 | 8 | 1994–2004, 2116, 2229, 2288, 2407–2417, 2528, 5251–5284, 7157–7195 |
| `backdropCard` | 12 | 8 | 963–969, 1084, 1994–2004, 2133, 2217, 2470–2479, 2506, 2815 |
| `cardBox` | 12 | 8 | 428–476, 502, 748, 903, 1010, 6423, 6681, 6970 |
| `emby-button` | 11 | 8 | 620–637, 664–682, 3154, 3215–3222, 3620, 3655, 3808, 4352 |
| `nowPlayingBar` | 8 | 8 | 318, 3078, 5877, 6462, 6550, 6634, 6660, 6929 |
| `loginPage` | 16 | 7 | 3753, 5628–5659, 5698, 5726–5745, 6452, 6495, 6807–6834 |
| `listItem` | 17 | 6 | 302, 637, 2483, 4254–4280, 4311–4343, 6947–6964 |
| `navMenuOption` | 12 | 6 | 637, 733–743, 3994, 4321–4343, 4409–4414, 6720–6731 |
| `paper-icon-button-light` | 11 | 6 | 582–637, 1660, 1730, 1828, 3381–3401, 5110 |
| `verticalSection` | 11 | 6 | 1734, 2717–2722, 4715, 6508, 6600, 6844 |
| `button-link` | 10 | 6 | 637, 664–682, 3028–3037, 3098–3108, 3154, 7120 |
| `person` | 8 | 6 | 1994–2015, 2217, 2470, 2515–2524, 3881, 7152 |
| `mainDrawer` | 7 | 6 | 3042, 3958, 4192, 6452–6462, 6707, 6746 |
| `detailImageContainer` | 20 | 5 | 1994–2015, 2121–2185, 2217, 2457–2479, 2506–2524 |
| `osdHeader` | 15 | 5 | 1703–1721, 6029–6098, 6124–6149, 6499, 6929 |
| `actionSheetMenuItem` | 11 | 5 | 637, 4254–4265, 4311, 4389–4405, 6480 |
| `sectionTabs` | 10 | 5 | 1797, 3732, 4219, 6070–6075, 6215–6241 |
| `cardImageIcon` | 8 | 5 | 420–424, 2470–2479, 2542, 3468, 5825 |
| `headerTop` | 8 | 5 | 4159, 4192, 6040–6065, 6116–6133, 6160–6164 |
| `sectionTitle` | 7 | 5 | 1734, 1807–1814, 4060, 4788–4796, 5693 |
| `emby-scroller-container` | 6 | 5 | 1734–1739, 1777, 2707, 6508, 6600 |
| `portraitCard` | 6 | 5 | 1084, 1162, 1918–1923, 2181, 2815 |
| `scss` | 5 | 5 | 284, 776, 1036, 3490, 6600 |
| `skinHeader-withBackground` | 5 | 5 | 1642, 3929, 5624, 6029, 6079 |
| `btnPlay` | 16 | 4 | 519–543, 582–637, 3684–3726, 3759–3786 |
| `cardOverlayContainer` | 12 | 4 | 937–969, 1014–1036, 1096, 6929–6947 |
| `itemName` | 11 | 4 | 694, 2288, 5197–5243, 5334–5351 |
| `backdropImage` | 10 | 4 | 2607–2634, 2661–2665, 6416, 6516–6524 |
| `emby-tab-button` | 10 | 4 | 637, 704–713, 3732, 6200–6236 |
| `upNextContainer` | 10 | 4 | 4880–4899, 4925–4951, 6452–6462, 6488 |
| `emby-scroller` | 9 | 4 | 1739, 1777–1783, 6750–6797, 6908–6924 |
| `backgroundContainer` | 8 | 4 | 2084, 2598, 2639–2657, 2689 |
| `detailRibbon` | 8 | 4 | 1599–1627, 1833, 1918–1930, 7152 |
| `listItemBodyText` | 7 | 4 | 4275–4294, 4334, 4393, 6964 |
| `visualCardBox` | 7 | 4 | 428, 842–855, 881–886, 1010 |
| `button-submit` | 6 | 4 | 3753, 3840, 5726–5734, 7032–7046 |
| `cardText-secondary` | 6 | 4 | 302, 924, 3473–3477, 6578–6586 |
| `detailPagePrimaryContent` | 6 | 4 | 1614–1632, 2422, 4709, 6664 |
| `skip-button` | 6 | 4 | 637, 3737, 4974–4991, 5018–5024 |
| `squareCard` | 6 | 4 | 865, 2470, 2506–2524, 5702–5706 |
| `skinHeader-blurred` | 5 | 4 | 5624, 6058–6065, 6648, 6929 |
| `appfooter` | 4 | 4 | 2758, 6174, 6539, 6929 |
| `itemsContainer` | 4 | 4 | 748, 1766, 1801, 4715 |
| `raised` | 4 | 4 | 637, 723, 3620, 3655 |
| `detailButton` | 13 | 3 | 582–637, 3665–3726, 3782–3786 |
| `itemSelectionPanel` | 9 | 3 | 894–898, 3413, 3441–3484 |
| `check` | 8 | 3 | 3441, 3674, 4385–4405 |
| `pageTitle` | 8 | 3 | 1678–1721, 6090, 6149 |
| `sectionTitleTextButton` | 8 | 3 | 4771–4779, 4806–4818, 4852–4862 |
| `homePage` | 7 | 3 | 4159, 4192–4219, 6258 |
| `playedIndicator` | 7 | 3 | 776–790, 3557, 6681–6702 |
| `detailSectionContent` | 6 | 3 | 3247, 4510–4520, 4600–4610 |
| `emby-checkbox` | 6 | 3 | 3418, 3455–3459, 3508–3520 |
| `actionSheetContent` | 5 | 3 | 4377–4381, 6452–6462, 6488 |
| `cardText-first` | 5 | 3 | 924, 3447–3473, 5806 |
| `dialog` | 5 | 3 | 3297–3307, 6452–6462, 6488 |
| `guideProgramName` | 5 | 3 | 637, 5375–5386, 5429–5434 |
| `noHomeButtonHeader` | 5 | 3 | 1660, 6090, 6200–6208 |
| `overflowBackdropCard` | 5 | 3 | 963–969, 3451, 5801–5806 |
| `secondary` | 5 | 3 | 302, 4284–4294, 4334 |
| `album` | 4 | 3 | 2217, 2475–2479, 2515 |
| `cardPadder` | 4 | 3 | 424, 1010, 3464–3468 |
| `cardText` | 4 | 3 | 924–934, 3473, 6823 |
| `detailPageContent` | 4 | 3 | 1756, 4441, 4702–4709 |
| `dialog-fullscreen` | 4 | 3 | 3307, 6452–6462, 6488 |
| `emby-scrollbuttons` | 4 | 3 | 1819–1824, 6844, 7304 |
| `folder` | 4 | 3 | 1918–1923, 3574, 3638 |
| `formDialogFooter` | 4 | 3 | 3365, 3847, 6981–7005 |
| `infoWrapper` | 4 | 3 | 2160–2165, 2422, 2450 |
| `listItemImage` | 4 | 3 | 2792–2797, 4248, 6964 |
| `musicParentName` | 4 | 3 | 1994, 2528, 5316–5325 |
| `semiTransparent` | 4 | 3 | 1642, 5624, 6058–6079 |
| `toast` | 4 | 3 | 4872, 6452–6462, 6488 |
| `cardFooter` | 3 | 3 | 3484, 6556, 6591 |
| `defaultCardBackground` | 3 | 3 | 3595, 5821, 5920 |
| `detailPageSecondaryContainer` | 3 | 3 | 1609, 1636, 1756 |
| `formDialogFooterItem` | 3 | 3 | 3365, 3633, 3759 |
| `formDialogHeader` | 3 | 3 | 3847, 6929, 6981 |
| `iconOsd` | 3 | 3 | 5602, 6929, 6981 |
| `live_tv` | 3 | 3 | 1994, 2515, 3881 |
| `myPreferencesMenuPage` | 3 | 3 | 397, 4419, 4723 |
| `page` | 3 | 3 | 1006, 2689, 6508 |
| `playerStats` | 3 | 3 | 5602, 6981, 7017 |
| `sectionTitle-cards` | 3 | 3 | 1734, 4788, 4848 |
| `sectionTitleContainer` | 3 | 3 | 1766, 1824, 4634 |
| `x` | 3 | 3 | 2288, 5299, 6600 |
| `itemExternalLinks` | 13 | 2 | 3091–3169, 3247 |
| `checkboxOutline` | 10 | 2 | 3418–3459, 3490–3520 |
| `itemBackdrop` | 9 | 2 | 1960–2015, 2190 |
| `mdl-slider` | 9 | 2 | 2888, 2943–3001 |
| `listItemIcon` | 8 | 2 | 3877–3881, 4389–4419 |
| `sliderContainer` | 8 | 2 | 2892, 2920–2985 |
| `cardOverlayButton-br` | 7 | 2 | 1022, 1051–1089 |
| `detail-clamp-text` | 7 | 2 | 3183–3209, 3235–3239 |
| `divUsers` | 7 | 2 | 5702–5706, 6807–6834 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3455–3459, 3489–3508 |
| `countIndicator` | 6 | 2 | 767–797, 6981–7005 |
| `detailPagePrimaryContainer` | 6 | 2 | 1586–1632, 2422 |
| `detailsGroupItem` | 6 | 2 | 4472, 4540–4577 |
| `headerButton` | 6 | 2 | 557–637, 6142 |
| `headerLeft` | 6 | 2 | 1684–1721, 6345 |
| `selectionCommandsPanel` | 6 | 2 | 3375–3409, 6929 |
| `trackSelections` | 6 | 2 | 4445–4472, 4605–4610 |
| `withBackdrop` | 6 | 2 | 2598, 2639–2657 |
| `detailSection` | 5 | 2 | 4428–4437, 4590–4610 |
| `fullSyncIndicator` | 5 | 2 | 767–790, 6981–7005 |
| `mainDrawer-scrollContainer` | 5 | 2 | 3051, 6720–6737 |
| `mediaInfoItem` | 5 | 2 | 1837–1880, 6600 |
| `overview-expand` | 5 | 2 | 3215–3239, 4510 |
| `scrollX` | 5 | 2 | 1739, 1777–1797 |
| `videoIndicator` | 5 | 2 | 3563–3591, 6981 |
| `withSectionTabs` | 5 | 2 | 2648–2665, 6065 |
| `alphaPickerButton` | 4 | 2 | 637, 4649–4661 |
| `backgroundProgress` | 4 | 2 | 2803–2815, 2845 |
| `emby-tab-button-active` | 4 | 2 | 3819, 6227–6241 |
| `mediaSourceIndicator` | 4 | 2 | 767–790, 6981 |
| `play_arrow` | 4 | 2 | 3600–3616, 3786 |
| `playbackProgress` | 4 | 2 | 2803–2815, 2850 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4275–4280, 5914–5920 |
| `programCell` | 4 | 2 | 5366, 5425–5434 |
| `programGuideSection` | 4 | 2 | 2483–2498, 4610–4625 |
| `section0` | 4 | 2 | 976–1006, 6508 |
| `visualLoginForm` | 4 | 2 | 5693–5710, 5751 |
| `cardOverlayButtonIcon` | 3 | 2 | 1022–1034, 1089 |
| `castCollapsible` | 3 | 2 | 833, 3459–3468 |
| `collectionItems` | 3 | 2 | 1766, 4610–4634 |
| `emby-input` | 3 | 2 | 5124–5140, 7046 |
| `emby-scrollbuttons-button` | 3 | 2 | 1828, 7311–7318 |
| `guestCastContent` | 3 | 2 | 833, 3459–3468 |
| `guide-channelHeaderCell` | 3 | 2 | 637, 5400–5416 |
| `guide-date-tab-button` | 3 | 2 | 637, 3819–3827 |
| `headerUserButton` | 3 | 2 | 557–570, 4727 |
| `manualLoginForm` | 3 | 2 | 5693–5710, 5751 |
| `overview` | 3 | 2 | 3235–3239, 4520 |
| `add` | 2 | 2 | 1739, 6600 |
| `alphaPicker-fixed-right` | 2 | 2 | 2689, 4661 |
| `backdropImageFadeIn` | 2 | 2 | 2742, 7021 |
| `book` | 2 | 2 | 1994, 2515 |
| `btnDeleteImage` | 2 | 2 | 3620, 3833 |
| `cardContent` | 2 | 2 | 833, 865 |
| `cardOverlayButton` | 2 | 2 | 1036, 1072 |
| `cardOverlayButton-hover` | 2 | 2 | 919, 1051 |
| `chevron_right` | 2 | 2 | 4818, 4862 |
| `classList` | 2 | 2 | 1739, 6600 |
| `collapseContent` | 2 | 2 | 3370, 3845 |
| `collectionItemsContainer` | 2 | 2 | 1766, 4638 |
| `content-primary` | 2 | 2 | 4702, 4754 |
| `editorsChoiceItemOverview` | 2 | 2 | 7241, 7322 |
| `emby-select` | 2 | 2 | 5124, 7046 |
| `endsAt` | 2 | 2 | 1858, 6600 |
| `fieldDescription` | 2 | 2 | 302, 7046 |
| `formDialogFooter-clear` | 2 | 2 | 3365, 3847 |
| `guide-programNameCaret` | 2 | 2 | 302, 5382 |
| `headroom` | 2 | 2 | 6053, 6090 |
| `indicator` | 2 | 2 | 797, 3552 |
| `mediaInfoOfficialRating` | 2 | 2 | 1858, 6600 |
| `navMenuOption-selected` | 2 | 2 | 4424, 6731 |
| `nowPlayingInfoContainer` | 2 | 2 | 3082, 5851 |
| `org` | 2 | 2 | 3118, 3148 |
| `paperList` | 2 | 2 | 842, 3858 |
| `playlist` | 2 | 2 | 4270, 5829 |
| `programSecondaryTitle` | 2 | 2 | 302, 5434 |
| `queue` | 2 | 2 | 1994, 2515 |
| `readOnlyContent` | 2 | 2 | 3889, 6274 |
| `recordingFields` | 2 | 2 | 4464, 4605 |
| `runtime` | 2 | 2 | 5763, 5791 |
| `sectionTitleContainer-cards` | 2 | 2 | 4783, 4848 |
| `sidebarHeader` | 2 | 2 | 3981, 6737 |
| `tagline` | 2 | 2 | 2589, 4520 |
| `tsx` | 2 | 2 | 4159, 4223 |
| `upNextDialog-title` | 2 | 2 | 4904, 4938 |
| `vertical-list` | 2 | 2 | 1801, 7147 |
| `vertical-wrap` | 2 | 2 | 763, 1766 |
| `videoOsdBottom` | 2 | 2 | 3074, 6020 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3074, 6020 |
| `userPreferencesPage` | 12 | 1 | 7032–7127 |
| `checkboxContainer` | 7 | 1 | 3447–3484 |
| `itemDetailsGroup` | 7 | 1 | 4524–4610 |
| `itemProgressBar` | 6 | 1 | 2792–2826 |
| `trackSelectionFieldContainer` | 6 | 1 | 4483–4506 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7278–7318 |
| `innerCardFooter` | 5 | 1 | 3260–3289 |
| `chapterCardImageContainer` | 4 | 1 | 3260–3289 |
| `endTimeText` | 4 | 1 | 5763–5791 |
| `mainDetailButtons` | 4 | 1 | 3782–3796 |
| `overview-controls` | 4 | 1 | 3235–3247 |
| `startTimeText` | 4 | 1 | 5763–5785 |
| `button-flat` | 3 | 1 | 3055–3065 |
| `cardIndicators` | 3 | 1 | 3537–3547 |
| `cardOverlayFab-primary` | 3 | 1 | 1014–1036 |
| `com` | 3 | 1 | 3124–3142 |
| `content` | 3 | 1 | 4546–4577 |
| `discover-card` | 3 | 1 | 7329–7352 |
| `emby-select-withcolor` | 3 | 1 | 5124–5158 |
| `emby-textarea` | 3 | 1 | 5115–5140 |
| `fab` | 3 | 1 | 3642–3655 |
| `listChildrenCollapsible` | 3 | 1 | 4595–4610 |
| `mdl-slider-background-flex` | 3 | 1 | 2912–2925 |
| `mediaInfoCriticRating` | 3 | 1 | 1899–1908 |
| `nextUpSection` | 3 | 1 | 4590–4610 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 5815–5825 |
| `serverInfo` | 3 | 1 | 3862–3871 |
| `transcodingProgress` | 3 | 1 | 2803–2815 |
