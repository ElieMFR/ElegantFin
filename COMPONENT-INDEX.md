# Index des composants — ElegantFin Cinema Edition v1.5.7

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.5.7.css` — 8051 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 38 | 16 | 457–487, 518–553, 791, 908, 1569–1589, 2203–2236, 2263–2267, 2544–2562, 2598, 6957, 6993–7003, 7144, 7244–7263, 7341–7363, 7393–7400, 7564 |
| `cardScalable` | 30 | 14 | 457, 487, 541–553, 854–898, 924–968, 2562, 3644, 3755, 3834, 6021, 6971–7003, 7074, 7244, 7384–7400 |
| `cardImageContainer` | 22 | 13 | 468, 536, 876, 904–933, 968, 1026–1050, 6177–6181, 6261, 6963, 7066–7074, 7114, 7244–7263, 7384 |
| `material-icons` | 17 | 13 | 393–412, 1794, 1892, 1945, 3601, 3760, 3834–3840, 3946, 4109, 4664, 5200, 5234–5244, 5838 |
| `itemDetailPage` | 20 | 12 | 1632, 1718, 1803, 1830, 2059–2099, 2134–2149, 2185–2189, 2299, 2611, 4787, 5093, 7818–7856 |
| `skinHeader` | 20 | 12 | 296, 1718, 4089–4105, 4476, 4522–4549, 6029–6033, 6470, 6526–6534, 6604–6629, 7057, 7211, 7889 |
| `js` | 13 | 12 | 330, 360, 1704–1718, 1803, 2370, 2976, 3405, 3734, 5838, 6835, 7163, 7410 |
| `nameContainer` | 27 | 9 | 737, 2306–2329, 2370, 2399, 2434–2481, 2518, 2549–2553, 5594–5647, 7818–7856 |
| `emby-button` | 12 | 9 | 663–680, 707–725, 3238, 3373–3380, 3780, 3815, 3968, 4682, 5416 |
| `card-hoverable` | 23 | 8 | 553, 864, 924–1019, 6181, 6981, 7114–7153, 7244, 7629 |
| `parentName` | 23 | 8 | 737, 2311–2329, 2370, 2399, 2434–2481, 5600–5647, 5720, 7818–7856 |
| `detailLogo` | 20 | 8 | 737, 2088–2099, 2134–2149, 2176–2189, 2299–2329, 2399, 2434–2481, 2549 |
| `listItem` | 19 | 8 | 314, 680, 2566, 4584–4610, 4641–4673, 4718, 4762, 7606–7623 |
| `detailPageWrapperContainer` | 17 | 8 | 737, 1600–1610, 2099, 2272, 2306–2329, 2399, 2434–2481, 2549 |
| `subtitle` | 17 | 8 | 2059–2069, 2185–2189, 2311, 2370, 2490–2500, 2611, 5655–5688, 7818–7856 |
| `cardBox` | 13 | 8 | 457–487, 518–542, 791, 946–950, 1055, 6957, 7244, 7629 |
| `backdropCard` | 12 | 8 | 1013–1019, 1136, 2059–2069, 2215, 2299, 2553–2562, 2589, 2899 |
| `nowPlayingBar` | 8 | 8 | 330, 3162, 6313, 7020, 7108, 7197, 7223, 7569 |
| `loginPage` | 18 | 7 | 3912, 6033–6067, 6107–6126, 6162–6181, 7010, 7053, 7373–7400 |
| `navMenuOption` | 12 | 6 | 680, 776–786, 4159, 4651–4673, 4768–4773, 7286–7297 |
| `emby-tab-button` | 11 | 6 | 680, 747–756, 3887, 6680–6691, 6719–6736, 7901 |
| `paper-icon-button-light` | 11 | 6 | 625–680, 1718, 1794, 1892, 3541–3561, 5500 |
| `verticalSection` | 11 | 6 | 1798, 2801–2806, 5093, 7066, 7163, 7410 |
| `button-link` | 10 | 6 | 680, 707–725, 3112–3121, 3182–3192, 3238, 7780 |
| `headerTop` | 9 | 6 | 2189, 4476, 4522, 6476–6501, 6596–6613, 6640–6644 |
| `person` | 8 | 6 | 2059–2084, 2299, 2553, 2598–2607, 4041, 7813 |
| `mainDrawer` | 7 | 6 | 3126, 4123, 4522, 7010–7020, 7273, 7312 |
| `scss` | 6 | 6 | 296, 819, 1081, 3650, 4165, 7163 |
| `detailImageContainer` | 20 | 5 | 2059–2084, 2203–2267, 2299, 2540–2562, 2589–2607 |
| `osdHeader` | 15 | 5 | 1767–1785, 6465–6534, 6604–6629, 7057, 7569 |
| `cardOverlayContainer` | 12 | 5 | 987–1019, 1059–1081, 1154, 7569, 7606 |
| `sectionTabs` | 11 | 5 | 1861, 3887, 4549, 6506–6511, 6697–6741 |
| `actionSheetMenuItem` | 10 | 5 | 680, 4584–4595, 4641, 4718–4762, 7038 |
| `cardImageIcon` | 8 | 5 | 449–453, 2553–2562, 2625, 3628, 6261 |
| `sectionTitle` | 7 | 5 | 1798, 1871–1878, 4377, 5170–5178, 6102 |
| `semiTransparent` | 7 | 5 | 1700, 4089–4105, 6029, 6494–6515, 6551 |
| `emby-scroller-container` | 6 | 5 | 1798–1803, 1841, 2791, 7066, 7163 |
| `portraitCard` | 6 | 5 | 1136, 1220, 1983–1988, 2263, 2899 |
| `appfooter` | 5 | 5 | 330, 2842, 6654, 7097, 7569 |
| `skinHeader-withBackground` | 5 | 5 | 1700, 4089, 6029, 6465, 6515 |
| `btnPlay` | 16 | 4 | 562–586, 625–680, 3844–3886, 3918–3946 |
| `itemName` | 11 | 4 | 737, 2370, 5600–5647, 5738–5755 |
| `backdropImage` | 10 | 4 | 2690–2718, 2745–2749, 6950, 7074–7082 |
| `upNextContainer` | 10 | 4 | 5262–5281, 5307–5333, 7010–7020, 7046 |
| `emby-scroller` | 9 | 4 | 1803, 1841–1847, 7316–7363, 7548–7564 |
| `sectionTitleTextButton` | 9 | 4 | 479, 5153–5161, 5188–5200, 5234–5244 |
| `backgroundContainer` | 8 | 4 | 2153, 2681, 2723–2741, 2773 |
| `detailRibbon` | 8 | 4 | 1657–1685, 1898, 1983–1995, 7813 |
| `listItemBodyText` | 7 | 4 | 4605–4624, 4664, 4739, 7623 |
| `skip-button` | 7 | 4 | 680, 3896, 5356–5373, 5400–5418 |
| `visualCardBox` | 7 | 4 | 457, 885–898, 924–929, 1055 |
| `button-submit` | 6 | 4 | 3912, 4000, 6162–6170, 7691–7706 |
| `cardText-secondary` | 6 | 4 | 314, 973, 3633–3637, 7136–7144 |
| `detailPagePrimaryContent` | 6 | 4 | 1672–1690, 2505, 5087, 7227 |
| `skinHeader-blurred` | 6 | 4 | 6029, 6494–6501, 7211, 7569–7588 |
| `squareCard` | 6 | 4 | 908, 2553, 2589–2607, 6131–6135 |
| `itemsContainer` | 4 | 4 | 791, 1830, 1865, 5093 |
| `raised` | 4 | 4 | 680, 766, 3780, 3815 |
| `tsx` | 4 | 4 | 1136, 1718, 4476, 4553 |
| `x` | 4 | 4 | 2370, 4165, 5703, 7163 |
| `detailButton` | 13 | 3 | 625–680, 3825–3886, 3942–3946 |
| `itemSelectionPanel` | 9 | 3 | 937–941, 3573, 3601–3644 |
| `pageTitle` | 8 | 3 | 1742–1785, 6526, 6629 |
| `homePage` | 7 | 3 | 4476, 4522–4549, 6758 |
| `playedIndicator` | 7 | 3 | 819–833, 3717, 7244–7268 |
| `check` | 6 | 3 | 3601, 3834, 4718–4762 |
| `detailSectionContent` | 6 | 3 | 3405, 4873–4883, 4966–4976 |
| `emby-checkbox` | 6 | 3 | 3578, 3615–3619, 3668–3680 |
| `actionSheetContent` | 5 | 3 | 4710–4714, 7010–7020, 7046 |
| `cardText-first` | 5 | 3 | 973, 3607–3633, 6242 |
| `dialog` | 5 | 3 | 3457–3467, 7010–7020, 7046 |
| `guideProgramName` | 5 | 3 | 680, 5779–5790, 5833–5838 |
| `noHomeButtonHeader` | 5 | 3 | 1718, 6526, 6680–6691 |
| `overflowBackdropCard` | 5 | 3 | 1013–1019, 3611, 6237–6242 |
| `secondary` | 5 | 3 | 314, 4614–4624, 4664 |
| `album` | 4 | 3 | 2299, 2558–2562, 2598 |
| `cardPadder` | 4 | 3 | 453, 1055, 3624–3628 |
| `cardText` | 4 | 3 | 973–983, 3633, 7389 |
| `detailPageContent` | 4 | 3 | 1820, 4800, 5080–5087 |
| `dialog-fullscreen` | 4 | 3 | 3467, 7010–7020, 7046 |
| `emby-scrollbuttons` | 4 | 3 | 1883–1888, 7410, 7935 |
| `folder` | 4 | 3 | 1983–1988, 3734, 3798 |
| `formDialogFooter` | 4 | 3 | 3525, 4007, 7640–7664 |
| `infoWrapper` | 4 | 3 | 2242–2247, 2505, 2533 |
| `listItemImage` | 4 | 3 | 2876–2881, 4578, 7623 |
| `musicParentName` | 4 | 3 | 2059, 2611, 5720–5729 |
| `programGuideSection` | 4 | 3 | 2566–2581, 4976, 5003 |
| `toast` | 4 | 3 | 5254, 7010–7020, 7046 |
| `cardFooter` | 3 | 3 | 3644, 7114, 7153 |
| `collectionItems` | 3 | 3 | 1830, 4976, 5012 |
| `defaultCardBackground` | 3 | 3 | 3755, 6257, 6356 |
| `detailPageSecondaryContainer` | 3 | 3 | 1667, 1694, 1820 |
| `emby-input` | 3 | 3 | 5514, 5543, 7706 |
| `formDialogFooterItem` | 3 | 3 | 3525, 3793, 3918 |
| `formDialogHeader` | 3 | 3 | 4007, 7569, 7640 |
| `iconOsd` | 3 | 3 | 6007, 7569, 7640 |
| `live_tv` | 3 | 3 | 2059, 2598, 4041 |
| `myPreferencesMenuPage` | 3 | 3 | 426, 4778, 5101 |
| `playerStats` | 3 | 3 | 6007, 7640, 7676 |
| `readOnlyContent` | 3 | 3 | 4049, 6120, 6774 |
| `sectionTitle-cards` | 3 | 3 | 1798, 5170, 5230 |
| `sectionTitleContainer` | 3 | 3 | 1830, 1888, 5012 |
| `itemExternalLinks` | 13 | 2 | 3175–3253, 3405 |
| `checkboxOutline` | 10 | 2 | 3578–3619, 3650–3680 |
| `itemBackdrop` | 9 | 2 | 2025–2084, 2272 |
| `mdl-slider` | 9 | 2 | 2972, 3027–3085 |
| `cardOverlayButton-br` | 8 | 2 | 1067, 1096–1147 |
| `listItemIcon` | 8 | 2 | 4037–4041, 4718–4778 |
| `sliderContainer` | 8 | 2 | 2976, 3004–3069 |
| `detail-clamp-text` | 7 | 2 | 3341–3367, 3393–3397 |
| `divUsers` | 7 | 2 | 6131–6135, 7373–7400 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3615–3619, 3649–3668 |
| `countIndicator` | 6 | 2 | 810–840, 7640–7664 |
| `detailPagePrimaryContainer` | 6 | 2 | 1644–1690, 2505 |
| `detailsGroupItem` | 6 | 2 | 4835, 4906–4943 |
| `headerButton` | 6 | 2 | 600–680, 6622 |
| `headerLeft` | 6 | 2 | 1748–1785, 6879 |
| `selectionCommandsPanel` | 6 | 2 | 3535–3569, 7569 |
| `trackSelections` | 6 | 2 | 4804–4835, 4971–4976 |
| `withBackdrop` | 6 | 2 | 2681, 2723–2741 |
| `detailSection` | 5 | 2 | 4787–4796, 4956–4976 |
| `fullSyncIndicator` | 5 | 2 | 810–833, 7640–7664 |
| `mainDrawer-scrollContainer` | 5 | 2 | 3135, 7286–7303 |
| `manualLoginForm` | 5 | 2 | 6102–6146, 6187 |
| `mediaInfoItem` | 5 | 2 | 1902–1945, 7163 |
| `overview-expand` | 5 | 2 | 3373–3397, 4873 |
| `scrollX` | 5 | 2 | 1803, 1841–1861 |
| `videoIndicator` | 5 | 2 | 3723–3751, 7640 |
| `visualLoginForm` | 5 | 2 | 6102–6146, 6187 |
| `withSectionTabs` | 5 | 2 | 2732–2749, 6501 |
| `alphaPickerButton` | 4 | 2 | 680, 5027–5039 |
| `backgroundProgress` | 4 | 2 | 2887–2899, 2929 |
| `emby-select` | 4 | 2 | 5514–5526, 7706 |
| `emby-tab-button-active` | 4 | 2 | 3979, 6727–6741 |
| `mediaSourceIndicator` | 4 | 2 | 810–833, 7640 |
| `play_arrow` | 4 | 2 | 3760–3776, 3946 |
| `playbackProgress` | 4 | 2 | 2887–2899, 2934 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4605–4610, 6350–6356 |
| `programCell` | 4 | 2 | 5770, 5829–5838 |
| `cardOverlayButtonIcon` | 3 | 2 | 1067–1079, 1147 |
| `castCollapsible` | 3 | 2 | 876, 3619–3628 |
| `emby-scrollbuttons-button` | 3 | 2 | 1892, 7942–7949 |
| `emby-textarea` | 3 | 2 | 5505–5514, 5543 |
| `guestCastContent` | 3 | 2 | 876, 3619–3628 |
| `guide-channelHeaderCell` | 3 | 2 | 680, 5804–5820 |
| `guide-date-tab-button` | 3 | 2 | 680, 3979–3987 |
| `headerUserButton` | 3 | 2 | 600–613, 5105 |
| `noHeaderRight` | 3 | 2 | 1718, 6029–6033 |
| `overview` | 3 | 2 | 3393–3397, 4883 |
| `section0` | 3 | 2 | 1026–1050, 7066 |
| `add` | 2 | 2 | 1803, 7163 |
| `alphaPicker-fixed-right` | 2 | 2 | 2773, 5039 |
| `backdropImageFadeIn` | 2 | 2 | 2826, 7680 |
| `book` | 2 | 2 | 2059, 2598 |
| `btnDeleteImage` | 2 | 2 | 3780, 3993 |
| `cardContent` | 2 | 2 | 876, 908 |
| `cardOverlayButton` | 2 | 2 | 1081, 1124 |
| `cardOverlayButton-hover` | 2 | 2 | 968, 1096 |
| `chevron_right` | 2 | 2 | 5200, 5244 |
| `classList` | 2 | 2 | 1803, 7163 |
| `collapseContent` | 2 | 2 | 3530, 4005 |
| `collectionItemsContainer` | 2 | 2 | 1830, 5016 |
| `content-primary` | 2 | 2 | 5080, 5136 |
| `editorsChoiceContainer` | 2 | 2 | 6835, 7860 |
| `editorsChoiceItemBanner` | 2 | 2 | 6835, 7588 |
| `editorsChoiceItemOverview` | 2 | 2 | 7860, 7953 |
| `endsAt` | 2 | 2 | 1923, 7163 |
| `fieldDescription` | 2 | 2 | 314, 7706 |
| `formDialogFooter-clear` | 2 | 2 | 3525, 4007 |
| `guide-programNameCaret` | 2 | 2 | 314, 5786 |
| `headroom` | 2 | 2 | 6489, 6526 |
| `indicator` | 2 | 2 | 840, 3712 |
| `mc-row` | 2 | 2 | 468, 7480 |
| `mediaInfoOfficialRating` | 2 | 2 | 1923, 7163 |
| `navMenuOption-selected` | 2 | 2 | 4783, 7297 |
| `nowPlayingInfoContainer` | 2 | 2 | 3166, 6287 |
| `org` | 2 | 2 | 3202, 3232 |
| `page` | 2 | 2 | 2773, 7066 |
| `paperList` | 2 | 2 | 885, 4018 |
| `playlist` | 2 | 2 | 4600, 6265 |
| `programSecondaryTitle` | 2 | 2 | 314, 5838 |
| `queue` | 2 | 2 | 2059, 2598 |
| `reactRoot` | 2 | 2 | 4476, 6885 |
| `recordingFields` | 2 | 2 | 4827, 4971 |
| `runtime` | 2 | 2 | 6199, 6227 |
| `sectionTitleContainer-cards` | 2 | 2 | 5165, 5230 |
| `sidebarHeader` | 2 | 2 | 4146, 7303 |
| `splide` | 2 | 2 | 6835, 7909 |
| `tagline` | 2 | 2 | 2672, 4883 |
| `upNextDialog-title` | 2 | 2 | 5286, 5320 |
| `vertical-list` | 2 | 2 | 1865, 7808 |
| `vertical-wrap` | 2 | 2 | 806, 1830 |
| `videoOsdBottom` | 2 | 2 | 3158, 6456 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3158, 6456 |
| `userPreferencesPage` | 12 | 1 | 7691–7787 |
| `checkboxContainer` | 7 | 1 | 3607–3644 |
| `itemDetailsGroup` | 7 | 1 | 4890–4976 |
| `itemProgressBar` | 6 | 1 | 2876–2910 |
| `streaming-lookup-container` | 6 | 1 | 3260–3305 |
| `trackSelectionFieldContainer` | 6 | 1 | 4846–4869 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7909–7949 |
| `innerCardFooter` | 5 | 1 | 3420–3449 |
| `chapterCardImageContainer` | 4 | 1 | 3420–3449 |
| `emby-select-withcolor` | 4 | 1 | 5514–5561 |
| `endTimeText` | 4 | 1 | 6199–6227 |
| `mainDetailButtons` | 4 | 1 | 3942–3956 |
| `overview-controls` | 4 | 1 | 3393–3405 |
| `startTimeText` | 4 | 1 | 6199–6221 |
| `button-flat` | 3 | 1 | 3139–3149 |
| `cardIndicators` | 3 | 1 | 3697–3707 |
| `cardOverlayFab-primary` | 3 | 1 | 1059–1081 |
| `com` | 3 | 1 | 3208–3226 |
| `content` | 3 | 1 | 4912–4943 |
| `fab` | 3 | 1 | 3802–3815 |
| `listChildrenCollapsible` | 3 | 1 | 4961–4976 |
| `mdl-slider-background-flex` | 3 | 1 | 2996–3009 |
| `mediaInfoCriticRating` | 3 | 1 | 1964–1973 |
| `nextUpSection` | 3 | 1 | 4956–4976 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 6251–6261 |
| `serverInfo` | 3 | 1 | 4022–4031 |
| `transcodingProgress` | 3 | 1 | 2887–2899 |
