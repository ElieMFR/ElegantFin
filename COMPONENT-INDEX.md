# Index des composants — ElegantFin Cinema Edition v1.5.9

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.5.9.css` — 8057 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 38 | 16 | 451–481, 512–547, 785, 898, 1559–1579, 2188–2221, 2248–2252, 2529–2547, 2583, 6964, 7000–7010, 7150, 7250–7269, 7347–7369, 7399–7406, 7570 |
| `cardScalable` | 29 | 14 | 451, 481, 535–547, 848–888, 914–958, 2547, 3628, 3740, 3818, 6028, 6978–7010, 7080, 7250, 7390–7406 |
| `cardImageContainer` | 21 | 13 | 462, 530, 866, 894–923, 958, 1016–1040, 6184–6188, 6268, 6970, 7080, 7120, 7250–7269, 7390 |
| `material-icons` | 17 | 13 | 393–412, 1779, 1877, 1930, 3585, 3745, 3818–3824, 3939, 4101, 4655, 5184, 5218–5228, 5845 |
| `itemDetailPage` | 20 | 12 | 1622, 1703, 1788, 1815, 2044–2084, 2119–2134, 2170–2174, 2284, 2596, 4782, 5077, 7824–7862 |
| `skinHeader` | 20 | 12 | 296, 1703, 4081–4097, 4467, 4513–4540, 6036–6040, 6477, 6533–6541, 6611–6636, 7064, 7217, 7895 |
| `js` | 13 | 12 | 330, 360, 1689–1703, 1788, 2355, 2962, 3389, 3719, 5845, 6842, 7169, 7416 |
| `emby-button` | 13 | 10 | 657–674, 701–719, 3223, 3357–3364, 3765, 3799, 3961, 4673, 5362, 5415 |
| `nameContainer` | 27 | 9 | 731, 2291–2314, 2355, 2384, 2419–2466, 2503, 2534–2538, 5601–5654, 7824–7862 |
| `parentName` | 23 | 8 | 731, 2296–2314, 2355, 2384, 2419–2466, 5607–5654, 5727, 7824–7862 |
| `detailLogo` | 20 | 8 | 731, 2073–2084, 2119–2134, 2161–2174, 2284–2314, 2384, 2419–2466, 2534 |
| `detailPageWrapperContainer` | 17 | 8 | 731, 1590–1600, 2084, 2257, 2291–2314, 2384, 2419–2466, 2534 |
| `subtitle` | 17 | 8 | 2044–2054, 2170–2174, 2296, 2355, 2475–2485, 2596, 5662–5695, 7824–7862 |
| `cardBox` | 13 | 8 | 451–481, 512–536, 785, 936–940, 1045, 6964, 7250, 7635 |
| `backdropCard` | 12 | 8 | 1003–1009, 1126, 2044–2054, 2200, 2284, 2538–2547, 2574, 2885 |
| `nowPlayingBar` | 8 | 8 | 330, 3147, 6320, 7027, 7114, 7203, 7229, 7575 |
| `card-hoverable` | 22 | 7 | 547, 914–1009, 6188, 6988, 7120–7159, 7250, 7635 |
| `listItem` | 18 | 7 | 314, 674, 2551, 4575–4601, 4632–4664, 4709, 7612–7629 |
| `loginPage` | 18 | 7 | 3905, 6040–6074, 6114–6133, 6169–6188, 7017, 7060, 7379–7406 |
| `paper-icon-button-light` | 12 | 7 | 619–674, 1703, 1779, 1877, 3525–3545, 5362, 5499 |
| `navMenuOption` | 12 | 6 | 674, 770–780, 4150, 4642–4664, 4763–4768, 7292–7303 |
| `emby-tab-button` | 11 | 6 | 674, 741–750, 3880, 6687–6698, 6726–6743, 7907 |
| `verticalSection` | 11 | 6 | 1783, 2787–2792, 5077, 7073, 7169, 7416 |
| `button-link` | 10 | 6 | 674, 701–719, 3098–3107, 3167–3177, 3223, 7786 |
| `headerTop` | 9 | 6 | 2174, 4467, 4513, 6483–6508, 6603–6620, 6647–6651 |
| `person` | 8 | 6 | 2044–2069, 2284, 2538, 2583–2592, 4033, 7819 |
| `mainDrawer` | 7 | 6 | 3112, 4115, 4513, 7017–7027, 7279, 7318 |
| `scss` | 6 | 6 | 296, 813, 1071, 3634, 4156, 7169 |
| `detailImageContainer` | 20 | 5 | 2044–2069, 2188–2252, 2284, 2525–2547, 2574–2592 |
| `btnPlay` | 19 | 5 | 556–580, 619–674, 3828–3879, 3911–3939, 5362 |
| `osdHeader` | 15 | 5 | 1752–1770, 6472–6541, 6611–6636, 7064, 7575 |
| `cardOverlayContainer` | 12 | 5 | 977–1009, 1049–1071, 1144, 7575, 7612 |
| `sectionTabs` | 11 | 5 | 1846, 3880, 4540, 6513–6518, 6704–6748 |
| `cardImageIcon` | 8 | 5 | 443–447, 2538–2547, 2610, 3612, 6268 |
| `sectionTitle` | 7 | 5 | 1783, 1856–1863, 4368, 5154–5162, 6109 |
| `semiTransparent` | 7 | 5 | 1685, 4081–4097, 6036, 6501–6522, 6558 |
| `emby-scroller-container` | 6 | 5 | 1783–1788, 1826, 2775, 7073, 7169 |
| `portraitCard` | 6 | 5 | 1126, 1210, 1968–1973, 2248, 2885 |
| `appfooter` | 5 | 5 | 330, 2828, 6661, 7103, 7575 |
| `skinHeader-withBackground` | 5 | 5 | 1685, 4081, 6036, 6472, 6522 |
| `detailButton` | 15 | 4 | 619–674, 3809–3879, 3935–3939, 5362 |
| `itemName` | 11 | 4 | 731, 2355, 5607–5654, 5745–5762 |
| `backdropImage` | 10 | 4 | 2674–2702, 2729–2733, 6957, 7080–7088 |
| `upNextContainer` | 10 | 4 | 5245–5263, 5289–5315, 7017–7027, 7053 |
| `emby-scroller` | 9 | 4 | 1788, 1826–1832, 7322–7369, 7554–7570 |
| `sectionTitleTextButton` | 9 | 4 | 473, 5137–5145, 5172–5184, 5218–5228 |
| `skip-button` | 9 | 4 | 674, 3889, 5338–5372, 5399–5417 |
| `backgroundContainer` | 8 | 4 | 2138, 2666, 2707–2725, 2757 |
| `detailRibbon` | 8 | 4 | 1647–1671, 1883, 1968–1980, 7819 |
| `visualCardBox` | 7 | 4 | 451, 875–888, 914–919, 1045 |
| `actionSheetMenuItem` | 6 | 4 | 674, 4575–4586, 4632, 7045 |
| `button-submit` | 6 | 4 | 3905, 3992, 6169–6177, 7697–7712 |
| `cardText-secondary` | 6 | 4 | 314, 963, 3617–3621, 7142–7150 |
| `skinHeader-blurred` | 6 | 4 | 6036, 6501–6508, 7217, 7575–7594 |
| `squareCard` | 6 | 4 | 898, 2538, 2574–2592, 6138–6142 |
| `itemsContainer` | 4 | 4 | 785, 1815, 1850, 5077 |
| `raised` | 4 | 4 | 674, 760, 3765, 3799 |
| `tsx` | 4 | 4 | 1126, 1703, 4467, 4544 |
| `x` | 4 | 4 | 2355, 4156, 5710, 7169 |
| `itemSelectionPanel` | 9 | 3 | 927–931, 3557, 3585–3628 |
| `pageTitle` | 8 | 3 | 1727–1770, 6533, 6636 |
| `headerButton` | 7 | 3 | 594–674, 5362, 6629 |
| `homePage` | 7 | 3 | 4467, 4513–4540, 6765 |
| `playedIndicator` | 7 | 3 | 813–827, 3701, 7250–7274 |
| `detailSectionContent` | 6 | 3 | 3389, 4864–4874, 4957–4967 |
| `emby-checkbox` | 6 | 3 | 3562, 3599–3603, 3652–3664 |
| `listItemBodyText` | 6 | 3 | 4596–4615, 4655, 7629 |
| `actionSheetContent` | 5 | 3 | 4701–4705, 7017–7027, 7053 |
| `cardText-first` | 5 | 3 | 963, 3591–3617, 6249 |
| `detailPagePrimaryContent` | 5 | 3 | 1660–1676, 2490, 7233 |
| `dialog` | 5 | 3 | 3441–3451, 7017–7027, 7053 |
| `guideProgramName` | 5 | 3 | 674, 5786–5797, 5840–5845 |
| `noHomeButtonHeader` | 5 | 3 | 1703, 6533, 6687–6698 |
| `overflowBackdropCard` | 5 | 3 | 1003–1009, 3595, 6244–6249 |
| `secondary` | 5 | 3 | 314, 4605–4615, 4655 |
| `album` | 4 | 3 | 2284, 2543–2547, 2583 |
| `cardPadder` | 4 | 3 | 447, 1045, 3608–3612 |
| `cardText` | 4 | 3 | 963–973, 3617, 7395 |
| `dialog-fullscreen` | 4 | 3 | 3451, 7017–7027, 7053 |
| `emby-input` | 4 | 3 | 5513, 5542–5560, 7712 |
| `emby-scrollbuttons` | 4 | 3 | 1868–1873, 7416, 7941 |
| `folder` | 4 | 3 | 1968–1973, 3719, 3782 |
| `formDialogFooter` | 4 | 3 | 3509, 3999, 7646–7670 |
| `infoWrapper` | 4 | 3 | 2227–2232, 2490, 2518 |
| `listItemIcon` | 4 | 3 | 4029–4033, 4709, 4773 |
| `listItemImage` | 4 | 3 | 2862–2867, 4569, 7629 |
| `musicParentName` | 4 | 3 | 2044, 2596, 5727–5736 |
| `programGuideSection` | 4 | 3 | 2551–2566, 4967, 4994 |
| `toast` | 4 | 3 | 5238, 7017–7027, 7053 |
| `cardFooter` | 3 | 3 | 3628, 7120, 7159 |
| `check` | 3 | 3 | 3585, 3818, 4709 |
| `collectionItems` | 3 | 3 | 1815, 4967, 5003 |
| `defaultCardBackground` | 3 | 3 | 3740, 6264, 6363 |
| `formDialogFooterItem` | 3 | 3 | 3509, 3777, 3911 |
| `formDialogHeader` | 3 | 3 | 3999, 7575, 7646 |
| `iconOsd` | 3 | 3 | 6014, 7575, 7646 |
| `live_tv` | 3 | 3 | 2044, 2583, 4033 |
| `myPreferencesMenuPage` | 3 | 3 | 421, 4773, 5085 |
| `playerStats` | 3 | 3 | 6014, 7646, 7682 |
| `readOnlyContent` | 3 | 3 | 4041, 6127, 6781 |
| `sectionTitle-cards` | 3 | 3 | 1783, 5154, 5214 |
| `sectionTitleContainer` | 3 | 3 | 1815, 1873, 5003 |
| `itemExternalLinks` | 13 | 2 | 3160–3238, 3389 |
| `checkboxOutline` | 10 | 2 | 3562–3603, 3634–3664 |
| `itemBackdrop` | 9 | 2 | 2010–2069, 2257 |
| `mdl-slider` | 9 | 2 | 2958, 3013–3071 |
| `cardOverlayButton-br` | 8 | 2 | 1057, 1086–1137 |
| `sliderContainer` | 8 | 2 | 2962, 2990–3055 |
| `detail-clamp-text` | 7 | 2 | 3325–3351, 3377–3381 |
| `divUsers` | 7 | 2 | 6138–6142, 7379–7406 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3599–3603, 3633–3652 |
| `countIndicator` | 6 | 2 | 804–834, 7646–7670 |
| `detailPagePrimaryContainer` | 6 | 2 | 1634–1676, 2490 |
| `detailsGroupItem` | 6 | 2 | 4826, 4897–4934 |
| `headerLeft` | 6 | 2 | 1733–1770, 6886 |
| `selectionCommandsPanel` | 6 | 2 | 3519–3553, 7575 |
| `trackSelections` | 6 | 2 | 4795–4826, 4962–4967 |
| `withBackdrop` | 6 | 2 | 2666, 2707–2725 |
| `detailSection` | 5 | 2 | 4782–4791, 4947–4967 |
| `fullSyncIndicator` | 5 | 2 | 804–827, 7646–7670 |
| `mainDrawer-scrollContainer` | 5 | 2 | 3120, 7292–7309 |
| `manualLoginForm` | 5 | 2 | 6109–6153, 6194 |
| `mediaInfoItem` | 5 | 2 | 1887–1930, 7169 |
| `overview-expand` | 5 | 2 | 3357–3381, 4864 |
| `scrollX` | 5 | 2 | 1788, 1826–1846 |
| `videoIndicator` | 5 | 2 | 3708–3736, 7646 |
| `visualLoginForm` | 5 | 2 | 6109–6153, 6194 |
| `withSectionTabs` | 5 | 2 | 2716–2733, 6508 |
| `alphaPickerButton` | 4 | 2 | 674, 5018–5030 |
| `backgroundProgress` | 4 | 2 | 2873–2885, 2915 |
| `emby-select` | 4 | 2 | 5513–5525, 7712 |
| `emby-tab-button-active` | 4 | 2 | 3972, 6734–6748 |
| `emby-textarea` | 4 | 2 | 5504–5513, 5542–5560 |
| `mediaSourceIndicator` | 4 | 2 | 804–827, 7646 |
| `play_arrow` | 4 | 2 | 3745–3761, 3939 |
| `playbackProgress` | 4 | 2 | 2873–2885, 2920 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4596–4601, 6357–6363 |
| `programCell` | 4 | 2 | 5777, 5836–5845 |
| `cardOverlayButtonIcon` | 3 | 2 | 1057–1069, 1137 |
| `castCollapsible` | 3 | 2 | 866, 3603–3612 |
| `detailPageSecondaryContainer` | 3 | 2 | 1655–1680, 1805 |
| `emby-scrollbuttons-button` | 3 | 2 | 1877, 7948–7955 |
| `guestCastContent` | 3 | 2 | 866, 3603–3612 |
| `guide-channelHeaderCell` | 3 | 2 | 674, 5811–5827 |
| `guide-date-tab-button` | 3 | 2 | 674, 3972–3980 |
| `headerUserButton` | 3 | 2 | 594–607, 5089 |
| `noHeaderRight` | 3 | 2 | 1703, 6036–6040 |
| `overview` | 3 | 2 | 3377–3381, 4874 |
| `add` | 2 | 2 | 1788, 7169 |
| `alphaPicker-fixed-right` | 2 | 2 | 2757, 5030 |
| `backdropImageFadeIn` | 2 | 2 | 2812, 7686 |
| `book` | 2 | 2 | 2044, 2583 |
| `btnDeleteImage` | 2 | 2 | 3765, 3986 |
| `cardContent` | 2 | 2 | 866, 898 |
| `cardOverlayButton` | 2 | 2 | 1071, 1114 |
| `cardOverlayButton-hover` | 2 | 2 | 958, 1086 |
| `chevron_right` | 2 | 2 | 5184, 5228 |
| `classList` | 2 | 2 | 1788, 7169 |
| `collapseContent` | 2 | 2 | 3514, 3997 |
| `collectionItemsContainer` | 2 | 2 | 1815, 5007 |
| `content-primary` | 2 | 2 | 5071, 5120 |
| `editorsChoiceContainer` | 2 | 2 | 6842, 7866 |
| `editorsChoiceItemBanner` | 2 | 2 | 6842, 7594 |
| `editorsChoiceItemOverview` | 2 | 2 | 7866, 7959 |
| `endsAt` | 2 | 2 | 1908, 7169 |
| `f5f5f5` | 2 | 2 | 5338, 5377 |
| `fieldDescription` | 2 | 2 | 314, 7712 |
| `formDialogFooter-clear` | 2 | 2 | 3509, 3999 |
| `guide-programNameCaret` | 2 | 2 | 314, 5793 |
| `headroom` | 2 | 2 | 6496, 6533 |
| `indicator` | 2 | 2 | 834, 3696 |
| `mc-row` | 2 | 2 | 462, 7486 |
| `mediaInfoOfficialRating` | 2 | 2 | 1908, 7169 |
| `navMenuOption-selected` | 2 | 2 | 4778, 7303 |
| `nowPlayingInfoContainer` | 2 | 2 | 3151, 6294 |
| `org` | 2 | 2 | 3187, 3217 |
| `page` | 2 | 2 | 2757, 7073 |
| `paperList` | 2 | 2 | 875, 4010 |
| `playlist` | 2 | 2 | 4591, 6272 |
| `programSecondaryTitle` | 2 | 2 | 314, 5845 |
| `queue` | 2 | 2 | 2044, 2583 |
| `reactRoot` | 2 | 2 | 4467, 6892 |
| `recordingFields` | 2 | 2 | 4818, 4962 |
| `runtime` | 2 | 2 | 6206, 6234 |
| `sectionTitleContainer-cards` | 2 | 2 | 5149, 5214 |
| `sidebarHeader` | 2 | 2 | 4137, 7309 |
| `splide` | 2 | 2 | 6842, 7915 |
| `tagline` | 2 | 2 | 2657, 4874 |
| `upNextDialog-title` | 2 | 2 | 5268, 5302 |
| `vertical-list` | 2 | 2 | 1850, 7814 |
| `vertical-wrap` | 2 | 2 | 800, 1815 |
| `videoOsdBottom` | 2 | 2 | 3143, 6463 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3143, 6463 |
| `userPreferencesPage` | 12 | 1 | 7697–7793 |
| `checkboxContainer` | 7 | 1 | 3591–3628 |
| `itemDetailsGroup` | 7 | 1 | 4881–4967 |
| `itemProgressBar` | 6 | 1 | 2862–2896 |
| `streaming-lookup-container` | 6 | 1 | 3245–3290 |
| `trackSelectionFieldContainer` | 6 | 1 | 4837–4860 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7915–7955 |
| `emby-select-withcolor` | 5 | 1 | 5513–5568 |
| `innerCardFooter` | 5 | 1 | 3404–3433 |
| `chapterCardImageContainer` | 4 | 1 | 3404–3433 |
| `endTimeText` | 4 | 1 | 6206–6234 |
| `mainDetailButtons` | 4 | 1 | 3935–3949 |
| `overview-controls` | 4 | 1 | 3377–3389 |
| `startTimeText` | 4 | 1 | 6206–6228 |
| `button-flat` | 3 | 1 | 3124–3134 |
| `cardIndicators` | 3 | 1 | 3681–3691 |
| `cardOverlayFab-primary` | 3 | 1 | 1049–1071 |
| `com` | 3 | 1 | 3193–3211 |
| `content` | 3 | 1 | 4903–4934 |
| `fab` | 3 | 1 | 3786–3799 |
| `listChildrenCollapsible` | 3 | 1 | 4952–4967 |
| `mdl-slider-background-flex` | 3 | 1 | 2982–2995 |
| `mediaInfoCriticRating` | 3 | 1 | 1949–1958 |
| `nextUpSection` | 3 | 1 | 4947–4967 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 6258–6268 |
| `serverInfo` | 3 | 1 | 4014–4023 |
| `transcodingProgress` | 3 | 1 | 2873–2885 |
