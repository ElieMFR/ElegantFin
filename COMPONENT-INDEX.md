# Index des composants — ElegantFin Cinema Edition v1.5.3

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.5.3.css` — 8091 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 38 | 16 | 454–465, 496–542, 780, 897, 1562–1582, 2196–2229, 2256–2260, 2537–2555, 2591, 6933, 6969–6979, 7215–7234, 7312–7334, 7364–7371, 7535, 7969 |
| `cardScalable` | 31 | 13 | 454–465, 519–542, 843–887, 913–957, 2555, 3637, 3748, 3827, 6007, 6947–6979, 7050, 7215, 7355–7371 |
| `material-icons` | 17 | 13 | 390–409, 1787, 1885, 1938, 3594, 3753, 3827–3833, 3940, 4103, 4654, 5186, 5220–5230, 5824 |
| `cardImageContainer` | 22 | 12 | 514, 865, 893–922, 957, 1014–1044, 6155–6159, 6239, 6939, 7042–7050, 7090, 7215–7234, 7355 |
| `itemDetailPage` | 20 | 12 | 1625, 1711, 1796, 1823, 2052–2092, 2127–2142, 2178–2182, 2292, 2604, 4777, 5079, 7789–7827 |
| `skinHeader` | 20 | 12 | 293, 1711, 4083–4099, 4466, 4512–4539, 6015–6019, 6448, 6504–6512, 6582–6607, 7033, 7182, 7898 |
| `js` | 13 | 12 | 327, 357, 1697–1711, 1796, 2363, 2969, 3398, 3727, 5824, 6811, 7134, 7381 |
| `nameContainer` | 27 | 9 | 726, 2299–2322, 2363, 2392, 2427–2474, 2511, 2542–2546, 5580–5633, 7789–7827 |
| `cardBox` | 13 | 9 | 454–465, 496–508, 534, 780, 935–939, 1048, 6933, 7215, 7600 |
| `emby-button` | 12 | 9 | 652–669, 696–714, 3231, 3366–3373, 3773, 3808, 3962, 4672, 5402 |
| `card-hoverable` | 23 | 8 | 542, 853, 913–1007, 6159, 6957, 7090–7125, 7215, 7600 |
| `parentName` | 23 | 8 | 726, 2304–2322, 2363, 2392, 2427–2474, 5586–5633, 5706, 7789–7827 |
| `detailLogo` | 20 | 8 | 726, 2081–2092, 2127–2142, 2169–2182, 2292–2322, 2392, 2427–2474, 2542 |
| `listItem` | 19 | 8 | 311, 669, 2559, 4574–4600, 4631–4663, 4708, 4752, 7577–7594 |
| `detailPageWrapperContainer` | 17 | 8 | 726, 1593–1603, 2092, 2265, 2299–2322, 2392, 2427–2474, 2542 |
| `subtitle` | 17 | 8 | 2052–2062, 2178–2182, 2304, 2363, 2483–2493, 2604, 5641–5674, 7789–7827 |
| `backdropCard` | 12 | 8 | 1001–1007, 1129, 2052–2062, 2208, 2292, 2546–2555, 2582, 2892 |
| `nowPlayingBar` | 8 | 8 | 327, 3155, 6291, 6996, 7084, 7168, 7194, 7540 |
| `loginPage` | 18 | 7 | 3906, 6019–6053, 6093–6111, 6140–6159, 6986, 7029, 7344–7371 |
| `navMenuOption` | 12 | 6 | 669, 765–775, 4153, 4641–4663, 4758–4763, 7257–7268 |
| `emby-tab-button` | 11 | 6 | 669, 736–745, 3885, 6658–6666, 6695–6712, 7910 |
| `paper-icon-button-light` | 11 | 6 | 614–669, 1711, 1787, 1885, 3534–3554, 5486 |
| `verticalSection` | 11 | 6 | 1791, 2794–2799, 5079, 7042, 7134, 7381 |
| `button-link` | 10 | 6 | 669, 696–714, 3105–3114, 3175–3185, 3231, 7751 |
| `headerTop` | 9 | 6 | 2182, 4466, 4512, 6454–6479, 6574–6591, 6618–6622 |
| `person` | 8 | 6 | 2052–2077, 2292, 2546, 2591–2600, 4035, 7784 |
| `mainDrawer` | 7 | 6 | 3119, 4117, 4512, 6986–6996, 7244, 7283 |
| `scss` | 6 | 6 | 293, 808, 1074, 3643, 4159, 7134 |
| `detailImageContainer` | 20 | 5 | 2052–2077, 2196–2260, 2292, 2533–2555, 2582–2600 |
| `osdHeader` | 15 | 5 | 1760–1778, 6443–6512, 6582–6607, 7033, 7540 |
| `cardOverlayContainer` | 12 | 5 | 975–1007, 1052–1074, 1147, 7540, 7577 |
| `sectionTabs` | 11 | 5 | 1854, 3885, 4539, 6484–6489, 6673–6717 |
| `actionSheetMenuItem` | 10 | 5 | 669, 4574–4585, 4631, 4708–4752, 7014 |
| `cardImageIcon` | 8 | 5 | 446–450, 2546–2555, 2618, 3621, 6239 |
| `sectionTitle` | 7 | 5 | 1791, 1864–1871, 4367, 5156–5164, 6088 |
| `semiTransparent` | 7 | 5 | 1693, 4083–4099, 6015, 6472–6493, 6529 |
| `emby-scroller-container` | 6 | 5 | 1791–1796, 1834, 2784, 7042, 7134 |
| `portraitCard` | 6 | 5 | 1129, 1213, 1976–1981, 2256, 2892 |
| `appfooter` | 5 | 5 | 327, 2835, 6632, 7073, 7540 |
| `skinHeader-withBackground` | 5 | 5 | 1693, 4083, 6015, 6443, 6493 |
| `btnPlay` | 16 | 4 | 551–575, 614–669, 3837–3879, 3912–3940 |
| `itemName` | 11 | 4 | 726, 2363, 5586–5633, 5724–5741 |
| `backdropImage` | 10 | 4 | 2683–2711, 2738–2742, 6926, 7050–7058 |
| `upNextContainer` | 10 | 4 | 5248–5267, 5293–5319, 6986–6996, 7022 |
| `emby-scroller` | 9 | 4 | 1796, 1834–1840, 7287–7334, 7519–7535 |
| `backgroundContainer` | 8 | 4 | 2146, 2674, 2716–2734, 2766 |
| `detailRibbon` | 8 | 4 | 1650–1678, 1891, 1976–1988, 7784 |
| `listItemBodyText` | 7 | 4 | 4595–4614, 4654, 4729, 7594 |
| `skip-button` | 7 | 4 | 669, 3890, 5342–5359, 5386–5404 |
| `visualCardBox` | 7 | 4 | 454, 874–887, 913–918, 1048 |
| `button-submit` | 6 | 4 | 3906, 3994, 6140–6148, 7662–7677 |
| `cardText-secondary` | 6 | 4 | 311, 962, 3626–3630, 7112–7120 |
| `detailPagePrimaryContent` | 6 | 4 | 1665–1683, 2498, 5073, 7198 |
| `skinHeader-blurred` | 6 | 4 | 6015, 6472–6479, 7182, 7540–7559 |
| `squareCard` | 6 | 4 | 897, 2546, 2582–2600, 6116–6120 |
| `itemsContainer` | 4 | 4 | 780, 1823, 1858, 5079 |
| `raised` | 4 | 4 | 669, 755, 3773, 3808 |
| `tsx` | 4 | 4 | 1129, 1711, 4466, 4543 |
| `x` | 4 | 4 | 2363, 4159, 5689, 7134 |
| `detailButton` | 13 | 3 | 614–669, 3818–3879, 3936–3940 |
| `itemSelectionPanel` | 9 | 3 | 926–930, 3566, 3594–3637 |
| `pageTitle` | 8 | 3 | 1735–1778, 6504, 6607 |
| `sectionTitleTextButton` | 8 | 3 | 5139–5147, 5174–5186, 5220–5230 |
| `homePage` | 7 | 3 | 4466, 4512–4539, 6734 |
| `playedIndicator` | 7 | 3 | 808–822, 3710, 7215–7239 |
| `check` | 6 | 3 | 3594, 3827, 4708–4752 |
| `detailSectionContent` | 6 | 3 | 3398, 4859–4869, 4952–4962 |
| `emby-checkbox` | 6 | 3 | 3571, 3608–3612, 3661–3673 |
| `actionSheetContent` | 5 | 3 | 4700–4704, 6986–6996, 7022 |
| `cardText-first` | 5 | 3 | 962, 3600–3626, 6220 |
| `dialog` | 5 | 3 | 3450–3460, 6986–6996, 7022 |
| `guideProgramName` | 5 | 3 | 669, 5765–5776, 5819–5824 |
| `noHomeButtonHeader` | 5 | 3 | 1711, 6504, 6658–6666 |
| `overflowBackdropCard` | 5 | 3 | 1001–1007, 3604, 6215–6220 |
| `secondary` | 5 | 3 | 311, 4604–4614, 4654 |
| `album` | 4 | 3 | 2292, 2551–2555, 2591 |
| `cardPadder` | 4 | 3 | 450, 1048, 3617–3621 |
| `cardText` | 4 | 3 | 962–972, 3626, 7360 |
| `detailPageContent` | 4 | 3 | 1813, 4790, 5066–5073 |
| `dialog-fullscreen` | 4 | 3 | 3460, 6986–6996, 7022 |
| `emby-scrollbuttons` | 4 | 3 | 1876–1881, 7381, 7944 |
| `folder` | 4 | 3 | 1976–1981, 3727, 3791 |
| `formDialogFooter` | 4 | 3 | 3518, 4001, 7611–7635 |
| `infoWrapper` | 4 | 3 | 2235–2240, 2498, 2526 |
| `listItemImage` | 4 | 3 | 2869–2874, 4568, 7594 |
| `musicParentName` | 4 | 3 | 2052, 2604, 5706–5715 |
| `programGuideSection` | 4 | 3 | 2559–2574, 4962, 4989 |
| `toast` | 4 | 3 | 5240, 6986–6996, 7022 |
| `cardFooter` | 3 | 3 | 3637, 7090, 7125 |
| `collectionItems` | 3 | 3 | 1823, 4962, 4998 |
| `defaultCardBackground` | 3 | 3 | 3748, 6235, 6334 |
| `detailPageSecondaryContainer` | 3 | 3 | 1660, 1687, 1813 |
| `emby-input` | 3 | 3 | 5500, 5529, 7677 |
| `formDialogFooterItem` | 3 | 3 | 3518, 3786, 3912 |
| `formDialogHeader` | 3 | 3 | 4001, 7540, 7611 |
| `iconOsd` | 3 | 3 | 5993, 7540, 7611 |
| `live_tv` | 3 | 3 | 2052, 2591, 4035 |
| `myPreferencesMenuPage` | 3 | 3 | 423, 4768, 5087 |
| `page` | 3 | 3 | 1044, 2766, 7042 |
| `playerStats` | 3 | 3 | 5993, 7611, 7647 |
| `readOnlyContent` | 3 | 3 | 4043, 6105, 6750 |
| `sectionTitle-cards` | 3 | 3 | 1791, 5156, 5216 |
| `sectionTitleContainer` | 3 | 3 | 1823, 1881, 4998 |
| `itemExternalLinks` | 13 | 2 | 3168–3246, 3398 |
| `checkboxOutline` | 10 | 2 | 3571–3612, 3643–3673 |
| `itemBackdrop` | 9 | 2 | 2018–2077, 2265 |
| `mdl-slider` | 9 | 2 | 2965, 3020–3078 |
| `cardOverlayButton-br` | 8 | 2 | 1060, 1089–1140 |
| `listItemIcon` | 8 | 2 | 4031–4035, 4708–4768 |
| `sliderContainer` | 8 | 2 | 2969, 2997–3062 |
| `detail-clamp-text` | 7 | 2 | 3334–3360, 3386–3390 |
| `divUsers` | 7 | 2 | 6116–6120, 7344–7371 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3608–3612, 3642–3661 |
| `countIndicator` | 6 | 2 | 799–829, 7611–7635 |
| `detailPagePrimaryContainer` | 6 | 2 | 1637–1683, 2498 |
| `detailsGroupItem` | 6 | 2 | 4821, 4892–4929 |
| `headerButton` | 6 | 2 | 589–669, 6600 |
| `headerLeft` | 6 | 2 | 1741–1778, 6855 |
| `selectionCommandsPanel` | 6 | 2 | 3528–3562, 7540 |
| `trackSelections` | 6 | 2 | 4794–4821, 4957–4962 |
| `withBackdrop` | 6 | 2 | 2674, 2716–2734 |
| `detailSection` | 5 | 2 | 4777–4786, 4942–4962 |
| `fullSyncIndicator` | 5 | 2 | 799–822, 7611–7635 |
| `mainDrawer-scrollContainer` | 5 | 2 | 3128, 7257–7274 |
| `mediaInfoItem` | 5 | 2 | 1895–1938, 7134 |
| `overview-expand` | 5 | 2 | 3366–3390, 4859 |
| `scrollX` | 5 | 2 | 1796, 1834–1854 |
| `videoIndicator` | 5 | 2 | 3716–3744, 7611 |
| `withSectionTabs` | 5 | 2 | 2725–2742, 6479 |
| `alphaPickerButton` | 4 | 2 | 669, 5013–5025 |
| `backgroundProgress` | 4 | 2 | 2880–2892, 2922 |
| `emby-select` | 4 | 2 | 5500–5512, 7677 |
| `emby-tab-button-active` | 4 | 2 | 3973, 6703–6717 |
| `manualLoginForm` | 4 | 2 | 6088–6124, 6165 |
| `mediaSourceIndicator` | 4 | 2 | 799–822, 7611 |
| `play_arrow` | 4 | 2 | 3753–3769, 3940 |
| `playbackProgress` | 4 | 2 | 2880–2892, 2927 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4595–4600, 6328–6334 |
| `programCell` | 4 | 2 | 5756, 5815–5824 |
| `section0` | 4 | 2 | 1014–1044, 7042 |
| `visualLoginForm` | 4 | 2 | 6088–6124, 6165 |
| `cardOverlayButtonIcon` | 3 | 2 | 1060–1072, 1140 |
| `castCollapsible` | 3 | 2 | 865, 3612–3621 |
| `emby-scrollbuttons-button` | 3 | 2 | 1885, 7951–7958 |
| `emby-textarea` | 3 | 2 | 5491–5500, 5529 |
| `guestCastContent` | 3 | 2 | 865, 3612–3621 |
| `guide-channelHeaderCell` | 3 | 2 | 669, 5790–5806 |
| `guide-date-tab-button` | 3 | 2 | 669, 3973–3981 |
| `headerUserButton` | 3 | 2 | 589–602, 5091 |
| `noHeaderRight` | 3 | 2 | 1711, 6015–6019 |
| `overview` | 3 | 2 | 3386–3390, 4869 |
| `add` | 2 | 2 | 1796, 7134 |
| `alphaPicker-fixed-right` | 2 | 2 | 2766, 5025 |
| `backdropImageFadeIn` | 2 | 2 | 2819, 7651 |
| `book` | 2 | 2 | 2052, 2591 |
| `btnDeleteImage` | 2 | 2 | 3773, 3987 |
| `cardContent` | 2 | 2 | 865, 897 |
| `cardOverlayButton` | 2 | 2 | 1074, 1117 |
| `cardOverlayButton-hover` | 2 | 2 | 957, 1089 |
| `chevron_right` | 2 | 2 | 5186, 5230 |
| `classList` | 2 | 2 | 1796, 7134 |
| `collapseContent` | 2 | 2 | 3523, 3999 |
| `collectionItemsContainer` | 2 | 2 | 1823, 5002 |
| `content-primary` | 2 | 2 | 5066, 5122 |
| `editorsChoiceContainer` | 2 | 2 | 6811, 7873 |
| `editorsChoiceItemBanner` | 2 | 2 | 6811, 7559 |
| `editorsChoiceItemOverview` | 2 | 2 | 7873, 7962 |
| `endsAt` | 2 | 2 | 1916, 7134 |
| `fieldDescription` | 2 | 2 | 311, 7677 |
| `formDialogFooter-clear` | 2 | 2 | 3518, 4001 |
| `guide-programNameCaret` | 2 | 2 | 311, 5772 |
| `headroom` | 2 | 2 | 6467, 6504 |
| `indicator` | 2 | 2 | 829, 3705 |
| `mediaInfoOfficialRating` | 2 | 2 | 1916, 7134 |
| `navMenuOption-selected` | 2 | 2 | 4773, 7268 |
| `nowPlayingInfoContainer` | 2 | 2 | 3159, 6265 |
| `org` | 2 | 2 | 3195, 3225 |
| `paperList` | 2 | 2 | 874, 4012 |
| `playlist` | 2 | 2 | 4590, 6243 |
| `programSecondaryTitle` | 2 | 2 | 311, 5824 |
| `queue` | 2 | 2 | 2052, 2591 |
| `reactRoot` | 2 | 2 | 4466, 6861 |
| `recordingFields` | 2 | 2 | 4813, 4957 |
| `runtime` | 2 | 2 | 6177, 6205 |
| `sectionTitleContainer-cards` | 2 | 2 | 5151, 5216 |
| `sidebarHeader` | 2 | 2 | 4140, 7274 |
| `splide` | 2 | 2 | 6811, 7918 |
| `tagline` | 2 | 2 | 2665, 4869 |
| `upNextDialog-title` | 2 | 2 | 5272, 5306 |
| `vertical-list` | 2 | 2 | 1858, 7779 |
| `vertical-wrap` | 2 | 2 | 795, 1823 |
| `videoOsdBottom` | 2 | 2 | 3151, 6434 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3151, 6434 |
| `userPreferencesPage` | 12 | 1 | 7662–7758 |
| `checkboxContainer` | 7 | 1 | 3600–3637 |
| `itemDetailsGroup` | 7 | 1 | 4876–4962 |
| `itemProgressBar` | 6 | 1 | 2869–2903 |
| `streaming-lookup-container` | 6 | 1 | 3253–3298 |
| `trackSelectionFieldContainer` | 6 | 1 | 4832–4855 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7918–7958 |
| `innerCardFooter` | 5 | 1 | 3413–3442 |
| `chapterCardImageContainer` | 4 | 1 | 3413–3442 |
| `emby-select-withcolor` | 4 | 1 | 5500–5547 |
| `endTimeText` | 4 | 1 | 6177–6205 |
| `mainDetailButtons` | 4 | 1 | 3936–3950 |
| `overview-controls` | 4 | 1 | 3386–3398 |
| `startTimeText` | 4 | 1 | 6177–6199 |
| `button-flat` | 3 | 1 | 3132–3142 |
| `cardIndicators` | 3 | 1 | 3690–3700 |
| `cardOverlayFab-primary` | 3 | 1 | 1052–1074 |
| `com` | 3 | 1 | 3201–3219 |
| `content` | 3 | 1 | 4898–4929 |
| `discover-card` | 3 | 1 | 7969–7992 |
| `fab` | 3 | 1 | 3795–3808 |
| `listChildrenCollapsible` | 3 | 1 | 4947–4962 |
| `mdl-slider-background-flex` | 3 | 1 | 2989–3002 |
| `mediaInfoCriticRating` | 3 | 1 | 1957–1966 |
| `nextUpSection` | 3 | 1 | 4942–4962 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 6229–6239 |
| `serverInfo` | 3 | 1 | 4016–4025 |
| `transcodingProgress` | 3 | 1 | 2880–2892 |
