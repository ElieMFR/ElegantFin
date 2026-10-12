# Index des composants — ElegantFin Cinema Edition v1.3.25

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.25.css` — 7907 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 38 | 16 | 428–439, 470–518, 756, 873, 1531–1551, 2142–2175, 2202–2206, 2483–2501, 2537, 6778, 6810–6821, 7058–7077, 7155–7177, 7207–7214, 7378, 7785 |
| `cardScalable` | 31 | 13 | 428–439, 493–518, 819–863, 889–933, 2501, 3581, 3692, 3771, 5925, 6792–6821, 6893, 7058, 7198–7214 |
| `itemDetailPage` | 21 | 13 | 1594, 1680, 1759, 1786, 2015–2051, 2086–2101, 2137, 2238, 2550, 4027–4038, 4698, 4997, 7613–7651 |
| `material-icons` | 17 | 13 | 364–383, 1750, 1848, 1901, 3538, 3697, 3771–3777, 3884, 4042, 4575, 5104, 5138–5148, 5742 |
| `cardImageContainer` | 22 | 12 | 488, 841, 869–898, 933, 990–1020, 6051–6055, 6135, 6784, 6885–6893, 6933, 7058–7077, 7198 |
| `skinHeader` | 16 | 10 | 284, 4387, 4433–4460, 5933, 6344, 6400–6408, 6474–6499, 6876, 7025, 7722 |
| `nameContainer` | 27 | 9 | 702, 2245–2268, 2309, 2338, 2373–2420, 2457, 2488–2492, 5498–5551, 7613–7651 |
| `cardBox` | 13 | 9 | 428–439, 470–482, 510, 756, 911–915, 1024, 6778, 7058, 7424 |
| `emby-button` | 12 | 9 | 628–645, 672–690, 3177, 3312–3319, 3717, 3752, 3906, 4593, 5320 |
| `js` | 9 | 9 | 331, 1666, 1759, 2309, 2915, 3671, 5742, 6977, 7224 |
| `card-hoverable` | 23 | 8 | 518, 829, 889–983, 6055, 6802, 6933–6968, 7058, 7424 |
| `parentName` | 23 | 8 | 702, 2250–2268, 2309, 2338, 2373–2420, 5504–5551, 5624, 7613–7651 |
| `detailLogo` | 20 | 8 | 702, 2025–2051, 2086–2101, 2128–2137, 2238–2268, 2338, 2373–2420, 2488 |
| `listItem` | 19 | 8 | 302, 645, 2505, 4495–4521, 4552–4584, 4629, 4673, 7401–7418 |
| `detailPageWrapperContainer` | 17 | 8 | 702, 1562–1572, 2051, 2211, 2245–2268, 2338, 2373–2420, 2488 |
| `subtitle` | 16 | 8 | 2015–2025, 2137, 2250, 2309, 2429–2439, 2550, 5559–5592, 7613–7651 |
| `backdropCard` | 12 | 8 | 977–983, 1098, 2015–2025, 2154, 2238, 2492–2501, 2528, 2838 |
| `nowPlayingBar` | 8 | 8 | 318, 3101, 6187, 6839, 6927, 7011, 7037, 7383 |
| `loginPage` | 16 | 7 | 3850, 5937–5968, 6008, 6036–6055, 6829, 6872, 7187–7214 |
| `navMenuOption` | 12 | 6 | 645, 741–751, 4092, 4562–4584, 4679–4684, 7100–7111 |
| `paper-icon-button-light` | 11 | 6 | 590–645, 1680, 1750, 1848, 3478–3498, 5404 |
| `verticalSection` | 11 | 6 | 1754, 2740–2745, 4997, 6885, 6977, 7224 |
| `button-link` | 10 | 6 | 645, 672–690, 3051–3060, 3121–3131, 3177, 7575 |
| `person` | 8 | 6 | 2015–2036, 2238, 2492, 2537–2546, 3979, 7608 |
| `mainDrawer` | 7 | 6 | 3065, 4056, 4433, 6829–6839, 7087, 7126 |
| `scss` | 6 | 6 | 284, 784, 1050, 3587, 4098, 6977 |
| `detailImageContainer` | 20 | 5 | 2015–2036, 2142–2206, 2238, 2479–2501, 2528–2546 |
| `osdHeader` | 15 | 5 | 1723–1741, 6339–6408, 6474–6499, 6876, 7383 |
| `actionSheetMenuItem` | 10 | 5 | 645, 4495–4506, 4552, 4629–4673, 6857 |
| `sectionTabs` | 10 | 5 | 1817, 3829, 4460, 6380–6385, 6565–6596 |
| `cardImageIcon` | 8 | 5 | 420–424, 2492–2501, 2564, 3565, 6135 |
| `headerTop` | 8 | 5 | 4387, 4433, 6350–6375, 6466–6483, 6510–6514 |
| `sectionTitle` | 7 | 5 | 1754, 1827–1834, 4288, 5074–5082, 6003 |
| `emby-scroller-container` | 6 | 5 | 1754–1759, 1797, 2730, 6885, 6977 |
| `portraitCard` | 6 | 5 | 1098, 1182, 1939–1944, 2202, 2838 |
| `skinHeader-withBackground` | 5 | 5 | 1662, 4027, 5933, 6339, 6389 |
| `btnPlay` | 16 | 4 | 527–551, 590–645, 3781–3823, 3856–3884 |
| `cardOverlayContainer` | 12 | 4 | 951–983, 1028–1050, 1116, 7383–7401 |
| `itemName` | 11 | 4 | 702, 2309, 5504–5551, 5642–5659 |
| `backdropImage` | 10 | 4 | 2629–2657, 2684–2688, 6771, 6893–6901 |
| `emby-tab-button` | 10 | 4 | 645, 712–721, 3829, 6550–6591 |
| `upNextContainer` | 10 | 4 | 5166–5185, 5211–5237, 6829–6839, 6865 |
| `emby-scroller` | 9 | 4 | 1759, 1797–1803, 7130–7177, 7362–7378 |
| `backgroundContainer` | 8 | 4 | 2105, 2620, 2662–2680, 2712 |
| `detailRibbon` | 8 | 4 | 1619–1647, 1854, 1939–1951, 7608 |
| `listItemBodyText` | 7 | 4 | 4516–4535, 4575, 4650, 7418 |
| `skip-button` | 7 | 4 | 645, 3834, 5260–5277, 5304–5322 |
| `visualCardBox` | 7 | 4 | 428, 850–863, 889–894, 1024 |
| `button-submit` | 6 | 4 | 3850, 3938, 6036–6044, 7486–7501 |
| `cardText-secondary` | 6 | 4 | 302, 938, 3570–3574, 6955–6963 |
| `detailPagePrimaryContent` | 6 | 4 | 1634–1652, 2444, 4991, 7041 |
| `squareCard` | 6 | 4 | 873, 2492, 2528–2546, 6012–6016 |
| `semiTransparent` | 5 | 4 | 1662, 5933, 6368–6389, 6425 |
| `skinHeader-blurred` | 5 | 4 | 5933, 6368–6375, 7025, 7383 |
| `appfooter` | 4 | 4 | 2781, 6524, 6916, 7383 |
| `itemsContainer` | 4 | 4 | 756, 1786, 1821, 4997 |
| `raised` | 4 | 4 | 645, 731, 3717, 3752 |
| `x` | 4 | 4 | 2309, 4098, 5607, 6977 |
| `detailButton` | 13 | 3 | 590–645, 3762–3823, 3880–3884 |
| `itemSelectionPanel` | 9 | 3 | 902–906, 3510, 3538–3581 |
| `pageTitle` | 8 | 3 | 1698–1741, 6400, 6499 |
| `sectionTitleTextButton` | 8 | 3 | 5057–5065, 5092–5104, 5138–5148 |
| `homePage` | 7 | 3 | 4387, 4433–4460, 6613 |
| `playedIndicator` | 7 | 3 | 784–798, 3654, 7058–7082 |
| `check` | 6 | 3 | 3538, 3771, 4629–4673 |
| `detailSectionContent` | 6 | 3 | 3344, 4780–4790, 4870–4880 |
| `emby-checkbox` | 6 | 3 | 3515, 3552–3556, 3605–3617 |
| `actionSheetContent` | 5 | 3 | 4621–4625, 6829–6839, 6865 |
| `cardText-first` | 5 | 3 | 938, 3544–3570, 6116 |
| `dialog` | 5 | 3 | 3394–3404, 6829–6839, 6865 |
| `guideProgramName` | 5 | 3 | 645, 5683–5694, 5737–5742 |
| `noHomeButtonHeader` | 5 | 3 | 1680, 6400, 6550–6558 |
| `overflowBackdropCard` | 5 | 3 | 977–983, 3548, 6111–6116 |
| `secondary` | 5 | 3 | 302, 4525–4535, 4575 |
| `album` | 4 | 3 | 2238, 2497–2501, 2537 |
| `cardPadder` | 4 | 3 | 424, 1024, 3561–3565 |
| `cardText` | 4 | 3 | 938–948, 3570, 7203 |
| `detailPageContent` | 4 | 3 | 1776, 4711, 4984–4991 |
| `dialog-fullscreen` | 4 | 3 | 3404, 6829–6839, 6865 |
| `emby-scrollbuttons` | 4 | 3 | 1839–1844, 7224, 7760 |
| `folder` | 4 | 3 | 1939–1944, 3671, 3735 |
| `formDialogFooter` | 4 | 3 | 3462, 3945, 7435–7459 |
| `infoWrapper` | 4 | 3 | 2181–2186, 2444, 2472 |
| `listItemImage` | 4 | 3 | 2815–2820, 4489, 7418 |
| `musicParentName` | 4 | 3 | 2015, 2550, 5624–5633 |
| `programGuideSection` | 4 | 3 | 2505–2520, 4880, 4907 |
| `toast` | 4 | 3 | 5158, 6829–6839, 6865 |
| `cardFooter` | 3 | 3 | 3581, 6933, 6968 |
| `collectionItems` | 3 | 3 | 1786, 4880, 4916 |
| `defaultCardBackground` | 3 | 3 | 3692, 6131, 6230 |
| `detailPageSecondaryContainer` | 3 | 3 | 1629, 1656, 1776 |
| `emby-input` | 3 | 3 | 5418, 5447, 7501 |
| `formDialogFooterItem` | 3 | 3 | 3462, 3730, 3856 |
| `formDialogHeader` | 3 | 3 | 3945, 7383, 7435 |
| `iconOsd` | 3 | 3 | 5911, 7383, 7435 |
| `live_tv` | 3 | 3 | 2015, 2537, 3979 |
| `myPreferencesMenuPage` | 3 | 3 | 397, 4689, 5005 |
| `page` | 3 | 3 | 1020, 2712, 6885 |
| `playerStats` | 3 | 3 | 5911, 7435, 7471 |
| `sectionTitle-cards` | 3 | 3 | 1754, 5074, 5134 |
| `sectionTitleContainer` | 3 | 3 | 1786, 1844, 4916 |
| `tsx` | 3 | 3 | 1098, 4387, 4464 |
| `itemExternalLinks` | 13 | 2 | 3114–3192, 3344 |
| `checkboxOutline` | 10 | 2 | 3515–3556, 3587–3617 |
| `itemBackdrop` | 9 | 2 | 1981–2036, 2211 |
| `mdl-slider` | 9 | 2 | 2911, 2966–3024 |
| `listItemIcon` | 8 | 2 | 3975–3979, 4629–4689 |
| `sliderContainer` | 8 | 2 | 2915, 2943–3008 |
| `cardOverlayButton-br` | 7 | 2 | 1036, 1065–1109 |
| `detail-clamp-text` | 7 | 2 | 3280–3306, 3332–3336 |
| `divUsers` | 7 | 2 | 6012–6016, 7187–7214 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3552–3556, 3586–3605 |
| `countIndicator` | 6 | 2 | 775–805, 7435–7459 |
| `detailPagePrimaryContainer` | 6 | 2 | 1606–1652, 2444 |
| `detailsGroupItem` | 6 | 2 | 4742, 4810–4847 |
| `headerButton` | 6 | 2 | 565–645, 6492 |
| `headerLeft` | 6 | 2 | 1704–1741, 6700 |
| `selectionCommandsPanel` | 6 | 2 | 3472–3506, 7383 |
| `trackSelections` | 6 | 2 | 4715–4742, 4875–4880 |
| `withBackdrop` | 6 | 2 | 2620, 2662–2680 |
| `detailSection` | 5 | 2 | 4698–4707, 4860–4880 |
| `fullSyncIndicator` | 5 | 2 | 775–798, 7435–7459 |
| `mainDrawer-scrollContainer` | 5 | 2 | 3074, 7100–7117 |
| `mediaInfoItem` | 5 | 2 | 1858–1901, 6977 |
| `overview-expand` | 5 | 2 | 3312–3336, 4780 |
| `scrollX` | 5 | 2 | 1759, 1797–1817 |
| `videoIndicator` | 5 | 2 | 3660–3688, 7435 |
| `withSectionTabs` | 5 | 2 | 2671–2688, 6375 |
| `alphaPickerButton` | 4 | 2 | 645, 4931–4943 |
| `backgroundProgress` | 4 | 2 | 2826–2838, 2868 |
| `emby-select` | 4 | 2 | 5418–5430, 7501 |
| `emby-tab-button-active` | 4 | 2 | 3917, 6582–6596 |
| `mediaSourceIndicator` | 4 | 2 | 775–798, 7435 |
| `play_arrow` | 4 | 2 | 3697–3713, 3884 |
| `playbackProgress` | 4 | 2 | 2826–2838, 2873 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4516–4521, 6224–6230 |
| `programCell` | 4 | 2 | 5674, 5733–5742 |
| `section0` | 4 | 2 | 990–1020, 6885 |
| `visualLoginForm` | 4 | 2 | 6003–6020, 6061 |
| `cardOverlayButtonIcon` | 3 | 2 | 1036–1048, 1109 |
| `castCollapsible` | 3 | 2 | 841, 3556–3565 |
| `emby-scrollbuttons-button` | 3 | 2 | 1848, 7767–7774 |
| `emby-textarea` | 3 | 2 | 5409–5418, 5447 |
| `guestCastContent` | 3 | 2 | 841, 3556–3565 |
| `guide-channelHeaderCell` | 3 | 2 | 645, 5708–5724 |
| `guide-date-tab-button` | 3 | 2 | 645, 3917–3925 |
| `headerUserButton` | 3 | 2 | 565–578, 5009 |
| `manualLoginForm` | 3 | 2 | 6003–6020, 6061 |
| `overview` | 3 | 2 | 3332–3336, 4790 |
| `add` | 2 | 2 | 1759, 6977 |
| `alphaPicker-fixed-right` | 2 | 2 | 2712, 4943 |
| `backdropImageFadeIn` | 2 | 2 | 2765, 7475 |
| `book` | 2 | 2 | 2015, 2537 |
| `btnDeleteImage` | 2 | 2 | 3717, 3931 |
| `cardContent` | 2 | 2 | 841, 873 |
| `cardOverlayButton` | 2 | 2 | 1050, 1086 |
| `cardOverlayButton-hover` | 2 | 2 | 933, 1065 |
| `chevron_right` | 2 | 2 | 5104, 5148 |
| `classList` | 2 | 2 | 1759, 6977 |
| `collapseContent` | 2 | 2 | 3467, 3943 |
| `collectionItemsContainer` | 2 | 2 | 1786, 4920 |
| `content-primary` | 2 | 2 | 4984, 5040 |
| `editorsChoiceItemOverview` | 2 | 2 | 7697, 7778 |
| `endsAt` | 2 | 2 | 1879, 6977 |
| `fieldDescription` | 2 | 2 | 302, 7501 |
| `formDialogFooter-clear` | 2 | 2 | 3462, 3945 |
| `guide-programNameCaret` | 2 | 2 | 302, 5690 |
| `headroom` | 2 | 2 | 6363, 6400 |
| `indicator` | 2 | 2 | 805, 3649 |
| `mediaInfoOfficialRating` | 2 | 2 | 1879, 6977 |
| `navMenuOption-selected` | 2 | 2 | 4694, 7111 |
| `nowPlayingInfoContainer` | 2 | 2 | 3105, 6161 |
| `org` | 2 | 2 | 3141, 3171 |
| `paperList` | 2 | 2 | 850, 3956 |
| `playlist` | 2 | 2 | 4511, 6139 |
| `programSecondaryTitle` | 2 | 2 | 302, 5742 |
| `queue` | 2 | 2 | 2015, 2537 |
| `reactRoot` | 2 | 2 | 4387, 6706 |
| `readOnlyContent` | 2 | 2 | 3987, 6629 |
| `recordingFields` | 2 | 2 | 4734, 4875 |
| `runtime` | 2 | 2 | 6073, 6101 |
| `sectionTitleContainer-cards` | 2 | 2 | 5069, 5134 |
| `sidebarHeader` | 2 | 2 | 4079, 7117 |
| `tagline` | 2 | 2 | 2611, 4790 |
| `upNextDialog-title` | 2 | 2 | 5190, 5224 |
| `vertical-list` | 2 | 2 | 1821, 7603 |
| `vertical-wrap` | 2 | 2 | 771, 1786 |
| `videoOsdBottom` | 2 | 2 | 3097, 6330 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3097, 6330 |
| `userPreferencesPage` | 12 | 1 | 7486–7582 |
| `checkboxContainer` | 7 | 1 | 3544–3581 |
| `itemDetailsGroup` | 7 | 1 | 4794–4880 |
| `itemProgressBar` | 6 | 1 | 2815–2849 |
| `streaming-lookup-container` | 6 | 1 | 3199–3244 |
| `trackSelectionFieldContainer` | 6 | 1 | 4753–4776 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7734–7774 |
| `innerCardFooter` | 5 | 1 | 3357–3386 |
| `chapterCardImageContainer` | 4 | 1 | 3357–3386 |
| `emby-select-withcolor` | 4 | 1 | 5418–5465 |
| `endTimeText` | 4 | 1 | 6073–6101 |
| `mainDetailButtons` | 4 | 1 | 3880–3894 |
| `overview-controls` | 4 | 1 | 3332–3344 |
| `startTimeText` | 4 | 1 | 6073–6095 |
| `button-flat` | 3 | 1 | 3078–3088 |
| `cardIndicators` | 3 | 1 | 3634–3644 |
| `cardOverlayFab-primary` | 3 | 1 | 1028–1050 |
| `com` | 3 | 1 | 3147–3165 |
| `content` | 3 | 1 | 4816–4847 |
| `discover-card` | 3 | 1 | 7785–7808 |
| `fab` | 3 | 1 | 3739–3752 |
| `listChildrenCollapsible` | 3 | 1 | 4865–4880 |
| `mdl-slider-background-flex` | 3 | 1 | 2935–2948 |
| `mediaInfoCriticRating` | 3 | 1 | 1920–1929 |
| `nextUpSection` | 3 | 1 | 4860–4880 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 6125–6135 |
| `serverInfo` | 3 | 1 | 3960–3969 |
| `transcodingProgress` | 3 | 1 | 2826–2838 |
