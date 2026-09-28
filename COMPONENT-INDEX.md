# Index des composants — ElegantFin Cinema Edition v1.3.12

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.12.css` — 7393 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 36 | 14 | 420–502, 740, 857, 1503–1523, 2065–2098, 2125–2129, 2405–2423, 2459, 6365, 6623–6639, 6717–6739, 6769–6776, 6866, 7271 |
| `cardScalable` | 28 | 13 | 420–431, 479–502, 803–847, 873–911, 2423, 3426, 3537, 3616, 5558, 6379–6389, 6458, 6623, 6760–6776 |
| `material-icons` | 17 | 13 | 356–375, 1722, 1820, 1872, 3383, 3542, 3616–3622, 3728, 3886, 4276, 4760, 4794–4804, 5376 |
| `cardImageContainer` | 22 | 12 | 474, 825, 853–882, 911, 968–998, 5683–5687, 5767, 6371, 6450–6458, 6498, 6623–6639, 6760 |
| `itemDetailPage` | 19 | 12 | 1566, 1652, 1731, 1758, 1991–2016, 2060, 2161, 2472–2477, 3871–3882, 4370, 4657, 7099–7137 |
| `skinHeader` | 16 | 10 | 284, 4101, 4134–4161, 5566, 5976, 6032–6040, 6066–6091, 6441, 6590, 7208 |
| `nameContainer` | 27 | 9 | 686, 2168–2191, 2232, 2261, 2296–2342, 2379, 2410–2414, 5133–5185, 7099–7137 |
| `backdropCard` | 12 | 9 | 955–961, 1076, 1991, 2077, 2161, 2414–2423, 2450, 2477, 2757 |
| `js` | 9 | 9 | 323, 1638, 1731, 2232, 2834, 3516, 5376, 6542, 6786 |
| `card-hoverable` | 23 | 8 | 502, 813, 873–961, 5687, 6389, 6498–6533, 6623, 6912 |
| `parentName` | 23 | 8 | 686, 2173–2191, 2232, 2261, 2296–2342, 5139–5185, 5258, 7099–7137 |
| `detailPageWrapperContainer` | 17 | 8 | 686, 1534–1544, 2016, 2134, 2168–2191, 2261, 2296–2342, 2410 |
| `subtitle` | 16 | 8 | 1991, 2060, 2173, 2232, 2351–2361, 2472–2477, 5193–5226, 7099–7137 |
| `cardBox` | 12 | 8 | 420–468, 494, 740, 895, 1002, 6365, 6623, 6912 |
| `emby-button` | 11 | 8 | 612–629, 656–674, 3096, 3157–3164, 3562, 3597, 3750, 4294 |
| `detailLogo` | 17 | 7 | 686, 2005–2016, 2051–2060, 2161–2191, 2261, 2296–2342, 2410 |
| `loginPage` | 16 | 7 | 3695, 5570–5601, 5640, 5668–5687, 6394, 6437, 6749–6776 |
| `nowPlayingBar` | 7 | 7 | 3020, 5819, 6404, 6492, 6576, 6602, 6871 |
| `listItem` | 17 | 6 | 302, 629, 2427, 4196–4222, 4253–4285, 6889–6906 |
| `navMenuOption` | 12 | 6 | 629, 725–735, 3936, 4263–4285, 4351–4356, 6662–6673 |
| `paper-icon-button-light` | 11 | 6 | 574–629, 1652, 1722, 1820, 3323–3343, 5052 |
| `verticalSection` | 11 | 6 | 1726, 2658–2663, 4657, 6450, 6542, 6786 |
| `button-link` | 10 | 6 | 629, 656–674, 2970–2979, 3040–3050, 3096, 7062 |
| `person` | 8 | 6 | 1991–2001, 2161, 2414, 2459–2468, 3823, 7094 |
| `mainDrawer` | 7 | 6 | 2984, 3900, 4134, 6394–6404, 6649, 6688 |
| `detailImageContainer` | 20 | 5 | 1991–2001, 2065–2129, 2161, 2401–2423, 2450–2477 |
| `osdHeader` | 15 | 5 | 1695–1713, 5971–6040, 6066–6091, 6441, 6871 |
| `actionSheetMenuItem` | 11 | 5 | 629, 4196–4207, 4253, 4331–4347, 6422 |
| `sectionTabs` | 10 | 5 | 1789, 3674, 4161, 6012–6017, 6157–6183 |
| `cardImageIcon` | 8 | 5 | 412–416, 2414–2423, 2483, 3410, 5767 |
| `headerTop` | 8 | 5 | 4101, 4134, 5982–6007, 6058–6075, 6102–6106 |
| `sectionTitle` | 7 | 5 | 1726, 1799–1806, 4002, 4730–4738, 5635 |
| `emby-scroller-container` | 6 | 5 | 1726–1731, 1769, 2648, 6450, 6542 |
| `portraitCard` | 5 | 5 | 1076, 1154, 1910, 2125, 2757 |
| `scss` | 5 | 5 | 284, 768, 1028, 3432, 6542 |
| `skinHeader-withBackground` | 5 | 5 | 1634, 3871, 5566, 5971, 6021 |
| `btnPlay` | 16 | 4 | 511–535, 574–629, 3626–3668, 3701–3728 |
| `cardOverlayContainer` | 12 | 4 | 929–961, 1006–1028, 1088, 6871–6889 |
| `itemName` | 11 | 4 | 686, 2232, 5139–5185, 5276–5293 |
| `backdropImage` | 10 | 4 | 2548–2575, 2602–2606, 6358, 6458–6466 |
| `emby-tab-button` | 10 | 4 | 629, 696–705, 3674, 6142–6178 |
| `upNextContainer` | 10 | 4 | 4822–4841, 4867–4893, 6394–6404, 6430 |
| `emby-scroller` | 9 | 4 | 1731, 1769–1775, 6692–6739, 6850–6866 |
| `detailRibbon` | 7 | 4 | 1591–1619, 1825, 1910–1915, 7094 |
| `listItemBodyText` | 7 | 4 | 4217–4236, 4276, 4335, 6906 |
| `visualCardBox` | 7 | 4 | 420, 834–847, 873–878, 1002 |
| `button-submit` | 6 | 4 | 3695, 3782, 5668–5676, 6974–6988 |
| `cardText-secondary` | 6 | 4 | 302, 916, 3415–3419, 6520–6528 |
| `detailPagePrimaryContent` | 6 | 4 | 1606–1624, 2366, 4651, 6606 |
| `skip-button` | 6 | 4 | 629, 3679, 4916–4933, 4960–4966 |
| `squareCard` | 6 | 4 | 857, 2414, 2450–2468, 5644–5648 |
| `skinHeader-blurred` | 5 | 4 | 5566, 6000–6007, 6590, 6871 |
| `appfooter` | 4 | 4 | 2700, 6116, 6481, 6871 |
| `itemsContainer` | 4 | 4 | 740, 1758, 1793, 4657 |
| `raised` | 4 | 4 | 629, 715, 3562, 3597 |
| `detailButton` | 13 | 3 | 574–629, 3607–3668, 3724–3728 |
| `itemBackdrop` | 9 | 3 | 1957–2001, 2134, 2477 |
| `itemSelectionPanel` | 9 | 3 | 886–890, 3355, 3383–3426 |
| `check` | 8 | 3 | 3383, 3616, 4327–4347 |
| `pageTitle` | 8 | 3 | 1670–1713, 6032, 6091 |
| `sectionTitleTextButton` | 8 | 3 | 4713–4721, 4748–4760, 4794–4804 |
| `backgroundContainer` | 7 | 3 | 2539, 2580–2598, 2630 |
| `homePage` | 7 | 3 | 4101, 4134–4161, 6200 |
| `playedIndicator` | 7 | 3 | 768–782, 3499, 6623–6644 |
| `detailSectionContent` | 6 | 3 | 3189, 4452–4462, 4542–4552 |
| `emby-checkbox` | 6 | 3 | 3360, 3397–3401, 3450–3462 |
| `actionSheetContent` | 5 | 3 | 4319–4323, 6394–6404, 6430 |
| `cardText-first` | 5 | 3 | 916, 3389–3415, 5748 |
| `dialog` | 5 | 3 | 3239–3249, 6394–6404, 6430 |
| `guideProgramName` | 5 | 3 | 629, 5317–5328, 5371–5376 |
| `musicParentName` | 5 | 3 | 1991, 2472–2477, 5258–5267 |
| `noHomeButtonHeader` | 5 | 3 | 1652, 6032, 6142–6150 |
| `overflowBackdropCard` | 5 | 3 | 955–961, 3393, 5743–5748 |
| `secondary` | 5 | 3 | 302, 4226–4236, 4276 |
| `album` | 4 | 3 | 2161, 2419–2423, 2459 |
| `cardPadder` | 4 | 3 | 416, 1002, 3406–3410 |
| `cardText` | 4 | 3 | 916–926, 3415, 6765 |
| `detailPageContent` | 4 | 3 | 1748, 4383, 4644–4651 |
| `dialog-fullscreen` | 4 | 3 | 3249, 6394–6404, 6430 |
| `emby-scrollbuttons` | 4 | 3 | 1811–1816, 6786, 7246 |
| `formDialogFooter` | 4 | 3 | 3307, 3789, 6923–6947 |
| `infoWrapper` | 4 | 3 | 2104–2109, 2366, 2394 |
| `listItemImage` | 4 | 3 | 2734–2739, 4190, 6906 |
| `semiTransparent` | 4 | 3 | 1634, 5566, 6000–6021 |
| `toast` | 4 | 3 | 4814, 6394–6404, 6430 |
| `cardFooter` | 3 | 3 | 3426, 6498, 6533 |
| `defaultCardBackground` | 3 | 3 | 3537, 5763, 5862 |
| `detailPageSecondaryContainer` | 3 | 3 | 1601, 1628, 1748 |
| `folder` | 3 | 3 | 1910, 3516, 3580 |
| `formDialogFooterItem` | 3 | 3 | 3307, 3575, 3701 |
| `formDialogHeader` | 3 | 3 | 3789, 6871, 6923 |
| `iconOsd` | 3 | 3 | 5544, 6871, 6923 |
| `live_tv` | 3 | 3 | 1991, 2459, 3823 |
| `myPreferencesMenuPage` | 3 | 3 | 389, 4361, 4665 |
| `page` | 3 | 3 | 998, 2630, 6450 |
| `playerStats` | 3 | 3 | 5544, 6923, 6959 |
| `sectionTitle-cards` | 3 | 3 | 1726, 4730, 4790 |
| `sectionTitleContainer` | 3 | 3 | 1758, 1816, 4576 |
| `x` | 3 | 3 | 2232, 5241, 6542 |
| `itemExternalLinks` | 13 | 2 | 3033–3111, 3189 |
| `checkboxOutline` | 10 | 2 | 3360–3401, 3432–3462 |
| `mdl-slider` | 9 | 2 | 2830, 2885–2943 |
| `listItemIcon` | 8 | 2 | 3819–3823, 4331–4361 |
| `sliderContainer` | 8 | 2 | 2834, 2862–2927 |
| `cardOverlayButton-br` | 7 | 2 | 1014, 1043–1081 |
| `detail-clamp-text` | 7 | 2 | 3125–3151, 3177–3181 |
| `divUsers` | 7 | 2 | 5644–5648, 6749–6776 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3397–3401, 3431–3450 |
| `countIndicator` | 6 | 2 | 759–789, 6923–6947 |
| `detailPagePrimaryContainer` | 6 | 2 | 1578–1624, 2366 |
| `detailsGroupItem` | 6 | 2 | 4414, 4482–4519 |
| `headerButton` | 6 | 2 | 549–629, 6084 |
| `headerLeft` | 6 | 2 | 1676–1713, 6287 |
| `selectionCommandsPanel` | 6 | 2 | 3317–3351, 6871 |
| `trackSelections` | 6 | 2 | 4387–4414, 4547–4552 |
| `withBackdrop` | 6 | 2 | 2539, 2580–2598 |
| `detailSection` | 5 | 2 | 4370–4379, 4532–4552 |
| `fullSyncIndicator` | 5 | 2 | 759–782, 6923–6947 |
| `mainDrawer-scrollContainer` | 5 | 2 | 2993, 6662–6679 |
| `mediaInfoItem` | 5 | 2 | 1829–1872, 6542 |
| `overview-expand` | 5 | 2 | 3157–3181, 4452 |
| `scrollX` | 5 | 2 | 1731, 1769–1789 |
| `videoIndicator` | 5 | 2 | 3505–3533, 6923 |
| `withSectionTabs` | 5 | 2 | 2589–2606, 6007 |
| `alphaPickerButton` | 4 | 2 | 629, 4591–4603 |
| `backgroundProgress` | 4 | 2 | 2745–2757, 2787 |
| `emby-tab-button-active` | 4 | 2 | 3761, 6169–6183 |
| `mediaSourceIndicator` | 4 | 2 | 759–782, 6923 |
| `play_arrow` | 4 | 2 | 3542–3558, 3728 |
| `playbackProgress` | 4 | 2 | 2745–2757, 2792 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4217–4222, 5856–5862 |
| `programCell` | 4 | 2 | 5308, 5367–5376 |
| `programGuideSection` | 4 | 2 | 2427–2442, 4552–4567 |
| `section0` | 4 | 2 | 968–998, 6450 |
| `visualLoginForm` | 4 | 2 | 5635–5652, 5693 |
| `cardOverlayButtonIcon` | 3 | 2 | 1014–1026, 1081 |
| `castCollapsible` | 3 | 2 | 825, 3401–3410 |
| `collectionItems` | 3 | 2 | 1758, 4552–4576 |
| `emby-input` | 3 | 2 | 5066–5082, 6988 |
| `emby-scrollbuttons-button` | 3 | 2 | 1820, 7253–7260 |
| `guestCastContent` | 3 | 2 | 825, 3401–3410 |
| `guide-channelHeaderCell` | 3 | 2 | 629, 5342–5358 |
| `guide-date-tab-button` | 3 | 2 | 629, 3761–3769 |
| `headerUserButton` | 3 | 2 | 549–562, 4669 |
| `manualLoginForm` | 3 | 2 | 5635–5652, 5693 |
| `overview` | 3 | 2 | 3177–3181, 4462 |
| `add` | 2 | 2 | 1731, 6542 |
| `alphaPicker-fixed-right` | 2 | 2 | 2630, 4603 |
| `backdropImageFadeIn` | 2 | 2 | 2684, 6963 |
| `book` | 2 | 2 | 1991, 2459 |
| `btnDeleteImage` | 2 | 2 | 3562, 3775 |
| `cardContent` | 2 | 2 | 825, 857 |
| `cardOverlayButton` | 2 | 2 | 1028, 1064 |
| `cardOverlayButton-hover` | 2 | 2 | 911, 1043 |
| `chevron_right` | 2 | 2 | 4760, 4804 |
| `classList` | 2 | 2 | 1731, 6542 |
| `collapseContent` | 2 | 2 | 3312, 3787 |
| `collectionItemsContainer` | 2 | 2 | 1758, 4580 |
| `content-primary` | 2 | 2 | 4644, 4696 |
| `editorsChoiceItemOverview` | 2 | 2 | 7183, 7264 |
| `emby-select` | 2 | 2 | 5066, 6988 |
| `endsAt` | 2 | 2 | 1850, 6542 |
| `fieldDescription` | 2 | 2 | 302, 6988 |
| `formDialogFooter-clear` | 2 | 2 | 3307, 3789 |
| `guide-programNameCaret` | 2 | 2 | 302, 5324 |
| `headroom` | 2 | 2 | 5995, 6032 |
| `indicator` | 2 | 2 | 789, 3494 |
| `mediaInfoOfficialRating` | 2 | 2 | 1850, 6542 |
| `navMenuOption-selected` | 2 | 2 | 4366, 6673 |
| `nowPlayingInfoContainer` | 2 | 2 | 3024, 5793 |
| `org` | 2 | 2 | 3060, 3090 |
| `paperList` | 2 | 2 | 834, 3800 |
| `playlist` | 2 | 2 | 4212, 5771 |
| `programSecondaryTitle` | 2 | 2 | 302, 5376 |
| `queue` | 2 | 2 | 1991, 2459 |
| `readOnlyContent` | 2 | 2 | 3831, 6216 |
| `recordingFields` | 2 | 2 | 4406, 4547 |
| `runtime` | 2 | 2 | 5705, 5733 |
| `sectionTitleContainer-cards` | 2 | 2 | 4725, 4790 |
| `sidebarHeader` | 2 | 2 | 3923, 6679 |
| `tagline` | 2 | 2 | 2530, 4462 |
| `tsx` | 2 | 2 | 4101, 4165 |
| `upNextDialog-title` | 2 | 2 | 4846, 4880 |
| `vertical-list` | 2 | 2 | 1793, 7089 |
| `vertical-wrap` | 2 | 2 | 755, 1758 |
| `videoOsdBottom` | 2 | 2 | 3016, 5962 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3016, 5962 |
| `userPreferencesPage` | 12 | 1 | 6974–7069 |
| `checkboxContainer` | 7 | 1 | 3389–3426 |
| `itemDetailsGroup` | 7 | 1 | 4466–4552 |
| `itemProgressBar` | 6 | 1 | 2734–2768 |
| `trackSelectionFieldContainer` | 6 | 1 | 4425–4448 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7220–7260 |
| `innerCardFooter` | 5 | 1 | 3202–3231 |
| `chapterCardImageContainer` | 4 | 1 | 3202–3231 |
| `endTimeText` | 4 | 1 | 5705–5733 |
| `mainDetailButtons` | 4 | 1 | 3724–3738 |
| `overview-controls` | 4 | 1 | 3177–3189 |
| `startTimeText` | 4 | 1 | 5705–5727 |
| `button-flat` | 3 | 1 | 2997–3007 |
| `cardIndicators` | 3 | 1 | 3479–3489 |
| `cardOverlayFab-primary` | 3 | 1 | 1006–1028 |
| `com` | 3 | 1 | 3066–3084 |
| `content` | 3 | 1 | 4488–4519 |
| `discover-card` | 3 | 1 | 7271–7294 |
| `emby-select-withcolor` | 3 | 1 | 5066–5100 |
| `emby-textarea` | 3 | 1 | 5057–5082 |
| `fab` | 3 | 1 | 3584–3597 |
| `listChildrenCollapsible` | 3 | 1 | 4537–4552 |
| `mdl-slider-background-flex` | 3 | 1 | 2854–2867 |
| `mediaInfoCriticRating` | 3 | 1 | 1891–1900 |
| `nextUpSection` | 3 | 1 | 4532–4552 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 5757–5767 |
| `serverInfo` | 3 | 1 | 3804–3813 |
| `transcodingProgress` | 3 | 1 | 2745–2757 |
