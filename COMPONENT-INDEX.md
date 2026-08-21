# Index des composants — ElegantFin Cinema Edition v1.2.93

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.2.93.css` — 6229 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 32 | 14 | 383–394, 426–438, 616, 698, 1332–1352, 1821–1854, 1881–1885, 2141–2172, 5422, 5706–5722, 5802–5824, 5854, 5926, 6199 |
| `cardScalable` | 25 | 13 | 383–394, 431–438, 644–688, 714–752, 2159, 3054, 3156, 3235, 4726, 5436–5446, 5515, 5706, 5845–5854 |
| `cardImageContainer` | 24 | 13 | 426, 666, 694–723, 752, 809–839, 4835–4839, 4920, 5428, 5507–5515, 5553–5569, 5706–5722, 5845, 5974 |
| `material-icons` | 15 | 11 | 319–338, 1517, 1576, 1628, 3017, 3161, 3235–3241, 3347, 3600, 4035, 4069–4079 |
| `itemDetailPage` | 16 | 10 | 1395, 1468, 1526, 1747–1772, 1816, 1896, 2187–2192, 3694, 3956, 6027–6065 |
| `nameContainer` | 27 | 9 | 575, 1904–1927, 1968, 1997, 2032–2078, 2115, 2146–2150, 4402–4454, 6027–6065 |
| `card-hoverable` | 23 | 8 | 438, 654, 714–802, 4839, 5446, 5580–5599, 5706, 5981 |
| `parentName` | 23 | 8 | 575, 1909–1927, 1968, 1997, 2032–2078, 4408–4454, 4527, 6027–6065 |
| `subtitle` | 16 | 8 | 1747, 1816, 1909, 1968, 2087–2097, 2187–2192, 4462–4495, 6027–6065 |
| `cardBox` | 11 | 8 | 383–394, 420–438, 616, 736, 843, 5422, 5706, 5981 |
| `detailLogo` | 17 | 7 | 575, 1761–1772, 1807–1816, 1896–1927, 1997, 2032–2078, 2146 |
| `detailPageWrapperContainer` | 17 | 7 | 575, 1363–1373, 1772, 1890–1927, 1997, 2032–2078, 2146 |
| `loginPage` | 14 | 7 | 3314, 4738–4753, 4792, 4820–4839, 5451, 5494, 5834–5854 |
| `backdropCard` | 12 | 7 | 796–802, 905, 1747, 1833, 1896, 2150–2192, 2457 |
| `skinHeader` | 11 | 7 | 4734, 5063, 5119–5127, 5153–5178, 5498, 5674, 6136 |
| `emby-button` | 9 | 7 | 512–529, 556, 2816–2823, 3181, 3216, 3369, 3618 |
| `nowPlayingBar` | 8 | 6 | 2701, 4972, 5461, 5540, 5655–5686, 5931 |
| `listItem` | 16 | 5 | 529, 2163, 3518–3544, 3575–3609, 5949–5966 |
| `osdHeader` | 15 | 5 | 1498–1508, 5058–5127, 5153–5178, 5498, 5931 |
| `actionSheetMenuItem` | 11 | 5 | 529, 3518–3529, 3575, 3655–3671, 5479 |
| `emby-scroller-container` | 11 | 5 | 1521–1534, 2348, 2379, 5507, 5609–5637 |
| `navMenuOption` | 11 | 5 | 529, 605–611, 3581–3609, 3675–3680, 5745–5756 |
| `verticalSection` | 10 | 5 | 1521, 2358–2363, 3956, 5507, 5862 |
| `cardImageIcon` | 8 | 5 | 375–379, 2150–2159, 2198, 3044, 4920 |
| `person` | 8 | 5 | 1747–1757, 1896, 2150–2183, 3436, 6022 |
| `portraitCard` | 5 | 5 | 905, 983, 1666, 1881, 2457 |
| `btnPlay` | 14 | 4 | 449, 488–529, 3245–3287, 3320–3347 |
| `cardOverlayContainer` | 12 | 4 | 770–802, 847–867, 917, 5931–5949 |
| `itemName` | 11 | 4 | 575, 1968, 4408–4454, 4545–4562 |
| `upNextContainer` | 10 | 4 | 4097–4116, 4142–4168, 5451–5461, 5487 |
| `backdropImage` | 9 | 4 | 2264–2291, 2318–2322, 5416, 5515 |
| `emby-tab-button` | 9 | 4 | 529, 585, 3293, 5215–5251 |
| `sectionTabs` | 9 | 4 | 1545, 3293, 5099–5104, 5230–5256 |
| `button-link` | 7 | 4 | 529, 556, 2651–2660, 2721–2731 |
| `detailRibbon` | 7 | 4 | 1420–1448, 1581, 1666–1671, 6022 |
| `listItemBodyText` | 7 | 4 | 3539–3558, 3600, 3659, 5966 |
| `visualCardBox` | 7 | 4 | 383, 675–688, 714–719, 843 |
| `detailPagePrimaryContent` | 6 | 4 | 1435–1453, 2102, 3950, 5690 |
| `paper-icon-button-light` | 6 | 4 | 488–529, 1517, 1576, 4321 |
| `skip-button` | 6 | 4 | 529, 3298, 4191–4208, 4235–4241 |
| `button-submit` | 5 | 4 | 3314, 3401, 4820–4828, 5997 |
| `mainDrawer` | 5 | 4 | 2665, 5451–5461, 5732, 5771 |
| `sectionTitle` | 5 | 4 | 1521, 1555–1562, 4015, 4787 |
| `skinHeader-blurred` | 5 | 4 | 4734, 5087–5094, 5674, 5931 |
| `js` | 4 | 4 | 286, 1968, 2515, 5862 |
| `page` | 4 | 4 | 839, 2339, 2379, 5507 |
| `raised` | 4 | 4 | 529, 595, 3181, 3216 |
| `skinHeader-withBackground` | 4 | 4 | 1463, 4734, 5058, 5108 |
| `detailImageContainer` | 19 | 3 | 1747–1757, 1821–1896, 2137–2192 |
| `detailButton` | 12 | 3 | 488–529, 3226–3287, 3343–3347 |
| `emby-scroller` | 9 | 3 | 1526–1540, 5777–5824, 5917–5926 |
| `check` | 8 | 3 | 3017, 3235, 3651–3671 |
| `itemSelectionPanel` | 8 | 3 | 727–731, 2989, 3017–3054 |
| `pageTitle` | 8 | 3 | 1472–1508, 5119, 5178 |
| `detailSectionContent` | 6 | 3 | 2848, 3776–3786, 3852–3862 |
| `emby-checkbox` | 6 | 3 | 2994, 3031–3035, 3077–3089 |
| `headerTop` | 6 | 3 | 5069–5094, 5145–5162, 5189–5193 |
| `squareCard` | 6 | 3 | 698, 2150–2183, 4796–4800 |
| `actionSheetContent` | 5 | 3 | 3643–3647, 5451–5461, 5487 |
| `cardText-first` | 5 | 3 | 757, 3023–3049, 4901 |
| `dialog` | 5 | 3 | 2898–2908, 5451–5461, 5487 |
| `guideProgramName` | 5 | 3 | 529, 4586–4597, 4640–4645 |
| `musicParentName` | 5 | 3 | 1747, 2187–2192, 4527–4536 |
| `overflowBackdropCard` | 5 | 3 | 796–802, 3027, 4896–4901 |
| `cardPadder` | 4 | 3 | 379, 843, 3040–3044 |
| `cardText` | 4 | 3 | 757–767, 3049, 5850 |
| `cardText-secondary` | 4 | 3 | 757, 3049, 5586–5594 |
| `dialog-fullscreen` | 4 | 3 | 2908, 5451–5461, 5487 |
| `emby-scrollbuttons` | 4 | 3 | 1567–1572, 5862, 6174 |
| `infoWrapper` | 4 | 3 | 1860–1865, 2102, 2130 |
| `listItemImage` | 4 | 3 | 2434–2439, 3512, 5966 |
| `semiTransparent` | 4 | 3 | 1463, 4734, 5087–5108 |
| `toast` | 4 | 3 | 4089, 5451–5461, 5487 |
| `appfooter` | 3 | 3 | 2400, 5523, 5931 |
| `defaultCardBackground` | 3 | 3 | 3156, 4916, 5015 |
| `folder` | 3 | 3 | 1666, 3143, 3199 |
| `formDialogFooterItem` | 3 | 3 | 2969, 3194, 3320 |
| `itemsContainer` | 3 | 3 | 616, 1549, 3956 |
| `live_tv` | 3 | 3 | 1747, 2172, 3436 |
| `myPreferencesMenuPage` | 3 | 3 | 352, 3685, 3964 |
| `sectionTitle-cards` | 3 | 3 | 1521, 4015, 4065 |
| `x` | 3 | 3 | 1968, 4510, 5641 |
| `itemExternalLinks` | 11 | 2 | 2714–2771, 2848 |
| `mdl-slider` | 9 | 2 | 2511, 2566–2624 |
| `itemBackdrop` | 8 | 2 | 1713–1757, 2192 |
| `listItemIcon` | 8 | 2 | 3432–3436, 3655–3685 |
| `sectionTitleTextButton` | 8 | 2 | 3998–4035, 4069–4079 |
| `sliderContainer` | 8 | 2 | 2515, 2543–2608 |
| `detail-clamp-text` | 7 | 2 | 2784–2810, 2836–2840 |
| `backgroundContainer` | 6 | 2 | 2254, 2296–2314 |
| `detailPagePrimaryContainer` | 6 | 2 | 1407–1453, 2102 |
| `detailsGroupItem` | 6 | 2 | 3738, 3806–3830 |
| `divUsers` | 6 | 2 | 4796–4800, 5834–5854 |
| `headerLeft` | 6 | 2 | 1478–1508, 5344 |
| `trackSelections` | 6 | 2 | 3711–3738, 3857–3862 |
| `withBackdrop` | 6 | 2 | 2254, 2296–2314 |
| `detailSection` | 5 | 2 | 3694–3703, 3842–3862 |
| `headerButton` | 5 | 2 | 474–529, 5171 |
| `itemDetailsGroup` | 5 | 2 | 3790–3802, 3838–3862 |
| `mainDrawer-scrollContainer` | 5 | 2 | 2674, 5745–5762 |
| `mediaInfoItem` | 5 | 2 | 1585–1628, 5641 |
| `overview-expand` | 5 | 2 | 2816–2840, 3776 |
| `playedIndicator` | 5 | 2 | 3126, 5706–5727 |
| `videoIndicator` | 5 | 2 | 3132–3152, 5988 |
| `withSectionTabs` | 5 | 2 | 2305–2322, 5094 |
| `album` | 4 | 2 | 1896, 2155–2172 |
| `emby-tab-button-active` | 4 | 2 | 3380, 5242–5256 |
| `noHomeButtonHeader` | 4 | 2 | 5119, 5215–5223 |
| `play_arrow` | 4 | 2 | 3161–3177, 3347 |
| `playlistIndexIndicatorImage` | 4 | 2 | 3539–3544, 5009–5015 |
| `programCell` | 4 | 2 | 4577, 4636–4645 |
| `secondary` | 4 | 2 | 3548–3558, 3600 |
| `section0` | 4 | 2 | 809–839, 5507 |
| `visualLoginForm` | 4 | 2 | 4787–4804, 4845 |
| `alphaPickerButton` | 3 | 2 | 529, 3901–3908 |
| `cardFooter` | 3 | 2 | 3054, 5580–5599 |
| `castCollapsible` | 3 | 2 | 666, 3035–3044 |
| `detailPageContent` | 3 | 2 | 3707, 3943–3950 |
| `emby-scrollbuttons-button` | 3 | 2 | 1576, 6181–6188 |
| `guestCastContent` | 3 | 2 | 666, 3035–3044 |
| `guide-channelHeaderCell` | 3 | 2 | 529, 4611–4627 |
| `guide-date-tab-button` | 3 | 2 | 529, 3380–3388 |
| `manualLoginForm` | 3 | 2 | 4787–4804, 4845 |
| `overview` | 3 | 2 | 2836–2840, 3786 |
| `programGuideSection` | 3 | 2 | 2163, 3862–3877 |
| `selectionCommandsPanel` | 3 | 2 | 2979–2985, 5931 |
| `blurhash-canvas` | 2 | 2 | 5553, 5974 |
| `book` | 2 | 2 | 1747, 2172 |
| `btnDeleteImage` | 2 | 2 | 3181, 3394 |
| `cardContent` | 2 | 2 | 666, 698 |
| `cardImage` | 2 | 2 | 5553, 5974 |
| `cardOverlayButton-hover` | 2 | 2 | 752, 872 |
| `cardOverlayButtonIcon` | 2 | 2 | 855, 910 |
| `chevron_right` | 2 | 2 | 4035, 4079 |
| `collapseContent` | 2 | 2 | 2974, 3406 |
| `content-primary` | 2 | 2 | 3943, 3981 |
| `countIndicator` | 2 | 2 | 635, 5534 |
| `detailPageSecondaryContainer` | 2 | 2 | 1430, 1457 |
| `editorsChoiceItemOverview` | 2 | 2 | 6111, 6192 |
| `endsAt` | 2 | 2 | 1606, 5641 |
| `formDialogFooter` | 2 | 2 | 2969, 3406 |
| `formDialogFooter-clear` | 2 | 2 | 2969, 3406 |
| `formDialogHeader` | 2 | 2 | 3406, 5931 |
| `headerUserButton` | 2 | 2 | 474, 3968 |
| `headroom` | 2 | 2 | 5082, 5119 |
| `iconOsd` | 2 | 2 | 4712, 5931 |
| `mediaSourceIndicator` | 2 | 2 | 635, 5988 |
| `navMenuOption-selected` | 2 | 2 | 3690, 5756 |
| `nowPlayingInfoContainer` | 2 | 2 | 2705, 4946 |
| `org` | 2 | 2 | 2741, 2771 |
| `paperList` | 2 | 2 | 675, 3413 |
| `playlist` | 2 | 2 | 3534, 4924 |
| `queue` | 2 | 2 | 1747, 2172 |
| `readOnlyContent` | 2 | 2 | 3444, 5273 |
| `recordingFields` | 2 | 2 | 3730, 3857 |
| `runtime` | 2 | 2 | 4857, 4886 |
| `sectionTitleContainer` | 2 | 2 | 1572, 3886 |
| `sectionTitleContainer-cards` | 2 | 2 | 4010, 4065 |
| `tagline` | 2 | 2 | 2245, 3786 |
| `upNextDialog-title` | 2 | 2 | 4121, 4155 |
| `vertical-list` | 2 | 2 | 1549, 6017 |
| `videoOsdBottom` | 2 | 2 | 2697, 5049 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 2697, 5049 |
| `checkboxOutline` | 10 | 1 | 2994–3089 |
| `cardOverlayButton-br` | 7 | 1 | 855–910 |
| `checkboxContainer` | 6 | 1 | 3023–3054 |
| `multiSelectCheckboxOutline` | 6 | 1 | 3031–3077 |
| `trackSelectionFieldContainer` | 6 | 1 | 3749–3772 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 6148–6188 |
| `innerCardFooter` | 5 | 1 | 2861–2890 |
| `itemProgressBar` | 5 | 1 | 2434–2457 |
| `backgroundProgress` | 4 | 1 | 2445–2468 |
| `chapterCardImageContainer` | 4 | 1 | 2861–2890 |
| `endTimeText` | 4 | 1 | 4857–4886 |
| `mainDetailButtons` | 4 | 1 | 3343–3357 |
| `overview-controls` | 4 | 1 | 2836–2848 |
| `playbackProgress` | 4 | 1 | 2445–2473 |
| `scrollX` | 4 | 1 | 1526–1545 |
| `startTimeText` | 4 | 1 | 4857–4880 |
| `button-flat` | 3 | 1 | 2678–2688 |
| `cardIndicators` | 3 | 1 | 3106–3116 |
| `cardOverlayFab-primary` | 3 | 1 | 847–867 |
| `com` | 3 | 1 | 2747–2765 |
| `discover-card` | 3 | 1 | 6199–6222 |
| `emby-select-withcolor` | 3 | 1 | 4335–4369 |
| `emby-textarea` | 3 | 1 | 4326–4351 |
| `fab` | 3 | 1 | 3203–3216 |
| `listChildrenCollapsible` | 3 | 1 | 3847–3862 |
| `mdl-slider-background-flex` | 3 | 1 | 2535–2548 |
| `mediaInfoCriticRating` | 3 | 1 | 1647–1656 |
| `nextUpSection` | 3 | 1 | 3842–3862 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 4910–4920 |
| `serverInfo` | 3 | 1 | 3417–3426 |
| `transcodingProgress` | 3 | 1 | 2445–2457 |
