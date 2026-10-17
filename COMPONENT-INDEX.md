# Index des composants — ElegantFin Cinema Edition v1.4.2

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.4.2.css` — 7940 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 38 | 16 | 435–446, 477–523, 761, 878, 1536–1556, 2160–2193, 2220–2224, 2501–2519, 2555, 6809, 6845–6855, 7091–7110, 7188–7210, 7240–7247, 7411, 7818 |
| `cardScalable` | 31 | 13 | 435–446, 500–523, 824–868, 894–938, 2519, 3599, 3710, 3789, 5943, 6823–6855, 6926, 7091, 7231–7247 |
| `itemDetailPage` | 22 | 13 | 1599, 1685, 1764, 1791, 2020–2056, 2091–2106, 2142–2146, 2256, 2568, 4045–4056, 4716, 5015, 7646–7684 |
| `material-icons` | 17 | 13 | 371–390, 1755, 1853, 1906, 3556, 3715, 3789–3795, 3902, 4060, 4593, 5122, 5156–5166, 5760 |
| `cardImageContainer` | 22 | 12 | 495, 846, 874–903, 938, 995–1025, 6069–6073, 6153, 6815, 6918–6926, 6966, 7091–7110, 7231 |
| `skinHeader` | 16 | 10 | 284, 4405, 4451–4478, 5951, 6362, 6418–6426, 6492–6517, 6909, 7058, 7755 |
| `nameContainer` | 27 | 9 | 707, 2263–2286, 2327, 2356, 2391–2438, 2475, 2506–2510, 5516–5569, 7646–7684 |
| `cardBox` | 13 | 9 | 435–446, 477–489, 515, 761, 916–920, 1029, 6809, 7091, 7457 |
| `emby-button` | 12 | 9 | 633–650, 677–695, 3195, 3330–3337, 3735, 3770, 3924, 4611, 5338 |
| `js` | 10 | 9 | 318–338, 1671, 1764, 2327, 2933, 3689, 5760, 7010, 7257 |
| `card-hoverable` | 23 | 8 | 523, 834, 894–988, 6073, 6833, 6966–7001, 7091, 7457 |
| `parentName` | 23 | 8 | 707, 2268–2286, 2327, 2356, 2391–2438, 5522–5569, 5642, 7646–7684 |
| `detailLogo` | 21 | 8 | 707, 2030–2056, 2091–2106, 2133–2146, 2256–2286, 2356, 2391–2438, 2506 |
| `listItem` | 19 | 8 | 302, 650, 2523, 4513–4539, 4570–4602, 4647, 4691, 7434–7451 |
| `detailPageWrapperContainer` | 17 | 8 | 707, 1567–1577, 2056, 2229, 2263–2286, 2356, 2391–2438, 2506 |
| `subtitle` | 17 | 8 | 2020–2030, 2142–2146, 2268, 2327, 2447–2457, 2568, 5577–5610, 7646–7684 |
| `backdropCard` | 12 | 8 | 982–988, 1103, 2020–2030, 2172, 2256, 2510–2519, 2546, 2856 |
| `nowPlayingBar` | 8 | 8 | 318, 3119, 6205, 6872, 6960, 7044, 7070, 7416 |
| `loginPage` | 16 | 7 | 3868, 5955–5986, 6026, 6054–6073, 6862, 6905, 7220–7247 |
| `navMenuOption` | 12 | 6 | 650, 746–756, 4110, 4580–4602, 4697–4702, 7133–7144 |
| `paper-icon-button-light` | 11 | 6 | 595–650, 1685, 1755, 1853, 3496–3516, 5422 |
| `verticalSection` | 11 | 6 | 1759, 2758–2763, 5015, 6918, 7010, 7257 |
| `button-link` | 10 | 6 | 650, 677–695, 3069–3078, 3139–3149, 3195, 7608 |
| `headerTop` | 9 | 6 | 2146, 4405, 4451, 6368–6393, 6484–6501, 6528–6532 |
| `person` | 8 | 6 | 2020–2041, 2256, 2510, 2555–2564, 3997, 7641 |
| `mainDrawer` | 7 | 6 | 3083, 4074, 4451, 6862–6872, 7120, 7159 |
| `scss` | 6 | 6 | 284, 789, 1055, 3605, 4116, 7010 |
| `detailImageContainer` | 20 | 5 | 2020–2041, 2160–2224, 2256, 2497–2519, 2546–2564 |
| `osdHeader` | 15 | 5 | 1728–1746, 6357–6426, 6492–6517, 6909, 7416 |
| `sectionTabs` | 11 | 5 | 1822, 3847, 4478, 6398–6403, 6583–6627 |
| `actionSheetMenuItem` | 10 | 5 | 650, 4513–4524, 4570, 4647–4691, 6890 |
| `emby-tab-button` | 10 | 5 | 650, 717–726, 3847, 6568–6576, 6605–6622 |
| `cardImageIcon` | 8 | 5 | 427–431, 2510–2519, 2582, 3583, 6153 |
| `sectionTitle` | 7 | 5 | 1759, 1832–1839, 4306, 5092–5100, 6021 |
| `emby-scroller-container` | 6 | 5 | 1759–1764, 1802, 2748, 6918, 7010 |
| `portraitCard` | 6 | 5 | 1103, 1187, 1944–1949, 2220, 2856 |
| `appfooter` | 5 | 5 | 318, 2799, 6542, 6949, 7416 |
| `skinHeader-withBackground` | 5 | 5 | 1667, 4045, 5951, 6357, 6407 |
| `btnPlay` | 16 | 4 | 532–556, 595–650, 3799–3841, 3874–3902 |
| `cardOverlayContainer` | 12 | 4 | 956–988, 1033–1055, 1121, 7416–7434 |
| `itemName` | 11 | 4 | 707, 2327, 5522–5569, 5660–5677 |
| `backdropImage` | 10 | 4 | 2647–2675, 2702–2706, 6802, 6926–6934 |
| `upNextContainer` | 10 | 4 | 5184–5203, 5229–5255, 6862–6872, 6898 |
| `emby-scroller` | 9 | 4 | 1764, 1802–1808, 7163–7210, 7395–7411 |
| `backgroundContainer` | 8 | 4 | 2110, 2638, 2680–2698, 2730 |
| `detailRibbon` | 8 | 4 | 1624–1652, 1859, 1944–1956, 7641 |
| `listItemBodyText` | 7 | 4 | 4534–4553, 4593, 4668, 7451 |
| `skip-button` | 7 | 4 | 650, 3852, 5278–5295, 5322–5340 |
| `visualCardBox` | 7 | 4 | 435, 855–868, 894–899, 1029 |
| `button-submit` | 6 | 4 | 3868, 3956, 6054–6062, 7519–7534 |
| `cardText-secondary` | 6 | 4 | 302, 943, 3588–3592, 6988–6996 |
| `detailPagePrimaryContent` | 6 | 4 | 1639–1657, 2462, 5009, 7074 |
| `squareCard` | 6 | 4 | 878, 2510, 2546–2564, 6030–6034 |
| `semiTransparent` | 5 | 4 | 1667, 5951, 6386–6407, 6443 |
| `skinHeader-blurred` | 5 | 4 | 5951, 6386–6393, 7058, 7416 |
| `itemsContainer` | 4 | 4 | 761, 1791, 1826, 5015 |
| `raised` | 4 | 4 | 650, 736, 3735, 3770 |
| `x` | 4 | 4 | 2327, 4116, 5625, 7010 |
| `detailButton` | 13 | 3 | 595–650, 3780–3841, 3898–3902 |
| `itemSelectionPanel` | 9 | 3 | 907–911, 3528, 3556–3599 |
| `pageTitle` | 8 | 3 | 1703–1746, 6418, 6517 |
| `sectionTitleTextButton` | 8 | 3 | 5075–5083, 5110–5122, 5156–5166 |
| `homePage` | 7 | 3 | 4405, 4451–4478, 6644 |
| `playedIndicator` | 7 | 3 | 789–803, 3672, 7091–7115 |
| `check` | 6 | 3 | 3556, 3789, 4647–4691 |
| `detailSectionContent` | 6 | 3 | 3362, 4798–4808, 4888–4898 |
| `emby-checkbox` | 6 | 3 | 3533, 3570–3574, 3623–3635 |
| `actionSheetContent` | 5 | 3 | 4639–4643, 6862–6872, 6898 |
| `cardText-first` | 5 | 3 | 943, 3562–3588, 6134 |
| `dialog` | 5 | 3 | 3412–3422, 6862–6872, 6898 |
| `guideProgramName` | 5 | 3 | 650, 5701–5712, 5755–5760 |
| `noHomeButtonHeader` | 5 | 3 | 1685, 6418, 6568–6576 |
| `overflowBackdropCard` | 5 | 3 | 982–988, 3566, 6129–6134 |
| `secondary` | 5 | 3 | 302, 4543–4553, 4593 |
| `album` | 4 | 3 | 2256, 2515–2519, 2555 |
| `cardPadder` | 4 | 3 | 431, 1029, 3579–3583 |
| `cardText` | 4 | 3 | 943–953, 3588, 7236 |
| `detailPageContent` | 4 | 3 | 1781, 4729, 5002–5009 |
| `dialog-fullscreen` | 4 | 3 | 3422, 6862–6872, 6898 |
| `emby-scrollbuttons` | 4 | 3 | 1844–1849, 7257, 7793 |
| `folder` | 4 | 3 | 1944–1949, 3689, 3753 |
| `formDialogFooter` | 4 | 3 | 3480, 3963, 7468–7492 |
| `infoWrapper` | 4 | 3 | 2199–2204, 2462, 2490 |
| `listItemImage` | 4 | 3 | 2833–2838, 4507, 7451 |
| `musicParentName` | 4 | 3 | 2020, 2568, 5642–5651 |
| `programGuideSection` | 4 | 3 | 2523–2538, 4898, 4925 |
| `toast` | 4 | 3 | 5176, 6862–6872, 6898 |
| `cardFooter` | 3 | 3 | 3599, 6966, 7001 |
| `collectionItems` | 3 | 3 | 1791, 4898, 4934 |
| `defaultCardBackground` | 3 | 3 | 3710, 6149, 6248 |
| `detailPageSecondaryContainer` | 3 | 3 | 1634, 1661, 1781 |
| `emby-input` | 3 | 3 | 5436, 5465, 7534 |
| `formDialogFooterItem` | 3 | 3 | 3480, 3748, 3874 |
| `formDialogHeader` | 3 | 3 | 3963, 7416, 7468 |
| `iconOsd` | 3 | 3 | 5929, 7416, 7468 |
| `live_tv` | 3 | 3 | 2020, 2555, 3997 |
| `myPreferencesMenuPage` | 3 | 3 | 404, 4707, 5023 |
| `page` | 3 | 3 | 1025, 2730, 6918 |
| `playerStats` | 3 | 3 | 5929, 7468, 7504 |
| `sectionTitle-cards` | 3 | 3 | 1759, 5092, 5152 |
| `sectionTitleContainer` | 3 | 3 | 1791, 1849, 4934 |
| `tsx` | 3 | 3 | 1103, 4405, 4482 |
| `itemExternalLinks` | 13 | 2 | 3132–3210, 3362 |
| `checkboxOutline` | 10 | 2 | 3533–3574, 3605–3635 |
| `itemBackdrop` | 9 | 2 | 1986–2041, 2229 |
| `mdl-slider` | 9 | 2 | 2929, 2984–3042 |
| `listItemIcon` | 8 | 2 | 3993–3997, 4647–4707 |
| `sliderContainer` | 8 | 2 | 2933, 2961–3026 |
| `cardOverlayButton-br` | 7 | 2 | 1041, 1070–1114 |
| `detail-clamp-text` | 7 | 2 | 3298–3324, 3350–3354 |
| `divUsers` | 7 | 2 | 6030–6034, 7220–7247 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3570–3574, 3604–3623 |
| `countIndicator` | 6 | 2 | 780–810, 7468–7492 |
| `detailPagePrimaryContainer` | 6 | 2 | 1611–1657, 2462 |
| `detailsGroupItem` | 6 | 2 | 4760, 4828–4865 |
| `headerButton` | 6 | 2 | 570–650, 6510 |
| `headerLeft` | 6 | 2 | 1709–1746, 6731 |
| `selectionCommandsPanel` | 6 | 2 | 3490–3524, 7416 |
| `trackSelections` | 6 | 2 | 4733–4760, 4893–4898 |
| `withBackdrop` | 6 | 2 | 2638, 2680–2698 |
| `detailSection` | 5 | 2 | 4716–4725, 4878–4898 |
| `fullSyncIndicator` | 5 | 2 | 780–803, 7468–7492 |
| `mainDrawer-scrollContainer` | 5 | 2 | 3092, 7133–7150 |
| `mediaInfoItem` | 5 | 2 | 1863–1906, 7010 |
| `overview-expand` | 5 | 2 | 3330–3354, 4798 |
| `scrollX` | 5 | 2 | 1764, 1802–1822 |
| `videoIndicator` | 5 | 2 | 3678–3706, 7468 |
| `withSectionTabs` | 5 | 2 | 2689–2706, 6393 |
| `alphaPickerButton` | 4 | 2 | 650, 4949–4961 |
| `backgroundProgress` | 4 | 2 | 2844–2856, 2886 |
| `emby-select` | 4 | 2 | 5436–5448, 7534 |
| `emby-tab-button-active` | 4 | 2 | 3935, 6613–6627 |
| `mediaSourceIndicator` | 4 | 2 | 780–803, 7468 |
| `play_arrow` | 4 | 2 | 3715–3731, 3902 |
| `playbackProgress` | 4 | 2 | 2844–2856, 2891 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4534–4539, 6242–6248 |
| `programCell` | 4 | 2 | 5692, 5751–5760 |
| `section0` | 4 | 2 | 995–1025, 6918 |
| `visualLoginForm` | 4 | 2 | 6021–6038, 6079 |
| `cardOverlayButtonIcon` | 3 | 2 | 1041–1053, 1114 |
| `castCollapsible` | 3 | 2 | 846, 3574–3583 |
| `emby-scrollbuttons-button` | 3 | 2 | 1853, 7800–7807 |
| `emby-textarea` | 3 | 2 | 5427–5436, 5465 |
| `guestCastContent` | 3 | 2 | 846, 3574–3583 |
| `guide-channelHeaderCell` | 3 | 2 | 650, 5726–5742 |
| `guide-date-tab-button` | 3 | 2 | 650, 3935–3943 |
| `headerUserButton` | 3 | 2 | 570–583, 5027 |
| `manualLoginForm` | 3 | 2 | 6021–6038, 6079 |
| `overview` | 3 | 2 | 3350–3354, 4808 |
| `add` | 2 | 2 | 1764, 7010 |
| `alphaPicker-fixed-right` | 2 | 2 | 2730, 4961 |
| `backdropImageFadeIn` | 2 | 2 | 2783, 7508 |
| `book` | 2 | 2 | 2020, 2555 |
| `btnDeleteImage` | 2 | 2 | 3735, 3949 |
| `cardContent` | 2 | 2 | 846, 878 |
| `cardOverlayButton` | 2 | 2 | 1055, 1091 |
| `cardOverlayButton-hover` | 2 | 2 | 938, 1070 |
| `chevron_right` | 2 | 2 | 5122, 5166 |
| `classList` | 2 | 2 | 1764, 7010 |
| `collapseContent` | 2 | 2 | 3485, 3961 |
| `collectionItemsContainer` | 2 | 2 | 1791, 4938 |
| `content-primary` | 2 | 2 | 5002, 5058 |
| `editorsChoiceItemOverview` | 2 | 2 | 7730, 7811 |
| `endsAt` | 2 | 2 | 1884, 7010 |
| `fieldDescription` | 2 | 2 | 302, 7534 |
| `formDialogFooter-clear` | 2 | 2 | 3480, 3963 |
| `guide-programNameCaret` | 2 | 2 | 302, 5708 |
| `headroom` | 2 | 2 | 6381, 6418 |
| `indicator` | 2 | 2 | 810, 3667 |
| `mediaInfoOfficialRating` | 2 | 2 | 1884, 7010 |
| `navMenuOption-selected` | 2 | 2 | 4712, 7144 |
| `nowPlayingInfoContainer` | 2 | 2 | 3123, 6179 |
| `org` | 2 | 2 | 3159, 3189 |
| `paperList` | 2 | 2 | 855, 3974 |
| `playlist` | 2 | 2 | 4529, 6157 |
| `programSecondaryTitle` | 2 | 2 | 302, 5760 |
| `queue` | 2 | 2 | 2020, 2555 |
| `reactRoot` | 2 | 2 | 4405, 6737 |
| `readOnlyContent` | 2 | 2 | 4005, 6660 |
| `recordingFields` | 2 | 2 | 4752, 4893 |
| `runtime` | 2 | 2 | 6091, 6119 |
| `sectionTitleContainer-cards` | 2 | 2 | 5087, 5152 |
| `sidebarHeader` | 2 | 2 | 4097, 7150 |
| `tagline` | 2 | 2 | 2629, 4808 |
| `upNextDialog-title` | 2 | 2 | 5208, 5242 |
| `vertical-list` | 2 | 2 | 1826, 7636 |
| `vertical-wrap` | 2 | 2 | 776, 1791 |
| `videoOsdBottom` | 2 | 2 | 3115, 6348 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3115, 6348 |
| `userPreferencesPage` | 12 | 1 | 7519–7615 |
| `checkboxContainer` | 7 | 1 | 3562–3599 |
| `itemDetailsGroup` | 7 | 1 | 4812–4898 |
| `itemProgressBar` | 6 | 1 | 2833–2867 |
| `streaming-lookup-container` | 6 | 1 | 3217–3262 |
| `trackSelectionFieldContainer` | 6 | 1 | 4771–4794 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7767–7807 |
| `innerCardFooter` | 5 | 1 | 3375–3404 |
| `chapterCardImageContainer` | 4 | 1 | 3375–3404 |
| `emby-select-withcolor` | 4 | 1 | 5436–5483 |
| `endTimeText` | 4 | 1 | 6091–6119 |
| `mainDetailButtons` | 4 | 1 | 3898–3912 |
| `overview-controls` | 4 | 1 | 3350–3362 |
| `startTimeText` | 4 | 1 | 6091–6113 |
| `button-flat` | 3 | 1 | 3096–3106 |
| `cardIndicators` | 3 | 1 | 3652–3662 |
| `cardOverlayFab-primary` | 3 | 1 | 1033–1055 |
| `com` | 3 | 1 | 3165–3183 |
| `content` | 3 | 1 | 4834–4865 |
| `discover-card` | 3 | 1 | 7818–7841 |
| `fab` | 3 | 1 | 3757–3770 |
| `listChildrenCollapsible` | 3 | 1 | 4883–4898 |
| `mdl-slider-background-flex` | 3 | 1 | 2953–2966 |
| `mediaInfoCriticRating` | 3 | 1 | 1925–1934 |
| `nextUpSection` | 3 | 1 | 4878–4898 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 6143–6153 |
| `serverInfo` | 3 | 1 | 3978–3987 |
| `transcodingProgress` | 3 | 1 | 2844–2856 |
