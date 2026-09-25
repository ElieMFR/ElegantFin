# Index des composants — ElegantFin Cinema Edition v1.3.9

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.9.css` — 7288 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 36 | 14 | 416–498, 736, 839, 1485–1505, 2027–2060, 2087–2091, 2367–2385, 2421, 6267, 6525–6541, 6619–6641, 6671–6678, 6761, 7166 |
| `cardScalable` | 28 | 13 | 416–427, 475–498, 785–829, 855–893, 2385, 3344, 3455, 3534, 5476, 6281–6291, 6360, 6525, 6662–6678 |
| `material-icons` | 17 | 13 | 352–371, 1704, 1782, 1834, 3301, 3460, 3534–3540, 3646, 3804, 4194, 4678, 4712–4722, 5294 |
| `cardImageContainer` | 22 | 12 | 470, 807, 835–864, 893, 950–980, 5585–5589, 5669, 6273, 6352–6360, 6400, 6525–6541, 6662 |
| `itemDetailPage` | 18 | 11 | 1548, 1634, 1713, 1953–1978, 2022, 2123, 2434–2439, 3789–3800, 4288, 4575, 6994–7032 |
| `skinHeader` | 16 | 10 | 280, 4019, 4052–4079, 5484, 5878, 5934–5942, 5968–5993, 6343, 6492, 7103 |
| `nameContainer` | 27 | 9 | 682, 2130–2153, 2194, 2223, 2258–2304, 2341, 2372–2376, 5051–5103, 6994–7032 |
| `backdropCard` | 12 | 9 | 937–943, 1058, 1953, 2039, 2123, 2376–2385, 2412, 2439, 2703 |
| `js` | 9 | 9 | 319, 1620, 1713, 2194, 2780, 3434, 5294, 6444, 6688 |
| `card-hoverable` | 23 | 8 | 498, 795, 855–943, 5589, 6291, 6400–6435, 6525, 6807 |
| `parentName` | 23 | 8 | 682, 2135–2153, 2194, 2223, 2258–2304, 5057–5103, 5176, 6994–7032 |
| `detailPageWrapperContainer` | 17 | 8 | 682, 1516–1526, 1978, 2096, 2130–2153, 2223, 2258–2304, 2372 |
| `subtitle` | 16 | 8 | 1953, 2022, 2135, 2194, 2313–2323, 2434–2439, 5111–5144, 6994–7032 |
| `cardBox` | 12 | 8 | 416–464, 490, 736, 877, 984, 6267, 6525, 6807 |
| `emby-button` | 11 | 8 | 608–625, 652–670, 3042, 3103–3110, 3480, 3515, 3668, 4212 |
| `detailLogo` | 17 | 7 | 682, 1967–1978, 2013–2022, 2123–2153, 2223, 2258–2304, 2372 |
| `loginPage` | 15 | 7 | 3613, 5488–5503, 5542, 5570–5589, 6296, 6339, 6651–6678 |
| `nowPlayingBar` | 7 | 7 | 2966, 5721, 6306, 6394, 6478, 6504, 6766 |
| `listItem` | 17 | 6 | 298, 625, 2389, 4114–4140, 4171–4203, 6784–6801 |
| `navMenuOption` | 12 | 6 | 625, 721–731, 3854, 4181–4203, 4269–4274, 6564–6575 |
| `verticalSection` | 11 | 6 | 1708, 2604–2609, 4575, 6352, 6444, 6688 |
| `button-link` | 10 | 6 | 625, 652–670, 2916–2925, 2986–2996, 3042, 6957 |
| `person` | 8 | 6 | 1953–1963, 2123, 2376, 2421–2430, 3741, 6989 |
| `mainDrawer` | 7 | 6 | 2930, 3818, 4052, 6296–6306, 6551, 6590 |
| `detailImageContainer` | 20 | 5 | 1953–1963, 2027–2091, 2123, 2363–2385, 2412–2439 |
| `osdHeader` | 15 | 5 | 1677–1695, 5873–5942, 5968–5993, 6343, 6766 |
| `actionSheetMenuItem` | 11 | 5 | 625, 4114–4125, 4171, 4249–4265, 6324 |
| `sectionTabs` | 10 | 5 | 1751, 3592, 4079, 5914–5919, 6059–6085 |
| `cardImageIcon` | 8 | 5 | 408–412, 2376–2385, 2445, 3328, 5669 |
| `headerTop` | 8 | 5 | 4019, 4052, 5884–5909, 5960–5977, 6004–6008 |
| `paper-icon-button-light` | 8 | 5 | 570–625, 1634, 1704, 1782, 4970 |
| `sectionTitle` | 7 | 5 | 1708, 1761–1768, 3920, 4648–4656, 5537 |
| `emby-scroller-container` | 6 | 5 | 1708–1713, 1740, 2594, 6352, 6444 |
| `portraitCard` | 5 | 5 | 1058, 1136, 1872, 2087, 2703 |
| `scss` | 5 | 5 | 280, 764, 1010, 3350, 6444 |
| `skinHeader-withBackground` | 5 | 5 | 1616, 3789, 5484, 5873, 5923 |
| `btnPlay` | 16 | 4 | 507–531, 570–625, 3544–3586, 3619–3646 |
| `cardOverlayContainer` | 12 | 4 | 911–943, 988–1010, 1070, 6766–6784 |
| `itemName` | 11 | 4 | 682, 2194, 5057–5103, 5194–5211 |
| `backdropImage` | 10 | 4 | 2510–2537, 2564–2568, 6260, 6360–6368 |
| `emby-tab-button` | 10 | 4 | 625, 692–701, 3592, 6044–6080 |
| `upNextContainer` | 10 | 4 | 4740–4759, 4785–4811, 6296–6306, 6332 |
| `emby-scroller` | 9 | 4 | 1713, 1740–1746, 6594–6641, 6752–6761 |
| `detailRibbon` | 7 | 4 | 1573–1601, 1787, 1872–1877, 6989 |
| `listItemBodyText` | 7 | 4 | 4135–4154, 4194, 4253, 6801 |
| `visualCardBox` | 7 | 4 | 416, 816–829, 855–860, 984 |
| `button-submit` | 6 | 4 | 3613, 3700, 5570–5578, 6869–6883 |
| `cardText-secondary` | 6 | 4 | 298, 898, 3333–3337, 6422–6430 |
| `detailPagePrimaryContent` | 6 | 4 | 1588–1606, 2328, 4569, 6508 |
| `skip-button` | 6 | 4 | 625, 3597, 4834–4851, 4878–4884 |
| `squareCard` | 6 | 4 | 839, 2376, 2412–2430, 5546–5550 |
| `skinHeader-blurred` | 5 | 4 | 5484, 5902–5909, 6492, 6766 |
| `appfooter` | 4 | 4 | 2646, 6018, 6383, 6766 |
| `raised` | 4 | 4 | 625, 711, 3480, 3515 |
| `detailButton` | 13 | 3 | 570–625, 3525–3586, 3642–3646 |
| `itemBackdrop` | 9 | 3 | 1919–1963, 2096, 2439 |
| `itemSelectionPanel` | 9 | 3 | 868–872, 3273, 3301–3344 |
| `check` | 8 | 3 | 3301, 3534, 4245–4265 |
| `pageTitle` | 8 | 3 | 1652–1695, 5934, 5993 |
| `sectionTitleTextButton` | 8 | 3 | 4631–4639, 4666–4678, 4712–4722 |
| `homePage` | 7 | 3 | 4019, 4052–4079, 6102 |
| `playedIndicator` | 7 | 3 | 764–778, 3417, 6525–6546 |
| `detailSectionContent` | 6 | 3 | 3135, 4370–4380, 4460–4470 |
| `emby-checkbox` | 6 | 3 | 3278, 3315–3319, 3368–3380 |
| `actionSheetContent` | 5 | 3 | 4237–4241, 6296–6306, 6332 |
| `cardText-first` | 5 | 3 | 898, 3307–3333, 5650 |
| `dialog` | 5 | 3 | 3185–3195, 6296–6306, 6332 |
| `guideProgramName` | 5 | 3 | 625, 5235–5246, 5289–5294 |
| `musicParentName` | 5 | 3 | 1953, 2434–2439, 5176–5185 |
| `noHomeButtonHeader` | 5 | 3 | 1634, 5934, 6044–6052 |
| `overflowBackdropCard` | 5 | 3 | 937–943, 3311, 5645–5650 |
| `secondary` | 5 | 3 | 298, 4144–4154, 4194 |
| `album` | 4 | 3 | 2123, 2381–2385, 2421 |
| `cardPadder` | 4 | 3 | 412, 984, 3324–3328 |
| `cardText` | 4 | 3 | 898–908, 3333, 6667 |
| `detailPageContent` | 4 | 3 | 1730, 4301, 4562–4569 |
| `dialog-fullscreen` | 4 | 3 | 3195, 6296–6306, 6332 |
| `emby-scrollbuttons` | 4 | 3 | 1773–1778, 6688, 7141 |
| `formDialogFooter` | 4 | 3 | 3253, 3707, 6818–6842 |
| `infoWrapper` | 4 | 3 | 2066–2071, 2328, 2356 |
| `listItemImage` | 4 | 3 | 2680–2685, 4108, 6801 |
| `semiTransparent` | 4 | 3 | 1616, 5484, 5902–5923 |
| `toast` | 4 | 3 | 4732, 6296–6306, 6332 |
| `cardFooter` | 3 | 3 | 3344, 6400, 6435 |
| `defaultCardBackground` | 3 | 3 | 3455, 5665, 5764 |
| `detailPageSecondaryContainer` | 3 | 3 | 1583, 1610, 1730 |
| `folder` | 3 | 3 | 1872, 3434, 3498 |
| `formDialogFooterItem` | 3 | 3 | 3253, 3493, 3619 |
| `formDialogHeader` | 3 | 3 | 3707, 6766, 6818 |
| `iconOsd` | 3 | 3 | 5462, 6766, 6818 |
| `itemsContainer` | 3 | 3 | 736, 1755, 4575 |
| `live_tv` | 3 | 3 | 1953, 2421, 3741 |
| `myPreferencesMenuPage` | 3 | 3 | 385, 4279, 4583 |
| `page` | 3 | 3 | 980, 2585, 6352 |
| `playerStats` | 3 | 3 | 5462, 6818, 6854 |
| `sectionTitle-cards` | 3 | 3 | 1708, 4648, 4708 |
| `x` | 3 | 3 | 2194, 5159, 6444 |
| `itemExternalLinks` | 13 | 2 | 2979–3057, 3135 |
| `checkboxOutline` | 10 | 2 | 3278–3319, 3350–3380 |
| `mdl-slider` | 9 | 2 | 2776, 2831–2889 |
| `listItemIcon` | 8 | 2 | 3737–3741, 4249–4279 |
| `sliderContainer` | 8 | 2 | 2780, 2808–2873 |
| `cardOverlayButton-br` | 7 | 2 | 996, 1025–1063 |
| `detail-clamp-text` | 7 | 2 | 3071–3097, 3123–3127 |
| `divUsers` | 7 | 2 | 5546–5550, 6651–6678 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3315–3319, 3349–3368 |
| `backgroundContainer` | 6 | 2 | 2501, 2542–2560 |
| `detailPagePrimaryContainer` | 6 | 2 | 1560–1606, 2328 |
| `detailsGroupItem` | 6 | 2 | 4332, 4400–4437 |
| `headerButton` | 6 | 2 | 545–625, 5986 |
| `headerLeft` | 6 | 2 | 1658–1695, 6189 |
| `trackSelections` | 6 | 2 | 4305–4332, 4465–4470 |
| `withBackdrop` | 6 | 2 | 2501, 2542–2560 |
| `countIndicator` | 5 | 2 | 755–778, 6818–6842 |
| `detailSection` | 5 | 2 | 4288–4297, 4450–4470 |
| `fullSyncIndicator` | 5 | 2 | 755–778, 6818–6842 |
| `mainDrawer-scrollContainer` | 5 | 2 | 2939, 6564–6581 |
| `mediaInfoItem` | 5 | 2 | 1791–1834, 6444 |
| `overview-expand` | 5 | 2 | 3103–3127, 4370 |
| `videoIndicator` | 5 | 2 | 3423–3451, 6818 |
| `withSectionTabs` | 5 | 2 | 2551–2568, 5909 |
| `alphaPickerButton` | 4 | 2 | 625, 4509–4521 |
| `backgroundProgress` | 4 | 2 | 2691–2703, 2733 |
| `emby-tab-button-active` | 4 | 2 | 3679, 6071–6085 |
| `mediaSourceIndicator` | 4 | 2 | 755–778, 6818 |
| `play_arrow` | 4 | 2 | 3460–3476, 3646 |
| `playbackProgress` | 4 | 2 | 2691–2703, 2738 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4135–4140, 5758–5764 |
| `programCell` | 4 | 2 | 5226, 5285–5294 |
| `programGuideSection` | 4 | 2 | 2389–2404, 4470–4485 |
| `scrollX` | 4 | 2 | 1713, 1740–1751 |
| `section0` | 4 | 2 | 950–980, 6352 |
| `visualLoginForm` | 4 | 2 | 5537–5554, 5595 |
| `cardOverlayButtonIcon` | 3 | 2 | 996–1008, 1063 |
| `castCollapsible` | 3 | 2 | 807, 3319–3328 |
| `emby-input` | 3 | 2 | 4984–5000, 6883 |
| `emby-scrollbuttons-button` | 3 | 2 | 1782, 7148–7155 |
| `guestCastContent` | 3 | 2 | 807, 3319–3328 |
| `guide-channelHeaderCell` | 3 | 2 | 625, 5260–5276 |
| `guide-date-tab-button` | 3 | 2 | 625, 3679–3687 |
| `headerUserButton` | 3 | 2 | 545–558, 4587 |
| `manualLoginForm` | 3 | 2 | 5537–5554, 5595 |
| `overview` | 3 | 2 | 3123–3127, 4380 |
| `selectionCommandsPanel` | 3 | 2 | 3263–3269, 6766 |
| `add` | 2 | 2 | 1713, 6444 |
| `backdropImageFadeIn` | 2 | 2 | 2630, 6858 |
| `book` | 2 | 2 | 1953, 2421 |
| `btnDeleteImage` | 2 | 2 | 3480, 3693 |
| `cardContent` | 2 | 2 | 807, 839 |
| `cardOverlayButton` | 2 | 2 | 1010, 1046 |
| `cardOverlayButton-hover` | 2 | 2 | 893, 1025 |
| `chevron_right` | 2 | 2 | 4678, 4722 |
| `classList` | 2 | 2 | 1713, 6444 |
| `collapseContent` | 2 | 2 | 3258, 3705 |
| `content-primary` | 2 | 2 | 4562, 4614 |
| `editorsChoiceItemOverview` | 2 | 2 | 7078, 7159 |
| `emby-select` | 2 | 2 | 4984, 6883 |
| `endsAt` | 2 | 2 | 1812, 6444 |
| `fieldDescription` | 2 | 2 | 298, 6883 |
| `formDialogFooter-clear` | 2 | 2 | 3253, 3707 |
| `guide-programNameCaret` | 2 | 2 | 298, 5242 |
| `headroom` | 2 | 2 | 5897, 5934 |
| `mediaInfoOfficialRating` | 2 | 2 | 1812, 6444 |
| `navMenuOption-selected` | 2 | 2 | 4284, 6575 |
| `nowPlayingInfoContainer` | 2 | 2 | 2970, 5695 |
| `org` | 2 | 2 | 3006, 3036 |
| `paperList` | 2 | 2 | 816, 3718 |
| `playlist` | 2 | 2 | 4130, 5673 |
| `programSecondaryTitle` | 2 | 2 | 298, 5294 |
| `queue` | 2 | 2 | 1953, 2421 |
| `readOnlyContent` | 2 | 2 | 3749, 6118 |
| `recordingFields` | 2 | 2 | 4324, 4465 |
| `runtime` | 2 | 2 | 5607, 5635 |
| `sectionTitleContainer` | 2 | 2 | 1778, 4494 |
| `sectionTitleContainer-cards` | 2 | 2 | 4643, 4708 |
| `sidebarHeader` | 2 | 2 | 3841, 6581 |
| `tagline` | 2 | 2 | 2492, 4380 |
| `tsx` | 2 | 2 | 4019, 4083 |
| `upNextDialog-title` | 2 | 2 | 4764, 4798 |
| `vertical-list` | 2 | 2 | 1755, 6984 |
| `videoOsdBottom` | 2 | 2 | 2962, 5864 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 2962, 5864 |
| `userPreferencesPage` | 12 | 1 | 6869–6964 |
| `checkboxContainer` | 7 | 1 | 3307–3344 |
| `itemDetailsGroup` | 7 | 1 | 4384–4470 |
| `itemProgressBar` | 6 | 1 | 2680–2714 |
| `trackSelectionFieldContainer` | 6 | 1 | 4343–4366 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7115–7155 |
| `innerCardFooter` | 5 | 1 | 3148–3177 |
| `chapterCardImageContainer` | 4 | 1 | 3148–3177 |
| `endTimeText` | 4 | 1 | 5607–5635 |
| `mainDetailButtons` | 4 | 1 | 3642–3656 |
| `overview-controls` | 4 | 1 | 3123–3135 |
| `startTimeText` | 4 | 1 | 5607–5629 |
| `button-flat` | 3 | 1 | 2943–2953 |
| `cardIndicators` | 3 | 1 | 3397–3407 |
| `cardOverlayFab-primary` | 3 | 1 | 988–1010 |
| `com` | 3 | 1 | 3012–3030 |
| `content` | 3 | 1 | 4406–4437 |
| `discover-card` | 3 | 1 | 7166–7189 |
| `emby-select-withcolor` | 3 | 1 | 4984–5018 |
| `emby-textarea` | 3 | 1 | 4975–5000 |
| `fab` | 3 | 1 | 3502–3515 |
| `listChildrenCollapsible` | 3 | 1 | 4455–4470 |
| `mdl-slider-background-flex` | 3 | 1 | 2800–2813 |
| `mediaInfoCriticRating` | 3 | 1 | 1853–1862 |
| `nextUpSection` | 3 | 1 | 4450–4470 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 5659–5669 |
| `serverInfo` | 3 | 1 | 3722–3731 |
| `transcodingProgress` | 3 | 1 | 2691–2703 |
