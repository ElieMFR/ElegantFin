# Index des composants — ElegantFin Cinema Edition v1.4.1

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.4.1.css` — 7914 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 38 | 16 | 435–446, 477–523, 761, 878, 1536–1556, 2147–2180, 2207–2211, 2488–2506, 2542, 6783, 6819–6829, 7065–7084, 7162–7184, 7214–7221, 7385, 7792 |
| `cardScalable` | 31 | 13 | 435–446, 500–523, 824–868, 894–938, 2506, 3586, 3697, 3776, 5930, 6797–6829, 6900, 7065, 7205–7221 |
| `itemDetailPage` | 21 | 13 | 1599, 1685, 1764, 1791, 2020–2056, 2091–2106, 2142, 2243, 2555, 4032–4043, 4703, 5002, 7620–7658 |
| `material-icons` | 17 | 13 | 371–390, 1755, 1853, 1906, 3543, 3702, 3776–3782, 3889, 4047, 4580, 5109, 5143–5153, 5747 |
| `cardImageContainer` | 22 | 12 | 495, 846, 874–903, 938, 995–1025, 6056–6060, 6140, 6789, 6892–6900, 6940, 7065–7084, 7205 |
| `skinHeader` | 16 | 10 | 284, 4392, 4438–4465, 5938, 6349, 6405–6413, 6479–6504, 6883, 7032, 7729 |
| `nameContainer` | 27 | 9 | 707, 2250–2273, 2314, 2343, 2378–2425, 2462, 2493–2497, 5503–5556, 7620–7658 |
| `cardBox` | 13 | 9 | 435–446, 477–489, 515, 761, 916–920, 1029, 6783, 7065, 7431 |
| `emby-button` | 12 | 9 | 633–650, 677–695, 3182, 3317–3324, 3722, 3757, 3911, 4598, 5325 |
| `js` | 10 | 9 | 318–338, 1671, 1764, 2314, 2920, 3676, 5747, 6984, 7231 |
| `card-hoverable` | 23 | 8 | 523, 834, 894–988, 6060, 6807, 6940–6975, 7065, 7431 |
| `parentName` | 23 | 8 | 707, 2255–2273, 2314, 2343, 2378–2425, 5509–5556, 5629, 7620–7658 |
| `detailLogo` | 20 | 8 | 707, 2030–2056, 2091–2106, 2133–2142, 2243–2273, 2343, 2378–2425, 2493 |
| `listItem` | 19 | 8 | 302, 650, 2510, 4500–4526, 4557–4589, 4634, 4678, 7408–7425 |
| `detailPageWrapperContainer` | 17 | 8 | 707, 1567–1577, 2056, 2216, 2250–2273, 2343, 2378–2425, 2493 |
| `subtitle` | 16 | 8 | 2020–2030, 2142, 2255, 2314, 2434–2444, 2555, 5564–5597, 7620–7658 |
| `backdropCard` | 12 | 8 | 982–988, 1103, 2020–2030, 2159, 2243, 2497–2506, 2533, 2843 |
| `nowPlayingBar` | 8 | 8 | 318, 3106, 6192, 6846, 6934, 7018, 7044, 7390 |
| `loginPage` | 16 | 7 | 3855, 5942–5973, 6013, 6041–6060, 6836, 6879, 7194–7221 |
| `navMenuOption` | 12 | 6 | 650, 746–756, 4097, 4567–4589, 4684–4689, 7107–7118 |
| `paper-icon-button-light` | 11 | 6 | 595–650, 1685, 1755, 1853, 3483–3503, 5409 |
| `verticalSection` | 11 | 6 | 1759, 2745–2750, 5002, 6892, 6984, 7231 |
| `button-link` | 10 | 6 | 650, 677–695, 3056–3065, 3126–3136, 3182, 7582 |
| `person` | 8 | 6 | 2020–2041, 2243, 2497, 2542–2551, 3984, 7615 |
| `mainDrawer` | 7 | 6 | 3070, 4061, 4438, 6836–6846, 7094, 7133 |
| `scss` | 6 | 6 | 284, 789, 1055, 3592, 4103, 6984 |
| `detailImageContainer` | 20 | 5 | 2020–2041, 2147–2211, 2243, 2484–2506, 2533–2551 |
| `osdHeader` | 15 | 5 | 1728–1746, 6344–6413, 6479–6504, 6883, 7390 |
| `actionSheetMenuItem` | 10 | 5 | 650, 4500–4511, 4557, 4634–4678, 6864 |
| `sectionTabs` | 10 | 5 | 1822, 3834, 4465, 6385–6390, 6570–6601 |
| `cardImageIcon` | 8 | 5 | 427–431, 2497–2506, 2569, 3570, 6140 |
| `headerTop` | 8 | 5 | 4392, 4438, 6355–6380, 6471–6488, 6515–6519 |
| `sectionTitle` | 7 | 5 | 1759, 1832–1839, 4293, 5079–5087, 6008 |
| `emby-scroller-container` | 6 | 5 | 1759–1764, 1802, 2735, 6892, 6984 |
| `portraitCard` | 6 | 5 | 1103, 1187, 1944–1949, 2207, 2843 |
| `appfooter` | 5 | 5 | 318, 2786, 6529, 6923, 7390 |
| `skinHeader-withBackground` | 5 | 5 | 1667, 4032, 5938, 6344, 6394 |
| `btnPlay` | 16 | 4 | 532–556, 595–650, 3786–3828, 3861–3889 |
| `cardOverlayContainer` | 12 | 4 | 956–988, 1033–1055, 1121, 7390–7408 |
| `itemName` | 11 | 4 | 707, 2314, 5509–5556, 5647–5664 |
| `backdropImage` | 10 | 4 | 2634–2662, 2689–2693, 6776, 6900–6908 |
| `emby-tab-button` | 10 | 4 | 650, 717–726, 3834, 6555–6596 |
| `upNextContainer` | 10 | 4 | 5171–5190, 5216–5242, 6836–6846, 6872 |
| `emby-scroller` | 9 | 4 | 1764, 1802–1808, 7137–7184, 7369–7385 |
| `backgroundContainer` | 8 | 4 | 2110, 2625, 2667–2685, 2717 |
| `detailRibbon` | 8 | 4 | 1624–1652, 1859, 1944–1956, 7615 |
| `listItemBodyText` | 7 | 4 | 4521–4540, 4580, 4655, 7425 |
| `skip-button` | 7 | 4 | 650, 3839, 5265–5282, 5309–5327 |
| `visualCardBox` | 7 | 4 | 435, 855–868, 894–899, 1029 |
| `button-submit` | 6 | 4 | 3855, 3943, 6041–6049, 7493–7508 |
| `cardText-secondary` | 6 | 4 | 302, 943, 3575–3579, 6962–6970 |
| `detailPagePrimaryContent` | 6 | 4 | 1639–1657, 2449, 4996, 7048 |
| `squareCard` | 6 | 4 | 878, 2497, 2533–2551, 6017–6021 |
| `semiTransparent` | 5 | 4 | 1667, 5938, 6373–6394, 6430 |
| `skinHeader-blurred` | 5 | 4 | 5938, 6373–6380, 7032, 7390 |
| `itemsContainer` | 4 | 4 | 761, 1791, 1826, 5002 |
| `raised` | 4 | 4 | 650, 736, 3722, 3757 |
| `x` | 4 | 4 | 2314, 4103, 5612, 6984 |
| `detailButton` | 13 | 3 | 595–650, 3767–3828, 3885–3889 |
| `itemSelectionPanel` | 9 | 3 | 907–911, 3515, 3543–3586 |
| `pageTitle` | 8 | 3 | 1703–1746, 6405, 6504 |
| `sectionTitleTextButton` | 8 | 3 | 5062–5070, 5097–5109, 5143–5153 |
| `homePage` | 7 | 3 | 4392, 4438–4465, 6618 |
| `playedIndicator` | 7 | 3 | 789–803, 3659, 7065–7089 |
| `check` | 6 | 3 | 3543, 3776, 4634–4678 |
| `detailSectionContent` | 6 | 3 | 3349, 4785–4795, 4875–4885 |
| `emby-checkbox` | 6 | 3 | 3520, 3557–3561, 3610–3622 |
| `actionSheetContent` | 5 | 3 | 4626–4630, 6836–6846, 6872 |
| `cardText-first` | 5 | 3 | 943, 3549–3575, 6121 |
| `dialog` | 5 | 3 | 3399–3409, 6836–6846, 6872 |
| `guideProgramName` | 5 | 3 | 650, 5688–5699, 5742–5747 |
| `noHomeButtonHeader` | 5 | 3 | 1685, 6405, 6555–6563 |
| `overflowBackdropCard` | 5 | 3 | 982–988, 3553, 6116–6121 |
| `secondary` | 5 | 3 | 302, 4530–4540, 4580 |
| `album` | 4 | 3 | 2243, 2502–2506, 2542 |
| `cardPadder` | 4 | 3 | 431, 1029, 3566–3570 |
| `cardText` | 4 | 3 | 943–953, 3575, 7210 |
| `detailPageContent` | 4 | 3 | 1781, 4716, 4989–4996 |
| `dialog-fullscreen` | 4 | 3 | 3409, 6836–6846, 6872 |
| `emby-scrollbuttons` | 4 | 3 | 1844–1849, 7231, 7767 |
| `folder` | 4 | 3 | 1944–1949, 3676, 3740 |
| `formDialogFooter` | 4 | 3 | 3467, 3950, 7442–7466 |
| `infoWrapper` | 4 | 3 | 2186–2191, 2449, 2477 |
| `listItemImage` | 4 | 3 | 2820–2825, 4494, 7425 |
| `musicParentName` | 4 | 3 | 2020, 2555, 5629–5638 |
| `programGuideSection` | 4 | 3 | 2510–2525, 4885, 4912 |
| `toast` | 4 | 3 | 5163, 6836–6846, 6872 |
| `cardFooter` | 3 | 3 | 3586, 6940, 6975 |
| `collectionItems` | 3 | 3 | 1791, 4885, 4921 |
| `defaultCardBackground` | 3 | 3 | 3697, 6136, 6235 |
| `detailPageSecondaryContainer` | 3 | 3 | 1634, 1661, 1781 |
| `emby-input` | 3 | 3 | 5423, 5452, 7508 |
| `formDialogFooterItem` | 3 | 3 | 3467, 3735, 3861 |
| `formDialogHeader` | 3 | 3 | 3950, 7390, 7442 |
| `iconOsd` | 3 | 3 | 5916, 7390, 7442 |
| `live_tv` | 3 | 3 | 2020, 2542, 3984 |
| `myPreferencesMenuPage` | 3 | 3 | 404, 4694, 5010 |
| `page` | 3 | 3 | 1025, 2717, 6892 |
| `playerStats` | 3 | 3 | 5916, 7442, 7478 |
| `sectionTitle-cards` | 3 | 3 | 1759, 5079, 5139 |
| `sectionTitleContainer` | 3 | 3 | 1791, 1849, 4921 |
| `tsx` | 3 | 3 | 1103, 4392, 4469 |
| `itemExternalLinks` | 13 | 2 | 3119–3197, 3349 |
| `checkboxOutline` | 10 | 2 | 3520–3561, 3592–3622 |
| `itemBackdrop` | 9 | 2 | 1986–2041, 2216 |
| `mdl-slider` | 9 | 2 | 2916, 2971–3029 |
| `listItemIcon` | 8 | 2 | 3980–3984, 4634–4694 |
| `sliderContainer` | 8 | 2 | 2920, 2948–3013 |
| `cardOverlayButton-br` | 7 | 2 | 1041, 1070–1114 |
| `detail-clamp-text` | 7 | 2 | 3285–3311, 3337–3341 |
| `divUsers` | 7 | 2 | 6017–6021, 7194–7221 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3557–3561, 3591–3610 |
| `countIndicator` | 6 | 2 | 780–810, 7442–7466 |
| `detailPagePrimaryContainer` | 6 | 2 | 1611–1657, 2449 |
| `detailsGroupItem` | 6 | 2 | 4747, 4815–4852 |
| `headerButton` | 6 | 2 | 570–650, 6497 |
| `headerLeft` | 6 | 2 | 1709–1746, 6705 |
| `selectionCommandsPanel` | 6 | 2 | 3477–3511, 7390 |
| `trackSelections` | 6 | 2 | 4720–4747, 4880–4885 |
| `withBackdrop` | 6 | 2 | 2625, 2667–2685 |
| `detailSection` | 5 | 2 | 4703–4712, 4865–4885 |
| `fullSyncIndicator` | 5 | 2 | 780–803, 7442–7466 |
| `mainDrawer-scrollContainer` | 5 | 2 | 3079, 7107–7124 |
| `mediaInfoItem` | 5 | 2 | 1863–1906, 6984 |
| `overview-expand` | 5 | 2 | 3317–3341, 4785 |
| `scrollX` | 5 | 2 | 1764, 1802–1822 |
| `videoIndicator` | 5 | 2 | 3665–3693, 7442 |
| `withSectionTabs` | 5 | 2 | 2676–2693, 6380 |
| `alphaPickerButton` | 4 | 2 | 650, 4936–4948 |
| `backgroundProgress` | 4 | 2 | 2831–2843, 2873 |
| `emby-select` | 4 | 2 | 5423–5435, 7508 |
| `emby-tab-button-active` | 4 | 2 | 3922, 6587–6601 |
| `mediaSourceIndicator` | 4 | 2 | 780–803, 7442 |
| `play_arrow` | 4 | 2 | 3702–3718, 3889 |
| `playbackProgress` | 4 | 2 | 2831–2843, 2878 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4521–4526, 6229–6235 |
| `programCell` | 4 | 2 | 5679, 5738–5747 |
| `section0` | 4 | 2 | 995–1025, 6892 |
| `visualLoginForm` | 4 | 2 | 6008–6025, 6066 |
| `cardOverlayButtonIcon` | 3 | 2 | 1041–1053, 1114 |
| `castCollapsible` | 3 | 2 | 846, 3561–3570 |
| `emby-scrollbuttons-button` | 3 | 2 | 1853, 7774–7781 |
| `emby-textarea` | 3 | 2 | 5414–5423, 5452 |
| `guestCastContent` | 3 | 2 | 846, 3561–3570 |
| `guide-channelHeaderCell` | 3 | 2 | 650, 5713–5729 |
| `guide-date-tab-button` | 3 | 2 | 650, 3922–3930 |
| `headerUserButton` | 3 | 2 | 570–583, 5014 |
| `manualLoginForm` | 3 | 2 | 6008–6025, 6066 |
| `overview` | 3 | 2 | 3337–3341, 4795 |
| `add` | 2 | 2 | 1764, 6984 |
| `alphaPicker-fixed-right` | 2 | 2 | 2717, 4948 |
| `backdropImageFadeIn` | 2 | 2 | 2770, 7482 |
| `book` | 2 | 2 | 2020, 2542 |
| `btnDeleteImage` | 2 | 2 | 3722, 3936 |
| `cardContent` | 2 | 2 | 846, 878 |
| `cardOverlayButton` | 2 | 2 | 1055, 1091 |
| `cardOverlayButton-hover` | 2 | 2 | 938, 1070 |
| `chevron_right` | 2 | 2 | 5109, 5153 |
| `classList` | 2 | 2 | 1764, 6984 |
| `collapseContent` | 2 | 2 | 3472, 3948 |
| `collectionItemsContainer` | 2 | 2 | 1791, 4925 |
| `content-primary` | 2 | 2 | 4989, 5045 |
| `editorsChoiceItemOverview` | 2 | 2 | 7704, 7785 |
| `endsAt` | 2 | 2 | 1884, 6984 |
| `fieldDescription` | 2 | 2 | 302, 7508 |
| `formDialogFooter-clear` | 2 | 2 | 3467, 3950 |
| `guide-programNameCaret` | 2 | 2 | 302, 5695 |
| `headroom` | 2 | 2 | 6368, 6405 |
| `indicator` | 2 | 2 | 810, 3654 |
| `mediaInfoOfficialRating` | 2 | 2 | 1884, 6984 |
| `navMenuOption-selected` | 2 | 2 | 4699, 7118 |
| `nowPlayingInfoContainer` | 2 | 2 | 3110, 6166 |
| `org` | 2 | 2 | 3146, 3176 |
| `paperList` | 2 | 2 | 855, 3961 |
| `playlist` | 2 | 2 | 4516, 6144 |
| `programSecondaryTitle` | 2 | 2 | 302, 5747 |
| `queue` | 2 | 2 | 2020, 2542 |
| `reactRoot` | 2 | 2 | 4392, 6711 |
| `readOnlyContent` | 2 | 2 | 3992, 6634 |
| `recordingFields` | 2 | 2 | 4739, 4880 |
| `runtime` | 2 | 2 | 6078, 6106 |
| `sectionTitleContainer-cards` | 2 | 2 | 5074, 5139 |
| `sidebarHeader` | 2 | 2 | 4084, 7124 |
| `tagline` | 2 | 2 | 2616, 4795 |
| `upNextDialog-title` | 2 | 2 | 5195, 5229 |
| `vertical-list` | 2 | 2 | 1826, 7610 |
| `vertical-wrap` | 2 | 2 | 776, 1791 |
| `videoOsdBottom` | 2 | 2 | 3102, 6335 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3102, 6335 |
| `userPreferencesPage` | 12 | 1 | 7493–7589 |
| `checkboxContainer` | 7 | 1 | 3549–3586 |
| `itemDetailsGroup` | 7 | 1 | 4799–4885 |
| `itemProgressBar` | 6 | 1 | 2820–2854 |
| `streaming-lookup-container` | 6 | 1 | 3204–3249 |
| `trackSelectionFieldContainer` | 6 | 1 | 4758–4781 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7741–7781 |
| `innerCardFooter` | 5 | 1 | 3362–3391 |
| `chapterCardImageContainer` | 4 | 1 | 3362–3391 |
| `emby-select-withcolor` | 4 | 1 | 5423–5470 |
| `endTimeText` | 4 | 1 | 6078–6106 |
| `mainDetailButtons` | 4 | 1 | 3885–3899 |
| `overview-controls` | 4 | 1 | 3337–3349 |
| `startTimeText` | 4 | 1 | 6078–6100 |
| `button-flat` | 3 | 1 | 3083–3093 |
| `cardIndicators` | 3 | 1 | 3639–3649 |
| `cardOverlayFab-primary` | 3 | 1 | 1033–1055 |
| `com` | 3 | 1 | 3152–3170 |
| `content` | 3 | 1 | 4821–4852 |
| `discover-card` | 3 | 1 | 7792–7815 |
| `fab` | 3 | 1 | 3744–3757 |
| `listChildrenCollapsible` | 3 | 1 | 4870–4885 |
| `mdl-slider-background-flex` | 3 | 1 | 2940–2953 |
| `mediaInfoCriticRating` | 3 | 1 | 1925–1934 |
| `nextUpSection` | 3 | 1 | 4865–4885 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 6130–6140 |
| `serverInfo` | 3 | 1 | 3965–3974 |
| `transcodingProgress` | 3 | 1 | 2831–2843 |
