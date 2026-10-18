# Index des composants — ElegantFin Cinema Edition v1.4.4

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.4.4.css` — 7952 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 38 | 16 | 435–446, 477–523, 761, 878, 1536–1556, 2160–2193, 2220–2224, 2501–2519, 2555, 6821, 6857–6867, 7103–7122, 7200–7222, 7252–7259, 7423, 7830 |
| `cardScalable` | 31 | 13 | 435–446, 500–523, 824–868, 894–938, 2519, 3599, 3710, 3789, 5955, 6835–6867, 6938, 7103, 7243–7259 |
| `itemDetailPage` | 22 | 13 | 1599, 1685, 1764, 1791, 2020–2056, 2091–2106, 2142–2146, 2256, 2568, 4045–4056, 4728, 5027, 7658–7696 |
| `material-icons` | 17 | 13 | 371–390, 1755, 1853, 1906, 3556, 3715, 3789–3795, 3902, 4060, 4605, 5134, 5168–5178, 5772 |
| `cardImageContainer` | 22 | 12 | 495, 846, 874–903, 938, 995–1025, 6081–6085, 6165, 6827, 6930–6938, 6978, 7103–7122, 7243 |
| `skinHeader` | 16 | 10 | 284, 4417, 4463–4490, 5963, 6374, 6430–6438, 6504–6529, 6921, 7070, 7767 |
| `nameContainer` | 27 | 9 | 707, 2263–2286, 2327, 2356, 2391–2438, 2475, 2506–2510, 5528–5581, 7658–7696 |
| `cardBox` | 13 | 9 | 435–446, 477–489, 515, 761, 916–920, 1029, 6821, 7103, 7469 |
| `emby-button` | 12 | 9 | 633–650, 677–695, 3195, 3330–3337, 3735, 3770, 3924, 4623, 5350 |
| `js` | 10 | 9 | 318–338, 1671, 1764, 2327, 2933, 3689, 5772, 7022, 7269 |
| `card-hoverable` | 23 | 8 | 523, 834, 894–988, 6085, 6845, 6978–7013, 7103, 7469 |
| `parentName` | 23 | 8 | 707, 2268–2286, 2327, 2356, 2391–2438, 5534–5581, 5654, 7658–7696 |
| `detailLogo` | 21 | 8 | 707, 2030–2056, 2091–2106, 2133–2146, 2256–2286, 2356, 2391–2438, 2506 |
| `listItem` | 19 | 8 | 302, 650, 2523, 4525–4551, 4582–4614, 4659, 4703, 7446–7463 |
| `detailPageWrapperContainer` | 17 | 8 | 707, 1567–1577, 2056, 2229, 2263–2286, 2356, 2391–2438, 2506 |
| `subtitle` | 17 | 8 | 2020–2030, 2142–2146, 2268, 2327, 2447–2457, 2568, 5589–5622, 7658–7696 |
| `backdropCard` | 12 | 8 | 982–988, 1103, 2020–2030, 2172, 2256, 2510–2519, 2546, 2856 |
| `nowPlayingBar` | 8 | 8 | 318, 3119, 6217, 6884, 6972, 7056, 7082, 7428 |
| `loginPage` | 16 | 7 | 3868, 5967–5998, 6038, 6066–6085, 6874, 6917, 7232–7259 |
| `navMenuOption` | 12 | 6 | 650, 746–756, 4110, 4592–4614, 4709–4714, 7145–7156 |
| `paper-icon-button-light` | 11 | 6 | 595–650, 1685, 1755, 1853, 3496–3516, 5434 |
| `verticalSection` | 11 | 6 | 1759, 2758–2763, 5027, 6930, 7022, 7269 |
| `button-link` | 10 | 6 | 650, 677–695, 3069–3078, 3139–3149, 3195, 7620 |
| `headerTop` | 9 | 6 | 2146, 4417, 4463, 6380–6405, 6496–6513, 6540–6544 |
| `person` | 8 | 6 | 2020–2041, 2256, 2510, 2555–2564, 3997, 7653 |
| `mainDrawer` | 7 | 6 | 3083, 4074, 4463, 6874–6884, 7132, 7171 |
| `scss` | 6 | 6 | 284, 789, 1055, 3605, 4116, 7022 |
| `detailImageContainer` | 20 | 5 | 2020–2041, 2160–2224, 2256, 2497–2519, 2546–2564 |
| `osdHeader` | 15 | 5 | 1728–1746, 6369–6438, 6504–6529, 6921, 7428 |
| `sectionTabs` | 11 | 5 | 1822, 3847, 4490, 6410–6415, 6595–6639 |
| `actionSheetMenuItem` | 10 | 5 | 650, 4525–4536, 4582, 4659–4703, 6902 |
| `emby-tab-button` | 10 | 5 | 650, 717–726, 3847, 6580–6588, 6617–6634 |
| `cardImageIcon` | 8 | 5 | 427–431, 2510–2519, 2582, 3583, 6165 |
| `sectionTitle` | 7 | 5 | 1759, 1832–1839, 4318, 5104–5112, 6033 |
| `emby-scroller-container` | 6 | 5 | 1759–1764, 1802, 2748, 6930, 7022 |
| `portraitCard` | 6 | 5 | 1103, 1187, 1944–1949, 2220, 2856 |
| `appfooter` | 5 | 5 | 318, 2799, 6554, 6961, 7428 |
| `skinHeader-withBackground` | 5 | 5 | 1667, 4045, 5963, 6369, 6419 |
| `btnPlay` | 16 | 4 | 532–556, 595–650, 3799–3841, 3874–3902 |
| `cardOverlayContainer` | 12 | 4 | 956–988, 1033–1055, 1121, 7428–7446 |
| `itemName` | 11 | 4 | 707, 2327, 5534–5581, 5672–5689 |
| `backdropImage` | 10 | 4 | 2647–2675, 2702–2706, 6814, 6938–6946 |
| `upNextContainer` | 10 | 4 | 5196–5215, 5241–5267, 6874–6884, 6910 |
| `emby-scroller` | 9 | 4 | 1764, 1802–1808, 7175–7222, 7407–7423 |
| `backgroundContainer` | 8 | 4 | 2110, 2638, 2680–2698, 2730 |
| `detailRibbon` | 8 | 4 | 1624–1652, 1859, 1944–1956, 7653 |
| `listItemBodyText` | 7 | 4 | 4546–4565, 4605, 4680, 7463 |
| `skip-button` | 7 | 4 | 650, 3852, 5290–5307, 5334–5352 |
| `visualCardBox` | 7 | 4 | 435, 855–868, 894–899, 1029 |
| `button-submit` | 6 | 4 | 3868, 3956, 6066–6074, 7531–7546 |
| `cardText-secondary` | 6 | 4 | 302, 943, 3588–3592, 7000–7008 |
| `detailPagePrimaryContent` | 6 | 4 | 1639–1657, 2462, 5021, 7086 |
| `squareCard` | 6 | 4 | 878, 2510, 2546–2564, 6042–6046 |
| `semiTransparent` | 5 | 4 | 1667, 5963, 6398–6419, 6455 |
| `skinHeader-blurred` | 5 | 4 | 5963, 6398–6405, 7070, 7428 |
| `itemsContainer` | 4 | 4 | 761, 1791, 1826, 5027 |
| `raised` | 4 | 4 | 650, 736, 3735, 3770 |
| `x` | 4 | 4 | 2327, 4116, 5637, 7022 |
| `detailButton` | 13 | 3 | 595–650, 3780–3841, 3898–3902 |
| `itemSelectionPanel` | 9 | 3 | 907–911, 3528, 3556–3599 |
| `pageTitle` | 8 | 3 | 1703–1746, 6430, 6529 |
| `sectionTitleTextButton` | 8 | 3 | 5087–5095, 5122–5134, 5168–5178 |
| `homePage` | 7 | 3 | 4417, 4463–4490, 6656 |
| `playedIndicator` | 7 | 3 | 789–803, 3672, 7103–7127 |
| `check` | 6 | 3 | 3556, 3789, 4659–4703 |
| `detailSectionContent` | 6 | 3 | 3362, 4810–4820, 4900–4910 |
| `emby-checkbox` | 6 | 3 | 3533, 3570–3574, 3623–3635 |
| `actionSheetContent` | 5 | 3 | 4651–4655, 6874–6884, 6910 |
| `cardText-first` | 5 | 3 | 943, 3562–3588, 6146 |
| `dialog` | 5 | 3 | 3412–3422, 6874–6884, 6910 |
| `guideProgramName` | 5 | 3 | 650, 5713–5724, 5767–5772 |
| `noHomeButtonHeader` | 5 | 3 | 1685, 6430, 6580–6588 |
| `overflowBackdropCard` | 5 | 3 | 982–988, 3566, 6141–6146 |
| `secondary` | 5 | 3 | 302, 4555–4565, 4605 |
| `album` | 4 | 3 | 2256, 2515–2519, 2555 |
| `cardPadder` | 4 | 3 | 431, 1029, 3579–3583 |
| `cardText` | 4 | 3 | 943–953, 3588, 7248 |
| `detailPageContent` | 4 | 3 | 1781, 4741, 5014–5021 |
| `dialog-fullscreen` | 4 | 3 | 3422, 6874–6884, 6910 |
| `emby-scrollbuttons` | 4 | 3 | 1844–1849, 7269, 7805 |
| `folder` | 4 | 3 | 1944–1949, 3689, 3753 |
| `formDialogFooter` | 4 | 3 | 3480, 3963, 7480–7504 |
| `infoWrapper` | 4 | 3 | 2199–2204, 2462, 2490 |
| `listItemImage` | 4 | 3 | 2833–2838, 4519, 7463 |
| `musicParentName` | 4 | 3 | 2020, 2568, 5654–5663 |
| `programGuideSection` | 4 | 3 | 2523–2538, 4910, 4937 |
| `toast` | 4 | 3 | 5188, 6874–6884, 6910 |
| `cardFooter` | 3 | 3 | 3599, 6978, 7013 |
| `collectionItems` | 3 | 3 | 1791, 4910, 4946 |
| `defaultCardBackground` | 3 | 3 | 3710, 6161, 6260 |
| `detailPageSecondaryContainer` | 3 | 3 | 1634, 1661, 1781 |
| `emby-input` | 3 | 3 | 5448, 5477, 7546 |
| `formDialogFooterItem` | 3 | 3 | 3480, 3748, 3874 |
| `formDialogHeader` | 3 | 3 | 3963, 7428, 7480 |
| `iconOsd` | 3 | 3 | 5941, 7428, 7480 |
| `live_tv` | 3 | 3 | 2020, 2555, 3997 |
| `myPreferencesMenuPage` | 3 | 3 | 404, 4719, 5035 |
| `page` | 3 | 3 | 1025, 2730, 6930 |
| `playerStats` | 3 | 3 | 5941, 7480, 7516 |
| `sectionTitle-cards` | 3 | 3 | 1759, 5104, 5164 |
| `sectionTitleContainer` | 3 | 3 | 1791, 1849, 4946 |
| `tsx` | 3 | 3 | 1103, 4417, 4494 |
| `itemExternalLinks` | 13 | 2 | 3132–3210, 3362 |
| `checkboxOutline` | 10 | 2 | 3533–3574, 3605–3635 |
| `itemBackdrop` | 9 | 2 | 1986–2041, 2229 |
| `mdl-slider` | 9 | 2 | 2929, 2984–3042 |
| `listItemIcon` | 8 | 2 | 3993–3997, 4659–4719 |
| `sliderContainer` | 8 | 2 | 2933, 2961–3026 |
| `cardOverlayButton-br` | 7 | 2 | 1041, 1070–1114 |
| `detail-clamp-text` | 7 | 2 | 3298–3324, 3350–3354 |
| `divUsers` | 7 | 2 | 6042–6046, 7232–7259 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3570–3574, 3604–3623 |
| `countIndicator` | 6 | 2 | 780–810, 7480–7504 |
| `detailPagePrimaryContainer` | 6 | 2 | 1611–1657, 2462 |
| `detailsGroupItem` | 6 | 2 | 4772, 4840–4877 |
| `headerButton` | 6 | 2 | 570–650, 6522 |
| `headerLeft` | 6 | 2 | 1709–1746, 6743 |
| `selectionCommandsPanel` | 6 | 2 | 3490–3524, 7428 |
| `trackSelections` | 6 | 2 | 4745–4772, 4905–4910 |
| `withBackdrop` | 6 | 2 | 2638, 2680–2698 |
| `detailSection` | 5 | 2 | 4728–4737, 4890–4910 |
| `fullSyncIndicator` | 5 | 2 | 780–803, 7480–7504 |
| `mainDrawer-scrollContainer` | 5 | 2 | 3092, 7145–7162 |
| `mediaInfoItem` | 5 | 2 | 1863–1906, 7022 |
| `overview-expand` | 5 | 2 | 3330–3354, 4810 |
| `scrollX` | 5 | 2 | 1764, 1802–1822 |
| `videoIndicator` | 5 | 2 | 3678–3706, 7480 |
| `withSectionTabs` | 5 | 2 | 2689–2706, 6405 |
| `alphaPickerButton` | 4 | 2 | 650, 4961–4973 |
| `backgroundProgress` | 4 | 2 | 2844–2856, 2886 |
| `emby-select` | 4 | 2 | 5448–5460, 7546 |
| `emby-tab-button-active` | 4 | 2 | 3935, 6625–6639 |
| `mediaSourceIndicator` | 4 | 2 | 780–803, 7480 |
| `play_arrow` | 4 | 2 | 3715–3731, 3902 |
| `playbackProgress` | 4 | 2 | 2844–2856, 2891 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4546–4551, 6254–6260 |
| `programCell` | 4 | 2 | 5704, 5763–5772 |
| `section0` | 4 | 2 | 995–1025, 6930 |
| `visualLoginForm` | 4 | 2 | 6033–6050, 6091 |
| `cardOverlayButtonIcon` | 3 | 2 | 1041–1053, 1114 |
| `castCollapsible` | 3 | 2 | 846, 3574–3583 |
| `emby-scrollbuttons-button` | 3 | 2 | 1853, 7812–7819 |
| `emby-textarea` | 3 | 2 | 5439–5448, 5477 |
| `guestCastContent` | 3 | 2 | 846, 3574–3583 |
| `guide-channelHeaderCell` | 3 | 2 | 650, 5738–5754 |
| `guide-date-tab-button` | 3 | 2 | 650, 3935–3943 |
| `headerUserButton` | 3 | 2 | 570–583, 5039 |
| `manualLoginForm` | 3 | 2 | 6033–6050, 6091 |
| `overview` | 3 | 2 | 3350–3354, 4820 |
| `add` | 2 | 2 | 1764, 7022 |
| `alphaPicker-fixed-right` | 2 | 2 | 2730, 4973 |
| `backdropImageFadeIn` | 2 | 2 | 2783, 7520 |
| `book` | 2 | 2 | 2020, 2555 |
| `btnDeleteImage` | 2 | 2 | 3735, 3949 |
| `cardContent` | 2 | 2 | 846, 878 |
| `cardOverlayButton` | 2 | 2 | 1055, 1091 |
| `cardOverlayButton-hover` | 2 | 2 | 938, 1070 |
| `chevron_right` | 2 | 2 | 5134, 5178 |
| `classList` | 2 | 2 | 1764, 7022 |
| `collapseContent` | 2 | 2 | 3485, 3961 |
| `collectionItemsContainer` | 2 | 2 | 1791, 4950 |
| `content-primary` | 2 | 2 | 5014, 5070 |
| `editorsChoiceItemOverview` | 2 | 2 | 7742, 7823 |
| `endsAt` | 2 | 2 | 1884, 7022 |
| `fieldDescription` | 2 | 2 | 302, 7546 |
| `formDialogFooter-clear` | 2 | 2 | 3480, 3963 |
| `guide-programNameCaret` | 2 | 2 | 302, 5720 |
| `headroom` | 2 | 2 | 6393, 6430 |
| `indicator` | 2 | 2 | 810, 3667 |
| `mediaInfoOfficialRating` | 2 | 2 | 1884, 7022 |
| `navMenuOption-selected` | 2 | 2 | 4724, 7156 |
| `nowPlayingInfoContainer` | 2 | 2 | 3123, 6191 |
| `org` | 2 | 2 | 3159, 3189 |
| `paperList` | 2 | 2 | 855, 3974 |
| `playlist` | 2 | 2 | 4541, 6169 |
| `programSecondaryTitle` | 2 | 2 | 302, 5772 |
| `queue` | 2 | 2 | 2020, 2555 |
| `reactRoot` | 2 | 2 | 4417, 6749 |
| `readOnlyContent` | 2 | 2 | 4005, 6672 |
| `recordingFields` | 2 | 2 | 4764, 4905 |
| `runtime` | 2 | 2 | 6103, 6131 |
| `sectionTitleContainer-cards` | 2 | 2 | 5099, 5164 |
| `sidebarHeader` | 2 | 2 | 4097, 7162 |
| `tagline` | 2 | 2 | 2629, 4820 |
| `upNextDialog-title` | 2 | 2 | 5220, 5254 |
| `vertical-list` | 2 | 2 | 1826, 7648 |
| `vertical-wrap` | 2 | 2 | 776, 1791 |
| `videoOsdBottom` | 2 | 2 | 3115, 6360 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3115, 6360 |
| `userPreferencesPage` | 12 | 1 | 7531–7627 |
| `checkboxContainer` | 7 | 1 | 3562–3599 |
| `itemDetailsGroup` | 7 | 1 | 4824–4910 |
| `itemProgressBar` | 6 | 1 | 2833–2867 |
| `streaming-lookup-container` | 6 | 1 | 3217–3262 |
| `trackSelectionFieldContainer` | 6 | 1 | 4783–4806 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7779–7819 |
| `innerCardFooter` | 5 | 1 | 3375–3404 |
| `chapterCardImageContainer` | 4 | 1 | 3375–3404 |
| `emby-select-withcolor` | 4 | 1 | 5448–5495 |
| `endTimeText` | 4 | 1 | 6103–6131 |
| `mainDetailButtons` | 4 | 1 | 3898–3912 |
| `overview-controls` | 4 | 1 | 3350–3362 |
| `startTimeText` | 4 | 1 | 6103–6125 |
| `button-flat` | 3 | 1 | 3096–3106 |
| `cardIndicators` | 3 | 1 | 3652–3662 |
| `cardOverlayFab-primary` | 3 | 1 | 1033–1055 |
| `com` | 3 | 1 | 3165–3183 |
| `content` | 3 | 1 | 4846–4877 |
| `discover-card` | 3 | 1 | 7830–7853 |
| `fab` | 3 | 1 | 3757–3770 |
| `listChildrenCollapsible` | 3 | 1 | 4895–4910 |
| `mdl-slider-background-flex` | 3 | 1 | 2953–2966 |
| `mediaInfoCriticRating` | 3 | 1 | 1925–1934 |
| `nextUpSection` | 3 | 1 | 4890–4910 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 6155–6165 |
| `serverInfo` | 3 | 1 | 3978–3987 |
| `transcodingProgress` | 3 | 1 | 2844–2856 |
