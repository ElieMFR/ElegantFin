# Index des composants — ElegantFin Cinema Edition v1.5.0

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.5.0.css` — 8027 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 38 | 16 | 454–465, 496–542, 780, 897, 1562–1582, 2196–2229, 2256–2260, 2537–2555, 2591, 6888, 6924–6934, 7170–7189, 7267–7289, 7319–7326, 7490, 7905 |
| `cardScalable` | 31 | 13 | 454–465, 519–542, 843–887, 913–957, 2555, 3637, 3748, 3827, 6001, 6902–6934, 7005, 7170, 7310–7326 |
| `material-icons` | 17 | 13 | 390–409, 1787, 1885, 1938, 3594, 3753, 3827–3833, 3940, 4103, 4648, 5180, 5214–5224, 5818 |
| `cardImageContainer` | 22 | 12 | 514, 865, 893–922, 957, 1014–1044, 6148–6152, 6232, 6894, 6997–7005, 7045, 7170–7189, 7310 |
| `itemDetailPage` | 20 | 12 | 1625, 1711, 1796, 1823, 2052–2092, 2127–2142, 2178–2182, 2292, 2604, 4771, 5073, 7725–7763 |
| `skinHeader` | 20 | 12 | 293, 1711, 4083–4099, 4460, 4506–4533, 6009–6013, 6441, 6497–6505, 6571–6596, 6988, 7137, 7834 |
| `js` | 12 | 11 | 327, 357, 1697–1711, 1796, 2363, 2969, 3398, 3727, 5818, 7089, 7336 |
| `nameContainer` | 27 | 9 | 726, 2299–2322, 2363, 2392, 2427–2474, 2511, 2542–2546, 5574–5627, 7725–7763 |
| `cardBox` | 13 | 9 | 454–465, 496–508, 534, 780, 935–939, 1048, 6888, 7170, 7536 |
| `emby-button` | 12 | 9 | 652–669, 696–714, 3231, 3366–3373, 3773, 3808, 3962, 4666, 5396 |
| `card-hoverable` | 23 | 8 | 542, 853, 913–1007, 6152, 6912, 7045–7080, 7170, 7536 |
| `parentName` | 23 | 8 | 726, 2304–2322, 2363, 2392, 2427–2474, 5580–5627, 5700, 7725–7763 |
| `detailLogo` | 20 | 8 | 726, 2081–2092, 2127–2142, 2169–2182, 2292–2322, 2392, 2427–2474, 2542 |
| `listItem` | 19 | 8 | 311, 669, 2559, 4568–4594, 4625–4657, 4702, 4746, 7513–7530 |
| `detailPageWrapperContainer` | 17 | 8 | 726, 1593–1603, 2092, 2265, 2299–2322, 2392, 2427–2474, 2542 |
| `subtitle` | 17 | 8 | 2052–2062, 2178–2182, 2304, 2363, 2483–2493, 2604, 5635–5668, 7725–7763 |
| `backdropCard` | 12 | 8 | 1001–1007, 1129, 2052–2062, 2208, 2292, 2546–2555, 2582, 2892 |
| `nowPlayingBar` | 8 | 8 | 327, 3155, 6284, 6951, 7039, 7123, 7149, 7495 |
| `loginPage` | 18 | 7 | 3906, 6013–6047, 6087–6104, 6133–6152, 6941, 6984, 7299–7326 |
| `navMenuOption` | 12 | 6 | 669, 765–775, 4153, 4635–4657, 4752–4757, 7212–7223 |
| `emby-tab-button` | 11 | 6 | 669, 736–745, 3885, 6647–6655, 6684–6701, 7846 |
| `paper-icon-button-light` | 11 | 6 | 614–669, 1711, 1787, 1885, 3534–3554, 5480 |
| `verticalSection` | 11 | 6 | 1791, 2794–2799, 5073, 6997, 7089, 7336 |
| `button-link` | 10 | 6 | 669, 696–714, 3105–3114, 3175–3185, 3231, 7687 |
| `headerTop` | 9 | 6 | 2182, 4460, 4506, 6447–6472, 6563–6580, 6607–6611 |
| `person` | 8 | 6 | 2052–2077, 2292, 2546, 2591–2600, 4035, 7720 |
| `mainDrawer` | 7 | 6 | 3119, 4117, 4506, 6941–6951, 7199, 7238 |
| `scss` | 6 | 6 | 293, 808, 1074, 3643, 4159, 7089 |
| `detailImageContainer` | 20 | 5 | 2052–2077, 2196–2260, 2292, 2533–2555, 2582–2600 |
| `osdHeader` | 15 | 5 | 1760–1778, 6436–6505, 6571–6596, 6988, 7495 |
| `sectionTabs` | 11 | 5 | 1854, 3885, 4533, 6477–6482, 6662–6706 |
| `actionSheetMenuItem` | 10 | 5 | 669, 4568–4579, 4625, 4702–4746, 6969 |
| `cardImageIcon` | 8 | 5 | 446–450, 2546–2555, 2618, 3621, 6232 |
| `sectionTitle` | 7 | 5 | 1791, 1864–1871, 4361, 5150–5158, 6082 |
| `semiTransparent` | 7 | 5 | 1693, 4083–4099, 6009, 6465–6486, 6522 |
| `emby-scroller-container` | 6 | 5 | 1791–1796, 1834, 2784, 6997, 7089 |
| `portraitCard` | 6 | 5 | 1129, 1213, 1976–1981, 2256, 2892 |
| `appfooter` | 5 | 5 | 327, 2835, 6621, 7028, 7495 |
| `skinHeader-withBackground` | 5 | 5 | 1693, 4083, 6009, 6436, 6486 |
| `btnPlay` | 16 | 4 | 551–575, 614–669, 3837–3879, 3912–3940 |
| `cardOverlayContainer` | 12 | 4 | 975–1007, 1052–1074, 1147, 7495–7513 |
| `itemName` | 11 | 4 | 726, 2363, 5580–5627, 5718–5735 |
| `backdropImage` | 10 | 4 | 2683–2711, 2738–2742, 6881, 7005–7013 |
| `upNextContainer` | 10 | 4 | 5242–5261, 5287–5313, 6941–6951, 6977 |
| `emby-scroller` | 9 | 4 | 1796, 1834–1840, 7242–7289, 7474–7490 |
| `backgroundContainer` | 8 | 4 | 2146, 2674, 2716–2734, 2766 |
| `detailRibbon` | 8 | 4 | 1650–1678, 1891, 1976–1988, 7720 |
| `listItemBodyText` | 7 | 4 | 4589–4608, 4648, 4723, 7530 |
| `skip-button` | 7 | 4 | 669, 3890, 5336–5353, 5380–5398 |
| `visualCardBox` | 7 | 4 | 454, 874–887, 913–918, 1048 |
| `button-submit` | 6 | 4 | 3906, 3994, 6133–6141, 7598–7613 |
| `cardText-secondary` | 6 | 4 | 311, 962, 3626–3630, 7067–7075 |
| `detailPagePrimaryContent` | 6 | 4 | 1665–1683, 2498, 5067, 7153 |
| `squareCard` | 6 | 4 | 897, 2546, 2582–2600, 6109–6113 |
| `skinHeader-blurred` | 5 | 4 | 6009, 6465–6472, 7137, 7495 |
| `itemsContainer` | 4 | 4 | 780, 1823, 1858, 5073 |
| `raised` | 4 | 4 | 669, 755, 3773, 3808 |
| `tsx` | 4 | 4 | 1129, 1711, 4460, 4537 |
| `x` | 4 | 4 | 2363, 4159, 5683, 7089 |
| `detailButton` | 13 | 3 | 614–669, 3818–3879, 3936–3940 |
| `itemSelectionPanel` | 9 | 3 | 926–930, 3566, 3594–3637 |
| `pageTitle` | 8 | 3 | 1735–1778, 6497, 6596 |
| `sectionTitleTextButton` | 8 | 3 | 5133–5141, 5168–5180, 5214–5224 |
| `homePage` | 7 | 3 | 4460, 4506–4533, 6723 |
| `playedIndicator` | 7 | 3 | 808–822, 3710, 7170–7194 |
| `check` | 6 | 3 | 3594, 3827, 4702–4746 |
| `detailSectionContent` | 6 | 3 | 3398, 4853–4863, 4946–4956 |
| `emby-checkbox` | 6 | 3 | 3571, 3608–3612, 3661–3673 |
| `actionSheetContent` | 5 | 3 | 4694–4698, 6941–6951, 6977 |
| `cardText-first` | 5 | 3 | 962, 3600–3626, 6213 |
| `dialog` | 5 | 3 | 3450–3460, 6941–6951, 6977 |
| `guideProgramName` | 5 | 3 | 669, 5759–5770, 5813–5818 |
| `noHomeButtonHeader` | 5 | 3 | 1711, 6497, 6647–6655 |
| `overflowBackdropCard` | 5 | 3 | 1001–1007, 3604, 6208–6213 |
| `secondary` | 5 | 3 | 311, 4598–4608, 4648 |
| `album` | 4 | 3 | 2292, 2551–2555, 2591 |
| `cardPadder` | 4 | 3 | 450, 1048, 3617–3621 |
| `cardText` | 4 | 3 | 962–972, 3626, 7315 |
| `detailPageContent` | 4 | 3 | 1813, 4784, 5060–5067 |
| `dialog-fullscreen` | 4 | 3 | 3460, 6941–6951, 6977 |
| `emby-scrollbuttons` | 4 | 3 | 1876–1881, 7336, 7880 |
| `folder` | 4 | 3 | 1976–1981, 3727, 3791 |
| `formDialogFooter` | 4 | 3 | 3518, 4001, 7547–7571 |
| `infoWrapper` | 4 | 3 | 2235–2240, 2498, 2526 |
| `listItemImage` | 4 | 3 | 2869–2874, 4562, 7530 |
| `musicParentName` | 4 | 3 | 2052, 2604, 5700–5709 |
| `programGuideSection` | 4 | 3 | 2559–2574, 4956, 4983 |
| `toast` | 4 | 3 | 5234, 6941–6951, 6977 |
| `cardFooter` | 3 | 3 | 3637, 7045, 7080 |
| `collectionItems` | 3 | 3 | 1823, 4956, 4992 |
| `defaultCardBackground` | 3 | 3 | 3748, 6228, 6327 |
| `detailPageSecondaryContainer` | 3 | 3 | 1660, 1687, 1813 |
| `emby-input` | 3 | 3 | 5494, 5523, 7613 |
| `formDialogFooterItem` | 3 | 3 | 3518, 3786, 3912 |
| `formDialogHeader` | 3 | 3 | 4001, 7495, 7547 |
| `iconOsd` | 3 | 3 | 5987, 7495, 7547 |
| `live_tv` | 3 | 3 | 2052, 2591, 4035 |
| `myPreferencesMenuPage` | 3 | 3 | 423, 4762, 5081 |
| `page` | 3 | 3 | 1044, 2766, 6997 |
| `playerStats` | 3 | 3 | 5987, 7547, 7583 |
| `readOnlyContent` | 3 | 3 | 4043, 6098, 6739 |
| `sectionTitle-cards` | 3 | 3 | 1791, 5150, 5210 |
| `sectionTitleContainer` | 3 | 3 | 1823, 1881, 4992 |
| `itemExternalLinks` | 13 | 2 | 3168–3246, 3398 |
| `checkboxOutline` | 10 | 2 | 3571–3612, 3643–3673 |
| `itemBackdrop` | 9 | 2 | 2018–2077, 2265 |
| `mdl-slider` | 9 | 2 | 2965, 3020–3078 |
| `cardOverlayButton-br` | 8 | 2 | 1060, 1089–1140 |
| `listItemIcon` | 8 | 2 | 4031–4035, 4702–4762 |
| `sliderContainer` | 8 | 2 | 2969, 2997–3062 |
| `detail-clamp-text` | 7 | 2 | 3334–3360, 3386–3390 |
| `divUsers` | 7 | 2 | 6109–6113, 7299–7326 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3608–3612, 3642–3661 |
| `countIndicator` | 6 | 2 | 799–829, 7547–7571 |
| `detailPagePrimaryContainer` | 6 | 2 | 1637–1683, 2498 |
| `detailsGroupItem` | 6 | 2 | 4815, 4886–4923 |
| `headerButton` | 6 | 2 | 589–669, 6589 |
| `headerLeft` | 6 | 2 | 1741–1778, 6810 |
| `selectionCommandsPanel` | 6 | 2 | 3528–3562, 7495 |
| `trackSelections` | 6 | 2 | 4788–4815, 4951–4956 |
| `withBackdrop` | 6 | 2 | 2674, 2716–2734 |
| `detailSection` | 5 | 2 | 4771–4780, 4936–4956 |
| `fullSyncIndicator` | 5 | 2 | 799–822, 7547–7571 |
| `mainDrawer-scrollContainer` | 5 | 2 | 3128, 7212–7229 |
| `mediaInfoItem` | 5 | 2 | 1895–1938, 7089 |
| `overview-expand` | 5 | 2 | 3366–3390, 4853 |
| `scrollX` | 5 | 2 | 1796, 1834–1854 |
| `videoIndicator` | 5 | 2 | 3716–3744, 7547 |
| `withSectionTabs` | 5 | 2 | 2725–2742, 6472 |
| `alphaPickerButton` | 4 | 2 | 669, 5007–5019 |
| `backgroundProgress` | 4 | 2 | 2880–2892, 2922 |
| `emby-select` | 4 | 2 | 5494–5506, 7613 |
| `emby-tab-button-active` | 4 | 2 | 3973, 6692–6706 |
| `manualLoginForm` | 4 | 2 | 6082–6117, 6158 |
| `mediaSourceIndicator` | 4 | 2 | 799–822, 7547 |
| `play_arrow` | 4 | 2 | 3753–3769, 3940 |
| `playbackProgress` | 4 | 2 | 2880–2892, 2927 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4589–4594, 6321–6327 |
| `programCell` | 4 | 2 | 5750, 5809–5818 |
| `section0` | 4 | 2 | 1014–1044, 6997 |
| `visualLoginForm` | 4 | 2 | 6082–6117, 6158 |
| `cardOverlayButtonIcon` | 3 | 2 | 1060–1072, 1140 |
| `castCollapsible` | 3 | 2 | 865, 3612–3621 |
| `emby-scrollbuttons-button` | 3 | 2 | 1885, 7887–7894 |
| `emby-textarea` | 3 | 2 | 5485–5494, 5523 |
| `guestCastContent` | 3 | 2 | 865, 3612–3621 |
| `guide-channelHeaderCell` | 3 | 2 | 669, 5784–5800 |
| `guide-date-tab-button` | 3 | 2 | 669, 3973–3981 |
| `headerUserButton` | 3 | 2 | 589–602, 5085 |
| `noHeaderRight` | 3 | 2 | 1711, 6009–6013 |
| `overview` | 3 | 2 | 3386–3390, 4863 |
| `add` | 2 | 2 | 1796, 7089 |
| `alphaPicker-fixed-right` | 2 | 2 | 2766, 5019 |
| `backdropImageFadeIn` | 2 | 2 | 2819, 7587 |
| `book` | 2 | 2 | 2052, 2591 |
| `btnDeleteImage` | 2 | 2 | 3773, 3987 |
| `cardContent` | 2 | 2 | 865, 897 |
| `cardOverlayButton` | 2 | 2 | 1074, 1117 |
| `cardOverlayButton-hover` | 2 | 2 | 957, 1089 |
| `chevron_right` | 2 | 2 | 5180, 5224 |
| `classList` | 2 | 2 | 1796, 7089 |
| `collapseContent` | 2 | 2 | 3523, 3999 |
| `collectionItemsContainer` | 2 | 2 | 1823, 4996 |
| `content-primary` | 2 | 2 | 5060, 5116 |
| `editorsChoiceItemOverview` | 2 | 2 | 7809, 7898 |
| `endsAt` | 2 | 2 | 1916, 7089 |
| `fieldDescription` | 2 | 2 | 311, 7613 |
| `formDialogFooter-clear` | 2 | 2 | 3518, 4001 |
| `guide-programNameCaret` | 2 | 2 | 311, 5766 |
| `headroom` | 2 | 2 | 6460, 6497 |
| `indicator` | 2 | 2 | 829, 3705 |
| `mediaInfoOfficialRating` | 2 | 2 | 1916, 7089 |
| `navMenuOption-selected` | 2 | 2 | 4767, 7223 |
| `nowPlayingInfoContainer` | 2 | 2 | 3159, 6258 |
| `org` | 2 | 2 | 3195, 3225 |
| `paperList` | 2 | 2 | 874, 4012 |
| `playlist` | 2 | 2 | 4584, 6236 |
| `programSecondaryTitle` | 2 | 2 | 311, 5818 |
| `queue` | 2 | 2 | 2052, 2591 |
| `reactRoot` | 2 | 2 | 4460, 6816 |
| `recordingFields` | 2 | 2 | 4807, 4951 |
| `runtime` | 2 | 2 | 6170, 6198 |
| `sectionTitleContainer-cards` | 2 | 2 | 5145, 5210 |
| `sidebarHeader` | 2 | 2 | 4140, 7229 |
| `tagline` | 2 | 2 | 2665, 4863 |
| `upNextDialog-title` | 2 | 2 | 5266, 5300 |
| `vertical-list` | 2 | 2 | 1858, 7715 |
| `vertical-wrap` | 2 | 2 | 795, 1823 |
| `videoOsdBottom` | 2 | 2 | 3151, 6427 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3151, 6427 |
| `userPreferencesPage` | 12 | 1 | 7598–7694 |
| `checkboxContainer` | 7 | 1 | 3600–3637 |
| `itemDetailsGroup` | 7 | 1 | 4870–4956 |
| `itemProgressBar` | 6 | 1 | 2869–2903 |
| `streaming-lookup-container` | 6 | 1 | 3253–3298 |
| `trackSelectionFieldContainer` | 6 | 1 | 4826–4849 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7854–7894 |
| `innerCardFooter` | 5 | 1 | 3413–3442 |
| `chapterCardImageContainer` | 4 | 1 | 3413–3442 |
| `emby-select-withcolor` | 4 | 1 | 5494–5541 |
| `endTimeText` | 4 | 1 | 6170–6198 |
| `mainDetailButtons` | 4 | 1 | 3936–3950 |
| `overview-controls` | 4 | 1 | 3386–3398 |
| `startTimeText` | 4 | 1 | 6170–6192 |
| `button-flat` | 3 | 1 | 3132–3142 |
| `cardIndicators` | 3 | 1 | 3690–3700 |
| `cardOverlayFab-primary` | 3 | 1 | 1052–1074 |
| `com` | 3 | 1 | 3201–3219 |
| `content` | 3 | 1 | 4892–4923 |
| `discover-card` | 3 | 1 | 7905–7928 |
| `fab` | 3 | 1 | 3795–3808 |
| `listChildrenCollapsible` | 3 | 1 | 4941–4956 |
| `mdl-slider-background-flex` | 3 | 1 | 2989–3002 |
| `mediaInfoCriticRating` | 3 | 1 | 1957–1966 |
| `nextUpSection` | 3 | 1 | 4936–4956 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 6222–6232 |
| `serverInfo` | 3 | 1 | 4016–4025 |
| `transcodingProgress` | 3 | 1 | 2880–2892 |
