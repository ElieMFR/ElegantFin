# Index des composants — ElegantFin Cinema Edition v1.5.7

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.5.7.css` — 8048 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 38 | 16 | 456–486, 517–552, 790, 903, 1564–1584, 2198–2231, 2258–2262, 2539–2557, 2593, 6955, 6991–7001, 7141, 7241–7260, 7338–7360, 7390–7397, 7561 |
| `cardScalable` | 29 | 14 | 456, 486, 540–552, 853–893, 919–963, 2557, 3639, 3750, 3828, 6019, 6969–7001, 7071, 7241, 7381–7397 |
| `cardImageContainer` | 21 | 13 | 467, 535, 871, 899–928, 963, 1021–1045, 6175–6179, 6259, 6961, 7071, 7111, 7241–7260, 7381 |
| `material-icons` | 17 | 13 | 392–411, 1789, 1887, 1940, 3596, 3755, 3828–3834, 3940, 4102, 4656, 5192, 5226–5236, 5836 |
| `itemDetailPage` | 20 | 12 | 1627, 1713, 1798, 1825, 2054–2094, 2129–2144, 2180–2184, 2294, 2606, 4779, 5085, 7815–7853 |
| `skinHeader` | 20 | 12 | 295, 1713, 4082–4098, 4468, 4514–4541, 6027–6031, 6468, 6524–6532, 6602–6627, 7055, 7208, 7886 |
| `js` | 13 | 12 | 329, 359, 1699–1713, 1798, 2365, 2972, 3400, 3729, 5836, 6833, 7160, 7407 |
| `nameContainer` | 27 | 9 | 736, 2301–2324, 2365, 2394, 2429–2476, 2513, 2544–2548, 5592–5645, 7815–7853 |
| `emby-button` | 12 | 9 | 662–679, 706–724, 3233, 3368–3375, 3775, 3809, 3962, 4674, 5414 |
| `parentName` | 23 | 8 | 736, 2306–2324, 2365, 2394, 2429–2476, 5598–5645, 5718, 7815–7853 |
| `detailLogo` | 20 | 8 | 736, 2083–2094, 2129–2144, 2171–2184, 2294–2324, 2394, 2429–2476, 2544 |
| `listItem` | 19 | 8 | 313, 679, 2561, 4576–4602, 4633–4665, 4710, 4754, 7603–7620 |
| `detailPageWrapperContainer` | 17 | 8 | 736, 1595–1605, 2094, 2267, 2301–2324, 2394, 2429–2476, 2544 |
| `subtitle` | 17 | 8 | 2054–2064, 2180–2184, 2306, 2365, 2485–2495, 2606, 5653–5686, 7815–7853 |
| `cardBox` | 13 | 8 | 456–486, 517–541, 790, 941–945, 1050, 6955, 7241, 7626 |
| `backdropCard` | 12 | 8 | 1008–1014, 1131, 2054–2064, 2210, 2294, 2548–2557, 2584, 2895 |
| `nowPlayingBar` | 8 | 8 | 329, 3157, 6311, 7018, 7105, 7194, 7220, 7566 |
| `card-hoverable` | 22 | 7 | 552, 919–1014, 6179, 6979, 7111–7150, 7241, 7626 |
| `loginPage` | 18 | 7 | 3906, 6031–6065, 6105–6124, 6160–6179, 7008, 7051, 7370–7397 |
| `navMenuOption` | 12 | 6 | 679, 775–785, 4151, 4643–4665, 4760–4765, 7283–7294 |
| `emby-tab-button` | 11 | 6 | 679, 746–755, 3881, 6678–6689, 6717–6734, 7898 |
| `paper-icon-button-light` | 11 | 6 | 624–679, 1713, 1789, 1887, 3536–3556, 5498 |
| `verticalSection` | 11 | 6 | 1793, 2797–2802, 5085, 7064, 7160, 7407 |
| `button-link` | 10 | 6 | 679, 706–724, 3108–3117, 3177–3187, 3233, 7777 |
| `headerTop` | 9 | 6 | 2184, 4468, 4514, 6474–6499, 6594–6611, 6638–6642 |
| `person` | 8 | 6 | 2054–2079, 2294, 2548, 2593–2602, 4034, 7810 |
| `mainDrawer` | 7 | 6 | 3122, 4116, 4514, 7008–7018, 7270, 7309 |
| `scss` | 6 | 6 | 295, 818, 1076, 3645, 4157, 7160 |
| `detailImageContainer` | 20 | 5 | 2054–2079, 2198–2262, 2294, 2535–2557, 2584–2602 |
| `osdHeader` | 15 | 5 | 1762–1780, 6463–6532, 6602–6627, 7055, 7566 |
| `cardOverlayContainer` | 12 | 5 | 982–1014, 1054–1076, 1149, 7566, 7603 |
| `sectionTabs` | 11 | 5 | 1856, 3881, 4541, 6504–6509, 6695–6739 |
| `actionSheetMenuItem` | 10 | 5 | 679, 4576–4587, 4633, 4710–4754, 7036 |
| `cardImageIcon` | 8 | 5 | 448–452, 2548–2557, 2620, 3623, 6259 |
| `sectionTitle` | 7 | 5 | 1793, 1866–1873, 4369, 5162–5170, 6100 |
| `semiTransparent` | 7 | 5 | 1695, 4082–4098, 6027, 6492–6513, 6549 |
| `emby-scroller-container` | 6 | 5 | 1793–1798, 1836, 2785, 7064, 7160 |
| `portraitCard` | 6 | 5 | 1131, 1215, 1978–1983, 2258, 2895 |
| `appfooter` | 5 | 5 | 329, 2838, 6652, 7094, 7566 |
| `skinHeader-withBackground` | 5 | 5 | 1695, 4082, 6027, 6463, 6513 |
| `btnPlay` | 16 | 4 | 561–585, 624–679, 3838–3880, 3912–3940 |
| `itemName` | 11 | 4 | 736, 2365, 5598–5645, 5736–5753 |
| `backdropImage` | 10 | 4 | 2684–2712, 2739–2743, 6948, 7071–7079 |
| `upNextContainer` | 10 | 4 | 5253–5271, 5297–5323, 7008–7018, 7044 |
| `emby-scroller` | 9 | 4 | 1798, 1836–1842, 7313–7360, 7545–7561 |
| `sectionTitleTextButton` | 9 | 4 | 478, 5145–5153, 5180–5192, 5226–5236 |
| `backgroundContainer` | 8 | 4 | 2148, 2676, 2717–2735, 2767 |
| `detailRibbon` | 8 | 4 | 1652–1680, 1893, 1978–1990, 7810 |
| `skip-button` | 8 | 4 | 679, 3890, 5346–5371, 5398–5416 |
| `listItemBodyText` | 7 | 4 | 4597–4616, 4656, 4731, 7620 |
| `visualCardBox` | 7 | 4 | 456, 880–893, 919–924, 1050 |
| `button-submit` | 6 | 4 | 3906, 3993, 6160–6168, 7688–7703 |
| `cardText-secondary` | 6 | 4 | 313, 968, 3628–3632, 7133–7141 |
| `detailPagePrimaryContent` | 6 | 4 | 1667–1685, 2500, 5079, 7224 |
| `skinHeader-blurred` | 6 | 4 | 6027, 6492–6499, 7208, 7566–7585 |
| `squareCard` | 6 | 4 | 903, 2548, 2584–2602, 6129–6133 |
| `itemsContainer` | 4 | 4 | 790, 1825, 1860, 5085 |
| `raised` | 4 | 4 | 679, 765, 3775, 3809 |
| `tsx` | 4 | 4 | 1131, 1713, 4468, 4545 |
| `x` | 4 | 4 | 2365, 4157, 5701, 7160 |
| `detailButton` | 13 | 3 | 624–679, 3819–3880, 3936–3940 |
| `itemSelectionPanel` | 9 | 3 | 932–936, 3568, 3596–3639 |
| `pageTitle` | 8 | 3 | 1737–1780, 6524, 6627 |
| `homePage` | 7 | 3 | 4468, 4514–4541, 6756 |
| `playedIndicator` | 7 | 3 | 818–832, 3712, 7241–7265 |
| `check` | 6 | 3 | 3596, 3828, 4710–4754 |
| `detailSectionContent` | 6 | 3 | 3400, 4865–4875, 4958–4968 |
| `emby-checkbox` | 6 | 3 | 3573, 3610–3614, 3663–3675 |
| `actionSheetContent` | 5 | 3 | 4702–4706, 7008–7018, 7044 |
| `cardText-first` | 5 | 3 | 968, 3602–3628, 6240 |
| `dialog` | 5 | 3 | 3452–3462, 7008–7018, 7044 |
| `guideProgramName` | 5 | 3 | 679, 5777–5788, 5831–5836 |
| `noHomeButtonHeader` | 5 | 3 | 1713, 6524, 6678–6689 |
| `overflowBackdropCard` | 5 | 3 | 1008–1014, 3606, 6235–6240 |
| `secondary` | 5 | 3 | 313, 4606–4616, 4656 |
| `album` | 4 | 3 | 2294, 2553–2557, 2593 |
| `cardPadder` | 4 | 3 | 452, 1050, 3619–3623 |
| `cardText` | 4 | 3 | 968–978, 3628, 7386 |
| `detailPageContent` | 4 | 3 | 1815, 4792, 5072–5079 |
| `dialog-fullscreen` | 4 | 3 | 3462, 7008–7018, 7044 |
| `emby-scrollbuttons` | 4 | 3 | 1878–1883, 7407, 7932 |
| `folder` | 4 | 3 | 1978–1983, 3729, 3792 |
| `formDialogFooter` | 4 | 3 | 3520, 4000, 7637–7661 |
| `infoWrapper` | 4 | 3 | 2237–2242, 2500, 2528 |
| `listItemImage` | 4 | 3 | 2872–2877, 4570, 7620 |
| `musicParentName` | 4 | 3 | 2054, 2606, 5718–5727 |
| `programGuideSection` | 4 | 3 | 2561–2576, 4968, 4995 |
| `toast` | 4 | 3 | 5246, 7008–7018, 7044 |
| `cardFooter` | 3 | 3 | 3639, 7111, 7150 |
| `collectionItems` | 3 | 3 | 1825, 4968, 5004 |
| `defaultCardBackground` | 3 | 3 | 3750, 6255, 6354 |
| `detailPageSecondaryContainer` | 3 | 3 | 1662, 1689, 1815 |
| `emby-input` | 3 | 3 | 5512, 5541, 7703 |
| `formDialogFooterItem` | 3 | 3 | 3520, 3787, 3912 |
| `formDialogHeader` | 3 | 3 | 4000, 7566, 7637 |
| `iconOsd` | 3 | 3 | 6005, 7566, 7637 |
| `live_tv` | 3 | 3 | 2054, 2593, 4034 |
| `myPreferencesMenuPage` | 3 | 3 | 425, 4770, 5093 |
| `playerStats` | 3 | 3 | 6005, 7637, 7673 |
| `readOnlyContent` | 3 | 3 | 4042, 6118, 6772 |
| `sectionTitle-cards` | 3 | 3 | 1793, 5162, 5222 |
| `sectionTitleContainer` | 3 | 3 | 1825, 1883, 5004 |
| `itemExternalLinks` | 13 | 2 | 3170–3248, 3400 |
| `checkboxOutline` | 10 | 2 | 3573–3614, 3645–3675 |
| `itemBackdrop` | 9 | 2 | 2020–2079, 2267 |
| `mdl-slider` | 9 | 2 | 2968, 3023–3081 |
| `cardOverlayButton-br` | 8 | 2 | 1062, 1091–1142 |
| `listItemIcon` | 8 | 2 | 4030–4034, 4710–4770 |
| `sliderContainer` | 8 | 2 | 2972, 3000–3065 |
| `detail-clamp-text` | 7 | 2 | 3336–3362, 3388–3392 |
| `divUsers` | 7 | 2 | 6129–6133, 7370–7397 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3610–3614, 3644–3663 |
| `countIndicator` | 6 | 2 | 809–839, 7637–7661 |
| `detailPagePrimaryContainer` | 6 | 2 | 1639–1685, 2500 |
| `detailsGroupItem` | 6 | 2 | 4827, 4898–4935 |
| `headerButton` | 6 | 2 | 599–679, 6620 |
| `headerLeft` | 6 | 2 | 1743–1780, 6877 |
| `selectionCommandsPanel` | 6 | 2 | 3530–3564, 7566 |
| `trackSelections` | 6 | 2 | 4796–4827, 4963–4968 |
| `withBackdrop` | 6 | 2 | 2676, 2717–2735 |
| `detailSection` | 5 | 2 | 4779–4788, 4948–4968 |
| `fullSyncIndicator` | 5 | 2 | 809–832, 7637–7661 |
| `mainDrawer-scrollContainer` | 5 | 2 | 3130, 7283–7300 |
| `manualLoginForm` | 5 | 2 | 6100–6144, 6185 |
| `mediaInfoItem` | 5 | 2 | 1897–1940, 7160 |
| `overview-expand` | 5 | 2 | 3368–3392, 4865 |
| `scrollX` | 5 | 2 | 1798, 1836–1856 |
| `videoIndicator` | 5 | 2 | 3718–3746, 7637 |
| `visualLoginForm` | 5 | 2 | 6100–6144, 6185 |
| `withSectionTabs` | 5 | 2 | 2726–2743, 6499 |
| `alphaPickerButton` | 4 | 2 | 679, 5019–5031 |
| `backgroundProgress` | 4 | 2 | 2883–2895, 2925 |
| `emby-select` | 4 | 2 | 5512–5524, 7703 |
| `emby-tab-button-active` | 4 | 2 | 3973, 6725–6739 |
| `mediaSourceIndicator` | 4 | 2 | 809–832, 7637 |
| `play_arrow` | 4 | 2 | 3755–3771, 3940 |
| `playbackProgress` | 4 | 2 | 2883–2895, 2930 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4597–4602, 6348–6354 |
| `programCell` | 4 | 2 | 5768, 5827–5836 |
| `cardOverlayButtonIcon` | 3 | 2 | 1062–1074, 1142 |
| `castCollapsible` | 3 | 2 | 871, 3614–3623 |
| `emby-scrollbuttons-button` | 3 | 2 | 1887, 7939–7946 |
| `emby-textarea` | 3 | 2 | 5503–5512, 5541 |
| `guestCastContent` | 3 | 2 | 871, 3614–3623 |
| `guide-channelHeaderCell` | 3 | 2 | 679, 5802–5818 |
| `guide-date-tab-button` | 3 | 2 | 679, 3973–3981 |
| `headerUserButton` | 3 | 2 | 599–612, 5097 |
| `noHeaderRight` | 3 | 2 | 1713, 6027–6031 |
| `overview` | 3 | 2 | 3388–3392, 4875 |
| `add` | 2 | 2 | 1798, 7160 |
| `alphaPicker-fixed-right` | 2 | 2 | 2767, 5031 |
| `backdropImageFadeIn` | 2 | 2 | 2822, 7677 |
| `book` | 2 | 2 | 2054, 2593 |
| `btnDeleteImage` | 2 | 2 | 3775, 3987 |
| `cardContent` | 2 | 2 | 871, 903 |
| `cardOverlayButton` | 2 | 2 | 1076, 1119 |
| `cardOverlayButton-hover` | 2 | 2 | 963, 1091 |
| `chevron_right` | 2 | 2 | 5192, 5236 |
| `classList` | 2 | 2 | 1798, 7160 |
| `collapseContent` | 2 | 2 | 3525, 3998 |
| `collectionItemsContainer` | 2 | 2 | 1825, 5008 |
| `content-primary` | 2 | 2 | 5072, 5128 |
| `editorsChoiceContainer` | 2 | 2 | 6833, 7857 |
| `editorsChoiceItemBanner` | 2 | 2 | 6833, 7585 |
| `editorsChoiceItemOverview` | 2 | 2 | 7857, 7950 |
| `endsAt` | 2 | 2 | 1918, 7160 |
| `f5f5f5` | 2 | 2 | 5346, 5376 |
| `fieldDescription` | 2 | 2 | 313, 7703 |
| `formDialogFooter-clear` | 2 | 2 | 3520, 4000 |
| `guide-programNameCaret` | 2 | 2 | 313, 5784 |
| `headroom` | 2 | 2 | 6487, 6524 |
| `indicator` | 2 | 2 | 839, 3707 |
| `mc-row` | 2 | 2 | 467, 7477 |
| `mediaInfoOfficialRating` | 2 | 2 | 1918, 7160 |
| `navMenuOption-selected` | 2 | 2 | 4775, 7294 |
| `nowPlayingInfoContainer` | 2 | 2 | 3161, 6285 |
| `org` | 2 | 2 | 3197, 3227 |
| `page` | 2 | 2 | 2767, 7064 |
| `paperList` | 2 | 2 | 880, 4011 |
| `playlist` | 2 | 2 | 4592, 6263 |
| `programSecondaryTitle` | 2 | 2 | 313, 5836 |
| `queue` | 2 | 2 | 2054, 2593 |
| `reactRoot` | 2 | 2 | 4468, 6883 |
| `recordingFields` | 2 | 2 | 4819, 4963 |
| `runtime` | 2 | 2 | 6197, 6225 |
| `sectionTitleContainer-cards` | 2 | 2 | 5157, 5222 |
| `sidebarHeader` | 2 | 2 | 4138, 7300 |
| `splide` | 2 | 2 | 6833, 7906 |
| `tagline` | 2 | 2 | 2667, 4875 |
| `upNextDialog-title` | 2 | 2 | 5276, 5310 |
| `vertical-list` | 2 | 2 | 1860, 7805 |
| `vertical-wrap` | 2 | 2 | 805, 1825 |
| `videoOsdBottom` | 2 | 2 | 3153, 6454 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3153, 6454 |
| `userPreferencesPage` | 12 | 1 | 7688–7784 |
| `checkboxContainer` | 7 | 1 | 3602–3639 |
| `itemDetailsGroup` | 7 | 1 | 4882–4968 |
| `itemProgressBar` | 6 | 1 | 2872–2906 |
| `streaming-lookup-container` | 6 | 1 | 3255–3300 |
| `trackSelectionFieldContainer` | 6 | 1 | 4838–4861 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7906–7946 |
| `innerCardFooter` | 5 | 1 | 3415–3444 |
| `chapterCardImageContainer` | 4 | 1 | 3415–3444 |
| `emby-select-withcolor` | 4 | 1 | 5512–5559 |
| `endTimeText` | 4 | 1 | 6197–6225 |
| `mainDetailButtons` | 4 | 1 | 3936–3950 |
| `overview-controls` | 4 | 1 | 3388–3400 |
| `startTimeText` | 4 | 1 | 6197–6219 |
| `button-flat` | 3 | 1 | 3134–3144 |
| `cardIndicators` | 3 | 1 | 3692–3702 |
| `cardOverlayFab-primary` | 3 | 1 | 1054–1076 |
| `com` | 3 | 1 | 3203–3221 |
| `content` | 3 | 1 | 4904–4935 |
| `fab` | 3 | 1 | 3796–3809 |
| `listChildrenCollapsible` | 3 | 1 | 4953–4968 |
| `mdl-slider-background-flex` | 3 | 1 | 2992–3005 |
| `mediaInfoCriticRating` | 3 | 1 | 1959–1968 |
| `nextUpSection` | 3 | 1 | 4948–4968 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 6249–6259 |
| `serverInfo` | 3 | 1 | 4015–4024 |
| `transcodingProgress` | 3 | 1 | 2883–2895 |
