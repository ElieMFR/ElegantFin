# Index des composants — ElegantFin Cinema Edition v1.4.3

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.4.3.css` — 7945 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 38 | 16 | 435–446, 477–523, 761, 878, 1536–1556, 2160–2193, 2220–2224, 2501–2519, 2555, 6814, 6850–6860, 7096–7115, 7193–7215, 7245–7252, 7416, 7823 |
| `cardScalable` | 31 | 13 | 435–446, 500–523, 824–868, 894–938, 2519, 3599, 3710, 3789, 5948, 6828–6860, 6931, 7096, 7236–7252 |
| `itemDetailPage` | 22 | 13 | 1599, 1685, 1764, 1791, 2020–2056, 2091–2106, 2142–2146, 2256, 2568, 4045–4056, 4721, 5020, 7651–7689 |
| `material-icons` | 17 | 13 | 371–390, 1755, 1853, 1906, 3556, 3715, 3789–3795, 3902, 4060, 4598, 5127, 5161–5171, 5765 |
| `cardImageContainer` | 22 | 12 | 495, 846, 874–903, 938, 995–1025, 6074–6078, 6158, 6820, 6923–6931, 6971, 7096–7115, 7236 |
| `skinHeader` | 16 | 10 | 284, 4410, 4456–4483, 5956, 6367, 6423–6431, 6497–6522, 6914, 7063, 7760 |
| `nameContainer` | 27 | 9 | 707, 2263–2286, 2327, 2356, 2391–2438, 2475, 2506–2510, 5521–5574, 7651–7689 |
| `cardBox` | 13 | 9 | 435–446, 477–489, 515, 761, 916–920, 1029, 6814, 7096, 7462 |
| `emby-button` | 12 | 9 | 633–650, 677–695, 3195, 3330–3337, 3735, 3770, 3924, 4616, 5343 |
| `js` | 10 | 9 | 318–338, 1671, 1764, 2327, 2933, 3689, 5765, 7015, 7262 |
| `card-hoverable` | 23 | 8 | 523, 834, 894–988, 6078, 6838, 6971–7006, 7096, 7462 |
| `parentName` | 23 | 8 | 707, 2268–2286, 2327, 2356, 2391–2438, 5527–5574, 5647, 7651–7689 |
| `detailLogo` | 21 | 8 | 707, 2030–2056, 2091–2106, 2133–2146, 2256–2286, 2356, 2391–2438, 2506 |
| `listItem` | 19 | 8 | 302, 650, 2523, 4518–4544, 4575–4607, 4652, 4696, 7439–7456 |
| `detailPageWrapperContainer` | 17 | 8 | 707, 1567–1577, 2056, 2229, 2263–2286, 2356, 2391–2438, 2506 |
| `subtitle` | 17 | 8 | 2020–2030, 2142–2146, 2268, 2327, 2447–2457, 2568, 5582–5615, 7651–7689 |
| `backdropCard` | 12 | 8 | 982–988, 1103, 2020–2030, 2172, 2256, 2510–2519, 2546, 2856 |
| `nowPlayingBar` | 8 | 8 | 318, 3119, 6210, 6877, 6965, 7049, 7075, 7421 |
| `loginPage` | 16 | 7 | 3868, 5960–5991, 6031, 6059–6078, 6867, 6910, 7225–7252 |
| `navMenuOption` | 12 | 6 | 650, 746–756, 4110, 4585–4607, 4702–4707, 7138–7149 |
| `paper-icon-button-light` | 11 | 6 | 595–650, 1685, 1755, 1853, 3496–3516, 5427 |
| `verticalSection` | 11 | 6 | 1759, 2758–2763, 5020, 6923, 7015, 7262 |
| `button-link` | 10 | 6 | 650, 677–695, 3069–3078, 3139–3149, 3195, 7613 |
| `headerTop` | 9 | 6 | 2146, 4410, 4456, 6373–6398, 6489–6506, 6533–6537 |
| `person` | 8 | 6 | 2020–2041, 2256, 2510, 2555–2564, 3997, 7646 |
| `mainDrawer` | 7 | 6 | 3083, 4074, 4456, 6867–6877, 7125, 7164 |
| `scss` | 6 | 6 | 284, 789, 1055, 3605, 4116, 7015 |
| `detailImageContainer` | 20 | 5 | 2020–2041, 2160–2224, 2256, 2497–2519, 2546–2564 |
| `osdHeader` | 15 | 5 | 1728–1746, 6362–6431, 6497–6522, 6914, 7421 |
| `sectionTabs` | 11 | 5 | 1822, 3847, 4483, 6403–6408, 6588–6632 |
| `actionSheetMenuItem` | 10 | 5 | 650, 4518–4529, 4575, 4652–4696, 6895 |
| `emby-tab-button` | 10 | 5 | 650, 717–726, 3847, 6573–6581, 6610–6627 |
| `cardImageIcon` | 8 | 5 | 427–431, 2510–2519, 2582, 3583, 6158 |
| `sectionTitle` | 7 | 5 | 1759, 1832–1839, 4311, 5097–5105, 6026 |
| `emby-scroller-container` | 6 | 5 | 1759–1764, 1802, 2748, 6923, 7015 |
| `portraitCard` | 6 | 5 | 1103, 1187, 1944–1949, 2220, 2856 |
| `appfooter` | 5 | 5 | 318, 2799, 6547, 6954, 7421 |
| `skinHeader-withBackground` | 5 | 5 | 1667, 4045, 5956, 6362, 6412 |
| `btnPlay` | 16 | 4 | 532–556, 595–650, 3799–3841, 3874–3902 |
| `cardOverlayContainer` | 12 | 4 | 956–988, 1033–1055, 1121, 7421–7439 |
| `itemName` | 11 | 4 | 707, 2327, 5527–5574, 5665–5682 |
| `backdropImage` | 10 | 4 | 2647–2675, 2702–2706, 6807, 6931–6939 |
| `upNextContainer` | 10 | 4 | 5189–5208, 5234–5260, 6867–6877, 6903 |
| `emby-scroller` | 9 | 4 | 1764, 1802–1808, 7168–7215, 7400–7416 |
| `backgroundContainer` | 8 | 4 | 2110, 2638, 2680–2698, 2730 |
| `detailRibbon` | 8 | 4 | 1624–1652, 1859, 1944–1956, 7646 |
| `listItemBodyText` | 7 | 4 | 4539–4558, 4598, 4673, 7456 |
| `skip-button` | 7 | 4 | 650, 3852, 5283–5300, 5327–5345 |
| `visualCardBox` | 7 | 4 | 435, 855–868, 894–899, 1029 |
| `button-submit` | 6 | 4 | 3868, 3956, 6059–6067, 7524–7539 |
| `cardText-secondary` | 6 | 4 | 302, 943, 3588–3592, 6993–7001 |
| `detailPagePrimaryContent` | 6 | 4 | 1639–1657, 2462, 5014, 7079 |
| `squareCard` | 6 | 4 | 878, 2510, 2546–2564, 6035–6039 |
| `semiTransparent` | 5 | 4 | 1667, 5956, 6391–6412, 6448 |
| `skinHeader-blurred` | 5 | 4 | 5956, 6391–6398, 7063, 7421 |
| `itemsContainer` | 4 | 4 | 761, 1791, 1826, 5020 |
| `raised` | 4 | 4 | 650, 736, 3735, 3770 |
| `x` | 4 | 4 | 2327, 4116, 5630, 7015 |
| `detailButton` | 13 | 3 | 595–650, 3780–3841, 3898–3902 |
| `itemSelectionPanel` | 9 | 3 | 907–911, 3528, 3556–3599 |
| `pageTitle` | 8 | 3 | 1703–1746, 6423, 6522 |
| `sectionTitleTextButton` | 8 | 3 | 5080–5088, 5115–5127, 5161–5171 |
| `homePage` | 7 | 3 | 4410, 4456–4483, 6649 |
| `playedIndicator` | 7 | 3 | 789–803, 3672, 7096–7120 |
| `check` | 6 | 3 | 3556, 3789, 4652–4696 |
| `detailSectionContent` | 6 | 3 | 3362, 4803–4813, 4893–4903 |
| `emby-checkbox` | 6 | 3 | 3533, 3570–3574, 3623–3635 |
| `actionSheetContent` | 5 | 3 | 4644–4648, 6867–6877, 6903 |
| `cardText-first` | 5 | 3 | 943, 3562–3588, 6139 |
| `dialog` | 5 | 3 | 3412–3422, 6867–6877, 6903 |
| `guideProgramName` | 5 | 3 | 650, 5706–5717, 5760–5765 |
| `noHomeButtonHeader` | 5 | 3 | 1685, 6423, 6573–6581 |
| `overflowBackdropCard` | 5 | 3 | 982–988, 3566, 6134–6139 |
| `secondary` | 5 | 3 | 302, 4548–4558, 4598 |
| `album` | 4 | 3 | 2256, 2515–2519, 2555 |
| `cardPadder` | 4 | 3 | 431, 1029, 3579–3583 |
| `cardText` | 4 | 3 | 943–953, 3588, 7241 |
| `detailPageContent` | 4 | 3 | 1781, 4734, 5007–5014 |
| `dialog-fullscreen` | 4 | 3 | 3422, 6867–6877, 6903 |
| `emby-scrollbuttons` | 4 | 3 | 1844–1849, 7262, 7798 |
| `folder` | 4 | 3 | 1944–1949, 3689, 3753 |
| `formDialogFooter` | 4 | 3 | 3480, 3963, 7473–7497 |
| `infoWrapper` | 4 | 3 | 2199–2204, 2462, 2490 |
| `listItemImage` | 4 | 3 | 2833–2838, 4512, 7456 |
| `musicParentName` | 4 | 3 | 2020, 2568, 5647–5656 |
| `programGuideSection` | 4 | 3 | 2523–2538, 4903, 4930 |
| `toast` | 4 | 3 | 5181, 6867–6877, 6903 |
| `cardFooter` | 3 | 3 | 3599, 6971, 7006 |
| `collectionItems` | 3 | 3 | 1791, 4903, 4939 |
| `defaultCardBackground` | 3 | 3 | 3710, 6154, 6253 |
| `detailPageSecondaryContainer` | 3 | 3 | 1634, 1661, 1781 |
| `emby-input` | 3 | 3 | 5441, 5470, 7539 |
| `formDialogFooterItem` | 3 | 3 | 3480, 3748, 3874 |
| `formDialogHeader` | 3 | 3 | 3963, 7421, 7473 |
| `iconOsd` | 3 | 3 | 5934, 7421, 7473 |
| `live_tv` | 3 | 3 | 2020, 2555, 3997 |
| `myPreferencesMenuPage` | 3 | 3 | 404, 4712, 5028 |
| `page` | 3 | 3 | 1025, 2730, 6923 |
| `playerStats` | 3 | 3 | 5934, 7473, 7509 |
| `sectionTitle-cards` | 3 | 3 | 1759, 5097, 5157 |
| `sectionTitleContainer` | 3 | 3 | 1791, 1849, 4939 |
| `tsx` | 3 | 3 | 1103, 4410, 4487 |
| `itemExternalLinks` | 13 | 2 | 3132–3210, 3362 |
| `checkboxOutline` | 10 | 2 | 3533–3574, 3605–3635 |
| `itemBackdrop` | 9 | 2 | 1986–2041, 2229 |
| `mdl-slider` | 9 | 2 | 2929, 2984–3042 |
| `listItemIcon` | 8 | 2 | 3993–3997, 4652–4712 |
| `sliderContainer` | 8 | 2 | 2933, 2961–3026 |
| `cardOverlayButton-br` | 7 | 2 | 1041, 1070–1114 |
| `detail-clamp-text` | 7 | 2 | 3298–3324, 3350–3354 |
| `divUsers` | 7 | 2 | 6035–6039, 7225–7252 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3570–3574, 3604–3623 |
| `countIndicator` | 6 | 2 | 780–810, 7473–7497 |
| `detailPagePrimaryContainer` | 6 | 2 | 1611–1657, 2462 |
| `detailsGroupItem` | 6 | 2 | 4765, 4833–4870 |
| `headerButton` | 6 | 2 | 570–650, 6515 |
| `headerLeft` | 6 | 2 | 1709–1746, 6736 |
| `selectionCommandsPanel` | 6 | 2 | 3490–3524, 7421 |
| `trackSelections` | 6 | 2 | 4738–4765, 4898–4903 |
| `withBackdrop` | 6 | 2 | 2638, 2680–2698 |
| `detailSection` | 5 | 2 | 4721–4730, 4883–4903 |
| `fullSyncIndicator` | 5 | 2 | 780–803, 7473–7497 |
| `mainDrawer-scrollContainer` | 5 | 2 | 3092, 7138–7155 |
| `mediaInfoItem` | 5 | 2 | 1863–1906, 7015 |
| `overview-expand` | 5 | 2 | 3330–3354, 4803 |
| `scrollX` | 5 | 2 | 1764, 1802–1822 |
| `videoIndicator` | 5 | 2 | 3678–3706, 7473 |
| `withSectionTabs` | 5 | 2 | 2689–2706, 6398 |
| `alphaPickerButton` | 4 | 2 | 650, 4954–4966 |
| `backgroundProgress` | 4 | 2 | 2844–2856, 2886 |
| `emby-select` | 4 | 2 | 5441–5453, 7539 |
| `emby-tab-button-active` | 4 | 2 | 3935, 6618–6632 |
| `mediaSourceIndicator` | 4 | 2 | 780–803, 7473 |
| `play_arrow` | 4 | 2 | 3715–3731, 3902 |
| `playbackProgress` | 4 | 2 | 2844–2856, 2891 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4539–4544, 6247–6253 |
| `programCell` | 4 | 2 | 5697, 5756–5765 |
| `section0` | 4 | 2 | 995–1025, 6923 |
| `visualLoginForm` | 4 | 2 | 6026–6043, 6084 |
| `cardOverlayButtonIcon` | 3 | 2 | 1041–1053, 1114 |
| `castCollapsible` | 3 | 2 | 846, 3574–3583 |
| `emby-scrollbuttons-button` | 3 | 2 | 1853, 7805–7812 |
| `emby-textarea` | 3 | 2 | 5432–5441, 5470 |
| `guestCastContent` | 3 | 2 | 846, 3574–3583 |
| `guide-channelHeaderCell` | 3 | 2 | 650, 5731–5747 |
| `guide-date-tab-button` | 3 | 2 | 650, 3935–3943 |
| `headerUserButton` | 3 | 2 | 570–583, 5032 |
| `manualLoginForm` | 3 | 2 | 6026–6043, 6084 |
| `overview` | 3 | 2 | 3350–3354, 4813 |
| `add` | 2 | 2 | 1764, 7015 |
| `alphaPicker-fixed-right` | 2 | 2 | 2730, 4966 |
| `backdropImageFadeIn` | 2 | 2 | 2783, 7513 |
| `book` | 2 | 2 | 2020, 2555 |
| `btnDeleteImage` | 2 | 2 | 3735, 3949 |
| `cardContent` | 2 | 2 | 846, 878 |
| `cardOverlayButton` | 2 | 2 | 1055, 1091 |
| `cardOverlayButton-hover` | 2 | 2 | 938, 1070 |
| `chevron_right` | 2 | 2 | 5127, 5171 |
| `classList` | 2 | 2 | 1764, 7015 |
| `collapseContent` | 2 | 2 | 3485, 3961 |
| `collectionItemsContainer` | 2 | 2 | 1791, 4943 |
| `content-primary` | 2 | 2 | 5007, 5063 |
| `editorsChoiceItemOverview` | 2 | 2 | 7735, 7816 |
| `endsAt` | 2 | 2 | 1884, 7015 |
| `fieldDescription` | 2 | 2 | 302, 7539 |
| `formDialogFooter-clear` | 2 | 2 | 3480, 3963 |
| `guide-programNameCaret` | 2 | 2 | 302, 5713 |
| `headroom` | 2 | 2 | 6386, 6423 |
| `indicator` | 2 | 2 | 810, 3667 |
| `mediaInfoOfficialRating` | 2 | 2 | 1884, 7015 |
| `navMenuOption-selected` | 2 | 2 | 4717, 7149 |
| `nowPlayingInfoContainer` | 2 | 2 | 3123, 6184 |
| `org` | 2 | 2 | 3159, 3189 |
| `paperList` | 2 | 2 | 855, 3974 |
| `playlist` | 2 | 2 | 4534, 6162 |
| `programSecondaryTitle` | 2 | 2 | 302, 5765 |
| `queue` | 2 | 2 | 2020, 2555 |
| `reactRoot` | 2 | 2 | 4410, 6742 |
| `readOnlyContent` | 2 | 2 | 4005, 6665 |
| `recordingFields` | 2 | 2 | 4757, 4898 |
| `runtime` | 2 | 2 | 6096, 6124 |
| `sectionTitleContainer-cards` | 2 | 2 | 5092, 5157 |
| `sidebarHeader` | 2 | 2 | 4097, 7155 |
| `tagline` | 2 | 2 | 2629, 4813 |
| `upNextDialog-title` | 2 | 2 | 5213, 5247 |
| `vertical-list` | 2 | 2 | 1826, 7641 |
| `vertical-wrap` | 2 | 2 | 776, 1791 |
| `videoOsdBottom` | 2 | 2 | 3115, 6353 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3115, 6353 |
| `userPreferencesPage` | 12 | 1 | 7524–7620 |
| `checkboxContainer` | 7 | 1 | 3562–3599 |
| `itemDetailsGroup` | 7 | 1 | 4817–4903 |
| `itemProgressBar` | 6 | 1 | 2833–2867 |
| `streaming-lookup-container` | 6 | 1 | 3217–3262 |
| `trackSelectionFieldContainer` | 6 | 1 | 4776–4799 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7772–7812 |
| `innerCardFooter` | 5 | 1 | 3375–3404 |
| `chapterCardImageContainer` | 4 | 1 | 3375–3404 |
| `emby-select-withcolor` | 4 | 1 | 5441–5488 |
| `endTimeText` | 4 | 1 | 6096–6124 |
| `mainDetailButtons` | 4 | 1 | 3898–3912 |
| `overview-controls` | 4 | 1 | 3350–3362 |
| `startTimeText` | 4 | 1 | 6096–6118 |
| `button-flat` | 3 | 1 | 3096–3106 |
| `cardIndicators` | 3 | 1 | 3652–3662 |
| `cardOverlayFab-primary` | 3 | 1 | 1033–1055 |
| `com` | 3 | 1 | 3165–3183 |
| `content` | 3 | 1 | 4839–4870 |
| `discover-card` | 3 | 1 | 7823–7846 |
| `fab` | 3 | 1 | 3757–3770 |
| `listChildrenCollapsible` | 3 | 1 | 4888–4903 |
| `mdl-slider-background-flex` | 3 | 1 | 2953–2966 |
| `mediaInfoCriticRating` | 3 | 1 | 1925–1934 |
| `nextUpSection` | 3 | 1 | 4883–4903 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 6148–6158 |
| `serverInfo` | 3 | 1 | 3978–3987 |
| `transcodingProgress` | 3 | 1 | 2844–2856 |
