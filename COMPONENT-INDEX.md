# Index des composants — ElegantFin Cinema Edition v1.3.8

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.8.css` — 7266 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 36 | 14 | 416–498, 736, 839, 1485–1505, 2027–2060, 2087–2091, 2367–2385, 2421, 6245, 6503–6519, 6597–6619, 6649–6656, 6739, 7144 |
| `cardScalable` | 28 | 13 | 416–427, 475–498, 785–829, 855–893, 2385, 3322, 3433, 3512, 5454, 6259–6269, 6338, 6503, 6640–6656 |
| `material-icons` | 17 | 13 | 352–371, 1704, 1782, 1834, 3279, 3438, 3512–3518, 3624, 3782, 4172, 4656, 4690–4700, 5272 |
| `cardImageContainer` | 22 | 12 | 470, 807, 835–864, 893, 950–980, 5563–5567, 5647, 6251, 6330–6338, 6378, 6503–6519, 6640 |
| `itemDetailPage` | 18 | 11 | 1548, 1634, 1713, 1953–1978, 2022, 2123, 2434–2439, 3767–3778, 4266, 4553, 6972–7010 |
| `skinHeader` | 16 | 10 | 280, 3997, 4030–4057, 5462, 5856, 5912–5920, 5946–5971, 6321, 6470, 7081 |
| `nameContainer` | 27 | 9 | 682, 2130–2153, 2194, 2223, 2258–2304, 2341, 2372–2376, 5029–5081, 6972–7010 |
| `backdropCard` | 12 | 9 | 937–943, 1058, 1953, 2039, 2123, 2376–2385, 2412, 2439, 2703 |
| `js` | 9 | 9 | 319, 1620, 1713, 2194, 2780, 3412, 5272, 6422, 6666 |
| `card-hoverable` | 23 | 8 | 498, 795, 855–943, 5567, 6269, 6378–6413, 6503, 6785 |
| `parentName` | 23 | 8 | 682, 2135–2153, 2194, 2223, 2258–2304, 5035–5081, 5154, 6972–7010 |
| `detailPageWrapperContainer` | 17 | 8 | 682, 1516–1526, 1978, 2096, 2130–2153, 2223, 2258–2304, 2372 |
| `subtitle` | 16 | 8 | 1953, 2022, 2135, 2194, 2313–2323, 2434–2439, 5089–5122, 6972–7010 |
| `cardBox` | 12 | 8 | 416–464, 490, 736, 877, 984, 6245, 6503, 6785 |
| `detailLogo` | 17 | 7 | 682, 1967–1978, 2013–2022, 2123–2153, 2223, 2258–2304, 2372 |
| `loginPage` | 15 | 7 | 3591, 5466–5481, 5520, 5548–5567, 6274, 6317, 6629–6656 |
| `emby-button` | 10 | 7 | 608–625, 652–670, 3081–3088, 3458, 3493, 3646, 4190 |
| `nowPlayingBar` | 7 | 7 | 2966, 5699, 6284, 6372, 6456, 6482, 6744 |
| `listItem` | 17 | 6 | 298, 625, 2389, 4092–4118, 4149–4181, 6762–6779 |
| `navMenuOption` | 12 | 6 | 625, 721–731, 3832, 4159–4181, 4247–4252, 6542–6553 |
| `verticalSection` | 11 | 6 | 1708, 2604–2609, 4553, 6330, 6422, 6666 |
| `person` | 8 | 6 | 1953–1963, 2123, 2376, 2421–2430, 3719, 6967 |
| `mainDrawer` | 7 | 6 | 2930, 3796, 4030, 6274–6284, 6529, 6568 |
| `detailImageContainer` | 20 | 5 | 1953–1963, 2027–2091, 2123, 2363–2385, 2412–2439 |
| `osdHeader` | 15 | 5 | 1677–1695, 5851–5920, 5946–5971, 6321, 6744 |
| `actionSheetMenuItem` | 11 | 5 | 625, 4092–4103, 4149, 4227–4243, 6302 |
| `sectionTabs` | 10 | 5 | 1751, 3570, 4057, 5892–5897, 6037–6063 |
| `button-link` | 9 | 5 | 625, 652–670, 2916–2925, 2986–2996, 6935 |
| `cardImageIcon` | 8 | 5 | 408–412, 2376–2385, 2445, 3306, 5647 |
| `headerTop` | 8 | 5 | 3997, 4030, 5862–5887, 5938–5955, 5982–5986 |
| `paper-icon-button-light` | 8 | 5 | 570–625, 1634, 1704, 1782, 4948 |
| `sectionTitle` | 7 | 5 | 1708, 1761–1768, 3898, 4626–4634, 5515 |
| `emby-scroller-container` | 6 | 5 | 1708–1713, 1740, 2594, 6330, 6422 |
| `portraitCard` | 5 | 5 | 1058, 1136, 1872, 2087, 2703 |
| `scss` | 5 | 5 | 280, 764, 1010, 3328, 6422 |
| `skinHeader-withBackground` | 5 | 5 | 1616, 3767, 5462, 5851, 5901 |
| `btnPlay` | 16 | 4 | 507–531, 570–625, 3522–3564, 3597–3624 |
| `cardOverlayContainer` | 12 | 4 | 911–943, 988–1010, 1070, 6744–6762 |
| `itemName` | 11 | 4 | 682, 2194, 5035–5081, 5172–5189 |
| `backdropImage` | 10 | 4 | 2510–2537, 2564–2568, 6238, 6338–6346 |
| `emby-tab-button` | 10 | 4 | 625, 692–701, 3570, 6022–6058 |
| `upNextContainer` | 10 | 4 | 4718–4737, 4763–4789, 6274–6284, 6310 |
| `emby-scroller` | 9 | 4 | 1713, 1740–1746, 6572–6619, 6730–6739 |
| `detailRibbon` | 7 | 4 | 1573–1601, 1787, 1872–1877, 6967 |
| `listItemBodyText` | 7 | 4 | 4113–4132, 4172, 4231, 6779 |
| `visualCardBox` | 7 | 4 | 416, 816–829, 855–860, 984 |
| `button-submit` | 6 | 4 | 3591, 3678, 5548–5556, 6847–6861 |
| `cardText-secondary` | 6 | 4 | 298, 898, 3311–3315, 6400–6408 |
| `detailPagePrimaryContent` | 6 | 4 | 1588–1606, 2328, 4547, 6486 |
| `skip-button` | 6 | 4 | 625, 3575, 4812–4829, 4856–4862 |
| `squareCard` | 6 | 4 | 839, 2376, 2412–2430, 5524–5528 |
| `skinHeader-blurred` | 5 | 4 | 5462, 5880–5887, 6470, 6744 |
| `appfooter` | 4 | 4 | 2646, 5996, 6361, 6744 |
| `raised` | 4 | 4 | 625, 711, 3458, 3493 |
| `detailButton` | 13 | 3 | 570–625, 3503–3564, 3620–3624 |
| `itemBackdrop` | 9 | 3 | 1919–1963, 2096, 2439 |
| `itemSelectionPanel` | 9 | 3 | 868–872, 3251, 3279–3322 |
| `check` | 8 | 3 | 3279, 3512, 4223–4243 |
| `pageTitle` | 8 | 3 | 1652–1695, 5912, 5971 |
| `sectionTitleTextButton` | 8 | 3 | 4609–4617, 4644–4656, 4690–4700 |
| `homePage` | 7 | 3 | 3997, 4030–4057, 6080 |
| `playedIndicator` | 7 | 3 | 764–778, 3395, 6503–6524 |
| `detailSectionContent` | 6 | 3 | 3113, 4348–4358, 4438–4448 |
| `emby-checkbox` | 6 | 3 | 3256, 3293–3297, 3346–3358 |
| `actionSheetContent` | 5 | 3 | 4215–4219, 6274–6284, 6310 |
| `cardText-first` | 5 | 3 | 898, 3285–3311, 5628 |
| `dialog` | 5 | 3 | 3163–3173, 6274–6284, 6310 |
| `guideProgramName` | 5 | 3 | 625, 5213–5224, 5267–5272 |
| `musicParentName` | 5 | 3 | 1953, 2434–2439, 5154–5163 |
| `noHomeButtonHeader` | 5 | 3 | 1634, 5912, 6022–6030 |
| `overflowBackdropCard` | 5 | 3 | 937–943, 3289, 5623–5628 |
| `secondary` | 5 | 3 | 298, 4122–4132, 4172 |
| `album` | 4 | 3 | 2123, 2381–2385, 2421 |
| `cardPadder` | 4 | 3 | 412, 984, 3302–3306 |
| `cardText` | 4 | 3 | 898–908, 3311, 6645 |
| `detailPageContent` | 4 | 3 | 1730, 4279, 4540–4547 |
| `dialog-fullscreen` | 4 | 3 | 3173, 6274–6284, 6310 |
| `emby-scrollbuttons` | 4 | 3 | 1773–1778, 6666, 7119 |
| `formDialogFooter` | 4 | 3 | 3231, 3685, 6796–6820 |
| `infoWrapper` | 4 | 3 | 2066–2071, 2328, 2356 |
| `listItemImage` | 4 | 3 | 2680–2685, 4086, 6779 |
| `semiTransparent` | 4 | 3 | 1616, 5462, 5880–5901 |
| `toast` | 4 | 3 | 4710, 6274–6284, 6310 |
| `cardFooter` | 3 | 3 | 3322, 6378, 6413 |
| `defaultCardBackground` | 3 | 3 | 3433, 5643, 5742 |
| `detailPageSecondaryContainer` | 3 | 3 | 1583, 1610, 1730 |
| `folder` | 3 | 3 | 1872, 3412, 3476 |
| `formDialogFooterItem` | 3 | 3 | 3231, 3471, 3597 |
| `formDialogHeader` | 3 | 3 | 3685, 6744, 6796 |
| `iconOsd` | 3 | 3 | 5440, 6744, 6796 |
| `itemsContainer` | 3 | 3 | 736, 1755, 4553 |
| `live_tv` | 3 | 3 | 1953, 2421, 3719 |
| `myPreferencesMenuPage` | 3 | 3 | 385, 4257, 4561 |
| `page` | 3 | 3 | 980, 2585, 6330 |
| `playerStats` | 3 | 3 | 5440, 6796, 6832 |
| `sectionTitle-cards` | 3 | 3 | 1708, 4626, 4686 |
| `x` | 3 | 3 | 2194, 5137, 6422 |
| `itemExternalLinks` | 11 | 2 | 2979–3036, 3113 |
| `checkboxOutline` | 10 | 2 | 3256–3297, 3328–3358 |
| `mdl-slider` | 9 | 2 | 2776, 2831–2889 |
| `listItemIcon` | 8 | 2 | 3715–3719, 4227–4257 |
| `sliderContainer` | 8 | 2 | 2780, 2808–2873 |
| `cardOverlayButton-br` | 7 | 2 | 996, 1025–1063 |
| `detail-clamp-text` | 7 | 2 | 3049–3075, 3101–3105 |
| `divUsers` | 7 | 2 | 5524–5528, 6629–6656 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3293–3297, 3327–3346 |
| `backgroundContainer` | 6 | 2 | 2501, 2542–2560 |
| `detailPagePrimaryContainer` | 6 | 2 | 1560–1606, 2328 |
| `detailsGroupItem` | 6 | 2 | 4310, 4378–4415 |
| `headerButton` | 6 | 2 | 545–625, 5964 |
| `headerLeft` | 6 | 2 | 1658–1695, 6167 |
| `trackSelections` | 6 | 2 | 4283–4310, 4443–4448 |
| `withBackdrop` | 6 | 2 | 2501, 2542–2560 |
| `countIndicator` | 5 | 2 | 755–778, 6796–6820 |
| `detailSection` | 5 | 2 | 4266–4275, 4428–4448 |
| `fullSyncIndicator` | 5 | 2 | 755–778, 6796–6820 |
| `mainDrawer-scrollContainer` | 5 | 2 | 2939, 6542–6559 |
| `mediaInfoItem` | 5 | 2 | 1791–1834, 6422 |
| `overview-expand` | 5 | 2 | 3081–3105, 4348 |
| `videoIndicator` | 5 | 2 | 3401–3429, 6796 |
| `withSectionTabs` | 5 | 2 | 2551–2568, 5887 |
| `alphaPickerButton` | 4 | 2 | 625, 4487–4499 |
| `backgroundProgress` | 4 | 2 | 2691–2703, 2733 |
| `emby-tab-button-active` | 4 | 2 | 3657, 6049–6063 |
| `mediaSourceIndicator` | 4 | 2 | 755–778, 6796 |
| `play_arrow` | 4 | 2 | 3438–3454, 3624 |
| `playbackProgress` | 4 | 2 | 2691–2703, 2738 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4113–4118, 5736–5742 |
| `programCell` | 4 | 2 | 5204, 5263–5272 |
| `programGuideSection` | 4 | 2 | 2389–2404, 4448–4463 |
| `scrollX` | 4 | 2 | 1713, 1740–1751 |
| `section0` | 4 | 2 | 950–980, 6330 |
| `visualLoginForm` | 4 | 2 | 5515–5532, 5573 |
| `cardOverlayButtonIcon` | 3 | 2 | 996–1008, 1063 |
| `castCollapsible` | 3 | 2 | 807, 3297–3306 |
| `emby-input` | 3 | 2 | 4962–4978, 6861 |
| `emby-scrollbuttons-button` | 3 | 2 | 1782, 7126–7133 |
| `guestCastContent` | 3 | 2 | 807, 3297–3306 |
| `guide-channelHeaderCell` | 3 | 2 | 625, 5238–5254 |
| `guide-date-tab-button` | 3 | 2 | 625, 3657–3665 |
| `headerUserButton` | 3 | 2 | 545–558, 4565 |
| `manualLoginForm` | 3 | 2 | 5515–5532, 5573 |
| `overview` | 3 | 2 | 3101–3105, 4358 |
| `selectionCommandsPanel` | 3 | 2 | 3241–3247, 6744 |
| `add` | 2 | 2 | 1713, 6422 |
| `backdropImageFadeIn` | 2 | 2 | 2630, 6836 |
| `book` | 2 | 2 | 1953, 2421 |
| `btnDeleteImage` | 2 | 2 | 3458, 3671 |
| `cardContent` | 2 | 2 | 807, 839 |
| `cardOverlayButton` | 2 | 2 | 1010, 1046 |
| `cardOverlayButton-hover` | 2 | 2 | 893, 1025 |
| `chevron_right` | 2 | 2 | 4656, 4700 |
| `classList` | 2 | 2 | 1713, 6422 |
| `collapseContent` | 2 | 2 | 3236, 3683 |
| `content-primary` | 2 | 2 | 4540, 4592 |
| `editorsChoiceItemOverview` | 2 | 2 | 7056, 7137 |
| `emby-select` | 2 | 2 | 4962, 6861 |
| `endsAt` | 2 | 2 | 1812, 6422 |
| `fieldDescription` | 2 | 2 | 298, 6861 |
| `formDialogFooter-clear` | 2 | 2 | 3231, 3685 |
| `guide-programNameCaret` | 2 | 2 | 298, 5220 |
| `headroom` | 2 | 2 | 5875, 5912 |
| `mediaInfoOfficialRating` | 2 | 2 | 1812, 6422 |
| `navMenuOption-selected` | 2 | 2 | 4262, 6553 |
| `nowPlayingInfoContainer` | 2 | 2 | 2970, 5673 |
| `org` | 2 | 2 | 3006, 3036 |
| `paperList` | 2 | 2 | 816, 3696 |
| `playlist` | 2 | 2 | 4108, 5651 |
| `programSecondaryTitle` | 2 | 2 | 298, 5272 |
| `queue` | 2 | 2 | 1953, 2421 |
| `readOnlyContent` | 2 | 2 | 3727, 6096 |
| `recordingFields` | 2 | 2 | 4302, 4443 |
| `runtime` | 2 | 2 | 5585, 5613 |
| `sectionTitleContainer` | 2 | 2 | 1778, 4472 |
| `sectionTitleContainer-cards` | 2 | 2 | 4621, 4686 |
| `sidebarHeader` | 2 | 2 | 3819, 6559 |
| `tagline` | 2 | 2 | 2492, 4358 |
| `tsx` | 2 | 2 | 3997, 4061 |
| `upNextDialog-title` | 2 | 2 | 4742, 4776 |
| `vertical-list` | 2 | 2 | 1755, 6962 |
| `videoOsdBottom` | 2 | 2 | 2962, 5842 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 2962, 5842 |
| `userPreferencesPage` | 12 | 1 | 6847–6942 |
| `checkboxContainer` | 7 | 1 | 3285–3322 |
| `itemDetailsGroup` | 7 | 1 | 4362–4448 |
| `itemProgressBar` | 6 | 1 | 2680–2714 |
| `trackSelectionFieldContainer` | 6 | 1 | 4321–4344 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7093–7133 |
| `innerCardFooter` | 5 | 1 | 3126–3155 |
| `chapterCardImageContainer` | 4 | 1 | 3126–3155 |
| `endTimeText` | 4 | 1 | 5585–5613 |
| `mainDetailButtons` | 4 | 1 | 3620–3634 |
| `overview-controls` | 4 | 1 | 3101–3113 |
| `startTimeText` | 4 | 1 | 5585–5607 |
| `button-flat` | 3 | 1 | 2943–2953 |
| `cardIndicators` | 3 | 1 | 3375–3385 |
| `cardOverlayFab-primary` | 3 | 1 | 988–1010 |
| `com` | 3 | 1 | 3012–3030 |
| `content` | 3 | 1 | 4384–4415 |
| `discover-card` | 3 | 1 | 7144–7167 |
| `emby-select-withcolor` | 3 | 1 | 4962–4996 |
| `emby-textarea` | 3 | 1 | 4953–4978 |
| `fab` | 3 | 1 | 3480–3493 |
| `listChildrenCollapsible` | 3 | 1 | 4433–4448 |
| `mdl-slider-background-flex` | 3 | 1 | 2800–2813 |
| `mediaInfoCriticRating` | 3 | 1 | 1853–1862 |
| `nextUpSection` | 3 | 1 | 4428–4448 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 5637–5647 |
| `serverInfo` | 3 | 1 | 3700–3709 |
| `transcodingProgress` | 3 | 1 | 2691–2703 |
