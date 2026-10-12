# Index des composants — ElegantFin Cinema Edition v1.3.25

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.25.css` — 7877 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 36 | 15 | 428–439, 469–516, 754, 871, 1523–1543, 2134–2167, 2194–2198, 2475–2493, 2529, 6770, 7028–7047, 7125–7147, 7177–7184, 7348, 7755 |
| `cardScalable` | 28 | 13 | 428–439, 491–516, 817–861, 887–925, 2493, 3573, 3684, 3763, 5917, 6784–6794, 6863, 7028, 7168–7184 |
| `itemDetailPage` | 21 | 13 | 1586, 1672, 1751, 1778, 2007–2043, 2078–2093, 2129, 2230, 2542, 4019–4030, 4690, 4989, 7583–7621 |
| `material-icons` | 17 | 13 | 364–383, 1742, 1840, 1893, 3530, 3689, 3763–3769, 3876, 4034, 4567, 5096, 5130–5140, 5734 |
| `cardImageContainer` | 22 | 12 | 486, 839, 867–896, 925, 982–1012, 6043–6047, 6127, 6776, 6855–6863, 6903, 7028–7047, 7168 |
| `skinHeader` | 16 | 10 | 284, 4379, 4425–4452, 5925, 6336, 6392–6400, 6466–6491, 6846, 6995, 7692 |
| `nameContainer` | 27 | 9 | 700, 2237–2260, 2301, 2330, 2365–2412, 2449, 2480–2484, 5490–5543, 7583–7621 |
| `cardBox` | 12 | 9 | 428–439, 469–480, 508, 754, 909, 1016, 6770, 7028, 7394 |
| `emby-button` | 12 | 9 | 626–643, 670–688, 3169, 3304–3311, 3709, 3744, 3898, 4585, 5312 |
| `js` | 9 | 9 | 331, 1658, 1751, 2301, 2907, 3663, 5734, 6947, 7194 |
| `card-hoverable` | 23 | 8 | 516, 827, 887–975, 6047, 6794, 6903–6938, 7028, 7394 |
| `parentName` | 23 | 8 | 700, 2242–2260, 2301, 2330, 2365–2412, 5496–5543, 5616, 7583–7621 |
| `detailLogo` | 20 | 8 | 700, 2017–2043, 2078–2093, 2120–2129, 2230–2260, 2330, 2365–2412, 2480 |
| `listItem` | 19 | 8 | 302, 643, 2497, 4487–4513, 4544–4576, 4621, 4665, 7371–7388 |
| `detailPageWrapperContainer` | 17 | 8 | 700, 1554–1564, 2043, 2203, 2237–2260, 2330, 2365–2412, 2480 |
| `subtitle` | 16 | 8 | 2007–2017, 2129, 2242, 2301, 2421–2431, 2542, 5551–5584, 7583–7621 |
| `backdropCard` | 12 | 8 | 969–975, 1090, 2007–2017, 2146, 2230, 2484–2493, 2520, 2830 |
| `nowPlayingBar` | 8 | 8 | 318, 3093, 6179, 6809, 6897, 6981, 7007, 7353 |
| `loginPage` | 16 | 7 | 3842, 5929–5960, 6000, 6028–6047, 6799, 6842, 7157–7184 |
| `navMenuOption` | 12 | 6 | 643, 739–749, 4084, 4554–4576, 4671–4676, 7070–7081 |
| `paper-icon-button-light` | 11 | 6 | 588–643, 1672, 1742, 1840, 3470–3490, 5396 |
| `verticalSection` | 11 | 6 | 1746, 2732–2737, 4989, 6855, 6947, 7194 |
| `button-link` | 10 | 6 | 643, 670–688, 3043–3052, 3113–3123, 3169, 7545 |
| `person` | 8 | 6 | 2007–2028, 2230, 2484, 2529–2538, 3971, 7578 |
| `mainDrawer` | 7 | 6 | 3057, 4048, 4425, 6799–6809, 7057, 7096 |
| `scss` | 6 | 6 | 284, 782, 1042, 3579, 4090, 6947 |
| `detailImageContainer` | 20 | 5 | 2007–2028, 2134–2198, 2230, 2471–2493, 2520–2538 |
| `osdHeader` | 15 | 5 | 1715–1733, 6331–6400, 6466–6491, 6846, 7353 |
| `actionSheetMenuItem` | 10 | 5 | 643, 4487–4498, 4544, 4621–4665, 6827 |
| `sectionTabs` | 10 | 5 | 1809, 3821, 4452, 6372–6377, 6557–6588 |
| `cardImageIcon` | 8 | 5 | 420–424, 2484–2493, 2556, 3557, 6127 |
| `headerTop` | 8 | 5 | 4379, 4425, 6342–6367, 6458–6475, 6502–6506 |
| `sectionTitle` | 7 | 5 | 1746, 1819–1826, 4280, 5066–5074, 5995 |
| `emby-scroller-container` | 6 | 5 | 1746–1751, 1789, 2722, 6855, 6947 |
| `portraitCard` | 6 | 5 | 1090, 1174, 1931–1936, 2194, 2830 |
| `skinHeader-withBackground` | 5 | 5 | 1654, 4019, 5925, 6331, 6381 |
| `btnPlay` | 16 | 4 | 525–549, 588–643, 3773–3815, 3848–3876 |
| `cardOverlayContainer` | 12 | 4 | 943–975, 1020–1042, 1108, 7353–7371 |
| `itemName` | 11 | 4 | 700, 2301, 5496–5543, 5634–5651 |
| `backdropImage` | 10 | 4 | 2621–2649, 2676–2680, 6763, 6863–6871 |
| `emby-tab-button` | 10 | 4 | 643, 710–719, 3821, 6542–6583 |
| `upNextContainer` | 10 | 4 | 5158–5177, 5203–5229, 6799–6809, 6835 |
| `emby-scroller` | 9 | 4 | 1751, 1789–1795, 7100–7147, 7332–7348 |
| `backgroundContainer` | 8 | 4 | 2097, 2612, 2654–2672, 2704 |
| `detailRibbon` | 8 | 4 | 1611–1639, 1846, 1931–1943, 7578 |
| `listItemBodyText` | 7 | 4 | 4508–4527, 4567, 4642, 7388 |
| `skip-button` | 7 | 4 | 643, 3826, 5252–5269, 5296–5314 |
| `visualCardBox` | 7 | 4 | 428, 848–861, 887–892, 1016 |
| `button-submit` | 6 | 4 | 3842, 3930, 6028–6036, 7456–7471 |
| `cardText-secondary` | 6 | 4 | 302, 930, 3562–3566, 6925–6933 |
| `detailPagePrimaryContent` | 6 | 4 | 1626–1644, 2436, 4983, 7011 |
| `squareCard` | 6 | 4 | 871, 2484, 2520–2538, 6004–6008 |
| `semiTransparent` | 5 | 4 | 1654, 5925, 6360–6381, 6417 |
| `skinHeader-blurred` | 5 | 4 | 5925, 6360–6367, 6995, 7353 |
| `appfooter` | 4 | 4 | 2773, 6516, 6886, 7353 |
| `itemsContainer` | 4 | 4 | 754, 1778, 1813, 4989 |
| `raised` | 4 | 4 | 643, 729, 3709, 3744 |
| `x` | 4 | 4 | 2301, 4090, 5599, 6947 |
| `detailButton` | 13 | 3 | 588–643, 3754–3815, 3872–3876 |
| `itemSelectionPanel` | 9 | 3 | 900–904, 3502, 3530–3573 |
| `pageTitle` | 8 | 3 | 1690–1733, 6392, 6491 |
| `sectionTitleTextButton` | 8 | 3 | 5049–5057, 5084–5096, 5130–5140 |
| `homePage` | 7 | 3 | 4379, 4425–4452, 6605 |
| `playedIndicator` | 7 | 3 | 782–796, 3646, 7028–7052 |
| `check` | 6 | 3 | 3530, 3763, 4621–4665 |
| `detailSectionContent` | 6 | 3 | 3336, 4772–4782, 4862–4872 |
| `emby-checkbox` | 6 | 3 | 3507, 3544–3548, 3597–3609 |
| `actionSheetContent` | 5 | 3 | 4613–4617, 6799–6809, 6835 |
| `cardText-first` | 5 | 3 | 930, 3536–3562, 6108 |
| `dialog` | 5 | 3 | 3386–3396, 6799–6809, 6835 |
| `guideProgramName` | 5 | 3 | 643, 5675–5686, 5729–5734 |
| `noHomeButtonHeader` | 5 | 3 | 1672, 6392, 6542–6550 |
| `overflowBackdropCard` | 5 | 3 | 969–975, 3540, 6103–6108 |
| `secondary` | 5 | 3 | 302, 4517–4527, 4567 |
| `album` | 4 | 3 | 2230, 2489–2493, 2529 |
| `cardPadder` | 4 | 3 | 424, 1016, 3553–3557 |
| `cardText` | 4 | 3 | 930–940, 3562, 7173 |
| `detailPageContent` | 4 | 3 | 1768, 4703, 4976–4983 |
| `dialog-fullscreen` | 4 | 3 | 3396, 6799–6809, 6835 |
| `emby-scrollbuttons` | 4 | 3 | 1831–1836, 7194, 7730 |
| `folder` | 4 | 3 | 1931–1936, 3663, 3727 |
| `formDialogFooter` | 4 | 3 | 3454, 3937, 7405–7429 |
| `infoWrapper` | 4 | 3 | 2173–2178, 2436, 2464 |
| `listItemImage` | 4 | 3 | 2807–2812, 4481, 7388 |
| `musicParentName` | 4 | 3 | 2007, 2542, 5616–5625 |
| `programGuideSection` | 4 | 3 | 2497–2512, 4872, 4899 |
| `toast` | 4 | 3 | 5150, 6799–6809, 6835 |
| `cardFooter` | 3 | 3 | 3573, 6903, 6938 |
| `collectionItems` | 3 | 3 | 1778, 4872, 4908 |
| `defaultCardBackground` | 3 | 3 | 3684, 6123, 6222 |
| `detailPageSecondaryContainer` | 3 | 3 | 1621, 1648, 1768 |
| `emby-input` | 3 | 3 | 5410, 5439, 7471 |
| `formDialogFooterItem` | 3 | 3 | 3454, 3722, 3848 |
| `formDialogHeader` | 3 | 3 | 3937, 7353, 7405 |
| `iconOsd` | 3 | 3 | 5903, 7353, 7405 |
| `live_tv` | 3 | 3 | 2007, 2529, 3971 |
| `myPreferencesMenuPage` | 3 | 3 | 397, 4681, 4997 |
| `page` | 3 | 3 | 1012, 2704, 6855 |
| `playerStats` | 3 | 3 | 5903, 7405, 7441 |
| `sectionTitle-cards` | 3 | 3 | 1746, 5066, 5126 |
| `sectionTitleContainer` | 3 | 3 | 1778, 1836, 4908 |
| `tsx` | 3 | 3 | 1090, 4379, 4456 |
| `itemExternalLinks` | 13 | 2 | 3106–3184, 3336 |
| `checkboxOutline` | 10 | 2 | 3507–3548, 3579–3609 |
| `itemBackdrop` | 9 | 2 | 1973–2028, 2203 |
| `mdl-slider` | 9 | 2 | 2903, 2958–3016 |
| `listItemIcon` | 8 | 2 | 3967–3971, 4621–4681 |
| `sliderContainer` | 8 | 2 | 2907, 2935–3000 |
| `cardOverlayButton-br` | 7 | 2 | 1028, 1057–1101 |
| `detail-clamp-text` | 7 | 2 | 3272–3298, 3324–3328 |
| `divUsers` | 7 | 2 | 6004–6008, 7157–7184 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3544–3548, 3578–3597 |
| `countIndicator` | 6 | 2 | 773–803, 7405–7429 |
| `detailPagePrimaryContainer` | 6 | 2 | 1598–1644, 2436 |
| `detailsGroupItem` | 6 | 2 | 4734, 4802–4839 |
| `headerButton` | 6 | 2 | 563–643, 6484 |
| `headerLeft` | 6 | 2 | 1696–1733, 6692 |
| `selectionCommandsPanel` | 6 | 2 | 3464–3498, 7353 |
| `trackSelections` | 6 | 2 | 4707–4734, 4867–4872 |
| `withBackdrop` | 6 | 2 | 2612, 2654–2672 |
| `detailSection` | 5 | 2 | 4690–4699, 4852–4872 |
| `fullSyncIndicator` | 5 | 2 | 773–796, 7405–7429 |
| `mainDrawer-scrollContainer` | 5 | 2 | 3066, 7070–7087 |
| `mediaInfoItem` | 5 | 2 | 1850–1893, 6947 |
| `overview-expand` | 5 | 2 | 3304–3328, 4772 |
| `scrollX` | 5 | 2 | 1751, 1789–1809 |
| `videoIndicator` | 5 | 2 | 3652–3680, 7405 |
| `withSectionTabs` | 5 | 2 | 2663–2680, 6367 |
| `alphaPickerButton` | 4 | 2 | 643, 4923–4935 |
| `backgroundProgress` | 4 | 2 | 2818–2830, 2860 |
| `emby-select` | 4 | 2 | 5410–5422, 7471 |
| `emby-tab-button-active` | 4 | 2 | 3909, 6574–6588 |
| `mediaSourceIndicator` | 4 | 2 | 773–796, 7405 |
| `play_arrow` | 4 | 2 | 3689–3705, 3876 |
| `playbackProgress` | 4 | 2 | 2818–2830, 2865 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4508–4513, 6216–6222 |
| `programCell` | 4 | 2 | 5666, 5725–5734 |
| `section0` | 4 | 2 | 982–1012, 6855 |
| `visualLoginForm` | 4 | 2 | 5995–6012, 6053 |
| `cardOverlayButtonIcon` | 3 | 2 | 1028–1040, 1101 |
| `castCollapsible` | 3 | 2 | 839, 3548–3557 |
| `emby-scrollbuttons-button` | 3 | 2 | 1840, 7737–7744 |
| `emby-textarea` | 3 | 2 | 5401–5410, 5439 |
| `guestCastContent` | 3 | 2 | 839, 3548–3557 |
| `guide-channelHeaderCell` | 3 | 2 | 643, 5700–5716 |
| `guide-date-tab-button` | 3 | 2 | 643, 3909–3917 |
| `headerUserButton` | 3 | 2 | 563–576, 5001 |
| `manualLoginForm` | 3 | 2 | 5995–6012, 6053 |
| `overview` | 3 | 2 | 3324–3328, 4782 |
| `add` | 2 | 2 | 1751, 6947 |
| `alphaPicker-fixed-right` | 2 | 2 | 2704, 4935 |
| `backdropImageFadeIn` | 2 | 2 | 2757, 7445 |
| `book` | 2 | 2 | 2007, 2529 |
| `btnDeleteImage` | 2 | 2 | 3709, 3923 |
| `cardContent` | 2 | 2 | 839, 871 |
| `cardOverlayButton` | 2 | 2 | 1042, 1078 |
| `cardOverlayButton-hover` | 2 | 2 | 925, 1057 |
| `chevron_right` | 2 | 2 | 5096, 5140 |
| `classList` | 2 | 2 | 1751, 6947 |
| `collapseContent` | 2 | 2 | 3459, 3935 |
| `collectionItemsContainer` | 2 | 2 | 1778, 4912 |
| `content-primary` | 2 | 2 | 4976, 5032 |
| `editorsChoiceItemOverview` | 2 | 2 | 7667, 7748 |
| `endsAt` | 2 | 2 | 1871, 6947 |
| `fieldDescription` | 2 | 2 | 302, 7471 |
| `formDialogFooter-clear` | 2 | 2 | 3454, 3937 |
| `guide-programNameCaret` | 2 | 2 | 302, 5682 |
| `headroom` | 2 | 2 | 6355, 6392 |
| `indicator` | 2 | 2 | 803, 3641 |
| `mediaInfoOfficialRating` | 2 | 2 | 1871, 6947 |
| `navMenuOption-selected` | 2 | 2 | 4686, 7081 |
| `nowPlayingInfoContainer` | 2 | 2 | 3097, 6153 |
| `org` | 2 | 2 | 3133, 3163 |
| `paperList` | 2 | 2 | 848, 3948 |
| `playlist` | 2 | 2 | 4503, 6131 |
| `programSecondaryTitle` | 2 | 2 | 302, 5734 |
| `queue` | 2 | 2 | 2007, 2529 |
| `reactRoot` | 2 | 2 | 4379, 6698 |
| `readOnlyContent` | 2 | 2 | 3979, 6621 |
| `recordingFields` | 2 | 2 | 4726, 4867 |
| `runtime` | 2 | 2 | 6065, 6093 |
| `sectionTitleContainer-cards` | 2 | 2 | 5061, 5126 |
| `sidebarHeader` | 2 | 2 | 4071, 7087 |
| `tagline` | 2 | 2 | 2603, 4782 |
| `upNextDialog-title` | 2 | 2 | 5182, 5216 |
| `vertical-list` | 2 | 2 | 1813, 7573 |
| `vertical-wrap` | 2 | 2 | 769, 1778 |
| `videoOsdBottom` | 2 | 2 | 3089, 6322 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3089, 6322 |
| `userPreferencesPage` | 12 | 1 | 7456–7552 |
| `checkboxContainer` | 7 | 1 | 3536–3573 |
| `itemDetailsGroup` | 7 | 1 | 4786–4872 |
| `itemProgressBar` | 6 | 1 | 2807–2841 |
| `streaming-lookup-container` | 6 | 1 | 3191–3236 |
| `trackSelectionFieldContainer` | 6 | 1 | 4745–4768 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7704–7744 |
| `innerCardFooter` | 5 | 1 | 3349–3378 |
| `chapterCardImageContainer` | 4 | 1 | 3349–3378 |
| `emby-select-withcolor` | 4 | 1 | 5410–5457 |
| `endTimeText` | 4 | 1 | 6065–6093 |
| `mainDetailButtons` | 4 | 1 | 3872–3886 |
| `overview-controls` | 4 | 1 | 3324–3336 |
| `startTimeText` | 4 | 1 | 6065–6087 |
| `button-flat` | 3 | 1 | 3070–3080 |
| `cardIndicators` | 3 | 1 | 3626–3636 |
| `cardOverlayFab-primary` | 3 | 1 | 1020–1042 |
| `com` | 3 | 1 | 3139–3157 |
| `content` | 3 | 1 | 4808–4839 |
| `discover-card` | 3 | 1 | 7755–7778 |
| `fab` | 3 | 1 | 3731–3744 |
| `listChildrenCollapsible` | 3 | 1 | 4857–4872 |
| `mdl-slider-background-flex` | 3 | 1 | 2927–2940 |
| `mediaInfoCriticRating` | 3 | 1 | 1912–1921 |
| `nextUpSection` | 3 | 1 | 4852–4872 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 6117–6127 |
| `serverInfo` | 3 | 1 | 3952–3961 |
| `transcodingProgress` | 3 | 1 | 2818–2830 |
