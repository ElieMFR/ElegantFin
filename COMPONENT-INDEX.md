# Index des composants — ElegantFin Cinema Edition v1.3.22

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.22.css` — 7813 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 36 | 14 | 428–510, 748, 865, 1517–1537, 2128–2161, 2188–2192, 2469–2487, 2523, 6706, 6964–6983, 7061–7083, 7113–7120, 7284, 7691 |
| `cardScalable` | 28 | 13 | 428–439, 487–510, 811–855, 881–919, 2487, 3553, 3664, 3743, 5893, 6720–6730, 6799, 6964, 7104–7120 |
| `itemDetailPage` | 21 | 13 | 1580, 1666, 1745, 1772, 2001–2037, 2072–2087, 2123, 2224, 2536, 3999–4010, 4670, 4969, 7519–7557 |
| `material-icons` | 17 | 13 | 364–383, 1736, 1834, 1887, 3510, 3669, 3743–3749, 3856, 4014, 4547, 5072, 5106–5116, 5710 |
| `cardImageContainer` | 22 | 12 | 482, 833, 861–890, 919, 976–1006, 6019–6023, 6103, 6712, 6791–6799, 6839, 6964–6983, 7104 |
| `skinHeader` | 16 | 10 | 284, 4359, 4405–4432, 5901, 6312, 6368–6376, 6402–6427, 6782, 6931, 7628 |
| `nameContainer` | 27 | 9 | 694, 2231–2254, 2295, 2324, 2359–2406, 2443, 2474–2478, 5466–5519, 7519–7557 |
| `emby-button` | 12 | 9 | 620–637, 664–682, 3163, 3284–3291, 3689, 3724, 3878, 4565, 5288 |
| `js` | 9 | 9 | 331, 1652, 1745, 2295, 2901, 3643, 5710, 6883, 7130 |
| `card-hoverable` | 23 | 8 | 510, 821, 881–969, 6023, 6730, 6839–6874, 6964, 7330 |
| `parentName` | 23 | 8 | 694, 2236–2254, 2295, 2324, 2359–2406, 5472–5519, 5592, 7519–7557 |
| `detailLogo` | 20 | 8 | 694, 2011–2037, 2072–2087, 2114–2123, 2224–2254, 2324, 2359–2406, 2474 |
| `listItem` | 19 | 8 | 302, 637, 2491, 4467–4493, 4524–4556, 4601, 4645, 7307–7324 |
| `detailPageWrapperContainer` | 17 | 8 | 694, 1548–1558, 2037, 2197, 2231–2254, 2324, 2359–2406, 2474 |
| `subtitle` | 16 | 8 | 2001–2011, 2123, 2236, 2295, 2415–2425, 2536, 5527–5560, 7519–7557 |
| `backdropCard` | 12 | 8 | 963–969, 1084, 2001–2011, 2140, 2224, 2478–2487, 2514, 2824 |
| `cardBox` | 12 | 8 | 428–476, 502, 748, 903, 1010, 6706, 6964, 7330 |
| `nowPlayingBar` | 8 | 8 | 318, 3087, 6155, 6745, 6833, 6917, 6943, 7289 |
| `loginPage` | 16 | 7 | 3822, 5905–5936, 5976, 6004–6023, 6735, 6778, 7093–7120 |
| `navMenuOption` | 12 | 6 | 637, 733–743, 4064, 4534–4556, 4651–4656, 7006–7017 |
| `paper-icon-button-light` | 11 | 6 | 582–637, 1666, 1736, 1834, 3450–3470, 5372 |
| `verticalSection` | 11 | 6 | 1740, 2726–2731, 4969, 6791, 6883, 7130 |
| `button-link` | 10 | 6 | 637, 664–682, 3037–3046, 3107–3117, 3163, 7481 |
| `person` | 8 | 6 | 2001–2022, 2224, 2478, 2523–2532, 3951, 7514 |
| `mainDrawer` | 7 | 6 | 3051, 4028, 4405, 6735–6745, 6993, 7032 |
| `scss` | 6 | 6 | 284, 776, 1036, 3559, 4070, 6883 |
| `detailImageContainer` | 20 | 5 | 2001–2022, 2128–2192, 2224, 2465–2487, 2514–2532 |
| `osdHeader` | 15 | 5 | 1709–1727, 6307–6376, 6402–6427, 6782, 7289 |
| `actionSheetMenuItem` | 10 | 5 | 637, 4467–4478, 4524, 4601–4645, 6763 |
| `sectionTabs` | 10 | 5 | 1803, 3801, 4432, 6348–6353, 6493–6524 |
| `cardImageIcon` | 8 | 5 | 420–424, 2478–2487, 2550, 3537, 6103 |
| `headerTop` | 8 | 5 | 4359, 4405, 6318–6343, 6394–6411, 6438–6442 |
| `sectionTitle` | 7 | 5 | 1740, 1813–1820, 4260, 5042–5050, 5971 |
| `emby-scroller-container` | 6 | 5 | 1740–1745, 1783, 2716, 6791, 6883 |
| `portraitCard` | 6 | 5 | 1084, 1168, 1925–1930, 2188, 2824 |
| `skinHeader-withBackground` | 5 | 5 | 1648, 3999, 5901, 6307, 6357 |
| `btnPlay` | 16 | 4 | 519–543, 582–637, 3753–3795, 3828–3856 |
| `cardOverlayContainer` | 12 | 4 | 937–969, 1014–1036, 1102, 7289–7307 |
| `itemName` | 11 | 4 | 694, 2295, 5472–5519, 5610–5627 |
| `backdropImage` | 10 | 4 | 2615–2643, 2670–2674, 6699, 6799–6807 |
| `emby-tab-button` | 10 | 4 | 637, 704–713, 3801, 6478–6519 |
| `upNextContainer` | 10 | 4 | 5134–5153, 5179–5205, 6735–6745, 6771 |
| `emby-scroller` | 9 | 4 | 1745, 1783–1789, 7036–7083, 7268–7284 |
| `backgroundContainer` | 8 | 4 | 2091, 2606, 2648–2666, 2698 |
| `detailRibbon` | 8 | 4 | 1605–1633, 1840, 1925–1937, 7514 |
| `listItemBodyText` | 7 | 4 | 4488–4507, 4547, 4622, 7324 |
| `skip-button` | 7 | 4 | 637, 3806, 5228–5245, 5272–5290 |
| `visualCardBox` | 7 | 4 | 428, 842–855, 881–886, 1010 |
| `button-submit` | 6 | 4 | 3822, 3910, 6004–6012, 7392–7407 |
| `cardText-secondary` | 6 | 4 | 302, 924, 3542–3546, 6861–6869 |
| `detailPagePrimaryContent` | 6 | 4 | 1620–1638, 2430, 4963, 6947 |
| `squareCard` | 6 | 4 | 865, 2478, 2514–2532, 5980–5984 |
| `skinHeader-blurred` | 5 | 4 | 5901, 6336–6343, 6931, 7289 |
| `appfooter` | 4 | 4 | 2767, 6452, 6822, 7289 |
| `itemsContainer` | 4 | 4 | 748, 1772, 1807, 4969 |
| `raised` | 4 | 4 | 637, 723, 3689, 3724 |
| `x` | 4 | 4 | 2295, 4070, 5575, 6883 |
| `detailButton` | 13 | 3 | 582–637, 3734–3795, 3852–3856 |
| `itemSelectionPanel` | 9 | 3 | 894–898, 3482, 3510–3553 |
| `pageTitle` | 8 | 3 | 1684–1727, 6368, 6427 |
| `sectionTitleTextButton` | 8 | 3 | 5025–5033, 5060–5072, 5106–5116 |
| `homePage` | 7 | 3 | 4359, 4405–4432, 6541 |
| `playedIndicator` | 7 | 3 | 776–790, 3626, 6964–6988 |
| `check` | 6 | 3 | 3510, 3743, 4601–4645 |
| `detailSectionContent` | 6 | 3 | 3316, 4752–4762, 4842–4852 |
| `emby-checkbox` | 6 | 3 | 3487, 3524–3528, 3577–3589 |
| `actionSheetContent` | 5 | 3 | 4593–4597, 6735–6745, 6771 |
| `cardText-first` | 5 | 3 | 924, 3516–3542, 6084 |
| `dialog` | 5 | 3 | 3366–3376, 6735–6745, 6771 |
| `guideProgramName` | 5 | 3 | 637, 5651–5662, 5705–5710 |
| `noHomeButtonHeader` | 5 | 3 | 1666, 6368, 6478–6486 |
| `overflowBackdropCard` | 5 | 3 | 963–969, 3520, 6079–6084 |
| `secondary` | 5 | 3 | 302, 4497–4507, 4547 |
| `album` | 4 | 3 | 2224, 2483–2487, 2523 |
| `cardPadder` | 4 | 3 | 424, 1010, 3533–3537 |
| `cardText` | 4 | 3 | 924–934, 3542, 7109 |
| `detailPageContent` | 4 | 3 | 1762, 4683, 4956–4963 |
| `dialog-fullscreen` | 4 | 3 | 3376, 6735–6745, 6771 |
| `emby-scrollbuttons` | 4 | 3 | 1825–1830, 7130, 7666 |
| `folder` | 4 | 3 | 1925–1930, 3643, 3707 |
| `formDialogFooter` | 4 | 3 | 3434, 3917, 7341–7365 |
| `infoWrapper` | 4 | 3 | 2167–2172, 2430, 2458 |
| `listItemImage` | 4 | 3 | 2801–2806, 4461, 7324 |
| `musicParentName` | 4 | 3 | 2001, 2536, 5592–5601 |
| `programGuideSection` | 4 | 3 | 2491–2506, 4852, 4879 |
| `semiTransparent` | 4 | 3 | 1648, 5901, 6336–6357 |
| `toast` | 4 | 3 | 5126, 6735–6745, 6771 |
| `cardFooter` | 3 | 3 | 3553, 6839, 6874 |
| `collectionItems` | 3 | 3 | 1772, 4852, 4888 |
| `defaultCardBackground` | 3 | 3 | 3664, 6099, 6198 |
| `detailPageSecondaryContainer` | 3 | 3 | 1615, 1642, 1762 |
| `emby-input` | 3 | 3 | 5386, 5415, 7407 |
| `formDialogFooterItem` | 3 | 3 | 3434, 3702, 3828 |
| `formDialogHeader` | 3 | 3 | 3917, 7289, 7341 |
| `iconOsd` | 3 | 3 | 5879, 7289, 7341 |
| `live_tv` | 3 | 3 | 2001, 2523, 3951 |
| `myPreferencesMenuPage` | 3 | 3 | 397, 4661, 4977 |
| `page` | 3 | 3 | 1006, 2698, 6791 |
| `playerStats` | 3 | 3 | 5879, 7341, 7377 |
| `sectionTitle-cards` | 3 | 3 | 1740, 5042, 5102 |
| `sectionTitleContainer` | 3 | 3 | 1772, 1830, 4888 |
| `tsx` | 3 | 3 | 1084, 4359, 4436 |
| `itemExternalLinks` | 13 | 2 | 3100–3178, 3316 |
| `checkboxOutline` | 10 | 2 | 3487–3528, 3559–3589 |
| `itemBackdrop` | 9 | 2 | 1967–2022, 2197 |
| `mdl-slider` | 9 | 2 | 2897, 2952–3010 |
| `listItemIcon` | 8 | 2 | 3947–3951, 4601–4661 |
| `sliderContainer` | 8 | 2 | 2901, 2929–2994 |
| `cardOverlayButton-br` | 7 | 2 | 1022, 1051–1095 |
| `detail-clamp-text` | 7 | 2 | 3252–3278, 3304–3308 |
| `divUsers` | 7 | 2 | 5980–5984, 7093–7120 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3524–3528, 3558–3577 |
| `countIndicator` | 6 | 2 | 767–797, 7341–7365 |
| `detailPagePrimaryContainer` | 6 | 2 | 1592–1638, 2430 |
| `detailsGroupItem` | 6 | 2 | 4714, 4782–4819 |
| `headerButton` | 6 | 2 | 557–637, 6420 |
| `headerLeft` | 6 | 2 | 1690–1727, 6628 |
| `selectionCommandsPanel` | 6 | 2 | 3444–3478, 7289 |
| `trackSelections` | 6 | 2 | 4687–4714, 4847–4852 |
| `withBackdrop` | 6 | 2 | 2606, 2648–2666 |
| `detailSection` | 5 | 2 | 4670–4679, 4832–4852 |
| `fullSyncIndicator` | 5 | 2 | 767–790, 7341–7365 |
| `mainDrawer-scrollContainer` | 5 | 2 | 3060, 7006–7023 |
| `mediaInfoItem` | 5 | 2 | 1844–1887, 6883 |
| `overview-expand` | 5 | 2 | 3284–3308, 4752 |
| `scrollX` | 5 | 2 | 1745, 1783–1803 |
| `videoIndicator` | 5 | 2 | 3632–3660, 7341 |
| `withSectionTabs` | 5 | 2 | 2657–2674, 6343 |
| `alphaPickerButton` | 4 | 2 | 637, 4903–4915 |
| `backgroundProgress` | 4 | 2 | 2812–2824, 2854 |
| `emby-select` | 4 | 2 | 5386–5398, 7407 |
| `emby-tab-button-active` | 4 | 2 | 3889, 6510–6524 |
| `mediaSourceIndicator` | 4 | 2 | 767–790, 7341 |
| `play_arrow` | 4 | 2 | 3669–3685, 3856 |
| `playbackProgress` | 4 | 2 | 2812–2824, 2859 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4488–4493, 6192–6198 |
| `programCell` | 4 | 2 | 5642, 5701–5710 |
| `section0` | 4 | 2 | 976–1006, 6791 |
| `visualLoginForm` | 4 | 2 | 5971–5988, 6029 |
| `cardOverlayButtonIcon` | 3 | 2 | 1022–1034, 1095 |
| `castCollapsible` | 3 | 2 | 833, 3528–3537 |
| `emby-scrollbuttons-button` | 3 | 2 | 1834, 7673–7680 |
| `emby-textarea` | 3 | 2 | 5377–5386, 5415 |
| `guestCastContent` | 3 | 2 | 833, 3528–3537 |
| `guide-channelHeaderCell` | 3 | 2 | 637, 5676–5692 |
| `guide-date-tab-button` | 3 | 2 | 637, 3889–3897 |
| `headerUserButton` | 3 | 2 | 557–570, 4981 |
| `manualLoginForm` | 3 | 2 | 5971–5988, 6029 |
| `overview` | 3 | 2 | 3304–3308, 4762 |
| `add` | 2 | 2 | 1745, 6883 |
| `alphaPicker-fixed-right` | 2 | 2 | 2698, 4915 |
| `backdropImageFadeIn` | 2 | 2 | 2751, 7381 |
| `book` | 2 | 2 | 2001, 2523 |
| `btnDeleteImage` | 2 | 2 | 3689, 3903 |
| `cardContent` | 2 | 2 | 833, 865 |
| `cardOverlayButton` | 2 | 2 | 1036, 1072 |
| `cardOverlayButton-hover` | 2 | 2 | 919, 1051 |
| `chevron_right` | 2 | 2 | 5072, 5116 |
| `classList` | 2 | 2 | 1745, 6883 |
| `collapseContent` | 2 | 2 | 3439, 3915 |
| `collectionItemsContainer` | 2 | 2 | 1772, 4892 |
| `content-primary` | 2 | 2 | 4956, 5008 |
| `editorsChoiceItemOverview` | 2 | 2 | 7603, 7684 |
| `endsAt` | 2 | 2 | 1865, 6883 |
| `fieldDescription` | 2 | 2 | 302, 7407 |
| `formDialogFooter-clear` | 2 | 2 | 3434, 3917 |
| `guide-programNameCaret` | 2 | 2 | 302, 5658 |
| `headroom` | 2 | 2 | 6331, 6368 |
| `indicator` | 2 | 2 | 797, 3621 |
| `mediaInfoOfficialRating` | 2 | 2 | 1865, 6883 |
| `navMenuOption-selected` | 2 | 2 | 4666, 7017 |
| `nowPlayingInfoContainer` | 2 | 2 | 3091, 6129 |
| `org` | 2 | 2 | 3127, 3157 |
| `paperList` | 2 | 2 | 842, 3928 |
| `playlist` | 2 | 2 | 4483, 6107 |
| `programSecondaryTitle` | 2 | 2 | 302, 5710 |
| `queue` | 2 | 2 | 2001, 2523 |
| `reactRoot` | 2 | 2 | 4359, 6634 |
| `readOnlyContent` | 2 | 2 | 3959, 6557 |
| `recordingFields` | 2 | 2 | 4706, 4847 |
| `runtime` | 2 | 2 | 6041, 6069 |
| `sectionTitleContainer-cards` | 2 | 2 | 5037, 5102 |
| `sidebarHeader` | 2 | 2 | 4051, 7023 |
| `tagline` | 2 | 2 | 2597, 4762 |
| `upNextDialog-title` | 2 | 2 | 5158, 5192 |
| `vertical-list` | 2 | 2 | 1807, 7509 |
| `vertical-wrap` | 2 | 2 | 763, 1772 |
| `videoOsdBottom` | 2 | 2 | 3083, 6298 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3083, 6298 |
| `userPreferencesPage` | 12 | 1 | 7392–7488 |
| `checkboxContainer` | 7 | 1 | 3516–3553 |
| `itemDetailsGroup` | 7 | 1 | 4766–4852 |
| `itemProgressBar` | 6 | 1 | 2801–2835 |
| `streaming-lookup-container` | 6 | 1 | 3185–3230 |
| `trackSelectionFieldContainer` | 6 | 1 | 4725–4748 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7640–7680 |
| `innerCardFooter` | 5 | 1 | 3329–3358 |
| `chapterCardImageContainer` | 4 | 1 | 3329–3358 |
| `emby-select-withcolor` | 4 | 1 | 5386–5433 |
| `endTimeText` | 4 | 1 | 6041–6069 |
| `mainDetailButtons` | 4 | 1 | 3852–3866 |
| `overview-controls` | 4 | 1 | 3304–3316 |
| `startTimeText` | 4 | 1 | 6041–6063 |
| `button-flat` | 3 | 1 | 3064–3074 |
| `cardIndicators` | 3 | 1 | 3606–3616 |
| `cardOverlayFab-primary` | 3 | 1 | 1014–1036 |
| `com` | 3 | 1 | 3133–3151 |
| `content` | 3 | 1 | 4788–4819 |
| `discover-card` | 3 | 1 | 7691–7714 |
| `fab` | 3 | 1 | 3711–3724 |
| `listChildrenCollapsible` | 3 | 1 | 4837–4852 |
| `mdl-slider-background-flex` | 3 | 1 | 2921–2934 |
| `mediaInfoCriticRating` | 3 | 1 | 1906–1915 |
| `nextUpSection` | 3 | 1 | 4832–4852 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 6093–6103 |
| `serverInfo` | 3 | 1 | 3932–3941 |
| `transcodingProgress` | 3 | 1 | 2812–2824 |
