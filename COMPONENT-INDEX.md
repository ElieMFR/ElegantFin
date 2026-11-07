# Index des composants — ElegantFin Cinema Edition v1.5.5

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.5.5.css` — 8125 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 39 | 16 | 457–487, 518–564, 802, 919, 1579–1599, 2213–2246, 2273–2277, 2554–2572, 2608, 6967, 7003–7013, 7249–7268, 7346–7368, 7398–7405, 7569, 8003 |
| `cardScalable` | 31 | 14 | 457, 487, 541–564, 865–909, 935–979, 2572, 3654, 3765, 3844, 6032, 6981–7013, 7084, 7249, 7389–7405 |
| `cardImageContainer` | 22 | 13 | 468, 536, 887, 915–944, 979, 1036–1060, 6187–6191, 6271, 6973, 7076–7084, 7124, 7249–7268, 7389 |
| `material-icons` | 17 | 13 | 393–412, 1804, 1902, 1955, 3611, 3770, 3844–3850, 3957, 4120, 4675, 5211, 5245–5255, 5849 |
| `itemDetailPage` | 20 | 12 | 1642, 1728, 1813, 1840, 2069–2109, 2144–2159, 2195–2199, 2309, 2621, 4798, 5104, 7823–7861 |
| `skinHeader` | 20 | 12 | 296, 1728, 4100–4116, 4487, 4533–4560, 6040–6044, 6480, 6536–6544, 6614–6639, 7067, 7216, 7932 |
| `js` | 13 | 12 | 330, 360, 1714–1728, 1813, 2380, 2986, 3415, 3744, 5849, 6845, 7168, 7415 |
| `nameContainer` | 27 | 9 | 748, 2316–2339, 2380, 2409, 2444–2491, 2528, 2559–2563, 5605–5658, 7823–7861 |
| `cardBox` | 13 | 9 | 457–487, 518–530, 556, 802, 957–961, 1065, 6967, 7249, 7634 |
| `emby-button` | 12 | 9 | 674–691, 718–736, 3248, 3383–3390, 3790, 3825, 3979, 4693, 5427 |
| `card-hoverable` | 23 | 8 | 564, 875, 935–1029, 6191, 6991, 7124–7159, 7249, 7634 |
| `parentName` | 23 | 8 | 748, 2321–2339, 2380, 2409, 2444–2491, 5611–5658, 5731, 7823–7861 |
| `detailLogo` | 20 | 8 | 748, 2098–2109, 2144–2159, 2186–2199, 2309–2339, 2409, 2444–2491, 2559 |
| `listItem` | 19 | 8 | 314, 691, 2576, 4595–4621, 4652–4684, 4729, 4773, 7611–7628 |
| `detailPageWrapperContainer` | 17 | 8 | 748, 1610–1620, 2109, 2282, 2316–2339, 2409, 2444–2491, 2559 |
| `subtitle` | 17 | 8 | 2069–2079, 2195–2199, 2321, 2380, 2500–2510, 2621, 5666–5699, 7823–7861 |
| `backdropCard` | 12 | 8 | 1023–1029, 1146, 2069–2079, 2225, 2309, 2563–2572, 2599, 2909 |
| `nowPlayingBar` | 8 | 8 | 330, 3172, 6323, 7030, 7118, 7202, 7228, 7574 |
| `loginPage` | 18 | 7 | 3923, 6044–6078, 6118–6136, 6172–6191, 7020, 7063, 7378–7405 |
| `navMenuOption` | 12 | 6 | 691, 787–797, 4170, 4662–4684, 4779–4784, 7291–7302 |
| `emby-tab-button` | 11 | 6 | 691, 758–767, 3902, 6690–6701, 6729–6746, 7944 |
| `paper-icon-button-light` | 11 | 6 | 636–691, 1728, 1804, 1902, 3551–3571, 5511 |
| `verticalSection` | 11 | 6 | 1808, 2811–2816, 5104, 7076, 7168, 7415 |
| `button-link` | 10 | 6 | 691, 718–736, 3122–3131, 3192–3202, 3248, 7785 |
| `headerTop` | 9 | 6 | 2199, 4487, 4533, 6486–6511, 6606–6623, 6650–6654 |
| `person` | 8 | 6 | 2069–2094, 2309, 2563, 2608–2617, 4052, 7818 |
| `mainDrawer` | 7 | 6 | 3136, 4134, 4533, 7020–7030, 7278, 7317 |
| `scss` | 6 | 6 | 296, 830, 1091, 3660, 4176, 7168 |
| `detailImageContainer` | 20 | 5 | 2069–2094, 2213–2277, 2309, 2550–2572, 2599–2617 |
| `osdHeader` | 15 | 5 | 1777–1795, 6475–6544, 6614–6639, 7067, 7574 |
| `cardOverlayContainer` | 12 | 5 | 997–1029, 1069–1091, 1164, 7574, 7611 |
| `sectionTabs` | 11 | 5 | 1871, 3902, 4560, 6516–6521, 6707–6751 |
| `actionSheetMenuItem` | 10 | 5 | 691, 4595–4606, 4652, 4729–4773, 7048 |
| `cardImageIcon` | 8 | 5 | 449–453, 2563–2572, 2635, 3638, 6271 |
| `sectionTitle` | 7 | 5 | 1808, 1881–1888, 4388, 5181–5189, 6113 |
| `semiTransparent` | 7 | 5 | 1710, 4100–4116, 6040, 6504–6525, 6561 |
| `emby-scroller-container` | 6 | 5 | 1808–1813, 1851, 2801, 7076, 7168 |
| `portraitCard` | 6 | 5 | 1146, 1230, 1993–1998, 2273, 2909 |
| `appfooter` | 5 | 5 | 330, 2852, 6664, 7107, 7574 |
| `skinHeader-withBackground` | 5 | 5 | 1710, 4100, 6040, 6475, 6525 |
| `btnPlay` | 16 | 4 | 573–597, 636–691, 3854–3896, 3929–3957 |
| `itemName` | 11 | 4 | 748, 2380, 5611–5658, 5749–5766 |
| `backdropImage` | 10 | 4 | 2700–2728, 2755–2759, 6960, 7084–7092 |
| `upNextContainer` | 10 | 4 | 5273–5292, 5318–5344, 7020–7030, 7056 |
| `emby-scroller` | 9 | 4 | 1813, 1851–1857, 7321–7368, 7553–7569 |
| `sectionTitleTextButton` | 9 | 4 | 479, 5164–5172, 5199–5211, 5245–5255 |
| `backgroundContainer` | 8 | 4 | 2163, 2691, 2733–2751, 2783 |
| `detailRibbon` | 8 | 4 | 1667–1695, 1908, 1993–2005, 7818 |
| `listItemBodyText` | 7 | 4 | 4616–4635, 4675, 4750, 7628 |
| `skip-button` | 7 | 4 | 691, 3907, 5367–5384, 5411–5429 |
| `visualCardBox` | 7 | 4 | 457, 896–909, 935–940, 1065 |
| `button-submit` | 6 | 4 | 3923, 4011, 6172–6180, 7696–7711 |
| `cardText-secondary` | 6 | 4 | 314, 984, 3643–3647, 7146–7154 |
| `detailPagePrimaryContent` | 6 | 4 | 1682–1700, 2515, 5098, 7232 |
| `skinHeader-blurred` | 6 | 4 | 6040, 6504–6511, 7216, 7574–7593 |
| `squareCard` | 6 | 4 | 919, 2563, 2599–2617, 6141–6145 |
| `itemsContainer` | 4 | 4 | 802, 1840, 1875, 5104 |
| `raised` | 4 | 4 | 691, 777, 3790, 3825 |
| `tsx` | 4 | 4 | 1146, 1728, 4487, 4564 |
| `x` | 4 | 4 | 2380, 4176, 5714, 7168 |
| `detailButton` | 13 | 3 | 636–691, 3835–3896, 3953–3957 |
| `itemSelectionPanel` | 9 | 3 | 948–952, 3583, 3611–3654 |
| `pageTitle` | 8 | 3 | 1752–1795, 6536, 6639 |
| `homePage` | 7 | 3 | 4487, 4533–4560, 6768 |
| `playedIndicator` | 7 | 3 | 830–844, 3727, 7249–7273 |
| `check` | 6 | 3 | 3611, 3844, 4729–4773 |
| `detailSectionContent` | 6 | 3 | 3415, 4884–4894, 4977–4987 |
| `emby-checkbox` | 6 | 3 | 3588, 3625–3629, 3678–3690 |
| `actionSheetContent` | 5 | 3 | 4721–4725, 7020–7030, 7056 |
| `cardText-first` | 5 | 3 | 984, 3617–3643, 6252 |
| `dialog` | 5 | 3 | 3467–3477, 7020–7030, 7056 |
| `guideProgramName` | 5 | 3 | 691, 5790–5801, 5844–5849 |
| `noHomeButtonHeader` | 5 | 3 | 1728, 6536, 6690–6701 |
| `overflowBackdropCard` | 5 | 3 | 1023–1029, 3621, 6247–6252 |
| `secondary` | 5 | 3 | 314, 4625–4635, 4675 |
| `album` | 4 | 3 | 2309, 2568–2572, 2608 |
| `cardPadder` | 4 | 3 | 453, 1065, 3634–3638 |
| `cardText` | 4 | 3 | 984–994, 3643, 7394 |
| `detailPageContent` | 4 | 3 | 1830, 4811, 5091–5098 |
| `dialog-fullscreen` | 4 | 3 | 3477, 7020–7030, 7056 |
| `emby-scrollbuttons` | 4 | 3 | 1893–1898, 7415, 7978 |
| `folder` | 4 | 3 | 1993–1998, 3744, 3808 |
| `formDialogFooter` | 4 | 3 | 3535, 4018, 7645–7669 |
| `infoWrapper` | 4 | 3 | 2252–2257, 2515, 2543 |
| `listItemImage` | 4 | 3 | 2886–2891, 4589, 7628 |
| `musicParentName` | 4 | 3 | 2069, 2621, 5731–5740 |
| `programGuideSection` | 4 | 3 | 2576–2591, 4987, 5014 |
| `toast` | 4 | 3 | 5265, 7020–7030, 7056 |
| `cardFooter` | 3 | 3 | 3654, 7124, 7159 |
| `collectionItems` | 3 | 3 | 1840, 4987, 5023 |
| `defaultCardBackground` | 3 | 3 | 3765, 6267, 6366 |
| `detailPageSecondaryContainer` | 3 | 3 | 1677, 1704, 1830 |
| `emby-input` | 3 | 3 | 5525, 5554, 7711 |
| `formDialogFooterItem` | 3 | 3 | 3535, 3803, 3929 |
| `formDialogHeader` | 3 | 3 | 4018, 7574, 7645 |
| `iconOsd` | 3 | 3 | 6018, 7574, 7645 |
| `live_tv` | 3 | 3 | 2069, 2608, 4052 |
| `myPreferencesMenuPage` | 3 | 3 | 426, 4789, 5112 |
| `playerStats` | 3 | 3 | 6018, 7645, 7681 |
| `readOnlyContent` | 3 | 3 | 4060, 6130, 6784 |
| `sectionTitle-cards` | 3 | 3 | 1808, 5181, 5241 |
| `sectionTitleContainer` | 3 | 3 | 1840, 1898, 5023 |
| `itemExternalLinks` | 13 | 2 | 3185–3263, 3415 |
| `checkboxOutline` | 10 | 2 | 3588–3629, 3660–3690 |
| `itemBackdrop` | 9 | 2 | 2035–2094, 2282 |
| `mdl-slider` | 9 | 2 | 2982, 3037–3095 |
| `cardOverlayButton-br` | 8 | 2 | 1077, 1106–1157 |
| `listItemIcon` | 8 | 2 | 4048–4052, 4729–4789 |
| `sliderContainer` | 8 | 2 | 2986, 3014–3079 |
| `detail-clamp-text` | 7 | 2 | 3351–3377, 3403–3407 |
| `divUsers` | 7 | 2 | 6141–6145, 7378–7405 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3625–3629, 3659–3678 |
| `countIndicator` | 6 | 2 | 821–851, 7645–7669 |
| `detailPagePrimaryContainer` | 6 | 2 | 1654–1700, 2515 |
| `detailsGroupItem` | 6 | 2 | 4846, 4917–4954 |
| `headerButton` | 6 | 2 | 611–691, 6632 |
| `headerLeft` | 6 | 2 | 1758–1795, 6889 |
| `selectionCommandsPanel` | 6 | 2 | 3545–3579, 7574 |
| `trackSelections` | 6 | 2 | 4815–4846, 4982–4987 |
| `withBackdrop` | 6 | 2 | 2691, 2733–2751 |
| `detailSection` | 5 | 2 | 4798–4807, 4967–4987 |
| `fullSyncIndicator` | 5 | 2 | 821–844, 7645–7669 |
| `mainDrawer-scrollContainer` | 5 | 2 | 3145, 7291–7308 |
| `manualLoginForm` | 5 | 2 | 6113–6156, 6197 |
| `mediaInfoItem` | 5 | 2 | 1912–1955, 7168 |
| `overview-expand` | 5 | 2 | 3383–3407, 4884 |
| `scrollX` | 5 | 2 | 1813, 1851–1871 |
| `videoIndicator` | 5 | 2 | 3733–3761, 7645 |
| `visualLoginForm` | 5 | 2 | 6113–6156, 6197 |
| `withSectionTabs` | 5 | 2 | 2742–2759, 6511 |
| `alphaPickerButton` | 4 | 2 | 691, 5038–5050 |
| `backgroundProgress` | 4 | 2 | 2897–2909, 2939 |
| `emby-select` | 4 | 2 | 5525–5537, 7711 |
| `emby-tab-button-active` | 4 | 2 | 3990, 6737–6751 |
| `mediaSourceIndicator` | 4 | 2 | 821–844, 7645 |
| `play_arrow` | 4 | 2 | 3770–3786, 3957 |
| `playbackProgress` | 4 | 2 | 2897–2909, 2944 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4616–4621, 6360–6366 |
| `programCell` | 4 | 2 | 5781, 5840–5849 |
| `cardOverlayButtonIcon` | 3 | 2 | 1077–1089, 1157 |
| `castCollapsible` | 3 | 2 | 887, 3629–3638 |
| `emby-scrollbuttons-button` | 3 | 2 | 1902, 7985–7992 |
| `emby-textarea` | 3 | 2 | 5516–5525, 5554 |
| `guestCastContent` | 3 | 2 | 887, 3629–3638 |
| `guide-channelHeaderCell` | 3 | 2 | 691, 5815–5831 |
| `guide-date-tab-button` | 3 | 2 | 691, 3990–3998 |
| `headerUserButton` | 3 | 2 | 611–624, 5116 |
| `noHeaderRight` | 3 | 2 | 1728, 6040–6044 |
| `overview` | 3 | 2 | 3403–3407, 4894 |
| `section0` | 3 | 2 | 1036–1060, 7076 |
| `add` | 2 | 2 | 1813, 7168 |
| `alphaPicker-fixed-right` | 2 | 2 | 2783, 5050 |
| `backdropImageFadeIn` | 2 | 2 | 2836, 7685 |
| `book` | 2 | 2 | 2069, 2608 |
| `btnDeleteImage` | 2 | 2 | 3790, 4004 |
| `cardContent` | 2 | 2 | 887, 919 |
| `cardOverlayButton` | 2 | 2 | 1091, 1134 |
| `cardOverlayButton-hover` | 2 | 2 | 979, 1106 |
| `chevron_right` | 2 | 2 | 5211, 5255 |
| `classList` | 2 | 2 | 1813, 7168 |
| `collapseContent` | 2 | 2 | 3540, 4016 |
| `collectionItemsContainer` | 2 | 2 | 1840, 5027 |
| `content-primary` | 2 | 2 | 5091, 5147 |
| `editorsChoiceContainer` | 2 | 2 | 6845, 7907 |
| `editorsChoiceItemBanner` | 2 | 2 | 6845, 7593 |
| `editorsChoiceItemOverview` | 2 | 2 | 7907, 7996 |
| `endsAt` | 2 | 2 | 1933, 7168 |
| `fieldDescription` | 2 | 2 | 314, 7711 |
| `formDialogFooter-clear` | 2 | 2 | 3535, 4018 |
| `guide-programNameCaret` | 2 | 2 | 314, 5797 |
| `headroom` | 2 | 2 | 6499, 6536 |
| `indicator` | 2 | 2 | 851, 3722 |
| `mc-row` | 2 | 2 | 468, 7485 |
| `mediaInfoOfficialRating` | 2 | 2 | 1933, 7168 |
| `navMenuOption-selected` | 2 | 2 | 4794, 7302 |
| `nowPlayingInfoContainer` | 2 | 2 | 3176, 6297 |
| `org` | 2 | 2 | 3212, 3242 |
| `page` | 2 | 2 | 2783, 7076 |
| `paperList` | 2 | 2 | 896, 4029 |
| `playlist` | 2 | 2 | 4611, 6275 |
| `programSecondaryTitle` | 2 | 2 | 314, 5849 |
| `queue` | 2 | 2 | 2069, 2608 |
| `reactRoot` | 2 | 2 | 4487, 6895 |
| `recordingFields` | 2 | 2 | 4838, 4982 |
| `runtime` | 2 | 2 | 6209, 6237 |
| `sectionTitleContainer-cards` | 2 | 2 | 5176, 5241 |
| `sidebarHeader` | 2 | 2 | 4157, 7308 |
| `splide` | 2 | 2 | 6845, 7952 |
| `tagline` | 2 | 2 | 2682, 4894 |
| `upNextDialog-title` | 2 | 2 | 5297, 5331 |
| `vertical-list` | 2 | 2 | 1875, 7813 |
| `vertical-wrap` | 2 | 2 | 817, 1840 |
| `videoOsdBottom` | 2 | 2 | 3168, 6466 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3168, 6466 |
| `userPreferencesPage` | 12 | 1 | 7696–7792 |
| `checkboxContainer` | 7 | 1 | 3617–3654 |
| `itemDetailsGroup` | 7 | 1 | 4901–4987 |
| `itemProgressBar` | 6 | 1 | 2886–2920 |
| `streaming-lookup-container` | 6 | 1 | 3270–3315 |
| `trackSelectionFieldContainer` | 6 | 1 | 4857–4880 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7952–7992 |
| `innerCardFooter` | 5 | 1 | 3430–3459 |
| `chapterCardImageContainer` | 4 | 1 | 3430–3459 |
| `emby-select-withcolor` | 4 | 1 | 5525–5572 |
| `endTimeText` | 4 | 1 | 6209–6237 |
| `mainDetailButtons` | 4 | 1 | 3953–3967 |
| `overview-controls` | 4 | 1 | 3403–3415 |
| `startTimeText` | 4 | 1 | 6209–6231 |
| `button-flat` | 3 | 1 | 3149–3159 |
| `cardIndicators` | 3 | 1 | 3707–3717 |
| `cardOverlayFab-primary` | 3 | 1 | 1069–1091 |
| `com` | 3 | 1 | 3218–3236 |
| `content` | 3 | 1 | 4923–4954 |
| `discover-card` | 3 | 1 | 8003–8026 |
| `fab` | 3 | 1 | 3812–3825 |
| `listChildrenCollapsible` | 3 | 1 | 4972–4987 |
| `mdl-slider-background-flex` | 3 | 1 | 3006–3019 |
| `mediaInfoCriticRating` | 3 | 1 | 1974–1983 |
| `nextUpSection` | 3 | 1 | 4967–4987 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 6261–6271 |
| `serverInfo` | 3 | 1 | 4033–4042 |
| `transcodingProgress` | 3 | 1 | 2897–2909 |
