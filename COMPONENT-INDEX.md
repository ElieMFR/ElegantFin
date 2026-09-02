# Index des composants — ElegantFin Cinema Edition v1.2.94

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.2.94.css` — 6244 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 32 | 14 | 383–394, 426–438, 616, 698, 1332–1352, 1821–1854, 1881–1885, 2141–2172, 5437, 5721–5737, 5817–5839, 5869, 5941, 6214 |
| `cardScalable` | 25 | 13 | 383–394, 431–438, 644–688, 714–752, 2159, 3054, 3156, 3235, 4741, 5451–5461, 5530, 5721, 5860–5869 |
| `cardImageContainer` | 24 | 13 | 426, 666, 694–723, 752, 809–839, 4850–4854, 4935, 5443, 5522–5530, 5568–5584, 5721–5737, 5860, 5989 |
| `material-icons` | 15 | 11 | 319–338, 1517, 1576, 1628, 3017, 3161, 3235–3241, 3347, 3600, 4050, 4084–4094 |
| `itemDetailPage` | 16 | 10 | 1395, 1468, 1526, 1747–1772, 1816, 1896, 2187–2192, 3694, 3971, 6042–6080 |
| `nameContainer` | 27 | 9 | 575, 1904–1927, 1968, 1997, 2032–2078, 2115, 2146–2150, 4417–4469, 6042–6080 |
| `card-hoverable` | 23 | 8 | 438, 654, 714–802, 4854, 5461, 5595–5614, 5721, 5996 |
| `parentName` | 23 | 8 | 575, 1909–1927, 1968, 1997, 2032–2078, 4423–4469, 4542, 6042–6080 |
| `subtitle` | 16 | 8 | 1747, 1816, 1909, 1968, 2087–2097, 2187–2192, 4477–4510, 6042–6080 |
| `cardBox` | 11 | 8 | 383–394, 420–438, 616, 736, 843, 5437, 5721, 5996 |
| `detailLogo` | 17 | 7 | 575, 1761–1772, 1807–1816, 1896–1927, 1997, 2032–2078, 2146 |
| `detailPageWrapperContainer` | 17 | 7 | 575, 1363–1373, 1772, 1890–1927, 1997, 2032–2078, 2146 |
| `loginPage` | 14 | 7 | 3314, 4753–4768, 4807, 4835–4854, 5466, 5509, 5849–5869 |
| `backdropCard` | 12 | 7 | 796–802, 905, 1747, 1833, 1896, 2150–2192, 2457 |
| `skinHeader` | 11 | 7 | 4749, 5078, 5134–5142, 5168–5193, 5513, 5689, 6151 |
| `emby-button` | 9 | 7 | 512–529, 556, 2816–2823, 3181, 3216, 3369, 3618 |
| `nowPlayingBar` | 8 | 6 | 2701, 4987, 5476, 5555, 5670–5701, 5946 |
| `listItem` | 16 | 5 | 529, 2163, 3518–3544, 3575–3609, 5964–5981 |
| `osdHeader` | 15 | 5 | 1498–1508, 5073–5142, 5168–5193, 5513, 5946 |
| `actionSheetMenuItem` | 11 | 5 | 529, 3518–3529, 3575, 3655–3671, 5494 |
| `emby-scroller-container` | 11 | 5 | 1521–1534, 2348, 2379, 5522, 5624–5652 |
| `navMenuOption` | 11 | 5 | 529, 605–611, 3581–3609, 3675–3680, 5760–5771 |
| `verticalSection` | 10 | 5 | 1521, 2358–2363, 3971, 5522, 5877 |
| `cardImageIcon` | 8 | 5 | 375–379, 2150–2159, 2198, 3044, 4935 |
| `person` | 8 | 5 | 1747–1757, 1896, 2150–2183, 3436, 6037 |
| `portraitCard` | 5 | 5 | 905, 983, 1666, 1881, 2457 |
| `btnPlay` | 14 | 4 | 449, 488–529, 3245–3287, 3320–3347 |
| `cardOverlayContainer` | 12 | 4 | 770–802, 847–867, 917, 5946–5964 |
| `itemName` | 11 | 4 | 575, 1968, 4423–4469, 4560–4577 |
| `upNextContainer` | 10 | 4 | 4112–4131, 4157–4183, 5466–5476, 5502 |
| `backdropImage` | 9 | 4 | 2264–2291, 2318–2322, 5431, 5530 |
| `emby-tab-button` | 9 | 4 | 529, 585, 3293, 5230–5266 |
| `sectionTabs` | 9 | 4 | 1545, 3293, 5114–5119, 5245–5271 |
| `button-link` | 7 | 4 | 529, 556, 2651–2660, 2721–2731 |
| `detailRibbon` | 7 | 4 | 1420–1448, 1581, 1666–1671, 6037 |
| `listItemBodyText` | 7 | 4 | 3539–3558, 3600, 3659, 5981 |
| `visualCardBox` | 7 | 4 | 383, 675–688, 714–719, 843 |
| `detailPagePrimaryContent` | 6 | 4 | 1435–1453, 2102, 3965, 5705 |
| `paper-icon-button-light` | 6 | 4 | 488–529, 1517, 1576, 4336 |
| `skip-button` | 6 | 4 | 529, 3298, 4206–4223, 4250–4256 |
| `button-submit` | 5 | 4 | 3314, 3401, 4835–4843, 6012 |
| `mainDrawer` | 5 | 4 | 2665, 5466–5476, 5747, 5786 |
| `sectionTitle` | 5 | 4 | 1521, 1555–1562, 4030, 4802 |
| `skinHeader-blurred` | 5 | 4 | 4749, 5102–5109, 5689, 5946 |
| `js` | 4 | 4 | 286, 1968, 2515, 5877 |
| `page` | 4 | 4 | 839, 2339, 2379, 5522 |
| `raised` | 4 | 4 | 529, 595, 3181, 3216 |
| `skinHeader-withBackground` | 4 | 4 | 1463, 4749, 5073, 5123 |
| `detailImageContainer` | 19 | 3 | 1747–1757, 1821–1896, 2137–2192 |
| `detailButton` | 12 | 3 | 488–529, 3226–3287, 3343–3347 |
| `emby-scroller` | 9 | 3 | 1526–1540, 5792–5839, 5932–5941 |
| `check` | 8 | 3 | 3017, 3235, 3651–3671 |
| `itemSelectionPanel` | 8 | 3 | 727–731, 2989, 3017–3054 |
| `pageTitle` | 8 | 3 | 1472–1508, 5134, 5193 |
| `detailSectionContent` | 6 | 3 | 2848, 3776–3786, 3867–3877 |
| `emby-checkbox` | 6 | 3 | 2994, 3031–3035, 3077–3089 |
| `headerTop` | 6 | 3 | 5084–5109, 5160–5177, 5204–5208 |
| `squareCard` | 6 | 3 | 698, 2150–2183, 4811–4815 |
| `actionSheetContent` | 5 | 3 | 3643–3647, 5466–5476, 5502 |
| `cardText-first` | 5 | 3 | 757, 3023–3049, 4916 |
| `dialog` | 5 | 3 | 2898–2908, 5466–5476, 5502 |
| `guideProgramName` | 5 | 3 | 529, 4601–4612, 4655–4660 |
| `musicParentName` | 5 | 3 | 1747, 2187–2192, 4542–4551 |
| `overflowBackdropCard` | 5 | 3 | 796–802, 3027, 4911–4916 |
| `cardPadder` | 4 | 3 | 379, 843, 3040–3044 |
| `cardText` | 4 | 3 | 757–767, 3049, 5865 |
| `cardText-secondary` | 4 | 3 | 757, 3049, 5601–5609 |
| `dialog-fullscreen` | 4 | 3 | 2908, 5466–5476, 5502 |
| `emby-scrollbuttons` | 4 | 3 | 1567–1572, 5877, 6189 |
| `infoWrapper` | 4 | 3 | 1860–1865, 2102, 2130 |
| `listItemImage` | 4 | 3 | 2434–2439, 3512, 5981 |
| `semiTransparent` | 4 | 3 | 1463, 4749, 5102–5123 |
| `toast` | 4 | 3 | 4104, 5466–5476, 5502 |
| `appfooter` | 3 | 3 | 2400, 5538, 5946 |
| `defaultCardBackground` | 3 | 3 | 3156, 4931, 5030 |
| `folder` | 3 | 3 | 1666, 3143, 3199 |
| `formDialogFooterItem` | 3 | 3 | 2969, 3194, 3320 |
| `itemsContainer` | 3 | 3 | 616, 1549, 3971 |
| `live_tv` | 3 | 3 | 1747, 2172, 3436 |
| `myPreferencesMenuPage` | 3 | 3 | 352, 3685, 3979 |
| `sectionTitle-cards` | 3 | 3 | 1521, 4030, 4080 |
| `x` | 3 | 3 | 1968, 4525, 5656 |
| `itemExternalLinks` | 11 | 2 | 2714–2771, 2848 |
| `mdl-slider` | 9 | 2 | 2511, 2566–2624 |
| `itemBackdrop` | 8 | 2 | 1713–1757, 2192 |
| `listItemIcon` | 8 | 2 | 3432–3436, 3655–3685 |
| `sectionTitleTextButton` | 8 | 2 | 4013–4050, 4084–4094 |
| `sliderContainer` | 8 | 2 | 2515, 2543–2608 |
| `detail-clamp-text` | 7 | 2 | 2784–2810, 2836–2840 |
| `backgroundContainer` | 6 | 2 | 2254, 2296–2314 |
| `detailPagePrimaryContainer` | 6 | 2 | 1407–1453, 2102 |
| `detailsGroupItem` | 6 | 2 | 3738, 3806–3844 |
| `divUsers` | 6 | 2 | 4811–4815, 5849–5869 |
| `headerLeft` | 6 | 2 | 1478–1508, 5359 |
| `trackSelections` | 6 | 2 | 3711–3738, 3872–3877 |
| `withBackdrop` | 6 | 2 | 2254, 2296–2314 |
| `detailSection` | 5 | 2 | 3694–3703, 3857–3877 |
| `headerButton` | 5 | 2 | 474–529, 5186 |
| `mainDrawer-scrollContainer` | 5 | 2 | 2674, 5760–5777 |
| `mediaInfoItem` | 5 | 2 | 1585–1628, 5656 |
| `overview-expand` | 5 | 2 | 2816–2840, 3776 |
| `playedIndicator` | 5 | 2 | 3126, 5721–5742 |
| `videoIndicator` | 5 | 2 | 3132–3152, 6003 |
| `withSectionTabs` | 5 | 2 | 2305–2322, 5109 |
| `album` | 4 | 2 | 1896, 2155–2172 |
| `emby-tab-button-active` | 4 | 2 | 3380, 5257–5271 |
| `noHomeButtonHeader` | 4 | 2 | 5134, 5230–5238 |
| `play_arrow` | 4 | 2 | 3161–3177, 3347 |
| `playlistIndexIndicatorImage` | 4 | 2 | 3539–3544, 5024–5030 |
| `programCell` | 4 | 2 | 4592, 4651–4660 |
| `secondary` | 4 | 2 | 3548–3558, 3600 |
| `section0` | 4 | 2 | 809–839, 5522 |
| `visualLoginForm` | 4 | 2 | 4802–4819, 4860 |
| `alphaPickerButton` | 3 | 2 | 529, 3916–3923 |
| `cardFooter` | 3 | 2 | 3054, 5595–5614 |
| `castCollapsible` | 3 | 2 | 666, 3035–3044 |
| `detailPageContent` | 3 | 2 | 3707, 3958–3965 |
| `emby-scrollbuttons-button` | 3 | 2 | 1576, 6196–6203 |
| `guestCastContent` | 3 | 2 | 666, 3035–3044 |
| `guide-channelHeaderCell` | 3 | 2 | 529, 4626–4642 |
| `guide-date-tab-button` | 3 | 2 | 529, 3380–3388 |
| `manualLoginForm` | 3 | 2 | 4802–4819, 4860 |
| `overview` | 3 | 2 | 2836–2840, 3786 |
| `programGuideSection` | 3 | 2 | 2163, 3877–3892 |
| `selectionCommandsPanel` | 3 | 2 | 2979–2985, 5946 |
| `blurhash-canvas` | 2 | 2 | 5568, 5989 |
| `book` | 2 | 2 | 1747, 2172 |
| `btnDeleteImage` | 2 | 2 | 3181, 3394 |
| `cardContent` | 2 | 2 | 666, 698 |
| `cardImage` | 2 | 2 | 5568, 5989 |
| `cardOverlayButton-hover` | 2 | 2 | 752, 872 |
| `cardOverlayButtonIcon` | 2 | 2 | 855, 910 |
| `chevron_right` | 2 | 2 | 4050, 4094 |
| `collapseContent` | 2 | 2 | 2974, 3406 |
| `content-primary` | 2 | 2 | 3958, 3996 |
| `countIndicator` | 2 | 2 | 635, 5549 |
| `detailPageSecondaryContainer` | 2 | 2 | 1430, 1457 |
| `editorsChoiceItemOverview` | 2 | 2 | 6126, 6207 |
| `endsAt` | 2 | 2 | 1606, 5656 |
| `formDialogFooter` | 2 | 2 | 2969, 3406 |
| `formDialogFooter-clear` | 2 | 2 | 2969, 3406 |
| `formDialogHeader` | 2 | 2 | 3406, 5946 |
| `headerUserButton` | 2 | 2 | 474, 3983 |
| `headroom` | 2 | 2 | 5097, 5134 |
| `iconOsd` | 2 | 2 | 4727, 5946 |
| `mediaSourceIndicator` | 2 | 2 | 635, 6003 |
| `navMenuOption-selected` | 2 | 2 | 3690, 5771 |
| `nowPlayingInfoContainer` | 2 | 2 | 2705, 4961 |
| `org` | 2 | 2 | 2741, 2771 |
| `paperList` | 2 | 2 | 675, 3413 |
| `playlist` | 2 | 2 | 3534, 4939 |
| `queue` | 2 | 2 | 1747, 2172 |
| `readOnlyContent` | 2 | 2 | 3444, 5288 |
| `recordingFields` | 2 | 2 | 3730, 3872 |
| `runtime` | 2 | 2 | 4872, 4901 |
| `sectionTitleContainer` | 2 | 2 | 1572, 3901 |
| `sectionTitleContainer-cards` | 2 | 2 | 4025, 4080 |
| `tagline` | 2 | 2 | 2245, 3786 |
| `upNextDialog-title` | 2 | 2 | 4136, 4170 |
| `vertical-list` | 2 | 2 | 1549, 6032 |
| `videoOsdBottom` | 2 | 2 | 2697, 5064 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 2697, 5064 |
| `checkboxOutline` | 10 | 1 | 2994–3089 |
| `cardOverlayButton-br` | 7 | 1 | 855–910 |
| `itemDetailsGroup` | 7 | 1 | 3790–3877 |
| `checkboxContainer` | 6 | 1 | 3023–3054 |
| `multiSelectCheckboxOutline` | 6 | 1 | 3031–3077 |
| `trackSelectionFieldContainer` | 6 | 1 | 3749–3772 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 6163–6203 |
| `innerCardFooter` | 5 | 1 | 2861–2890 |
| `itemProgressBar` | 5 | 1 | 2434–2457 |
| `backgroundProgress` | 4 | 1 | 2445–2468 |
| `chapterCardImageContainer` | 4 | 1 | 2861–2890 |
| `endTimeText` | 4 | 1 | 4872–4901 |
| `mainDetailButtons` | 4 | 1 | 3343–3357 |
| `overview-controls` | 4 | 1 | 2836–2848 |
| `playbackProgress` | 4 | 1 | 2445–2473 |
| `scrollX` | 4 | 1 | 1526–1545 |
| `startTimeText` | 4 | 1 | 4872–4895 |
| `button-flat` | 3 | 1 | 2678–2688 |
| `cardIndicators` | 3 | 1 | 3106–3116 |
| `cardOverlayFab-primary` | 3 | 1 | 847–867 |
| `com` | 3 | 1 | 2747–2765 |
| `content` | 3 | 1 | 3813–3844 |
| `discover-card` | 3 | 1 | 6214–6237 |
| `emby-select-withcolor` | 3 | 1 | 4350–4384 |
| `emby-textarea` | 3 | 1 | 4341–4366 |
| `fab` | 3 | 1 | 3203–3216 |
| `listChildrenCollapsible` | 3 | 1 | 3862–3877 |
| `mdl-slider-background-flex` | 3 | 1 | 2535–2548 |
| `mediaInfoCriticRating` | 3 | 1 | 1647–1656 |
| `nextUpSection` | 3 | 1 | 3857–3877 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 4925–4935 |
| `serverInfo` | 3 | 1 | 3417–3426 |
| `transcodingProgress` | 3 | 1 | 2445–2457 |
