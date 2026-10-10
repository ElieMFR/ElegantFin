# Index des composants — ElegantFin Cinema Edition v1.3.20

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.20.css` — 7728 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 36 | 14 | 428–510, 748, 865, 1517–1537, 2128–2161, 2188–2192, 2469–2487, 2523, 6695, 6953–6972, 7050–7072, 7102–7109, 7199, 7606 |
| `cardScalable` | 28 | 13 | 428–439, 487–510, 811–855, 881–919, 2487, 3542, 3653, 3732, 5882, 6709–6719, 6788, 6953, 7093–7109 |
| `itemDetailPage` | 21 | 13 | 1580, 1666, 1745, 1772, 2001–2037, 2072–2087, 2123, 2224, 2536, 3988–3999, 4659, 4958, 7434–7472 |
| `material-icons` | 17 | 13 | 364–383, 1736, 1834, 1887, 3499, 3658, 3732–3738, 3845, 4003, 4536, 5061, 5095–5105, 5699 |
| `cardImageContainer` | 22 | 12 | 482, 833, 861–890, 919, 976–1006, 6008–6012, 6092, 6701, 6780–6788, 6828, 6953–6972, 7093 |
| `skinHeader` | 16 | 10 | 284, 4348, 4394–4421, 5890, 6301, 6357–6365, 6391–6416, 6771, 6920, 7543 |
| `nameContainer` | 27 | 9 | 694, 2231–2254, 2295, 2324, 2359–2406, 2443, 2474–2478, 5455–5508, 7434–7472 |
| `emby-button` | 12 | 9 | 620–637, 664–682, 3163, 3273–3280, 3678, 3713, 3867, 4554, 5277 |
| `js` | 9 | 9 | 331, 1652, 1745, 2295, 2901, 3632, 5699, 6872, 7119 |
| `card-hoverable` | 23 | 8 | 510, 821, 881–969, 6012, 6719, 6828–6863, 6953, 7245 |
| `parentName` | 23 | 8 | 694, 2236–2254, 2295, 2324, 2359–2406, 5461–5508, 5581, 7434–7472 |
| `detailLogo` | 20 | 8 | 694, 2011–2037, 2072–2087, 2114–2123, 2224–2254, 2324, 2359–2406, 2474 |
| `listItem` | 19 | 8 | 302, 637, 2491, 4456–4482, 4513–4545, 4590, 4634, 7222–7239 |
| `detailPageWrapperContainer` | 17 | 8 | 694, 1548–1558, 2037, 2197, 2231–2254, 2324, 2359–2406, 2474 |
| `subtitle` | 16 | 8 | 2001–2011, 2123, 2236, 2295, 2415–2425, 2536, 5516–5549, 7434–7472 |
| `backdropCard` | 12 | 8 | 963–969, 1084, 2001–2011, 2140, 2224, 2478–2487, 2514, 2824 |
| `cardBox` | 12 | 8 | 428–476, 502, 748, 903, 1010, 6695, 6953, 7245 |
| `nowPlayingBar` | 8 | 8 | 318, 3087, 6144, 6734, 6822, 6906, 6932, 7204 |
| `loginPage` | 16 | 7 | 3811, 5894–5925, 5965, 5993–6012, 6724, 6767, 7082–7109 |
| `navMenuOption` | 12 | 6 | 637, 733–743, 4053, 4523–4545, 4640–4645, 6995–7006 |
| `paper-icon-button-light` | 11 | 6 | 582–637, 1666, 1736, 1834, 3439–3459, 5361 |
| `verticalSection` | 11 | 6 | 1740, 2726–2731, 4958, 6780, 6872, 7119 |
| `button-link` | 10 | 6 | 637, 664–682, 3037–3046, 3107–3117, 3163, 7396 |
| `person` | 8 | 6 | 2001–2022, 2224, 2478, 2523–2532, 3940, 7429 |
| `mainDrawer` | 7 | 6 | 3051, 4017, 4394, 6724–6734, 6982, 7021 |
| `scss` | 6 | 6 | 284, 776, 1036, 3548, 4059, 6872 |
| `detailImageContainer` | 20 | 5 | 2001–2022, 2128–2192, 2224, 2465–2487, 2514–2532 |
| `osdHeader` | 15 | 5 | 1709–1727, 6296–6365, 6391–6416, 6771, 7204 |
| `actionSheetMenuItem` | 10 | 5 | 637, 4456–4467, 4513, 4590–4634, 6752 |
| `sectionTabs` | 10 | 5 | 1803, 3790, 4421, 6337–6342, 6482–6513 |
| `cardImageIcon` | 8 | 5 | 420–424, 2478–2487, 2550, 3526, 6092 |
| `headerTop` | 8 | 5 | 4348, 4394, 6307–6332, 6383–6400, 6427–6431 |
| `sectionTitle` | 7 | 5 | 1740, 1813–1820, 4249, 5031–5039, 5960 |
| `emby-scroller-container` | 6 | 5 | 1740–1745, 1783, 2716, 6780, 6872 |
| `portraitCard` | 6 | 5 | 1084, 1168, 1925–1930, 2188, 2824 |
| `skinHeader-withBackground` | 5 | 5 | 1648, 3988, 5890, 6296, 6346 |
| `btnPlay` | 16 | 4 | 519–543, 582–637, 3742–3784, 3817–3845 |
| `cardOverlayContainer` | 12 | 4 | 937–969, 1014–1036, 1102, 7204–7222 |
| `itemName` | 11 | 4 | 694, 2295, 5461–5508, 5599–5616 |
| `backdropImage` | 10 | 4 | 2615–2643, 2670–2674, 6688, 6788–6796 |
| `emby-tab-button` | 10 | 4 | 637, 704–713, 3790, 6467–6508 |
| `upNextContainer` | 10 | 4 | 5123–5142, 5168–5194, 6724–6734, 6760 |
| `emby-scroller` | 9 | 4 | 1745, 1783–1789, 7025–7072, 7183–7199 |
| `backgroundContainer` | 8 | 4 | 2091, 2606, 2648–2666, 2698 |
| `detailRibbon` | 8 | 4 | 1605–1633, 1840, 1925–1937, 7429 |
| `listItemBodyText` | 7 | 4 | 4477–4496, 4536, 4611, 7239 |
| `skip-button` | 7 | 4 | 637, 3795, 5217–5234, 5261–5279 |
| `visualCardBox` | 7 | 4 | 428, 842–855, 881–886, 1010 |
| `button-submit` | 6 | 4 | 3811, 3899, 5993–6001, 7307–7322 |
| `cardText-secondary` | 6 | 4 | 302, 924, 3531–3535, 6850–6858 |
| `detailPagePrimaryContent` | 6 | 4 | 1620–1638, 2430, 4952, 6936 |
| `squareCard` | 6 | 4 | 865, 2478, 2514–2532, 5969–5973 |
| `skinHeader-blurred` | 5 | 4 | 5890, 6325–6332, 6920, 7204 |
| `appfooter` | 4 | 4 | 2767, 6441, 6811, 7204 |
| `itemsContainer` | 4 | 4 | 748, 1772, 1807, 4958 |
| `raised` | 4 | 4 | 637, 723, 3678, 3713 |
| `x` | 4 | 4 | 2295, 4059, 5564, 6872 |
| `detailButton` | 13 | 3 | 582–637, 3723–3784, 3841–3845 |
| `itemSelectionPanel` | 9 | 3 | 894–898, 3471, 3499–3542 |
| `pageTitle` | 8 | 3 | 1684–1727, 6357, 6416 |
| `sectionTitleTextButton` | 8 | 3 | 5014–5022, 5049–5061, 5095–5105 |
| `homePage` | 7 | 3 | 4348, 4394–4421, 6530 |
| `playedIndicator` | 7 | 3 | 776–790, 3615, 6953–6977 |
| `check` | 6 | 3 | 3499, 3732, 4590–4634 |
| `detailSectionContent` | 6 | 3 | 3305, 4741–4751, 4831–4841 |
| `emby-checkbox` | 6 | 3 | 3476, 3513–3517, 3566–3578 |
| `actionSheetContent` | 5 | 3 | 4582–4586, 6724–6734, 6760 |
| `cardText-first` | 5 | 3 | 924, 3505–3531, 6073 |
| `dialog` | 5 | 3 | 3355–3365, 6724–6734, 6760 |
| `guideProgramName` | 5 | 3 | 637, 5640–5651, 5694–5699 |
| `noHomeButtonHeader` | 5 | 3 | 1666, 6357, 6467–6475 |
| `overflowBackdropCard` | 5 | 3 | 963–969, 3509, 6068–6073 |
| `secondary` | 5 | 3 | 302, 4486–4496, 4536 |
| `album` | 4 | 3 | 2224, 2483–2487, 2523 |
| `cardPadder` | 4 | 3 | 424, 1010, 3522–3526 |
| `cardText` | 4 | 3 | 924–934, 3531, 7098 |
| `detailPageContent` | 4 | 3 | 1762, 4672, 4945–4952 |
| `dialog-fullscreen` | 4 | 3 | 3365, 6724–6734, 6760 |
| `emby-scrollbuttons` | 4 | 3 | 1825–1830, 7119, 7581 |
| `folder` | 4 | 3 | 1925–1930, 3632, 3696 |
| `formDialogFooter` | 4 | 3 | 3423, 3906, 7256–7280 |
| `infoWrapper` | 4 | 3 | 2167–2172, 2430, 2458 |
| `listItemImage` | 4 | 3 | 2801–2806, 4450, 7239 |
| `musicParentName` | 4 | 3 | 2001, 2536, 5581–5590 |
| `programGuideSection` | 4 | 3 | 2491–2506, 4841, 4868 |
| `semiTransparent` | 4 | 3 | 1648, 5890, 6325–6346 |
| `toast` | 4 | 3 | 5115, 6724–6734, 6760 |
| `cardFooter` | 3 | 3 | 3542, 6828, 6863 |
| `collectionItems` | 3 | 3 | 1772, 4841, 4877 |
| `defaultCardBackground` | 3 | 3 | 3653, 6088, 6187 |
| `detailPageSecondaryContainer` | 3 | 3 | 1615, 1642, 1762 |
| `emby-input` | 3 | 3 | 5375, 5404, 7322 |
| `formDialogFooterItem` | 3 | 3 | 3423, 3691, 3817 |
| `formDialogHeader` | 3 | 3 | 3906, 7204, 7256 |
| `iconOsd` | 3 | 3 | 5868, 7204, 7256 |
| `live_tv` | 3 | 3 | 2001, 2523, 3940 |
| `myPreferencesMenuPage` | 3 | 3 | 397, 4650, 4966 |
| `page` | 3 | 3 | 1006, 2698, 6780 |
| `playerStats` | 3 | 3 | 5868, 7256, 7292 |
| `sectionTitle-cards` | 3 | 3 | 1740, 5031, 5091 |
| `sectionTitleContainer` | 3 | 3 | 1772, 1830, 4877 |
| `tsx` | 3 | 3 | 1084, 4348, 4425 |
| `itemExternalLinks` | 13 | 2 | 3100–3178, 3305 |
| `checkboxOutline` | 10 | 2 | 3476–3517, 3548–3578 |
| `itemBackdrop` | 9 | 2 | 1967–2022, 2197 |
| `mdl-slider` | 9 | 2 | 2897, 2952–3010 |
| `listItemIcon` | 8 | 2 | 3936–3940, 4590–4650 |
| `sliderContainer` | 8 | 2 | 2901, 2929–2994 |
| `cardOverlayButton-br` | 7 | 2 | 1022, 1051–1095 |
| `detail-clamp-text` | 7 | 2 | 3241–3267, 3293–3297 |
| `divUsers` | 7 | 2 | 5969–5973, 7082–7109 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3513–3517, 3547–3566 |
| `countIndicator` | 6 | 2 | 767–797, 7256–7280 |
| `detailPagePrimaryContainer` | 6 | 2 | 1592–1638, 2430 |
| `detailsGroupItem` | 6 | 2 | 4703, 4771–4808 |
| `headerButton` | 6 | 2 | 557–637, 6409 |
| `headerLeft` | 6 | 2 | 1690–1727, 6617 |
| `selectionCommandsPanel` | 6 | 2 | 3433–3467, 7204 |
| `trackSelections` | 6 | 2 | 4676–4703, 4836–4841 |
| `withBackdrop` | 6 | 2 | 2606, 2648–2666 |
| `detailSection` | 5 | 2 | 4659–4668, 4821–4841 |
| `fullSyncIndicator` | 5 | 2 | 767–790, 7256–7280 |
| `mainDrawer-scrollContainer` | 5 | 2 | 3060, 6995–7012 |
| `mediaInfoItem` | 5 | 2 | 1844–1887, 6872 |
| `overview-expand` | 5 | 2 | 3273–3297, 4741 |
| `scrollX` | 5 | 2 | 1745, 1783–1803 |
| `videoIndicator` | 5 | 2 | 3621–3649, 7256 |
| `withSectionTabs` | 5 | 2 | 2657–2674, 6332 |
| `alphaPickerButton` | 4 | 2 | 637, 4892–4904 |
| `backgroundProgress` | 4 | 2 | 2812–2824, 2854 |
| `emby-select` | 4 | 2 | 5375–5387, 7322 |
| `emby-tab-button-active` | 4 | 2 | 3878, 6499–6513 |
| `mediaSourceIndicator` | 4 | 2 | 767–790, 7256 |
| `play_arrow` | 4 | 2 | 3658–3674, 3845 |
| `playbackProgress` | 4 | 2 | 2812–2824, 2859 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4477–4482, 6181–6187 |
| `programCell` | 4 | 2 | 5631, 5690–5699 |
| `section0` | 4 | 2 | 976–1006, 6780 |
| `visualLoginForm` | 4 | 2 | 5960–5977, 6018 |
| `cardOverlayButtonIcon` | 3 | 2 | 1022–1034, 1095 |
| `castCollapsible` | 3 | 2 | 833, 3517–3526 |
| `emby-scrollbuttons-button` | 3 | 2 | 1834, 7588–7595 |
| `emby-textarea` | 3 | 2 | 5366–5375, 5404 |
| `guestCastContent` | 3 | 2 | 833, 3517–3526 |
| `guide-channelHeaderCell` | 3 | 2 | 637, 5665–5681 |
| `guide-date-tab-button` | 3 | 2 | 637, 3878–3886 |
| `headerUserButton` | 3 | 2 | 557–570, 4970 |
| `manualLoginForm` | 3 | 2 | 5960–5977, 6018 |
| `overview` | 3 | 2 | 3293–3297, 4751 |
| `add` | 2 | 2 | 1745, 6872 |
| `alphaPicker-fixed-right` | 2 | 2 | 2698, 4904 |
| `backdropImageFadeIn` | 2 | 2 | 2751, 7296 |
| `book` | 2 | 2 | 2001, 2523 |
| `btnDeleteImage` | 2 | 2 | 3678, 3892 |
| `cardContent` | 2 | 2 | 833, 865 |
| `cardOverlayButton` | 2 | 2 | 1036, 1072 |
| `cardOverlayButton-hover` | 2 | 2 | 919, 1051 |
| `chevron_right` | 2 | 2 | 5061, 5105 |
| `classList` | 2 | 2 | 1745, 6872 |
| `collapseContent` | 2 | 2 | 3428, 3904 |
| `collectionItemsContainer` | 2 | 2 | 1772, 4881 |
| `content-primary` | 2 | 2 | 4945, 4997 |
| `editorsChoiceItemOverview` | 2 | 2 | 7518, 7599 |
| `endsAt` | 2 | 2 | 1865, 6872 |
| `fieldDescription` | 2 | 2 | 302, 7322 |
| `formDialogFooter-clear` | 2 | 2 | 3423, 3906 |
| `guide-programNameCaret` | 2 | 2 | 302, 5647 |
| `headroom` | 2 | 2 | 6320, 6357 |
| `indicator` | 2 | 2 | 797, 3610 |
| `mediaInfoOfficialRating` | 2 | 2 | 1865, 6872 |
| `navMenuOption-selected` | 2 | 2 | 4655, 7006 |
| `nowPlayingInfoContainer` | 2 | 2 | 3091, 6118 |
| `org` | 2 | 2 | 3127, 3157 |
| `paperList` | 2 | 2 | 842, 3917 |
| `playlist` | 2 | 2 | 4472, 6096 |
| `programSecondaryTitle` | 2 | 2 | 302, 5699 |
| `queue` | 2 | 2 | 2001, 2523 |
| `reactRoot` | 2 | 2 | 4348, 6623 |
| `readOnlyContent` | 2 | 2 | 3948, 6546 |
| `recordingFields` | 2 | 2 | 4695, 4836 |
| `runtime` | 2 | 2 | 6030, 6058 |
| `sectionTitleContainer-cards` | 2 | 2 | 5026, 5091 |
| `sidebarHeader` | 2 | 2 | 4040, 7012 |
| `tagline` | 2 | 2 | 2597, 4751 |
| `upNextDialog-title` | 2 | 2 | 5147, 5181 |
| `vertical-list` | 2 | 2 | 1807, 7424 |
| `vertical-wrap` | 2 | 2 | 763, 1772 |
| `videoOsdBottom` | 2 | 2 | 3083, 6287 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3083, 6287 |
| `userPreferencesPage` | 12 | 1 | 7307–7403 |
| `checkboxContainer` | 7 | 1 | 3505–3542 |
| `itemDetailsGroup` | 7 | 1 | 4755–4841 |
| `itemProgressBar` | 6 | 1 | 2801–2835 |
| `streaming-lookup-container` | 6 | 1 | 3185–3230 |
| `trackSelectionFieldContainer` | 6 | 1 | 4714–4737 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7555–7595 |
| `innerCardFooter` | 5 | 1 | 3318–3347 |
| `chapterCardImageContainer` | 4 | 1 | 3318–3347 |
| `emby-select-withcolor` | 4 | 1 | 5375–5422 |
| `endTimeText` | 4 | 1 | 6030–6058 |
| `mainDetailButtons` | 4 | 1 | 3841–3855 |
| `overview-controls` | 4 | 1 | 3293–3305 |
| `startTimeText` | 4 | 1 | 6030–6052 |
| `button-flat` | 3 | 1 | 3064–3074 |
| `cardIndicators` | 3 | 1 | 3595–3605 |
| `cardOverlayFab-primary` | 3 | 1 | 1014–1036 |
| `com` | 3 | 1 | 3133–3151 |
| `content` | 3 | 1 | 4777–4808 |
| `discover-card` | 3 | 1 | 7606–7629 |
| `fab` | 3 | 1 | 3700–3713 |
| `listChildrenCollapsible` | 3 | 1 | 4826–4841 |
| `mdl-slider-background-flex` | 3 | 1 | 2921–2934 |
| `mediaInfoCriticRating` | 3 | 1 | 1906–1915 |
| `nextUpSection` | 3 | 1 | 4821–4841 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 6082–6092 |
| `serverInfo` | 3 | 1 | 3921–3930 |
| `transcodingProgress` | 3 | 1 | 2812–2824 |
