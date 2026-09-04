# Index des composants — ElegantFin Cinema Edition v1.2.97

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.2.97.css` — 6283 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 32 | 14 | 383–394, 426–438, 616, 698, 1332–1352, 1821–1854, 1881–1885, 2160–2191, 5473, 5760–5776, 5856–5878, 5908, 5980, 6253 |
| `cardScalable` | 25 | 13 | 383–394, 431–438, 644–688, 714–752, 2178, 3075, 3177, 3256, 4762, 5487–5497, 5566, 5760, 5899–5908 |
| `cardImageContainer` | 23 | 13 | 426, 666, 694–723, 752, 809–839, 4871–4875, 4956, 5479, 5558–5566, 5619, 5760–5776, 5899, 6028 |
| `material-icons` | 15 | 11 | 319–338, 1517, 1576, 1628, 3038, 3182, 3256–3262, 3368, 3621, 4071, 4105–4115 |
| `itemDetailPage` | 16 | 10 | 1395, 1468, 1526, 1747–1772, 1816, 1916, 2206–2211, 3715, 3992, 6081–6119 |
| `nameContainer` | 27 | 9 | 575, 1923–1946, 1987, 2016, 2051–2097, 2134, 2165–2169, 4438–4490, 6081–6119 |
| `card-hoverable` | 23 | 8 | 438, 654, 714–802, 4875, 5497, 5647–5666, 5760, 6035 |
| `parentName` | 23 | 8 | 575, 1928–1946, 1987, 2016, 2051–2097, 4444–4490, 4563, 6081–6119 |
| `detailPageWrapperContainer` | 17 | 8 | 575, 1363–1373, 1772, 1890, 1923–1946, 2016, 2051–2097, 2165 |
| `subtitle` | 16 | 8 | 1747, 1816, 1928, 1987, 2106–2116, 2206–2211, 4498–4531, 6081–6119 |
| `cardBox` | 11 | 8 | 383–394, 420–438, 616, 736, 843, 5473, 5760, 6035 |
| `detailLogo` | 17 | 7 | 575, 1761–1772, 1807–1816, 1916–1946, 2016, 2051–2097, 2165 |
| `loginPage` | 14 | 7 | 3335, 4774–4789, 4828, 4856–4875, 5502, 5545, 5888–5908 |
| `backdropCard` | 12 | 7 | 796–802, 905, 1747, 1833, 1916, 2169–2211, 2481 |
| `skinHeader` | 11 | 7 | 4770, 5099, 5155–5163, 5189–5214, 5549, 5728, 6190 |
| `emby-button` | 9 | 7 | 512–529, 556, 2840–2847, 3202, 3237, 3390, 3639 |
| `verticalSection` | 11 | 6 | 1521, 2377–2382, 3992, 5558, 5675, 5916 |
| `nowPlayingBar` | 8 | 6 | 2725, 5008, 5512, 5606, 5709–5740, 5985 |
| `listItem` | 16 | 5 | 529, 2182, 3539–3565, 3596–3630, 6003–6020 |
| `osdHeader` | 15 | 5 | 1498–1508, 5094–5163, 5189–5214, 5549, 5985 |
| `actionSheetMenuItem` | 11 | 5 | 529, 3539–3550, 3596, 3676–3692, 5530 |
| `navMenuOption` | 11 | 5 | 529, 605–611, 3602–3630, 3696–3701, 5799–5810 |
| `cardImageIcon` | 8 | 5 | 375–379, 2169–2178, 2217, 3065, 4956 |
| `person` | 8 | 5 | 1747–1757, 1916, 2169–2202, 3457, 6076 |
| `emby-scroller-container` | 7 | 5 | 1521–1534, 2367, 2403, 5558, 5675 |
| `js` | 5 | 5 | 286, 1987, 2539, 5675, 5916 |
| `portraitCard` | 5 | 5 | 905, 983, 1666, 1881, 2481 |
| `detailImageContainer` | 19 | 4 | 1747–1757, 1821–1885, 1916, 2156–2211 |
| `btnPlay` | 14 | 4 | 449, 488–529, 3266–3308, 3341–3368 |
| `cardOverlayContainer` | 12 | 4 | 770–802, 847–867, 917, 5985–6003 |
| `itemName` | 11 | 4 | 575, 1987, 4444–4490, 4581–4598 |
| `backdropImage` | 10 | 4 | 2283–2310, 2337–2341, 5466, 5566–5574 |
| `upNextContainer` | 10 | 4 | 4133–4152, 4178–4204, 5502–5512, 5538 |
| `emby-tab-button` | 9 | 4 | 529, 585, 3314, 5265–5301 |
| `sectionTabs` | 9 | 4 | 1545, 3314, 5135–5140, 5280–5306 |
| `button-link` | 7 | 4 | 529, 556, 2675–2684, 2745–2755 |
| `detailRibbon` | 7 | 4 | 1420–1448, 1581, 1666–1671, 6076 |
| `listItemBodyText` | 7 | 4 | 3560–3579, 3621, 3680, 6020 |
| `visualCardBox` | 7 | 4 | 383, 675–688, 714–719, 843 |
| `detailPagePrimaryContent` | 6 | 4 | 1435–1453, 2121, 3986, 5744 |
| `paper-icon-button-light` | 6 | 4 | 488–529, 1517, 1576, 4357 |
| `skip-button` | 6 | 4 | 529, 3319, 4227–4244, 4271–4277 |
| `button-submit` | 5 | 4 | 3335, 3422, 4856–4864, 6051 |
| `mainDrawer` | 5 | 4 | 2689, 5502–5512, 5786, 5825 |
| `sectionTitle` | 5 | 4 | 1521, 1555–1562, 4051, 4823 |
| `skinHeader-blurred` | 5 | 4 | 4770, 5123–5130, 5728, 5985 |
| `appfooter` | 4 | 4 | 2424, 5239, 5589, 5985 |
| `page` | 4 | 4 | 839, 2358, 2403, 5558 |
| `raised` | 4 | 4 | 529, 595, 3202, 3237 |
| `skinHeader-withBackground` | 4 | 4 | 1463, 4770, 5094, 5144 |
| `detailButton` | 12 | 3 | 488–529, 3247–3308, 3364–3368 |
| `emby-scroller` | 9 | 3 | 1526–1540, 5831–5878, 5971–5980 |
| `itemBackdrop` | 9 | 3 | 1713–1757, 1890, 2211 |
| `check` | 8 | 3 | 3038, 3256, 3672–3692 |
| `itemSelectionPanel` | 8 | 3 | 727–731, 3010, 3038–3075 |
| `pageTitle` | 8 | 3 | 1472–1508, 5155, 5214 |
| `detailSectionContent` | 6 | 3 | 2872, 3797–3807, 3888–3898 |
| `emby-checkbox` | 6 | 3 | 3015, 3052–3056, 3098–3110 |
| `headerTop` | 6 | 3 | 5105–5130, 5181–5198, 5225–5229 |
| `squareCard` | 6 | 3 | 698, 2169–2202, 4832–4836 |
| `actionSheetContent` | 5 | 3 | 3664–3668, 5502–5512, 5538 |
| `cardText-first` | 5 | 3 | 757, 3044–3070, 4937 |
| `dialog` | 5 | 3 | 2922–2932, 5502–5512, 5538 |
| `guideProgramName` | 5 | 3 | 529, 4622–4633, 4676–4681 |
| `musicParentName` | 5 | 3 | 1747, 2206–2211, 4563–4572 |
| `overflowBackdropCard` | 5 | 3 | 796–802, 3048, 4932–4937 |
| `cardPadder` | 4 | 3 | 379, 843, 3061–3065 |
| `cardText` | 4 | 3 | 757–767, 3070, 5904 |
| `cardText-secondary` | 4 | 3 | 757, 3070, 5653–5661 |
| `dialog-fullscreen` | 4 | 3 | 2932, 5502–5512, 5538 |
| `emby-scrollbuttons` | 4 | 3 | 1567–1572, 5916, 6228 |
| `infoWrapper` | 4 | 3 | 1860–1865, 2121, 2149 |
| `listItemImage` | 4 | 3 | 2458–2463, 3533, 6020 |
| `semiTransparent` | 4 | 3 | 1463, 4770, 5123–5144 |
| `toast` | 4 | 3 | 4125, 5502–5512, 5538 |
| `defaultCardBackground` | 3 | 3 | 3177, 4952, 5051 |
| `folder` | 3 | 3 | 1666, 3164, 3220 |
| `formDialogFooterItem` | 3 | 3 | 2990, 3215, 3341 |
| `itemsContainer` | 3 | 3 | 616, 1549, 3992 |
| `live_tv` | 3 | 3 | 1747, 2191, 3457 |
| `myPreferencesMenuPage` | 3 | 3 | 352, 3706, 4000 |
| `sectionTitle-cards` | 3 | 3 | 1521, 4051, 4101 |
| `x` | 3 | 3 | 1987, 4546, 5675 |
| `itemExternalLinks` | 11 | 2 | 2738–2795, 2872 |
| `mdl-slider` | 9 | 2 | 2535, 2590–2648 |
| `listItemIcon` | 8 | 2 | 3453–3457, 3676–3706 |
| `sectionTitleTextButton` | 8 | 2 | 4034–4071, 4105–4115 |
| `sliderContainer` | 8 | 2 | 2539, 2567–2632 |
| `detail-clamp-text` | 7 | 2 | 2808–2834, 2860–2864 |
| `backgroundContainer` | 6 | 2 | 2273, 2315–2333 |
| `detailPagePrimaryContainer` | 6 | 2 | 1407–1453, 2121 |
| `detailsGroupItem` | 6 | 2 | 3759, 3827–3865 |
| `divUsers` | 6 | 2 | 4832–4836, 5888–5908 |
| `headerLeft` | 6 | 2 | 1478–1508, 5394 |
| `trackSelections` | 6 | 2 | 3732–3759, 3893–3898 |
| `withBackdrop` | 6 | 2 | 2273, 2315–2333 |
| `detailSection` | 5 | 2 | 3715–3724, 3878–3898 |
| `headerButton` | 5 | 2 | 474–529, 5207 |
| `mainDrawer-scrollContainer` | 5 | 2 | 2698, 5799–5816 |
| `mediaInfoItem` | 5 | 2 | 1585–1628, 5675 |
| `overview-expand` | 5 | 2 | 2840–2864, 3797 |
| `playedIndicator` | 5 | 2 | 3147, 5760–5781 |
| `videoIndicator` | 5 | 2 | 3153–3173, 6042 |
| `withSectionTabs` | 5 | 2 | 2324–2341, 5130 |
| `album` | 4 | 2 | 1916, 2174–2191 |
| `emby-tab-button-active` | 4 | 2 | 3401, 5292–5306 |
| `noHomeButtonHeader` | 4 | 2 | 5155, 5265–5273 |
| `play_arrow` | 4 | 2 | 3182–3198, 3368 |
| `playlistIndexIndicatorImage` | 4 | 2 | 3560–3565, 5045–5051 |
| `programCell` | 4 | 2 | 4613, 4672–4681 |
| `secondary` | 4 | 2 | 3569–3579, 3621 |
| `section0` | 4 | 2 | 809–839, 5558 |
| `visualLoginForm` | 4 | 2 | 4823–4840, 4881 |
| `alphaPickerButton` | 3 | 2 | 529, 3937–3944 |
| `cardFooter` | 3 | 2 | 3075, 5647–5666 |
| `castCollapsible` | 3 | 2 | 666, 3056–3065 |
| `detailPageContent` | 3 | 2 | 3728, 3979–3986 |
| `emby-scrollbuttons-button` | 3 | 2 | 1576, 6235–6242 |
| `guestCastContent` | 3 | 2 | 666, 3056–3065 |
| `guide-channelHeaderCell` | 3 | 2 | 529, 4647–4663 |
| `guide-date-tab-button` | 3 | 2 | 529, 3401–3409 |
| `manualLoginForm` | 3 | 2 | 4823–4840, 4881 |
| `overview` | 3 | 2 | 2860–2864, 3807 |
| `programGuideSection` | 3 | 2 | 2182, 3898–3913 |
| `selectionCommandsPanel` | 3 | 2 | 3000–3006, 5985 |
| `blurhash-canvas` | 2 | 2 | 5619, 6028 |
| `book` | 2 | 2 | 1747, 2191 |
| `btnDeleteImage` | 2 | 2 | 3202, 3415 |
| `cardContent` | 2 | 2 | 666, 698 |
| `cardImage` | 2 | 2 | 5619, 6028 |
| `cardOverlayButton-hover` | 2 | 2 | 752, 872 |
| `cardOverlayButtonIcon` | 2 | 2 | 855, 910 |
| `chevron_right` | 2 | 2 | 4071, 4115 |
| `collapseContent` | 2 | 2 | 2995, 3427 |
| `content-primary` | 2 | 2 | 3979, 4017 |
| `countIndicator` | 2 | 2 | 635, 5600 |
| `detailPageSecondaryContainer` | 2 | 2 | 1430, 1457 |
| `editorsChoiceItemOverview` | 2 | 2 | 6165, 6246 |
| `endsAt` | 2 | 2 | 1606, 5675 |
| `formDialogFooter` | 2 | 2 | 2990, 3427 |
| `formDialogFooter-clear` | 2 | 2 | 2990, 3427 |
| `formDialogHeader` | 2 | 2 | 3427, 5985 |
| `headerUserButton` | 2 | 2 | 474, 4004 |
| `headroom` | 2 | 2 | 5118, 5155 |
| `iconOsd` | 2 | 2 | 4748, 5985 |
| `mediaSourceIndicator` | 2 | 2 | 635, 6042 |
| `navMenuOption-selected` | 2 | 2 | 3711, 5810 |
| `nowPlayingInfoContainer` | 2 | 2 | 2729, 4982 |
| `org` | 2 | 2 | 2765, 2795 |
| `paperList` | 2 | 2 | 675, 3434 |
| `playlist` | 2 | 2 | 3555, 4960 |
| `queue` | 2 | 2 | 1747, 2191 |
| `readOnlyContent` | 2 | 2 | 3465, 5323 |
| `recordingFields` | 2 | 2 | 3751, 3893 |
| `runtime` | 2 | 2 | 4893, 4922 |
| `sectionTitleContainer` | 2 | 2 | 1572, 3922 |
| `sectionTitleContainer-cards` | 2 | 2 | 4046, 4101 |
| `tagline` | 2 | 2 | 2264, 3807 |
| `upNextDialog-title` | 2 | 2 | 4157, 4191 |
| `vertical-list` | 2 | 2 | 1549, 6071 |
| `videoOsdBottom` | 2 | 2 | 2721, 5085 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 2721, 5085 |
| `checkboxOutline` | 10 | 1 | 3015–3110 |
| `cardOverlayButton-br` | 7 | 1 | 855–910 |
| `itemDetailsGroup` | 7 | 1 | 3811–3898 |
| `checkboxContainer` | 6 | 1 | 3044–3075 |
| `multiSelectCheckboxOutline` | 6 | 1 | 3052–3098 |
| `trackSelectionFieldContainer` | 6 | 1 | 3770–3793 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 6202–6242 |
| `innerCardFooter` | 5 | 1 | 2885–2914 |
| `itemProgressBar` | 5 | 1 | 2458–2481 |
| `backgroundProgress` | 4 | 1 | 2469–2492 |
| `chapterCardImageContainer` | 4 | 1 | 2885–2914 |
| `endTimeText` | 4 | 1 | 4893–4922 |
| `mainDetailButtons` | 4 | 1 | 3364–3378 |
| `overview-controls` | 4 | 1 | 2860–2872 |
| `playbackProgress` | 4 | 1 | 2469–2497 |
| `scrollX` | 4 | 1 | 1526–1545 |
| `startTimeText` | 4 | 1 | 4893–4916 |
| `button-flat` | 3 | 1 | 2702–2712 |
| `cardIndicators` | 3 | 1 | 3127–3137 |
| `cardOverlayFab-primary` | 3 | 1 | 847–867 |
| `com` | 3 | 1 | 2771–2789 |
| `content` | 3 | 1 | 3834–3865 |
| `discover-card` | 3 | 1 | 6253–6276 |
| `emby-select-withcolor` | 3 | 1 | 4371–4405 |
| `emby-textarea` | 3 | 1 | 4362–4387 |
| `fab` | 3 | 1 | 3224–3237 |
| `listChildrenCollapsible` | 3 | 1 | 3883–3898 |
| `mdl-slider-background-flex` | 3 | 1 | 2559–2572 |
| `mediaInfoCriticRating` | 3 | 1 | 1647–1656 |
| `nextUpSection` | 3 | 1 | 3878–3898 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 4946–4956 |
| `serverInfo` | 3 | 1 | 3438–3447 |
| `transcodingProgress` | 3 | 1 | 2469–2481 |
