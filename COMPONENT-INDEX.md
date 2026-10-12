# Index des composants — ElegantFin Cinema Edition v1.4.0

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.4.0.css` — 7907 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 38 | 16 | 428–439, 470–516, 754, 871, 1529–1549, 2140–2173, 2200–2204, 2481–2499, 2535, 6776, 6812–6822, 7058–7077, 7155–7177, 7207–7214, 7378, 7785 |
| `cardScalable` | 31 | 13 | 428–439, 493–516, 817–861, 887–931, 2499, 3579, 3690, 3769, 5923, 6790–6822, 6893, 7058, 7198–7214 |
| `itemDetailPage` | 21 | 13 | 1592, 1678, 1757, 1784, 2013–2049, 2084–2099, 2135, 2236, 2548, 4025–4036, 4696, 4995, 7613–7651 |
| `material-icons` | 17 | 13 | 364–383, 1748, 1846, 1899, 3536, 3695, 3769–3775, 3882, 4040, 4573, 5102, 5136–5146, 5740 |
| `cardImageContainer` | 22 | 12 | 488, 839, 867–896, 931, 988–1018, 6049–6053, 6133, 6782, 6885–6893, 6933, 7058–7077, 7198 |
| `skinHeader` | 16 | 10 | 284, 4385, 4431–4458, 5931, 6342, 6398–6406, 6472–6497, 6876, 7025, 7722 |
| `nameContainer` | 27 | 9 | 700, 2243–2266, 2307, 2336, 2371–2418, 2455, 2486–2490, 5496–5549, 7613–7651 |
| `cardBox` | 13 | 9 | 428–439, 470–482, 508, 754, 909–913, 1022, 6776, 7058, 7424 |
| `emby-button` | 12 | 9 | 626–643, 670–688, 3175, 3310–3317, 3715, 3750, 3904, 4591, 5318 |
| `js` | 9 | 9 | 331, 1664, 1757, 2307, 2913, 3669, 5740, 6977, 7224 |
| `card-hoverable` | 23 | 8 | 516, 827, 887–981, 6053, 6800, 6933–6968, 7058, 7424 |
| `parentName` | 23 | 8 | 700, 2248–2266, 2307, 2336, 2371–2418, 5502–5549, 5622, 7613–7651 |
| `detailLogo` | 20 | 8 | 700, 2023–2049, 2084–2099, 2126–2135, 2236–2266, 2336, 2371–2418, 2486 |
| `listItem` | 19 | 8 | 302, 643, 2503, 4493–4519, 4550–4582, 4627, 4671, 7401–7418 |
| `detailPageWrapperContainer` | 17 | 8 | 700, 1560–1570, 2049, 2209, 2243–2266, 2336, 2371–2418, 2486 |
| `subtitle` | 16 | 8 | 2013–2023, 2135, 2248, 2307, 2427–2437, 2548, 5557–5590, 7613–7651 |
| `backdropCard` | 12 | 8 | 975–981, 1096, 2013–2023, 2152, 2236, 2490–2499, 2526, 2836 |
| `nowPlayingBar` | 8 | 8 | 318, 3099, 6185, 6839, 6927, 7011, 7037, 7383 |
| `loginPage` | 16 | 7 | 3848, 5935–5966, 6006, 6034–6053, 6829, 6872, 7187–7214 |
| `navMenuOption` | 12 | 6 | 643, 739–749, 4090, 4560–4582, 4677–4682, 7100–7111 |
| `paper-icon-button-light` | 11 | 6 | 588–643, 1678, 1748, 1846, 3476–3496, 5402 |
| `verticalSection` | 11 | 6 | 1752, 2738–2743, 4995, 6885, 6977, 7224 |
| `button-link` | 10 | 6 | 643, 670–688, 3049–3058, 3119–3129, 3175, 7575 |
| `person` | 8 | 6 | 2013–2034, 2236, 2490, 2535–2544, 3977, 7608 |
| `mainDrawer` | 7 | 6 | 3063, 4054, 4431, 6829–6839, 7087, 7126 |
| `scss` | 6 | 6 | 284, 782, 1048, 3585, 4096, 6977 |
| `detailImageContainer` | 20 | 5 | 2013–2034, 2140–2204, 2236, 2477–2499, 2526–2544 |
| `osdHeader` | 15 | 5 | 1721–1739, 6337–6406, 6472–6497, 6876, 7383 |
| `actionSheetMenuItem` | 10 | 5 | 643, 4493–4504, 4550, 4627–4671, 6857 |
| `sectionTabs` | 10 | 5 | 1815, 3827, 4458, 6378–6383, 6563–6594 |
| `cardImageIcon` | 8 | 5 | 420–424, 2490–2499, 2562, 3563, 6133 |
| `headerTop` | 8 | 5 | 4385, 4431, 6348–6373, 6464–6481, 6508–6512 |
| `sectionTitle` | 7 | 5 | 1752, 1825–1832, 4286, 5072–5080, 6001 |
| `emby-scroller-container` | 6 | 5 | 1752–1757, 1795, 2728, 6885, 6977 |
| `portraitCard` | 6 | 5 | 1096, 1180, 1937–1942, 2200, 2836 |
| `skinHeader-withBackground` | 5 | 5 | 1660, 4025, 5931, 6337, 6387 |
| `btnPlay` | 16 | 4 | 525–549, 588–643, 3779–3821, 3854–3882 |
| `cardOverlayContainer` | 12 | 4 | 949–981, 1026–1048, 1114, 7383–7401 |
| `itemName` | 11 | 4 | 700, 2307, 5502–5549, 5640–5657 |
| `backdropImage` | 10 | 4 | 2627–2655, 2682–2686, 6769, 6893–6901 |
| `emby-tab-button` | 10 | 4 | 643, 710–719, 3827, 6548–6589 |
| `upNextContainer` | 10 | 4 | 5164–5183, 5209–5235, 6829–6839, 6865 |
| `emby-scroller` | 9 | 4 | 1757, 1795–1801, 7130–7177, 7362–7378 |
| `backgroundContainer` | 8 | 4 | 2103, 2618, 2660–2678, 2710 |
| `detailRibbon` | 8 | 4 | 1617–1645, 1852, 1937–1949, 7608 |
| `listItemBodyText` | 7 | 4 | 4514–4533, 4573, 4648, 7418 |
| `skip-button` | 7 | 4 | 643, 3832, 5258–5275, 5302–5320 |
| `visualCardBox` | 7 | 4 | 428, 848–861, 887–892, 1022 |
| `button-submit` | 6 | 4 | 3848, 3936, 6034–6042, 7486–7501 |
| `cardText-secondary` | 6 | 4 | 302, 936, 3568–3572, 6955–6963 |
| `detailPagePrimaryContent` | 6 | 4 | 1632–1650, 2442, 4989, 7041 |
| `squareCard` | 6 | 4 | 871, 2490, 2526–2544, 6010–6014 |
| `semiTransparent` | 5 | 4 | 1660, 5931, 6366–6387, 6423 |
| `skinHeader-blurred` | 5 | 4 | 5931, 6366–6373, 7025, 7383 |
| `appfooter` | 4 | 4 | 2779, 6522, 6916, 7383 |
| `itemsContainer` | 4 | 4 | 754, 1784, 1819, 4995 |
| `raised` | 4 | 4 | 643, 729, 3715, 3750 |
| `x` | 4 | 4 | 2307, 4096, 5605, 6977 |
| `detailButton` | 13 | 3 | 588–643, 3760–3821, 3878–3882 |
| `itemSelectionPanel` | 9 | 3 | 900–904, 3508, 3536–3579 |
| `pageTitle` | 8 | 3 | 1696–1739, 6398, 6497 |
| `sectionTitleTextButton` | 8 | 3 | 5055–5063, 5090–5102, 5136–5146 |
| `homePage` | 7 | 3 | 4385, 4431–4458, 6611 |
| `playedIndicator` | 7 | 3 | 782–796, 3652, 7058–7082 |
| `check` | 6 | 3 | 3536, 3769, 4627–4671 |
| `detailSectionContent` | 6 | 3 | 3342, 4778–4788, 4868–4878 |
| `emby-checkbox` | 6 | 3 | 3513, 3550–3554, 3603–3615 |
| `actionSheetContent` | 5 | 3 | 4619–4623, 6829–6839, 6865 |
| `cardText-first` | 5 | 3 | 936, 3542–3568, 6114 |
| `dialog` | 5 | 3 | 3392–3402, 6829–6839, 6865 |
| `guideProgramName` | 5 | 3 | 643, 5681–5692, 5735–5740 |
| `noHomeButtonHeader` | 5 | 3 | 1678, 6398, 6548–6556 |
| `overflowBackdropCard` | 5 | 3 | 975–981, 3546, 6109–6114 |
| `secondary` | 5 | 3 | 302, 4523–4533, 4573 |
| `album` | 4 | 3 | 2236, 2495–2499, 2535 |
| `cardPadder` | 4 | 3 | 424, 1022, 3559–3563 |
| `cardText` | 4 | 3 | 936–946, 3568, 7203 |
| `detailPageContent` | 4 | 3 | 1774, 4709, 4982–4989 |
| `dialog-fullscreen` | 4 | 3 | 3402, 6829–6839, 6865 |
| `emby-scrollbuttons` | 4 | 3 | 1837–1842, 7224, 7760 |
| `folder` | 4 | 3 | 1937–1942, 3669, 3733 |
| `formDialogFooter` | 4 | 3 | 3460, 3943, 7435–7459 |
| `infoWrapper` | 4 | 3 | 2179–2184, 2442, 2470 |
| `listItemImage` | 4 | 3 | 2813–2818, 4487, 7418 |
| `musicParentName` | 4 | 3 | 2013, 2548, 5622–5631 |
| `programGuideSection` | 4 | 3 | 2503–2518, 4878, 4905 |
| `toast` | 4 | 3 | 5156, 6829–6839, 6865 |
| `cardFooter` | 3 | 3 | 3579, 6933, 6968 |
| `collectionItems` | 3 | 3 | 1784, 4878, 4914 |
| `defaultCardBackground` | 3 | 3 | 3690, 6129, 6228 |
| `detailPageSecondaryContainer` | 3 | 3 | 1627, 1654, 1774 |
| `emby-input` | 3 | 3 | 5416, 5445, 7501 |
| `formDialogFooterItem` | 3 | 3 | 3460, 3728, 3854 |
| `formDialogHeader` | 3 | 3 | 3943, 7383, 7435 |
| `iconOsd` | 3 | 3 | 5909, 7383, 7435 |
| `live_tv` | 3 | 3 | 2013, 2535, 3977 |
| `myPreferencesMenuPage` | 3 | 3 | 397, 4687, 5003 |
| `page` | 3 | 3 | 1018, 2710, 6885 |
| `playerStats` | 3 | 3 | 5909, 7435, 7471 |
| `sectionTitle-cards` | 3 | 3 | 1752, 5072, 5132 |
| `sectionTitleContainer` | 3 | 3 | 1784, 1842, 4914 |
| `tsx` | 3 | 3 | 1096, 4385, 4462 |
| `itemExternalLinks` | 13 | 2 | 3112–3190, 3342 |
| `checkboxOutline` | 10 | 2 | 3513–3554, 3585–3615 |
| `itemBackdrop` | 9 | 2 | 1979–2034, 2209 |
| `mdl-slider` | 9 | 2 | 2909, 2964–3022 |
| `listItemIcon` | 8 | 2 | 3973–3977, 4627–4687 |
| `sliderContainer` | 8 | 2 | 2913, 2941–3006 |
| `cardOverlayButton-br` | 7 | 2 | 1034, 1063–1107 |
| `detail-clamp-text` | 7 | 2 | 3278–3304, 3330–3334 |
| `divUsers` | 7 | 2 | 6010–6014, 7187–7214 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3550–3554, 3584–3603 |
| `countIndicator` | 6 | 2 | 773–803, 7435–7459 |
| `detailPagePrimaryContainer` | 6 | 2 | 1604–1650, 2442 |
| `detailsGroupItem` | 6 | 2 | 4740, 4808–4845 |
| `headerButton` | 6 | 2 | 563–643, 6490 |
| `headerLeft` | 6 | 2 | 1702–1739, 6698 |
| `selectionCommandsPanel` | 6 | 2 | 3470–3504, 7383 |
| `trackSelections` | 6 | 2 | 4713–4740, 4873–4878 |
| `withBackdrop` | 6 | 2 | 2618, 2660–2678 |
| `detailSection` | 5 | 2 | 4696–4705, 4858–4878 |
| `fullSyncIndicator` | 5 | 2 | 773–796, 7435–7459 |
| `mainDrawer-scrollContainer` | 5 | 2 | 3072, 7100–7117 |
| `mediaInfoItem` | 5 | 2 | 1856–1899, 6977 |
| `overview-expand` | 5 | 2 | 3310–3334, 4778 |
| `scrollX` | 5 | 2 | 1757, 1795–1815 |
| `videoIndicator` | 5 | 2 | 3658–3686, 7435 |
| `withSectionTabs` | 5 | 2 | 2669–2686, 6373 |
| `alphaPickerButton` | 4 | 2 | 643, 4929–4941 |
| `backgroundProgress` | 4 | 2 | 2824–2836, 2866 |
| `emby-select` | 4 | 2 | 5416–5428, 7501 |
| `emby-tab-button-active` | 4 | 2 | 3915, 6580–6594 |
| `mediaSourceIndicator` | 4 | 2 | 773–796, 7435 |
| `play_arrow` | 4 | 2 | 3695–3711, 3882 |
| `playbackProgress` | 4 | 2 | 2824–2836, 2871 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4514–4519, 6222–6228 |
| `programCell` | 4 | 2 | 5672, 5731–5740 |
| `section0` | 4 | 2 | 988–1018, 6885 |
| `visualLoginForm` | 4 | 2 | 6001–6018, 6059 |
| `cardOverlayButtonIcon` | 3 | 2 | 1034–1046, 1107 |
| `castCollapsible` | 3 | 2 | 839, 3554–3563 |
| `emby-scrollbuttons-button` | 3 | 2 | 1846, 7767–7774 |
| `emby-textarea` | 3 | 2 | 5407–5416, 5445 |
| `guestCastContent` | 3 | 2 | 839, 3554–3563 |
| `guide-channelHeaderCell` | 3 | 2 | 643, 5706–5722 |
| `guide-date-tab-button` | 3 | 2 | 643, 3915–3923 |
| `headerUserButton` | 3 | 2 | 563–576, 5007 |
| `manualLoginForm` | 3 | 2 | 6001–6018, 6059 |
| `overview` | 3 | 2 | 3330–3334, 4788 |
| `add` | 2 | 2 | 1757, 6977 |
| `alphaPicker-fixed-right` | 2 | 2 | 2710, 4941 |
| `backdropImageFadeIn` | 2 | 2 | 2763, 7475 |
| `book` | 2 | 2 | 2013, 2535 |
| `btnDeleteImage` | 2 | 2 | 3715, 3929 |
| `cardContent` | 2 | 2 | 839, 871 |
| `cardOverlayButton` | 2 | 2 | 1048, 1084 |
| `cardOverlayButton-hover` | 2 | 2 | 931, 1063 |
| `chevron_right` | 2 | 2 | 5102, 5146 |
| `classList` | 2 | 2 | 1757, 6977 |
| `collapseContent` | 2 | 2 | 3465, 3941 |
| `collectionItemsContainer` | 2 | 2 | 1784, 4918 |
| `content-primary` | 2 | 2 | 4982, 5038 |
| `editorsChoiceItemOverview` | 2 | 2 | 7697, 7778 |
| `endsAt` | 2 | 2 | 1877, 6977 |
| `fieldDescription` | 2 | 2 | 302, 7501 |
| `formDialogFooter-clear` | 2 | 2 | 3460, 3943 |
| `guide-programNameCaret` | 2 | 2 | 302, 5688 |
| `headroom` | 2 | 2 | 6361, 6398 |
| `indicator` | 2 | 2 | 803, 3647 |
| `mediaInfoOfficialRating` | 2 | 2 | 1877, 6977 |
| `navMenuOption-selected` | 2 | 2 | 4692, 7111 |
| `nowPlayingInfoContainer` | 2 | 2 | 3103, 6159 |
| `org` | 2 | 2 | 3139, 3169 |
| `paperList` | 2 | 2 | 848, 3954 |
| `playlist` | 2 | 2 | 4509, 6137 |
| `programSecondaryTitle` | 2 | 2 | 302, 5740 |
| `queue` | 2 | 2 | 2013, 2535 |
| `reactRoot` | 2 | 2 | 4385, 6704 |
| `readOnlyContent` | 2 | 2 | 3985, 6627 |
| `recordingFields` | 2 | 2 | 4732, 4873 |
| `runtime` | 2 | 2 | 6071, 6099 |
| `sectionTitleContainer-cards` | 2 | 2 | 5067, 5132 |
| `sidebarHeader` | 2 | 2 | 4077, 7117 |
| `tagline` | 2 | 2 | 2609, 4788 |
| `upNextDialog-title` | 2 | 2 | 5188, 5222 |
| `vertical-list` | 2 | 2 | 1819, 7603 |
| `vertical-wrap` | 2 | 2 | 769, 1784 |
| `videoOsdBottom` | 2 | 2 | 3095, 6328 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3095, 6328 |
| `userPreferencesPage` | 12 | 1 | 7486–7582 |
| `checkboxContainer` | 7 | 1 | 3542–3579 |
| `itemDetailsGroup` | 7 | 1 | 4792–4878 |
| `itemProgressBar` | 6 | 1 | 2813–2847 |
| `streaming-lookup-container` | 6 | 1 | 3197–3242 |
| `trackSelectionFieldContainer` | 6 | 1 | 4751–4774 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7734–7774 |
| `innerCardFooter` | 5 | 1 | 3355–3384 |
| `chapterCardImageContainer` | 4 | 1 | 3355–3384 |
| `emby-select-withcolor` | 4 | 1 | 5416–5463 |
| `endTimeText` | 4 | 1 | 6071–6099 |
| `mainDetailButtons` | 4 | 1 | 3878–3892 |
| `overview-controls` | 4 | 1 | 3330–3342 |
| `startTimeText` | 4 | 1 | 6071–6093 |
| `button-flat` | 3 | 1 | 3076–3086 |
| `cardIndicators` | 3 | 1 | 3632–3642 |
| `cardOverlayFab-primary` | 3 | 1 | 1026–1048 |
| `com` | 3 | 1 | 3145–3163 |
| `content` | 3 | 1 | 4814–4845 |
| `discover-card` | 3 | 1 | 7785–7808 |
| `fab` | 3 | 1 | 3737–3750 |
| `listChildrenCollapsible` | 3 | 1 | 4863–4878 |
| `mdl-slider-background-flex` | 3 | 1 | 2933–2946 |
| `mediaInfoCriticRating` | 3 | 1 | 1918–1927 |
| `nextUpSection` | 3 | 1 | 4858–4878 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 6123–6133 |
| `serverInfo` | 3 | 1 | 3958–3967 |
| `transcodingProgress` | 3 | 1 | 2824–2836 |
