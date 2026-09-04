# Index des composants — ElegantFin Cinema Edition v1.2.96

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.2.96.css` — 6278 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 32 | 14 | 383–394, 426–438, 616, 698, 1332–1352, 1821–1854, 1881–1885, 2161–2192, 5471, 5755–5771, 5851–5873, 5903, 5975, 6248 |
| `cardScalable` | 25 | 13 | 383–394, 431–438, 644–688, 714–752, 2179, 3074, 3176, 3255, 4761, 5485–5495, 5564, 5755, 5894–5903 |
| `cardImageContainer` | 24 | 13 | 426, 666, 694–723, 752, 809–839, 4870–4874, 4955, 5477, 5556–5564, 5602–5618, 5755–5771, 5894, 6023 |
| `material-icons` | 15 | 11 | 319–338, 1517, 1576, 1628, 3037, 3181, 3255–3261, 3367, 3620, 4070, 4104–4114 |
| `itemDetailPage` | 16 | 10 | 1395, 1468, 1526, 1747–1772, 1816, 1916, 2207–2212, 3714, 3991, 6076–6114 |
| `nameContainer` | 27 | 9 | 575, 1924–1947, 1988, 2017, 2052–2098, 2135, 2166–2170, 4437–4489, 6076–6114 |
| `card-hoverable` | 23 | 8 | 438, 654, 714–802, 4874, 5495, 5629–5648, 5755, 6030 |
| `parentName` | 23 | 8 | 575, 1929–1947, 1988, 2017, 2052–2098, 4443–4489, 4562, 6076–6114 |
| `detailPageWrapperContainer` | 17 | 8 | 575, 1363–1373, 1772, 1890, 1924–1947, 2017, 2052–2098, 2166 |
| `subtitle` | 16 | 8 | 1747, 1816, 1929, 1988, 2107–2117, 2207–2212, 4497–4530, 6076–6114 |
| `cardBox` | 11 | 8 | 383–394, 420–438, 616, 736, 843, 5471, 5755, 6030 |
| `detailLogo` | 17 | 7 | 575, 1761–1772, 1807–1816, 1916–1947, 2017, 2052–2098, 2166 |
| `loginPage` | 14 | 7 | 3334, 4773–4788, 4827, 4855–4874, 5500, 5543, 5883–5903 |
| `backdropCard` | 12 | 7 | 796–802, 905, 1747, 1833, 1916, 2170–2212, 2477 |
| `skinHeader` | 11 | 7 | 4769, 5098, 5154–5162, 5188–5213, 5547, 5723, 6185 |
| `emby-button` | 9 | 7 | 512–529, 556, 2836–2843, 3201, 3236, 3389, 3638 |
| `nowPlayingBar` | 8 | 6 | 2721, 5007, 5510, 5589, 5704–5735, 5980 |
| `listItem` | 16 | 5 | 529, 2183, 3538–3564, 3595–3629, 5998–6015 |
| `osdHeader` | 15 | 5 | 1498–1508, 5093–5162, 5188–5213, 5547, 5980 |
| `actionSheetMenuItem` | 11 | 5 | 529, 3538–3549, 3595, 3675–3691, 5528 |
| `emby-scroller-container` | 11 | 5 | 1521–1534, 2368, 2399, 5556, 5658–5686 |
| `navMenuOption` | 11 | 5 | 529, 605–611, 3601–3629, 3695–3700, 5794–5805 |
| `verticalSection` | 10 | 5 | 1521, 2378–2383, 3991, 5556, 5911 |
| `cardImageIcon` | 8 | 5 | 375–379, 2170–2179, 2218, 3064, 4955 |
| `person` | 8 | 5 | 1747–1757, 1916, 2170–2203, 3456, 6071 |
| `portraitCard` | 5 | 5 | 905, 983, 1666, 1881, 2477 |
| `detailImageContainer` | 19 | 4 | 1747–1757, 1821–1885, 1916, 2157–2212 |
| `btnPlay` | 14 | 4 | 449, 488–529, 3265–3307, 3340–3367 |
| `cardOverlayContainer` | 12 | 4 | 770–802, 847–867, 917, 5980–5998 |
| `itemName` | 11 | 4 | 575, 1988, 4443–4489, 4580–4597 |
| `upNextContainer` | 10 | 4 | 4132–4151, 4177–4203, 5500–5510, 5536 |
| `backdropImage` | 9 | 4 | 2284–2311, 2338–2342, 5465, 5564 |
| `emby-tab-button` | 9 | 4 | 529, 585, 3313, 5264–5300 |
| `sectionTabs` | 9 | 4 | 1545, 3313, 5134–5139, 5279–5305 |
| `button-link` | 7 | 4 | 529, 556, 2671–2680, 2741–2751 |
| `detailRibbon` | 7 | 4 | 1420–1448, 1581, 1666–1671, 6071 |
| `listItemBodyText` | 7 | 4 | 3559–3578, 3620, 3679, 6015 |
| `visualCardBox` | 7 | 4 | 383, 675–688, 714–719, 843 |
| `detailPagePrimaryContent` | 6 | 4 | 1435–1453, 2122, 3985, 5739 |
| `paper-icon-button-light` | 6 | 4 | 488–529, 1517, 1576, 4356 |
| `skip-button` | 6 | 4 | 529, 3318, 4226–4243, 4270–4276 |
| `button-submit` | 5 | 4 | 3334, 3421, 4855–4863, 6046 |
| `mainDrawer` | 5 | 4 | 2685, 5500–5510, 5781, 5820 |
| `sectionTitle` | 5 | 4 | 1521, 1555–1562, 4050, 4822 |
| `skinHeader-blurred` | 5 | 4 | 4769, 5122–5129, 5723, 5980 |
| `appfooter` | 4 | 4 | 2420, 5238, 5572, 5980 |
| `js` | 4 | 4 | 286, 1988, 2535, 5911 |
| `page` | 4 | 4 | 839, 2359, 2399, 5556 |
| `raised` | 4 | 4 | 529, 595, 3201, 3236 |
| `skinHeader-withBackground` | 4 | 4 | 1463, 4769, 5093, 5143 |
| `detailButton` | 12 | 3 | 488–529, 3246–3307, 3363–3367 |
| `emby-scroller` | 9 | 3 | 1526–1540, 5826–5873, 5966–5975 |
| `itemBackdrop` | 9 | 3 | 1713–1757, 1890, 2212 |
| `check` | 8 | 3 | 3037, 3255, 3671–3691 |
| `itemSelectionPanel` | 8 | 3 | 727–731, 3009, 3037–3074 |
| `pageTitle` | 8 | 3 | 1472–1508, 5154, 5213 |
| `detailSectionContent` | 6 | 3 | 2868, 3796–3806, 3887–3897 |
| `emby-checkbox` | 6 | 3 | 3014, 3051–3055, 3097–3109 |
| `headerTop` | 6 | 3 | 5104–5129, 5180–5197, 5224–5228 |
| `squareCard` | 6 | 3 | 698, 2170–2203, 4831–4835 |
| `actionSheetContent` | 5 | 3 | 3663–3667, 5500–5510, 5536 |
| `cardText-first` | 5 | 3 | 757, 3043–3069, 4936 |
| `dialog` | 5 | 3 | 2918–2928, 5500–5510, 5536 |
| `guideProgramName` | 5 | 3 | 529, 4621–4632, 4675–4680 |
| `musicParentName` | 5 | 3 | 1747, 2207–2212, 4562–4571 |
| `overflowBackdropCard` | 5 | 3 | 796–802, 3047, 4931–4936 |
| `cardPadder` | 4 | 3 | 379, 843, 3060–3064 |
| `cardText` | 4 | 3 | 757–767, 3069, 5899 |
| `cardText-secondary` | 4 | 3 | 757, 3069, 5635–5643 |
| `dialog-fullscreen` | 4 | 3 | 2928, 5500–5510, 5536 |
| `emby-scrollbuttons` | 4 | 3 | 1567–1572, 5911, 6223 |
| `infoWrapper` | 4 | 3 | 1860–1865, 2122, 2150 |
| `listItemImage` | 4 | 3 | 2454–2459, 3532, 6015 |
| `semiTransparent` | 4 | 3 | 1463, 4769, 5122–5143 |
| `toast` | 4 | 3 | 4124, 5500–5510, 5536 |
| `defaultCardBackground` | 3 | 3 | 3176, 4951, 5050 |
| `folder` | 3 | 3 | 1666, 3163, 3219 |
| `formDialogFooterItem` | 3 | 3 | 2989, 3214, 3340 |
| `itemsContainer` | 3 | 3 | 616, 1549, 3991 |
| `live_tv` | 3 | 3 | 1747, 2192, 3456 |
| `myPreferencesMenuPage` | 3 | 3 | 352, 3705, 3999 |
| `sectionTitle-cards` | 3 | 3 | 1521, 4050, 4100 |
| `x` | 3 | 3 | 1988, 4545, 5690 |
| `itemExternalLinks` | 11 | 2 | 2734–2791, 2868 |
| `mdl-slider` | 9 | 2 | 2531, 2586–2644 |
| `listItemIcon` | 8 | 2 | 3452–3456, 3675–3705 |
| `sectionTitleTextButton` | 8 | 2 | 4033–4070, 4104–4114 |
| `sliderContainer` | 8 | 2 | 2535, 2563–2628 |
| `detail-clamp-text` | 7 | 2 | 2804–2830, 2856–2860 |
| `backgroundContainer` | 6 | 2 | 2274, 2316–2334 |
| `detailPagePrimaryContainer` | 6 | 2 | 1407–1453, 2122 |
| `detailsGroupItem` | 6 | 2 | 3758, 3826–3864 |
| `divUsers` | 6 | 2 | 4831–4835, 5883–5903 |
| `headerLeft` | 6 | 2 | 1478–1508, 5393 |
| `trackSelections` | 6 | 2 | 3731–3758, 3892–3897 |
| `withBackdrop` | 6 | 2 | 2274, 2316–2334 |
| `detailSection` | 5 | 2 | 3714–3723, 3877–3897 |
| `headerButton` | 5 | 2 | 474–529, 5206 |
| `mainDrawer-scrollContainer` | 5 | 2 | 2694, 5794–5811 |
| `mediaInfoItem` | 5 | 2 | 1585–1628, 5690 |
| `overview-expand` | 5 | 2 | 2836–2860, 3796 |
| `playedIndicator` | 5 | 2 | 3146, 5755–5776 |
| `videoIndicator` | 5 | 2 | 3152–3172, 6037 |
| `withSectionTabs` | 5 | 2 | 2325–2342, 5129 |
| `album` | 4 | 2 | 1916, 2175–2192 |
| `emby-tab-button-active` | 4 | 2 | 3400, 5291–5305 |
| `noHomeButtonHeader` | 4 | 2 | 5154, 5264–5272 |
| `play_arrow` | 4 | 2 | 3181–3197, 3367 |
| `playlistIndexIndicatorImage` | 4 | 2 | 3559–3564, 5044–5050 |
| `programCell` | 4 | 2 | 4612, 4671–4680 |
| `secondary` | 4 | 2 | 3568–3578, 3620 |
| `section0` | 4 | 2 | 809–839, 5556 |
| `visualLoginForm` | 4 | 2 | 4822–4839, 4880 |
| `alphaPickerButton` | 3 | 2 | 529, 3936–3943 |
| `cardFooter` | 3 | 2 | 3074, 5629–5648 |
| `castCollapsible` | 3 | 2 | 666, 3055–3064 |
| `detailPageContent` | 3 | 2 | 3727, 3978–3985 |
| `emby-scrollbuttons-button` | 3 | 2 | 1576, 6230–6237 |
| `guestCastContent` | 3 | 2 | 666, 3055–3064 |
| `guide-channelHeaderCell` | 3 | 2 | 529, 4646–4662 |
| `guide-date-tab-button` | 3 | 2 | 529, 3400–3408 |
| `manualLoginForm` | 3 | 2 | 4822–4839, 4880 |
| `overview` | 3 | 2 | 2856–2860, 3806 |
| `programGuideSection` | 3 | 2 | 2183, 3897–3912 |
| `selectionCommandsPanel` | 3 | 2 | 2999–3005, 5980 |
| `blurhash-canvas` | 2 | 2 | 5602, 6023 |
| `book` | 2 | 2 | 1747, 2192 |
| `btnDeleteImage` | 2 | 2 | 3201, 3414 |
| `cardContent` | 2 | 2 | 666, 698 |
| `cardImage` | 2 | 2 | 5602, 6023 |
| `cardOverlayButton-hover` | 2 | 2 | 752, 872 |
| `cardOverlayButtonIcon` | 2 | 2 | 855, 910 |
| `chevron_right` | 2 | 2 | 4070, 4114 |
| `collapseContent` | 2 | 2 | 2994, 3426 |
| `content-primary` | 2 | 2 | 3978, 4016 |
| `countIndicator` | 2 | 2 | 635, 5583 |
| `detailPageSecondaryContainer` | 2 | 2 | 1430, 1457 |
| `editorsChoiceItemOverview` | 2 | 2 | 6160, 6241 |
| `endsAt` | 2 | 2 | 1606, 5690 |
| `formDialogFooter` | 2 | 2 | 2989, 3426 |
| `formDialogFooter-clear` | 2 | 2 | 2989, 3426 |
| `formDialogHeader` | 2 | 2 | 3426, 5980 |
| `headerUserButton` | 2 | 2 | 474, 4003 |
| `headroom` | 2 | 2 | 5117, 5154 |
| `iconOsd` | 2 | 2 | 4747, 5980 |
| `mediaSourceIndicator` | 2 | 2 | 635, 6037 |
| `navMenuOption-selected` | 2 | 2 | 3710, 5805 |
| `nowPlayingInfoContainer` | 2 | 2 | 2725, 4981 |
| `org` | 2 | 2 | 2761, 2791 |
| `paperList` | 2 | 2 | 675, 3433 |
| `playlist` | 2 | 2 | 3554, 4959 |
| `queue` | 2 | 2 | 1747, 2192 |
| `readOnlyContent` | 2 | 2 | 3464, 5322 |
| `recordingFields` | 2 | 2 | 3750, 3892 |
| `runtime` | 2 | 2 | 4892, 4921 |
| `sectionTitleContainer` | 2 | 2 | 1572, 3921 |
| `sectionTitleContainer-cards` | 2 | 2 | 4045, 4100 |
| `tagline` | 2 | 2 | 2265, 3806 |
| `upNextDialog-title` | 2 | 2 | 4156, 4190 |
| `vertical-list` | 2 | 2 | 1549, 6066 |
| `videoOsdBottom` | 2 | 2 | 2717, 5084 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 2717, 5084 |
| `checkboxOutline` | 10 | 1 | 3014–3109 |
| `cardOverlayButton-br` | 7 | 1 | 855–910 |
| `itemDetailsGroup` | 7 | 1 | 3810–3897 |
| `checkboxContainer` | 6 | 1 | 3043–3074 |
| `multiSelectCheckboxOutline` | 6 | 1 | 3051–3097 |
| `trackSelectionFieldContainer` | 6 | 1 | 3769–3792 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 6197–6237 |
| `innerCardFooter` | 5 | 1 | 2881–2910 |
| `itemProgressBar` | 5 | 1 | 2454–2477 |
| `backgroundProgress` | 4 | 1 | 2465–2488 |
| `chapterCardImageContainer` | 4 | 1 | 2881–2910 |
| `endTimeText` | 4 | 1 | 4892–4921 |
| `mainDetailButtons` | 4 | 1 | 3363–3377 |
| `overview-controls` | 4 | 1 | 2856–2868 |
| `playbackProgress` | 4 | 1 | 2465–2493 |
| `scrollX` | 4 | 1 | 1526–1545 |
| `startTimeText` | 4 | 1 | 4892–4915 |
| `button-flat` | 3 | 1 | 2698–2708 |
| `cardIndicators` | 3 | 1 | 3126–3136 |
| `cardOverlayFab-primary` | 3 | 1 | 847–867 |
| `com` | 3 | 1 | 2767–2785 |
| `content` | 3 | 1 | 3833–3864 |
| `discover-card` | 3 | 1 | 6248–6271 |
| `emby-select-withcolor` | 3 | 1 | 4370–4404 |
| `emby-textarea` | 3 | 1 | 4361–4386 |
| `fab` | 3 | 1 | 3223–3236 |
| `listChildrenCollapsible` | 3 | 1 | 3882–3897 |
| `mdl-slider-background-flex` | 3 | 1 | 2555–2568 |
| `mediaInfoCriticRating` | 3 | 1 | 1647–1656 |
| `nextUpSection` | 3 | 1 | 3877–3897 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 4945–4955 |
| `serverInfo` | 3 | 1 | 3437–3446 |
| `transcodingProgress` | 3 | 1 | 2465–2477 |
