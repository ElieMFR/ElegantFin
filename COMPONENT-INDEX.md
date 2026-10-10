# Index des composants — ElegantFin Cinema Edition v1.3.19

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.19.css` — 7681 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 36 | 14 | 428–510, 748, 865, 1517–1537, 2127–2160, 2187–2191, 2467–2485, 2521, 6653, 6911–6927, 7005–7027, 7057–7064, 7154, 7559 |
| `cardScalable` | 28 | 13 | 428–439, 487–510, 811–855, 881–919, 2485, 3532, 3643, 3722, 5841, 6667–6677, 6746, 6911, 7048–7064 |
| `itemDetailPage` | 21 | 13 | 1580, 1666, 1745, 1772, 2000–2036, 2071–2086, 2122, 2223, 2534, 3977–3988, 4645, 4932, 7387–7425 |
| `material-icons` | 17 | 13 | 364–383, 1736, 1834, 1886, 3489, 3648, 3722–3728, 3834, 3992, 4525, 5035, 5069–5079, 5659 |
| `cardImageContainer` | 22 | 12 | 482, 833, 861–890, 919, 976–1006, 5966–5970, 6050, 6659, 6738–6746, 6786, 6911–6927, 7048 |
| `skinHeader` | 16 | 10 | 284, 4337, 4383–4410, 5849, 6259, 6315–6323, 6349–6374, 6729, 6878, 7496 |
| `nameContainer` | 27 | 9 | 694, 2230–2253, 2294, 2323, 2358–2404, 2441, 2472–2476, 5416–5468, 7387–7425 |
| `emby-button` | 12 | 9 | 620–637, 664–682, 3160, 3263–3270, 3668, 3703, 3856, 4543, 5251 |
| `js` | 9 | 9 | 331, 1652, 1745, 2294, 2898, 3622, 5659, 6830, 7074 |
| `card-hoverable` | 23 | 8 | 510, 821, 881–969, 5970, 6677, 6786–6821, 6911, 7200 |
| `parentName` | 23 | 8 | 694, 2235–2253, 2294, 2323, 2358–2404, 5422–5468, 5541, 7387–7425 |
| `detailLogo` | 20 | 8 | 694, 2010–2036, 2071–2086, 2113–2122, 2223–2253, 2323, 2358–2404, 2472 |
| `listItem` | 19 | 8 | 302, 637, 2489, 4445–4471, 4502–4534, 4579, 4620, 7177–7194 |
| `detailPageWrapperContainer` | 17 | 8 | 694, 1548–1558, 2036, 2196, 2230–2253, 2323, 2358–2404, 2472 |
| `subtitle` | 16 | 8 | 2000–2010, 2122, 2235, 2294, 2413–2423, 2534, 5476–5509, 7387–7425 |
| `backdropCard` | 12 | 8 | 963–969, 1084, 2000–2010, 2139, 2223, 2476–2485, 2512, 2821 |
| `cardBox` | 12 | 8 | 428–476, 502, 748, 903, 1010, 6653, 6911, 7200 |
| `nowPlayingBar` | 8 | 8 | 318, 3084, 6102, 6692, 6780, 6864, 6890, 7159 |
| `loginPage` | 16 | 7 | 3801, 5853–5884, 5923, 5951–5970, 6682, 6725, 7037–7064 |
| `navMenuOption` | 12 | 6 | 637, 733–743, 4042, 4512–4534, 4626–4631, 6950–6961 |
| `paper-icon-button-light` | 11 | 6 | 582–637, 1666, 1736, 1834, 3429–3449, 5335 |
| `verticalSection` | 11 | 6 | 1740, 2723–2728, 4932, 6738, 6830, 7074 |
| `button-link` | 10 | 6 | 637, 664–682, 3034–3043, 3104–3114, 3160, 7350 |
| `person` | 8 | 6 | 2000–2021, 2223, 2476, 2521–2530, 3929, 7382 |
| `mainDrawer` | 7 | 6 | 3048, 4006, 4383, 6682–6692, 6937, 6976 |
| `scss` | 6 | 6 | 284, 776, 1036, 3538, 4048, 6830 |
| `detailImageContainer` | 20 | 5 | 2000–2021, 2127–2191, 2223, 2463–2485, 2512–2530 |
| `osdHeader` | 15 | 5 | 1709–1727, 6254–6323, 6349–6374, 6729, 7159 |
| `actionSheetMenuItem` | 10 | 5 | 637, 4445–4456, 4502, 4579–4620, 6710 |
| `sectionTabs` | 10 | 5 | 1803, 3780, 4410, 6295–6300, 6440–6471 |
| `cardImageIcon` | 8 | 5 | 420–424, 2476–2485, 2548, 3516, 6050 |
| `headerTop` | 8 | 5 | 4337, 4383, 6265–6290, 6341–6358, 6385–6389 |
| `sectionTitle` | 7 | 5 | 1740, 1813–1820, 4238, 5005–5013, 5918 |
| `emby-scroller-container` | 6 | 5 | 1740–1745, 1783, 2713, 6738, 6830 |
| `portraitCard` | 6 | 5 | 1084, 1168, 1924–1929, 2187, 2821 |
| `skinHeader-withBackground` | 5 | 5 | 1648, 3977, 5849, 6254, 6304 |
| `btnPlay` | 16 | 4 | 519–543, 582–637, 3732–3774, 3807–3834 |
| `cardOverlayContainer` | 12 | 4 | 937–969, 1014–1036, 1102, 7159–7177 |
| `itemName` | 11 | 4 | 694, 2294, 5422–5468, 5559–5576 |
| `backdropImage` | 10 | 4 | 2613–2640, 2667–2671, 6646, 6746–6754 |
| `emby-tab-button` | 10 | 4 | 637, 704–713, 3780, 6425–6466 |
| `upNextContainer` | 10 | 4 | 5097–5116, 5142–5168, 6682–6692, 6718 |
| `emby-scroller` | 9 | 4 | 1745, 1783–1789, 6980–7027, 7138–7154 |
| `backgroundContainer` | 8 | 4 | 2090, 2604, 2645–2663, 2695 |
| `detailRibbon` | 8 | 4 | 1605–1633, 1839, 1924–1936, 7382 |
| `listItemBodyText` | 7 | 4 | 4466–4485, 4525, 4600, 7194 |
| `skip-button` | 7 | 4 | 637, 3785, 5191–5208, 5235–5253 |
| `visualCardBox` | 7 | 4 | 428, 842–855, 881–886, 1010 |
| `button-submit` | 6 | 4 | 3801, 3888, 5951–5959, 7262–7276 |
| `cardText-secondary` | 6 | 4 | 302, 924, 3521–3525, 6808–6816 |
| `detailPagePrimaryContent` | 6 | 4 | 1620–1638, 2428, 4926, 6894 |
| `squareCard` | 6 | 4 | 865, 2476, 2512–2530, 5927–5931 |
| `skinHeader-blurred` | 5 | 4 | 5849, 6283–6290, 6878, 7159 |
| `appfooter` | 4 | 4 | 2764, 6399, 6769, 7159 |
| `itemsContainer` | 4 | 4 | 748, 1772, 1807, 4932 |
| `raised` | 4 | 4 | 637, 723, 3668, 3703 |
| `x` | 4 | 4 | 2294, 4048, 5524, 6830 |
| `detailButton` | 13 | 3 | 582–637, 3713–3774, 3830–3834 |
| `itemSelectionPanel` | 9 | 3 | 894–898, 3461, 3489–3532 |
| `pageTitle` | 8 | 3 | 1684–1727, 6315, 6374 |
| `sectionTitleTextButton` | 8 | 3 | 4988–4996, 5023–5035, 5069–5079 |
| `homePage` | 7 | 3 | 4337, 4383–4410, 6488 |
| `playedIndicator` | 7 | 3 | 776–790, 3605, 6911–6932 |
| `check` | 6 | 3 | 3489, 3722, 4579–4620 |
| `detailSectionContent` | 6 | 3 | 3295, 4727–4737, 4817–4827 |
| `emby-checkbox` | 6 | 3 | 3466, 3503–3507, 3556–3568 |
| `actionSheetContent` | 5 | 3 | 4571–4575, 6682–6692, 6718 |
| `cardText-first` | 5 | 3 | 924, 3495–3521, 6031 |
| `dialog` | 5 | 3 | 3345–3355, 6682–6692, 6718 |
| `guideProgramName` | 5 | 3 | 637, 5600–5611, 5654–5659 |
| `noHomeButtonHeader` | 5 | 3 | 1666, 6315, 6425–6433 |
| `overflowBackdropCard` | 5 | 3 | 963–969, 3499, 6026–6031 |
| `secondary` | 5 | 3 | 302, 4475–4485, 4525 |
| `album` | 4 | 3 | 2223, 2481–2485, 2521 |
| `cardPadder` | 4 | 3 | 424, 1010, 3512–3516 |
| `cardText` | 4 | 3 | 924–934, 3521, 7053 |
| `detailPageContent` | 4 | 3 | 1762, 4658, 4919–4926 |
| `dialog-fullscreen` | 4 | 3 | 3355, 6682–6692, 6718 |
| `emby-scrollbuttons` | 4 | 3 | 1825–1830, 7074, 7534 |
| `folder` | 4 | 3 | 1924–1929, 3622, 3686 |
| `formDialogFooter` | 4 | 3 | 3413, 3895, 7211–7235 |
| `infoWrapper` | 4 | 3 | 2166–2171, 2428, 2456 |
| `listItemImage` | 4 | 3 | 2798–2803, 4439, 7194 |
| `musicParentName` | 4 | 3 | 2000, 2534, 5541–5550 |
| `semiTransparent` | 4 | 3 | 1648, 5849, 6283–6304 |
| `toast` | 4 | 3 | 5089, 6682–6692, 6718 |
| `cardFooter` | 3 | 3 | 3532, 6786, 6821 |
| `defaultCardBackground` | 3 | 3 | 3643, 6046, 6145 |
| `detailPageSecondaryContainer` | 3 | 3 | 1615, 1642, 1762 |
| `formDialogFooterItem` | 3 | 3 | 3413, 3681, 3807 |
| `formDialogHeader` | 3 | 3 | 3895, 7159, 7211 |
| `iconOsd` | 3 | 3 | 5827, 7159, 7211 |
| `live_tv` | 3 | 3 | 2000, 2521, 3929 |
| `myPreferencesMenuPage` | 3 | 3 | 397, 4636, 4940 |
| `page` | 3 | 3 | 1006, 2695, 6738 |
| `playerStats` | 3 | 3 | 5827, 7211, 7247 |
| `sectionTitle-cards` | 3 | 3 | 1740, 5005, 5065 |
| `sectionTitleContainer` | 3 | 3 | 1772, 1830, 4851 |
| `tsx` | 3 | 3 | 1084, 4337, 4414 |
| `itemExternalLinks` | 13 | 2 | 3097–3175, 3295 |
| `checkboxOutline` | 10 | 2 | 3466–3507, 3538–3568 |
| `itemBackdrop` | 9 | 2 | 1966–2021, 2196 |
| `mdl-slider` | 9 | 2 | 2894, 2949–3007 |
| `listItemIcon` | 8 | 2 | 3925–3929, 4579–4636 |
| `sliderContainer` | 8 | 2 | 2898, 2926–2991 |
| `cardOverlayButton-br` | 7 | 2 | 1022, 1051–1095 |
| `detail-clamp-text` | 7 | 2 | 3231–3257, 3283–3287 |
| `divUsers` | 7 | 2 | 5927–5931, 7037–7064 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3503–3507, 3537–3556 |
| `countIndicator` | 6 | 2 | 767–797, 7211–7235 |
| `detailPagePrimaryContainer` | 6 | 2 | 1592–1638, 2428 |
| `detailsGroupItem` | 6 | 2 | 4689, 4757–4794 |
| `headerButton` | 6 | 2 | 557–637, 6367 |
| `headerLeft` | 6 | 2 | 1690–1727, 6575 |
| `selectionCommandsPanel` | 6 | 2 | 3423–3457, 7159 |
| `trackSelections` | 6 | 2 | 4662–4689, 4822–4827 |
| `withBackdrop` | 6 | 2 | 2604, 2645–2663 |
| `detailSection` | 5 | 2 | 4645–4654, 4807–4827 |
| `fullSyncIndicator` | 5 | 2 | 767–790, 7211–7235 |
| `mainDrawer-scrollContainer` | 5 | 2 | 3057, 6950–6967 |
| `mediaInfoItem` | 5 | 2 | 1843–1886, 6830 |
| `overview-expand` | 5 | 2 | 3263–3287, 4727 |
| `scrollX` | 5 | 2 | 1745, 1783–1803 |
| `videoIndicator` | 5 | 2 | 3611–3639, 7211 |
| `withSectionTabs` | 5 | 2 | 2654–2671, 6290 |
| `alphaPickerButton` | 4 | 2 | 637, 4866–4878 |
| `backgroundProgress` | 4 | 2 | 2809–2821, 2851 |
| `emby-tab-button-active` | 4 | 2 | 3867, 6457–6471 |
| `mediaSourceIndicator` | 4 | 2 | 767–790, 7211 |
| `play_arrow` | 4 | 2 | 3648–3664, 3834 |
| `playbackProgress` | 4 | 2 | 2809–2821, 2856 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4466–4471, 6139–6145 |
| `programCell` | 4 | 2 | 5591, 5650–5659 |
| `programGuideSection` | 4 | 2 | 2489–2504, 4827–4842 |
| `section0` | 4 | 2 | 976–1006, 6738 |
| `visualLoginForm` | 4 | 2 | 5918–5935, 5976 |
| `cardOverlayButtonIcon` | 3 | 2 | 1022–1034, 1095 |
| `castCollapsible` | 3 | 2 | 833, 3507–3516 |
| `collectionItems` | 3 | 2 | 1772, 4827–4851 |
| `emby-input` | 3 | 2 | 5349–5365, 7276 |
| `emby-scrollbuttons-button` | 3 | 2 | 1834, 7541–7548 |
| `guestCastContent` | 3 | 2 | 833, 3507–3516 |
| `guide-channelHeaderCell` | 3 | 2 | 637, 5625–5641 |
| `guide-date-tab-button` | 3 | 2 | 637, 3867–3875 |
| `headerUserButton` | 3 | 2 | 557–570, 4944 |
| `manualLoginForm` | 3 | 2 | 5918–5935, 5976 |
| `overview` | 3 | 2 | 3283–3287, 4737 |
| `add` | 2 | 2 | 1745, 6830 |
| `alphaPicker-fixed-right` | 2 | 2 | 2695, 4878 |
| `backdropImageFadeIn` | 2 | 2 | 2748, 7251 |
| `book` | 2 | 2 | 2000, 2521 |
| `btnDeleteImage` | 2 | 2 | 3668, 3881 |
| `cardContent` | 2 | 2 | 833, 865 |
| `cardOverlayButton` | 2 | 2 | 1036, 1072 |
| `cardOverlayButton-hover` | 2 | 2 | 919, 1051 |
| `chevron_right` | 2 | 2 | 5035, 5079 |
| `classList` | 2 | 2 | 1745, 6830 |
| `collapseContent` | 2 | 2 | 3418, 3893 |
| `collectionItemsContainer` | 2 | 2 | 1772, 4855 |
| `content-primary` | 2 | 2 | 4919, 4971 |
| `editorsChoiceItemOverview` | 2 | 2 | 7471, 7552 |
| `emby-select` | 2 | 2 | 5349, 7276 |
| `endsAt` | 2 | 2 | 1864, 6830 |
| `fieldDescription` | 2 | 2 | 302, 7276 |
| `formDialogFooter-clear` | 2 | 2 | 3413, 3895 |
| `guide-programNameCaret` | 2 | 2 | 302, 5607 |
| `headroom` | 2 | 2 | 6278, 6315 |
| `indicator` | 2 | 2 | 797, 3600 |
| `mediaInfoOfficialRating` | 2 | 2 | 1864, 6830 |
| `navMenuOption-selected` | 2 | 2 | 4641, 6961 |
| `nowPlayingInfoContainer` | 2 | 2 | 3088, 6076 |
| `org` | 2 | 2 | 3124, 3154 |
| `paperList` | 2 | 2 | 842, 3906 |
| `playlist` | 2 | 2 | 4461, 6054 |
| `programSecondaryTitle` | 2 | 2 | 302, 5659 |
| `queue` | 2 | 2 | 2000, 2521 |
| `reactRoot` | 2 | 2 | 4337, 6581 |
| `readOnlyContent` | 2 | 2 | 3937, 6504 |
| `recordingFields` | 2 | 2 | 4681, 4822 |
| `runtime` | 2 | 2 | 5988, 6016 |
| `sectionTitleContainer-cards` | 2 | 2 | 5000, 5065 |
| `sidebarHeader` | 2 | 2 | 4029, 6967 |
| `tagline` | 2 | 2 | 2595, 4737 |
| `upNextDialog-title` | 2 | 2 | 5121, 5155 |
| `vertical-list` | 2 | 2 | 1807, 7377 |
| `vertical-wrap` | 2 | 2 | 763, 1772 |
| `videoOsdBottom` | 2 | 2 | 3080, 6245 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3080, 6245 |
| `userPreferencesPage` | 12 | 1 | 7262–7357 |
| `checkboxContainer` | 7 | 1 | 3495–3532 |
| `itemDetailsGroup` | 7 | 1 | 4741–4827 |
| `itemProgressBar` | 6 | 1 | 2798–2832 |
| `streaming-lookup-container` | 6 | 1 | 3182–3220 |
| `trackSelectionFieldContainer` | 6 | 1 | 4700–4723 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7508–7548 |
| `innerCardFooter` | 5 | 1 | 3308–3337 |
| `chapterCardImageContainer` | 4 | 1 | 3308–3337 |
| `endTimeText` | 4 | 1 | 5988–6016 |
| `mainDetailButtons` | 4 | 1 | 3830–3844 |
| `overview-controls` | 4 | 1 | 3283–3295 |
| `startTimeText` | 4 | 1 | 5988–6010 |
| `button-flat` | 3 | 1 | 3061–3071 |
| `cardIndicators` | 3 | 1 | 3585–3595 |
| `cardOverlayFab-primary` | 3 | 1 | 1014–1036 |
| `com` | 3 | 1 | 3130–3148 |
| `content` | 3 | 1 | 4763–4794 |
| `discover-card` | 3 | 1 | 7559–7582 |
| `emby-select-withcolor` | 3 | 1 | 5349–5383 |
| `emby-textarea` | 3 | 1 | 5340–5365 |
| `fab` | 3 | 1 | 3690–3703 |
| `listChildrenCollapsible` | 3 | 1 | 4812–4827 |
| `mdl-slider-background-flex` | 3 | 1 | 2918–2931 |
| `mediaInfoCriticRating` | 3 | 1 | 1905–1914 |
| `nextUpSection` | 3 | 1 | 4807–4827 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 6040–6050 |
| `serverInfo` | 3 | 1 | 3910–3919 |
| `transcodingProgress` | 3 | 1 | 2809–2821 |
