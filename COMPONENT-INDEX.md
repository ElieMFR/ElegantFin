# Index des composants — ElegantFin Cinema Edition v1.5.9

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.5.9.css` — 8082 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 38 | 16 | 451–481, 512–547, 785, 898, 1559–1579, 2188–2221, 2248–2252, 2529–2547, 2583, 6984, 7020–7030, 7170, 7270–7289, 7367–7389, 7419–7426, 7596 |
| `cardScalable` | 29 | 14 | 451, 481, 535–547, 848–888, 914–958, 2547, 3641, 3753, 3830, 6050, 6998–7030, 7100, 7270, 7410–7426 |
| `cardImageContainer` | 21 | 13 | 462, 530, 866, 894–923, 958, 1016–1040, 6204–6208, 6288, 6990, 7100, 7140, 7270–7289, 7410 |
| `material-icons` | 17 | 13 | 393–412, 1779, 1877, 1930, 3598, 3758, 3830–3836, 3951, 4112, 4674, 5203, 5237–5245, 5871 |
| `itemDetailPage` | 20 | 12 | 1622, 1703, 1788, 1815, 2044–2084, 2119–2134, 2170–2174, 2284, 2596, 4801, 5096, 7849–7887 |
| `skinHeader` | 20 | 12 | 296, 1703, 4092–4108, 4486, 4532–4559, 6058–6062, 6497, 6553–6561, 6631–6656, 7084, 7237, 7920 |
| `js` | 13 | 12 | 330, 360, 1689–1703, 1788, 2355, 2958, 3402, 3732, 5871, 6862, 7189, 7436 |
| `emby-button` | 13 | 10 | 657–674, 701–719, 3236, 3370–3377, 3778, 3811, 3973, 4692, 5379, 5432 |
| `nameContainer` | 27 | 9 | 731, 2291–2314, 2355, 2384, 2419–2466, 2503, 2534–2538, 5627–5680, 7849–7887 |
| `parentName` | 23 | 8 | 731, 2296–2314, 2355, 2384, 2419–2466, 5633–5680, 5753, 7849–7887 |
| `detailLogo` | 20 | 8 | 731, 2073–2084, 2119–2134, 2161–2174, 2284–2314, 2384, 2419–2466, 2534 |
| `detailPageWrapperContainer` | 17 | 8 | 731, 1590–1600, 2084, 2257, 2291–2314, 2384, 2419–2466, 2534 |
| `subtitle` | 17 | 8 | 2044–2054, 2170–2174, 2296, 2355, 2475–2485, 2596, 5688–5721, 7849–7887 |
| `cardBox` | 13 | 8 | 451–481, 512–536, 785, 936–940, 1045, 6984, 7270, 7661 |
| `backdropCard` | 12 | 8 | 1003–1009, 1126, 2044–2054, 2200, 2284, 2538–2547, 2574, 2891 |
| `nowPlayingBar` | 8 | 8 | 330, 3160, 6340, 7047, 7134, 7223, 7249, 7601 |
| `card-hoverable` | 22 | 7 | 547, 914–1009, 6208, 7008, 7140–7179, 7270, 7661 |
| `listItem` | 18 | 7 | 314, 674, 2551, 4594–4620, 4651–4683, 4728, 7638–7655 |
| `loginPage` | 18 | 7 | 3917, 6062–6096, 6134–6153, 6189–6208, 7037, 7080, 7399–7426 |
| `paper-icon-button-light` | 12 | 7 | 619–674, 1703, 1779, 1877, 3538–3558, 5379, 5516 |
| `navMenuOption` | 12 | 6 | 674, 770–780, 4161, 4661–4683, 4782–4787, 7312–7323 |
| `emby-tab-button` | 11 | 6 | 674, 741–750, 3892, 6707–6718, 6746–6763, 7932 |
| `verticalSection` | 11 | 6 | 1783, 2783–2788, 5096, 7093, 7189, 7436 |
| `button-link` | 10 | 6 | 674, 701–719, 3111–3120, 3180–3190, 3236, 7812 |
| `headerTop` | 9 | 6 | 2174, 4486, 4532, 6503–6528, 6623–6640, 6667–6671 |
| `person` | 8 | 6 | 2044–2069, 2284, 2538, 2583–2592, 4044, 7844 |
| `mainDrawer` | 7 | 6 | 3125, 4126, 4532, 7037–7047, 7299, 7338 |
| `scss` | 6 | 6 | 296, 813, 1071, 3647, 4167, 7189 |
| `detailImageContainer` | 20 | 5 | 2044–2069, 2188–2252, 2284, 2525–2547, 2574–2592 |
| `btnPlay` | 19 | 5 | 556–580, 619–674, 3840–3891, 3923–3951, 5379 |
| `osdHeader` | 15 | 5 | 1752–1770, 6492–6561, 6631–6656, 7084, 7601 |
| `cardOverlayContainer` | 12 | 5 | 977–1009, 1049–1071, 1144, 7601, 7638 |
| `sectionTabs` | 11 | 5 | 1846, 3892, 4559, 6533–6538, 6724–6768 |
| `cardImageIcon` | 8 | 5 | 443–447, 2538–2547, 2610, 3625, 6288 |
| `sectionTitle` | 7 | 5 | 1783, 1856–1863, 4379, 5173–5181, 6129 |
| `semiTransparent` | 7 | 5 | 1685, 4092–4108, 6058, 6521–6542, 6578 |
| `emby-scroller-container` | 6 | 5 | 1783–1788, 1826, 2771, 7093, 7189 |
| `portraitCard` | 6 | 5 | 1126, 1210, 1968–1973, 2248, 2891 |
| `appfooter` | 5 | 5 | 330, 2834, 6681, 7123, 7601 |
| `skinHeader-withBackground` | 5 | 5 | 1685, 4092, 6058, 6492, 6542 |
| `detailButton` | 15 | 4 | 619–674, 3821–3891, 3947–3951, 5379 |
| `itemName` | 11 | 4 | 731, 2355, 5633–5680, 5771–5788 |
| `backdropImage` | 10 | 4 | 2670–2698, 2725–2729, 6977, 7100–7108 |
| `upNextContainer` | 10 | 4 | 5262–5280, 5306–5332, 7037–7047, 7073 |
| `emby-scroller` | 9 | 4 | 1788, 1826–1832, 7342–7389, 7580–7596 |
| `sectionTitleTextButton` | 9 | 4 | 473, 5156–5164, 5191–5203, 5237–5245 |
| `skip-button` | 9 | 4 | 674, 3901, 5355–5389, 5416–5434 |
| `backgroundContainer` | 8 | 4 | 2138, 2662, 2703–2721, 2753 |
| `detailRibbon` | 8 | 4 | 1647–1671, 1883, 1968–1980, 7844 |
| `visualCardBox` | 7 | 4 | 451, 875–888, 914–919, 1045 |
| `actionSheetMenuItem` | 6 | 4 | 674, 4594–4605, 4651, 7065 |
| `button-submit` | 6 | 4 | 3917, 4003, 6189–6197, 7723–7738 |
| `cardText-secondary` | 6 | 4 | 314, 963, 3630–3634, 7162–7170 |
| `skinHeader-blurred` | 6 | 4 | 6058, 6521–6528, 7237, 7601–7620 |
| `squareCard` | 6 | 4 | 898, 2538, 2574–2592, 6158–6162 |
| `itemsContainer` | 4 | 4 | 785, 1815, 1850, 5096 |
| `raised` | 4 | 4 | 674, 760, 3778, 3811 |
| `tsx` | 4 | 4 | 1126, 1703, 4486, 4563 |
| `x` | 4 | 4 | 2355, 4167, 5736, 7189 |
| `itemSelectionPanel` | 9 | 3 | 927–931, 3570, 3598–3641 |
| `pageTitle` | 8 | 3 | 1727–1770, 6553, 6656 |
| `sliderContainer` | 8 | 3 | 2958, 2986–3024, 3061–3068 |
| `headerButton` | 7 | 3 | 594–674, 5379, 6649 |
| `homePage` | 7 | 3 | 4486, 4532–4559, 6785 |
| `playedIndicator` | 7 | 3 | 813–827, 3714, 7270–7294 |
| `detailSectionContent` | 6 | 3 | 3402, 4883–4893, 4976–4986 |
| `emby-checkbox` | 6 | 3 | 3575, 3612–3616, 3665–3677 |
| `listItemBodyText` | 6 | 3 | 4615–4634, 4674, 7655 |
| `actionSheetContent` | 5 | 3 | 4720–4724, 7037–7047, 7073 |
| `cardText-first` | 5 | 3 | 963, 3604–3630, 6269 |
| `detailPagePrimaryContent` | 5 | 3 | 1660–1676, 2490, 7253 |
| `dialog` | 5 | 3 | 3454–3464, 7037–7047, 7073 |
| `emby-input` | 5 | 3 | 5530–5540, 5568–5586, 7738 |
| `guideProgramName` | 5 | 3 | 674, 5812–5823, 5866–5871 |
| `noHomeButtonHeader` | 5 | 3 | 1703, 6553, 6707–6718 |
| `overflowBackdropCard` | 5 | 3 | 1003–1009, 3608, 6264–6269 |
| `secondary` | 5 | 3 | 314, 4624–4634, 4674 |
| `album` | 4 | 3 | 2284, 2543–2547, 2583 |
| `cardPadder` | 4 | 3 | 447, 1045, 3621–3625 |
| `cardText` | 4 | 3 | 963–973, 3630, 7415 |
| `dialog-fullscreen` | 4 | 3 | 3464, 7037–7047, 7073 |
| `emby-scrollbuttons` | 4 | 3 | 1868–1873, 7436, 7966 |
| `folder` | 4 | 3 | 1968–1973, 3732, 3794 |
| `formDialogFooter` | 4 | 3 | 3522, 4010, 7672–7696 |
| `infoWrapper` | 4 | 3 | 2227–2232, 2490, 2518 |
| `listItemIcon` | 4 | 3 | 4040–4044, 4728, 4792 |
| `listItemImage` | 4 | 3 | 2868–2873, 4588, 7655 |
| `musicParentName` | 4 | 3 | 2044, 2596, 5753–5762 |
| `programGuideSection` | 4 | 3 | 2551–2566, 4986, 5013 |
| `toast` | 4 | 3 | 5255, 7037–7047, 7073 |
| `cardFooter` | 3 | 3 | 3641, 7140, 7179 |
| `check` | 3 | 3 | 3598, 3830, 4728 |
| `collectionItems` | 3 | 3 | 1815, 4986, 5022 |
| `defaultCardBackground` | 3 | 3 | 3753, 6284, 6383 |
| `formDialogFooterItem` | 3 | 3 | 3522, 3789, 3923 |
| `formDialogHeader` | 3 | 3 | 4010, 7601, 7672 |
| `iconOsd` | 3 | 3 | 6036, 7601, 7672 |
| `live_tv` | 3 | 3 | 2044, 2583, 4044 |
| `myPreferencesMenuPage` | 3 | 3 | 421, 4792, 5104 |
| `playerStats` | 3 | 3 | 6036, 7672, 7708 |
| `readOnlyContent` | 3 | 3 | 4052, 6147, 6801 |
| `sectionTitle-cards` | 3 | 3 | 1783, 5173, 5233 |
| `sectionTitleContainer` | 3 | 3 | 1815, 1873, 5022 |
| `itemExternalLinks` | 13 | 2 | 3173–3251, 3402 |
| `mdl-slider` | 11 | 2 | 2954, 3009–3084 |
| `checkboxOutline` | 10 | 2 | 3575–3616, 3647–3677 |
| `itemBackdrop` | 9 | 2 | 2010–2069, 2257 |
| `cardOverlayButton-br` | 8 | 2 | 1057, 1086–1137 |
| `detail-clamp-text` | 7 | 2 | 3338–3364, 3390–3394 |
| `divUsers` | 7 | 2 | 6158–6162, 7399–7426 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3612–3616, 3646–3665 |
| `countIndicator` | 6 | 2 | 804–834, 7672–7696 |
| `detailPagePrimaryContainer` | 6 | 2 | 1634–1676, 2490 |
| `detailsGroupItem` | 6 | 2 | 4845, 4916–4953 |
| `headerLeft` | 6 | 2 | 1733–1770, 6906 |
| `selectionCommandsPanel` | 6 | 2 | 3532–3566, 7601 |
| `trackSelections` | 6 | 2 | 4814–4845, 4981–4986 |
| `withBackdrop` | 6 | 2 | 2662, 2703–2721 |
| `detailSection` | 5 | 2 | 4801–4810, 4966–4986 |
| `emby-textarea` | 5 | 2 | 5521–5540, 5568–5586 |
| `fullSyncIndicator` | 5 | 2 | 804–827, 7672–7696 |
| `mainDrawer-scrollContainer` | 5 | 2 | 3133, 7312–7329 |
| `manualLoginForm` | 5 | 2 | 6129–6173, 6214 |
| `mediaInfoItem` | 5 | 2 | 1887–1930, 7189 |
| `overview-expand` | 5 | 2 | 3370–3394, 4883 |
| `scrollX` | 5 | 2 | 1788, 1826–1846 |
| `videoIndicator` | 5 | 2 | 3721–3749, 7672 |
| `visualLoginForm` | 5 | 2 | 6129–6173, 6214 |
| `withSectionTabs` | 5 | 2 | 2712–2729, 6528 |
| `alphaPickerButton` | 4 | 2 | 674, 5037–5049 |
| `emby-select` | 4 | 2 | 5530–5551, 7738 |
| `emby-tab-button-active` | 4 | 2 | 3984, 6754–6768 |
| `mediaSourceIndicator` | 4 | 2 | 804–827, 7672 |
| `play_arrow` | 4 | 2 | 3758–3774, 3951 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4615–4620, 6377–6383 |
| `programCell` | 4 | 2 | 5803, 5862–5871 |
| `cardOverlayButtonIcon` | 3 | 2 | 1057–1069, 1137 |
| `castCollapsible` | 3 | 2 | 866, 3616–3625 |
| `detailPageSecondaryContainer` | 3 | 2 | 1655–1680, 1805 |
| `emby-scrollbuttons-button` | 3 | 2 | 1877, 7973–7980 |
| `guestCastContent` | 3 | 2 | 866, 3616–3625 |
| `guide-channelHeaderCell` | 3 | 2 | 674, 5837–5853 |
| `guide-date-tab-button` | 3 | 2 | 674, 3984–3992 |
| `headerUserButton` | 3 | 2 | 594–607, 5108 |
| `noHeaderRight` | 3 | 2 | 1703, 6058–6062 |
| `overview` | 3 | 2 | 3390–3394, 4893 |
| `add` | 2 | 2 | 1788, 7189 |
| `alphaPicker-fixed-right` | 2 | 2 | 2753, 5049 |
| `backdropImageFadeIn` | 2 | 2 | 2818, 7712 |
| `book` | 2 | 2 | 2044, 2583 |
| `btnDeleteImage` | 2 | 2 | 3778, 3998 |
| `cardContent` | 2 | 2 | 866, 898 |
| `cardOverlayButton` | 2 | 2 | 1071, 1114 |
| `cardOverlayButton-hover` | 2 | 2 | 958, 1086 |
| `chevron_right` | 2 | 2 | 5203, 5245 |
| `classList` | 2 | 2 | 1788, 7189 |
| `collapseContent` | 2 | 2 | 3527, 4008 |
| `collectionItemsContainer` | 2 | 2 | 1815, 5026 |
| `content-primary` | 2 | 2 | 5090, 5139 |
| `editorsChoiceContainer` | 2 | 2 | 6862, 7891 |
| `editorsChoiceItemBanner` | 2 | 2 | 6862, 7620 |
| `editorsChoiceItemOverview` | 2 | 2 | 7891, 7984 |
| `endsAt` | 2 | 2 | 1908, 7189 |
| `f5f5f5` | 2 | 2 | 5355, 5394 |
| `fieldDescription` | 2 | 2 | 314, 7738 |
| `formDialogFooter-clear` | 2 | 2 | 3522, 4010 |
| `guide-programNameCaret` | 2 | 2 | 314, 5819 |
| `headroom` | 2 | 2 | 6516, 6553 |
| `indicator` | 2 | 2 | 834, 3709 |
| `mc-row` | 2 | 2 | 462, 7512 |
| `mediaInfoOfficialRating` | 2 | 2 | 1908, 7189 |
| `navMenuOption-selected` | 2 | 2 | 4797, 7323 |
| `nowPlayingInfoContainer` | 2 | 2 | 3164, 6314 |
| `org` | 2 | 2 | 3200, 3230 |
| `page` | 2 | 2 | 2753, 7093 |
| `paperList` | 2 | 2 | 875, 4021 |
| `playlist` | 2 | 2 | 4610, 6292 |
| `programSecondaryTitle` | 2 | 2 | 314, 5871 |
| `queue` | 2 | 2 | 2044, 2583 |
| `reactRoot` | 2 | 2 | 4486, 6912 |
| `recordingFields` | 2 | 2 | 4837, 4981 |
| `runtime` | 2 | 2 | 6226, 6254 |
| `sectionTitleContainer-cards` | 2 | 2 | 5168, 5233 |
| `sidebarHeader` | 2 | 2 | 4148, 7329 |
| `splide` | 2 | 2 | 6862, 7940 |
| `tagline` | 2 | 2 | 2653, 4893 |
| `upNextDialog-title` | 2 | 2 | 5285, 5319 |
| `vertical-list` | 2 | 2 | 1850, 7839 |
| `vertical-wrap` | 2 | 2 | 800, 1815 |
| `videoOsdBottom` | 2 | 2 | 3156, 6483 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3156, 6483 |
| `userPreferencesPage` | 12 | 1 | 7723–7819 |
| `checkboxContainer` | 7 | 1 | 3604–3641 |
| `itemDetailsGroup` | 7 | 1 | 4900–4986 |
| `itemProgressBar` | 6 | 1 | 2868–2902 |
| `streaming-lookup-container` | 6 | 1 | 3258–3303 |
| `trackSelectionFieldContainer` | 6 | 1 | 4856–4879 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7940–7980 |
| `emby-select-withcolor` | 5 | 1 | 5530–5594 |
| `innerCardFooter` | 5 | 1 | 3417–3446 |
| `chapterCardImageContainer` | 4 | 1 | 3417–3446 |
| `endTimeText` | 4 | 1 | 6226–6254 |
| `mainDetailButtons` | 4 | 1 | 3947–3961 |
| `overview-controls` | 4 | 1 | 3390–3402 |
| `startTimeText` | 4 | 1 | 6226–6248 |
| `backgroundProgress` | 3 | 1 | 2879–2891 |
| `button-flat` | 3 | 1 | 3137–3147 |
| `cardIndicators` | 3 | 1 | 3694–3704 |
| `cardOverlayFab-primary` | 3 | 1 | 1049–1071 |
| `com` | 3 | 1 | 3206–3224 |
| `content` | 3 | 1 | 4922–4953 |
| `fab` | 3 | 1 | 3798–3811 |
| `listChildrenCollapsible` | 3 | 1 | 4971–4986 |
| `mdl-slider-background-flex` | 3 | 1 | 2978–2991 |
| `mediaInfoCriticRating` | 3 | 1 | 1949–1958 |
| `nextUpSection` | 3 | 1 | 4966–4986 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 6278–6288 |
| `playbackProgress` | 3 | 1 | 2879–2891 |
| `serverInfo` | 3 | 1 | 4025–4034 |
| `transcodingProgress` | 3 | 1 | 2879–2891 |
