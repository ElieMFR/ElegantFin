# Index des composants — ElegantFin Cinema Edition v1.3.7

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.7.css` — 7286 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 36 | 14 | 416–498, 736, 839, 1485–1505, 2027–2060, 2087–2091, 2367–2385, 2421, 6237, 6518–6534, 6612–6634, 6664–6671, 6754, 7164 |
| `cardScalable` | 28 | 13 | 416–427, 475–498, 785–829, 855–893, 2385, 3322, 3433, 3512, 5446, 6251–6261, 6330, 6518, 6655–6671 |
| `cardImageContainer` | 23 | 13 | 470, 807, 835–864, 893, 950–980, 5555–5559, 5639, 6243, 6322–6330, 6381, 6518–6534, 6655, 6802 |
| `material-icons` | 17 | 13 | 352–371, 1704, 1782, 1834, 3279, 3438, 3512–3518, 3624, 3782, 4164, 4648, 4682–4692, 5264 |
| `itemDetailPage` | 18 | 11 | 1548, 1634, 1713, 1953–1978, 2022, 2123, 2434–2439, 3767–3778, 4258, 4545, 6992–7030 |
| `nameContainer` | 27 | 9 | 682, 2130–2153, 2194, 2223, 2258–2304, 2341, 2372–2376, 5021–5073, 6992–7030 |
| `skinHeader` | 16 | 9 | 280, 3997–4049, 5454, 5848, 5904–5912, 5938–5963, 6313, 6485, 7101 |
| `backdropCard` | 12 | 9 | 937–943, 1058, 1953, 2039, 2123, 2376–2385, 2412, 2439, 2703 |
| `js` | 9 | 9 | 319, 1620, 1713, 2194, 2780, 3412, 5264, 6437, 6681 |
| `card-hoverable` | 23 | 8 | 498, 795, 855–943, 5559, 6261, 6409–6428, 6518, 6809 |
| `parentName` | 23 | 8 | 682, 2135–2153, 2194, 2223, 2258–2304, 5027–5073, 5146, 6992–7030 |
| `detailPageWrapperContainer` | 17 | 8 | 682, 1516–1526, 1978, 2096, 2130–2153, 2223, 2258–2304, 2372 |
| `subtitle` | 16 | 8 | 1953, 2022, 2135, 2194, 2313–2323, 2434–2439, 5081–5114, 6992–7030 |
| `cardBox` | 12 | 8 | 416–464, 490, 736, 877, 984, 6237, 6518, 6809 |
| `detailLogo` | 17 | 7 | 682, 1967–1978, 2013–2022, 2123–2153, 2223, 2258–2304, 2372 |
| `loginPage` | 15 | 7 | 3591, 5458–5473, 5512, 5540–5559, 6266, 6309, 6644–6671 |
| `emby-button` | 10 | 7 | 608–625, 652–670, 3081–3088, 3458, 3493, 3646, 4182 |
| `nowPlayingBar` | 7 | 7 | 2966, 5691, 6276, 6364, 6471, 6497, 6759 |
| `listItem` | 17 | 6 | 298, 625, 2389, 4084–4110, 4141–4173, 6777–6794 |
| `navMenuOption` | 12 | 6 | 625, 721–731, 3832, 4151–4173, 4239–4244, 6557–6568 |
| `verticalSection` | 11 | 6 | 1708, 2604–2609, 4545, 6322, 6437, 6681 |
| `person` | 8 | 6 | 1953–1963, 2123, 2376, 2421–2430, 3719, 6987 |
| `mainDrawer` | 7 | 6 | 2930, 3796, 4022, 6266–6276, 6544, 6583 |
| `detailImageContainer` | 20 | 5 | 1953–1963, 2027–2091, 2123, 2363–2385, 2412–2439 |
| `osdHeader` | 15 | 5 | 1677–1695, 5843–5912, 5938–5963, 6313, 6759 |
| `actionSheetMenuItem` | 11 | 5 | 625, 4084–4095, 4141, 4219–4235, 6294 |
| `sectionTabs` | 10 | 5 | 1751, 3570, 4049, 5884–5889, 6029–6055 |
| `button-link` | 9 | 5 | 625, 652–670, 2916–2925, 2986–2996, 6955 |
| `cardImageIcon` | 8 | 5 | 408–412, 2376–2385, 2445, 3306, 5639 |
| `paper-icon-button-light` | 8 | 5 | 570–625, 1634, 1704, 1782, 4940 |
| `sectionTitle` | 7 | 5 | 1708, 1761–1768, 3898, 4618–4626, 5507 |
| `emby-scroller-container` | 6 | 5 | 1708–1713, 1740, 2594, 6322, 6437 |
| `portraitCard` | 5 | 5 | 1058, 1136, 1872, 2087, 2703 |
| `scss` | 5 | 5 | 280, 764, 1010, 3328, 6437 |
| `skinHeader-withBackground` | 5 | 5 | 1616, 3767, 5454, 5843, 5893 |
| `btnPlay` | 16 | 4 | 507–531, 570–625, 3522–3564, 3597–3624 |
| `cardOverlayContainer` | 12 | 4 | 911–943, 988–1010, 1070, 6759–6777 |
| `itemName` | 11 | 4 | 682, 2194, 5027–5073, 5164–5181 |
| `backdropImage` | 10 | 4 | 2510–2537, 2564–2568, 6230, 6330–6338 |
| `emby-tab-button` | 10 | 4 | 625, 692–701, 3570, 6014–6050 |
| `upNextContainer` | 10 | 4 | 4710–4729, 4755–4781, 6266–6276, 6302 |
| `emby-scroller` | 9 | 4 | 1713, 1740–1746, 6587–6634, 6745–6754 |
| `headerTop` | 8 | 4 | 3997–4022, 5854–5879, 5930–5947, 5974–5978 |
| `detailRibbon` | 7 | 4 | 1573–1601, 1787, 1872–1877, 6987 |
| `listItemBodyText` | 7 | 4 | 4105–4124, 4164, 4223, 6794 |
| `visualCardBox` | 7 | 4 | 416, 816–829, 855–860, 984 |
| `button-submit` | 6 | 4 | 3591, 3678, 5540–5548, 6867–6881 |
| `cardText-secondary` | 6 | 4 | 298, 898, 3311–3315, 6415–6423 |
| `detailPagePrimaryContent` | 6 | 4 | 1588–1606, 2328, 4539, 6501 |
| `skip-button` | 6 | 4 | 625, 3575, 4804–4821, 4848–4854 |
| `squareCard` | 6 | 4 | 839, 2376, 2412–2430, 5516–5520 |
| `skinHeader-blurred` | 5 | 4 | 5454, 5872–5879, 6485, 6759 |
| `appfooter` | 4 | 4 | 2646, 5988, 6353, 6759 |
| `raised` | 4 | 4 | 625, 711, 3458, 3493 |
| `detailButton` | 13 | 3 | 570–625, 3503–3564, 3620–3624 |
| `itemBackdrop` | 9 | 3 | 1919–1963, 2096, 2439 |
| `itemSelectionPanel` | 9 | 3 | 868–872, 3251, 3279–3322 |
| `check` | 8 | 3 | 3279, 3512, 4215–4235 |
| `pageTitle` | 8 | 3 | 1652–1695, 5904, 5963 |
| `sectionTitleTextButton` | 8 | 3 | 4601–4609, 4636–4648, 4682–4692 |
| `playedIndicator` | 7 | 3 | 764–778, 3395, 6518–6539 |
| `detailSectionContent` | 6 | 3 | 3113, 4340–4350, 4430–4440 |
| `emby-checkbox` | 6 | 3 | 3256, 3293–3297, 3346–3358 |
| `actionSheetContent` | 5 | 3 | 4207–4211, 6266–6276, 6302 |
| `cardText-first` | 5 | 3 | 898, 3285–3311, 5620 |
| `dialog` | 5 | 3 | 3163–3173, 6266–6276, 6302 |
| `guideProgramName` | 5 | 3 | 625, 5205–5216, 5259–5264 |
| `musicParentName` | 5 | 3 | 1953, 2434–2439, 5146–5155 |
| `noHomeButtonHeader` | 5 | 3 | 1634, 5904, 6014–6022 |
| `overflowBackdropCard` | 5 | 3 | 937–943, 3289, 5615–5620 |
| `secondary` | 5 | 3 | 298, 4114–4124, 4164 |
| `album` | 4 | 3 | 2123, 2381–2385, 2421 |
| `cardPadder` | 4 | 3 | 412, 984, 3302–3306 |
| `cardText` | 4 | 3 | 898–908, 3311, 6660 |
| `detailPageContent` | 4 | 3 | 1730, 4271, 4532–4539 |
| `dialog-fullscreen` | 4 | 3 | 3173, 6266–6276, 6302 |
| `emby-scrollbuttons` | 4 | 3 | 1773–1778, 6681, 7139 |
| `formDialogFooter` | 4 | 3 | 3231, 3685, 6816–6840 |
| `infoWrapper` | 4 | 3 | 2066–2071, 2328, 2356 |
| `listItemImage` | 4 | 3 | 2680–2685, 4078, 6794 |
| `semiTransparent` | 4 | 3 | 1616, 5454, 5872–5893 |
| `toast` | 4 | 3 | 4702, 6266–6276, 6302 |
| `defaultCardBackground` | 3 | 3 | 3433, 5635, 5734 |
| `detailPageSecondaryContainer` | 3 | 3 | 1583, 1610, 1730 |
| `folder` | 3 | 3 | 1872, 3412, 3476 |
| `formDialogFooterItem` | 3 | 3 | 3231, 3471, 3597 |
| `formDialogHeader` | 3 | 3 | 3685, 6759, 6816 |
| `iconOsd` | 3 | 3 | 5432, 6759, 6816 |
| `itemsContainer` | 3 | 3 | 736, 1755, 4545 |
| `live_tv` | 3 | 3 | 1953, 2421, 3719 |
| `myPreferencesMenuPage` | 3 | 3 | 385, 4249, 4553 |
| `page` | 3 | 3 | 980, 2585, 6322 |
| `playerStats` | 3 | 3 | 5432, 6816, 6852 |
| `sectionTitle-cards` | 3 | 3 | 1708, 4618, 4678 |
| `x` | 3 | 3 | 2194, 5129, 6437 |
| `itemExternalLinks` | 11 | 2 | 2979–3036, 3113 |
| `checkboxOutline` | 10 | 2 | 3256–3297, 3328–3358 |
| `mdl-slider` | 9 | 2 | 2776, 2831–2889 |
| `listItemIcon` | 8 | 2 | 3715–3719, 4219–4249 |
| `sliderContainer` | 8 | 2 | 2780, 2808–2873 |
| `cardOverlayButton-br` | 7 | 2 | 996, 1025–1063 |
| `detail-clamp-text` | 7 | 2 | 3049–3075, 3101–3105 |
| `divUsers` | 7 | 2 | 5516–5520, 6644–6671 |
| `homePage` | 7 | 2 | 3997–4049, 6072 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3293–3297, 3327–3346 |
| `backgroundContainer` | 6 | 2 | 2501, 2542–2560 |
| `detailPagePrimaryContainer` | 6 | 2 | 1560–1606, 2328 |
| `detailsGroupItem` | 6 | 2 | 4302, 4370–4407 |
| `headerButton` | 6 | 2 | 545–625, 5956 |
| `headerLeft` | 6 | 2 | 1658–1695, 6159 |
| `trackSelections` | 6 | 2 | 4275–4302, 4435–4440 |
| `withBackdrop` | 6 | 2 | 2501, 2542–2560 |
| `countIndicator` | 5 | 2 | 755–778, 6816–6840 |
| `detailSection` | 5 | 2 | 4258–4267, 4420–4440 |
| `fullSyncIndicator` | 5 | 2 | 755–778, 6816–6840 |
| `mainDrawer-scrollContainer` | 5 | 2 | 2939, 6557–6574 |
| `mediaInfoItem` | 5 | 2 | 1791–1834, 6437 |
| `overview-expand` | 5 | 2 | 3081–3105, 4340 |
| `videoIndicator` | 5 | 2 | 3401–3429, 6816 |
| `withSectionTabs` | 5 | 2 | 2551–2568, 5879 |
| `alphaPickerButton` | 4 | 2 | 625, 4479–4491 |
| `backgroundProgress` | 4 | 2 | 2691–2703, 2733 |
| `emby-tab-button-active` | 4 | 2 | 3657, 6041–6055 |
| `mediaSourceIndicator` | 4 | 2 | 755–778, 6816 |
| `play_arrow` | 4 | 2 | 3438–3454, 3624 |
| `playbackProgress` | 4 | 2 | 2691–2703, 2738 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4105–4110, 5728–5734 |
| `programCell` | 4 | 2 | 5196, 5255–5264 |
| `programGuideSection` | 4 | 2 | 2389–2404, 4440–4455 |
| `scrollX` | 4 | 2 | 1713, 1740–1751 |
| `section0` | 4 | 2 | 950–980, 6322 |
| `visualLoginForm` | 4 | 2 | 5507–5524, 5565 |
| `cardFooter` | 3 | 2 | 3322, 6409–6428 |
| `cardOverlayButtonIcon` | 3 | 2 | 996–1008, 1063 |
| `castCollapsible` | 3 | 2 | 807, 3297–3306 |
| `emby-input` | 3 | 2 | 4954–4970, 6881 |
| `emby-scrollbuttons-button` | 3 | 2 | 1782, 7146–7153 |
| `guestCastContent` | 3 | 2 | 807, 3297–3306 |
| `guide-channelHeaderCell` | 3 | 2 | 625, 5230–5246 |
| `guide-date-tab-button` | 3 | 2 | 625, 3657–3665 |
| `headerUserButton` | 3 | 2 | 545–558, 4557 |
| `manualLoginForm` | 3 | 2 | 5507–5524, 5565 |
| `overview` | 3 | 2 | 3101–3105, 4350 |
| `selectionCommandsPanel` | 3 | 2 | 3241–3247, 6759 |
| `add` | 2 | 2 | 1713, 6437 |
| `backdropImageFadeIn` | 2 | 2 | 2630, 6856 |
| `blurhash-canvas` | 2 | 2 | 6381, 6802 |
| `book` | 2 | 2 | 1953, 2421 |
| `btnDeleteImage` | 2 | 2 | 3458, 3671 |
| `cardContent` | 2 | 2 | 807, 839 |
| `cardImage` | 2 | 2 | 6381, 6802 |
| `cardOverlayButton` | 2 | 2 | 1010, 1046 |
| `cardOverlayButton-hover` | 2 | 2 | 893, 1025 |
| `chevron_right` | 2 | 2 | 4648, 4692 |
| `classList` | 2 | 2 | 1713, 6437 |
| `collapseContent` | 2 | 2 | 3236, 3683 |
| `content-primary` | 2 | 2 | 4532, 4584 |
| `editorsChoiceItemOverview` | 2 | 2 | 7076, 7157 |
| `emby-select` | 2 | 2 | 4954, 6881 |
| `endsAt` | 2 | 2 | 1812, 6437 |
| `fieldDescription` | 2 | 2 | 298, 6881 |
| `formDialogFooter-clear` | 2 | 2 | 3231, 3685 |
| `guide-programNameCaret` | 2 | 2 | 298, 5212 |
| `headroom` | 2 | 2 | 5867, 5904 |
| `mediaInfoOfficialRating` | 2 | 2 | 1812, 6437 |
| `navMenuOption-selected` | 2 | 2 | 4254, 6568 |
| `nowPlayingInfoContainer` | 2 | 2 | 2970, 5665 |
| `org` | 2 | 2 | 3006, 3036 |
| `paperList` | 2 | 2 | 816, 3696 |
| `playlist` | 2 | 2 | 4100, 5643 |
| `programSecondaryTitle` | 2 | 2 | 298, 5264 |
| `queue` | 2 | 2 | 1953, 2421 |
| `readOnlyContent` | 2 | 2 | 3727, 6088 |
| `recordingFields` | 2 | 2 | 4294, 4435 |
| `runtime` | 2 | 2 | 5577, 5605 |
| `sectionTitleContainer` | 2 | 2 | 1778, 4464 |
| `sectionTitleContainer-cards` | 2 | 2 | 4613, 4678 |
| `sidebarHeader` | 2 | 2 | 3819, 6574 |
| `tagline` | 2 | 2 | 2492, 4350 |
| `tsx` | 2 | 2 | 3997, 4053 |
| `upNextDialog-title` | 2 | 2 | 4734, 4768 |
| `vertical-list` | 2 | 2 | 1755, 6982 |
| `videoOsdBottom` | 2 | 2 | 2962, 5834 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 2962, 5834 |
| `userPreferencesPage` | 12 | 1 | 6867–6962 |
| `checkboxContainer` | 7 | 1 | 3285–3322 |
| `itemDetailsGroup` | 7 | 1 | 4354–4440 |
| `itemProgressBar` | 6 | 1 | 2680–2714 |
| `trackSelectionFieldContainer` | 6 | 1 | 4313–4336 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7113–7153 |
| `innerCardFooter` | 5 | 1 | 3126–3155 |
| `chapterCardImageContainer` | 4 | 1 | 3126–3155 |
| `endTimeText` | 4 | 1 | 5577–5605 |
| `mainDetailButtons` | 4 | 1 | 3620–3634 |
| `overview-controls` | 4 | 1 | 3101–3113 |
| `startTimeText` | 4 | 1 | 5577–5599 |
| `button-flat` | 3 | 1 | 2943–2953 |
| `cardIndicators` | 3 | 1 | 3375–3385 |
| `cardOverlayFab-primary` | 3 | 1 | 988–1010 |
| `com` | 3 | 1 | 3012–3030 |
| `content` | 3 | 1 | 4376–4407 |
| `discover-card` | 3 | 1 | 7164–7187 |
| `emby-select-withcolor` | 3 | 1 | 4954–4988 |
| `emby-textarea` | 3 | 1 | 4945–4970 |
| `fab` | 3 | 1 | 3480–3493 |
| `listChildrenCollapsible` | 3 | 1 | 4425–4440 |
| `mdl-slider-background-flex` | 3 | 1 | 2800–2813 |
| `mediaInfoCriticRating` | 3 | 1 | 1853–1862 |
| `nextUpSection` | 3 | 1 | 4420–4440 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 5629–5639 |
| `serverInfo` | 3 | 1 | 3700–3709 |
| `transcodingProgress` | 3 | 1 | 2691–2703 |
