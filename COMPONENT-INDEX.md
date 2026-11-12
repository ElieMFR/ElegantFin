# Index des composants — ElegantFin Cinema Edition v1.5.7

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.5.7.css` — 8053 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 38 | 16 | 457–487, 518–553, 791, 904, 1565–1585, 2199–2232, 2259–2263, 2540–2558, 2594, 6960, 6996–7006, 7146, 7246–7265, 7343–7365, 7395–7402, 7566 |
| `cardScalable` | 29 | 14 | 457, 487, 541–553, 854–894, 920–964, 2558, 3639, 3751, 3829, 6024, 6974–7006, 7076, 7246, 7386–7402 |
| `cardImageContainer` | 21 | 13 | 468, 536, 872, 900–929, 964, 1022–1046, 6180–6184, 6264, 6966, 7076, 7116, 7246–7265, 7386 |
| `material-icons` | 17 | 13 | 393–412, 1790, 1888, 1941, 3596, 3756, 3829–3835, 3941, 4103, 4657, 5197, 5231–5241, 5841 |
| `itemDetailPage` | 20 | 12 | 1628, 1714, 1799, 1826, 2055–2095, 2130–2145, 2181–2185, 2295, 2607, 4784, 5090, 7820–7858 |
| `skinHeader` | 20 | 12 | 296, 1714, 4083–4099, 4469, 4515–4542, 6032–6036, 6473, 6529–6537, 6607–6632, 7060, 7213, 7891 |
| `js` | 13 | 12 | 330, 360, 1700–1714, 1799, 2366, 2973, 3400, 3730, 5841, 6838, 7165, 7412 |
| `nameContainer` | 27 | 9 | 737, 2302–2325, 2366, 2395, 2430–2477, 2514, 2545–2549, 5597–5650, 7820–7858 |
| `emby-button` | 12 | 9 | 663–680, 707–725, 3234, 3368–3375, 3776, 3810, 3963, 4675, 5419 |
| `parentName` | 23 | 8 | 737, 2307–2325, 2366, 2395, 2430–2477, 5603–5650, 5723, 7820–7858 |
| `detailLogo` | 20 | 8 | 737, 2084–2095, 2130–2145, 2172–2185, 2295–2325, 2395, 2430–2477, 2545 |
| `detailPageWrapperContainer` | 17 | 8 | 737, 1596–1606, 2095, 2268, 2302–2325, 2395, 2430–2477, 2545 |
| `subtitle` | 17 | 8 | 2055–2065, 2181–2185, 2307, 2366, 2486–2496, 2607, 5658–5691, 7820–7858 |
| `cardBox` | 13 | 8 | 457–487, 518–542, 791, 942–946, 1051, 6960, 7246, 7631 |
| `backdropCard` | 12 | 8 | 1009–1015, 1132, 2055–2065, 2211, 2295, 2549–2558, 2585, 2896 |
| `nowPlayingBar` | 8 | 8 | 330, 3158, 6316, 7023, 7110, 7199, 7225, 7571 |
| `card-hoverable` | 22 | 7 | 553, 920–1015, 6184, 6984, 7116–7155, 7246, 7631 |
| `listItem` | 18 | 7 | 314, 680, 2562, 4577–4603, 4634–4666, 4711, 7608–7625 |
| `loginPage` | 18 | 7 | 3907, 6036–6070, 6110–6129, 6165–6184, 7013, 7056, 7375–7402 |
| `navMenuOption` | 12 | 6 | 680, 776–786, 4152, 4644–4666, 4765–4770, 7288–7299 |
| `emby-tab-button` | 11 | 6 | 680, 747–756, 3882, 6683–6694, 6722–6739, 7903 |
| `paper-icon-button-light` | 11 | 6 | 625–680, 1714, 1790, 1888, 3536–3556, 5503 |
| `verticalSection` | 11 | 6 | 1794, 2798–2803, 5090, 7069, 7165, 7412 |
| `button-link` | 10 | 6 | 680, 707–725, 3109–3118, 3178–3188, 3234, 7782 |
| `headerTop` | 9 | 6 | 2185, 4469, 4515, 6479–6504, 6599–6616, 6643–6647 |
| `person` | 8 | 6 | 2055–2080, 2295, 2549, 2594–2603, 4035, 7815 |
| `mainDrawer` | 7 | 6 | 3123, 4117, 4515, 7013–7023, 7275, 7314 |
| `scss` | 6 | 6 | 296, 819, 1077, 3645, 4158, 7165 |
| `detailImageContainer` | 20 | 5 | 2055–2080, 2199–2263, 2295, 2536–2558, 2585–2603 |
| `osdHeader` | 15 | 5 | 1763–1781, 6468–6537, 6607–6632, 7060, 7571 |
| `cardOverlayContainer` | 12 | 5 | 983–1015, 1055–1077, 1150, 7571, 7608 |
| `sectionTabs` | 11 | 5 | 1857, 3882, 4542, 6509–6514, 6700–6744 |
| `cardImageIcon` | 8 | 5 | 449–453, 2549–2558, 2621, 3623, 6264 |
| `sectionTitle` | 7 | 5 | 1794, 1867–1874, 4370, 5167–5175, 6105 |
| `semiTransparent` | 7 | 5 | 1696, 4083–4099, 6032, 6497–6518, 6554 |
| `emby-scroller-container` | 6 | 5 | 1794–1799, 1837, 2786, 7069, 7165 |
| `portraitCard` | 6 | 5 | 1132, 1216, 1979–1984, 2259, 2896 |
| `appfooter` | 5 | 5 | 330, 2839, 6657, 7099, 7571 |
| `skinHeader-withBackground` | 5 | 5 | 1696, 4083, 6032, 6468, 6518 |
| `btnPlay` | 16 | 4 | 562–586, 625–680, 3839–3881, 3913–3941 |
| `itemName` | 11 | 4 | 737, 2366, 5603–5650, 5741–5758 |
| `backdropImage` | 10 | 4 | 2685–2713, 2740–2744, 6953, 7076–7084 |
| `upNextContainer` | 10 | 4 | 5258–5276, 5302–5328, 7013–7023, 7049 |
| `emby-scroller` | 9 | 4 | 1799, 1837–1843, 7318–7365, 7550–7566 |
| `sectionTitleTextButton` | 9 | 4 | 479, 5150–5158, 5185–5197, 5231–5241 |
| `backgroundContainer` | 8 | 4 | 2149, 2677, 2718–2736, 2768 |
| `detailRibbon` | 8 | 4 | 1653–1681, 1894, 1979–1991, 7815 |
| `skip-button` | 8 | 4 | 680, 3891, 5351–5376, 5403–5421 |
| `visualCardBox` | 7 | 4 | 457, 881–894, 920–925, 1051 |
| `actionSheetMenuItem` | 6 | 4 | 680, 4577–4588, 4634, 7041 |
| `button-submit` | 6 | 4 | 3907, 3994, 6165–6173, 7693–7708 |
| `cardText-secondary` | 6 | 4 | 314, 969, 3628–3632, 7138–7146 |
| `detailPagePrimaryContent` | 6 | 4 | 1668–1686, 2501, 5084, 7229 |
| `skinHeader-blurred` | 6 | 4 | 6032, 6497–6504, 7213, 7571–7590 |
| `squareCard` | 6 | 4 | 904, 2549, 2585–2603, 6134–6138 |
| `itemsContainer` | 4 | 4 | 791, 1826, 1861, 5090 |
| `raised` | 4 | 4 | 680, 766, 3776, 3810 |
| `tsx` | 4 | 4 | 1132, 1714, 4469, 4546 |
| `x` | 4 | 4 | 2366, 4158, 5706, 7165 |
| `detailButton` | 13 | 3 | 625–680, 3820–3881, 3937–3941 |
| `itemSelectionPanel` | 9 | 3 | 933–937, 3568, 3596–3639 |
| `pageTitle` | 8 | 3 | 1738–1781, 6529, 6632 |
| `homePage` | 7 | 3 | 4469, 4515–4542, 6761 |
| `playedIndicator` | 7 | 3 | 819–833, 3712, 7246–7270 |
| `detailSectionContent` | 6 | 3 | 3400, 4870–4880, 4963–4973 |
| `emby-checkbox` | 6 | 3 | 3573, 3610–3614, 3663–3675 |
| `listItemBodyText` | 6 | 3 | 4598–4617, 4657, 7625 |
| `actionSheetContent` | 5 | 3 | 4703–4707, 7013–7023, 7049 |
| `cardText-first` | 5 | 3 | 969, 3602–3628, 6245 |
| `dialog` | 5 | 3 | 3452–3462, 7013–7023, 7049 |
| `guideProgramName` | 5 | 3 | 680, 5782–5793, 5836–5841 |
| `noHomeButtonHeader` | 5 | 3 | 1714, 6529, 6683–6694 |
| `overflowBackdropCard` | 5 | 3 | 1009–1015, 3606, 6240–6245 |
| `secondary` | 5 | 3 | 314, 4607–4617, 4657 |
| `album` | 4 | 3 | 2295, 2554–2558, 2594 |
| `cardPadder` | 4 | 3 | 453, 1051, 3619–3623 |
| `cardText` | 4 | 3 | 969–979, 3628, 7391 |
| `detailPageContent` | 4 | 3 | 1816, 4797, 5077–5084 |
| `dialog-fullscreen` | 4 | 3 | 3462, 7013–7023, 7049 |
| `emby-scrollbuttons` | 4 | 3 | 1879–1884, 7412, 7937 |
| `folder` | 4 | 3 | 1979–1984, 3730, 3793 |
| `formDialogFooter` | 4 | 3 | 3520, 4001, 7642–7666 |
| `infoWrapper` | 4 | 3 | 2238–2243, 2501, 2529 |
| `listItemIcon` | 4 | 3 | 4031–4035, 4711, 4775 |
| `listItemImage` | 4 | 3 | 2873–2878, 4571, 7625 |
| `musicParentName` | 4 | 3 | 2055, 2607, 5723–5732 |
| `programGuideSection` | 4 | 3 | 2562–2577, 4973, 5000 |
| `toast` | 4 | 3 | 5251, 7013–7023, 7049 |
| `cardFooter` | 3 | 3 | 3639, 7116, 7155 |
| `check` | 3 | 3 | 3596, 3829, 4711 |
| `collectionItems` | 3 | 3 | 1826, 4973, 5009 |
| `defaultCardBackground` | 3 | 3 | 3751, 6260, 6359 |
| `detailPageSecondaryContainer` | 3 | 3 | 1663, 1690, 1816 |
| `emby-input` | 3 | 3 | 5517, 5546, 7708 |
| `formDialogFooterItem` | 3 | 3 | 3520, 3788, 3913 |
| `formDialogHeader` | 3 | 3 | 4001, 7571, 7642 |
| `iconOsd` | 3 | 3 | 6010, 7571, 7642 |
| `live_tv` | 3 | 3 | 2055, 2594, 4035 |
| `myPreferencesMenuPage` | 3 | 3 | 426, 4775, 5098 |
| `playerStats` | 3 | 3 | 6010, 7642, 7678 |
| `readOnlyContent` | 3 | 3 | 4043, 6123, 6777 |
| `sectionTitle-cards` | 3 | 3 | 1794, 5167, 5227 |
| `sectionTitleContainer` | 3 | 3 | 1826, 1884, 5009 |
| `itemExternalLinks` | 13 | 2 | 3171–3249, 3400 |
| `checkboxOutline` | 10 | 2 | 3573–3614, 3645–3675 |
| `itemBackdrop` | 9 | 2 | 2021–2080, 2268 |
| `mdl-slider` | 9 | 2 | 2969, 3024–3082 |
| `cardOverlayButton-br` | 8 | 2 | 1063, 1092–1143 |
| `sliderContainer` | 8 | 2 | 2973, 3001–3066 |
| `detail-clamp-text` | 7 | 2 | 3336–3362, 3388–3392 |
| `divUsers` | 7 | 2 | 6134–6138, 7375–7402 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3610–3614, 3644–3663 |
| `countIndicator` | 6 | 2 | 810–840, 7642–7666 |
| `detailPagePrimaryContainer` | 6 | 2 | 1640–1686, 2501 |
| `detailsGroupItem` | 6 | 2 | 4832, 4903–4940 |
| `headerButton` | 6 | 2 | 600–680, 6625 |
| `headerLeft` | 6 | 2 | 1744–1781, 6882 |
| `selectionCommandsPanel` | 6 | 2 | 3530–3564, 7571 |
| `trackSelections` | 6 | 2 | 4801–4832, 4968–4973 |
| `withBackdrop` | 6 | 2 | 2677, 2718–2736 |
| `detailSection` | 5 | 2 | 4784–4793, 4953–4973 |
| `fullSyncIndicator` | 5 | 2 | 810–833, 7642–7666 |
| `mainDrawer-scrollContainer` | 5 | 2 | 3131, 7288–7305 |
| `manualLoginForm` | 5 | 2 | 6105–6149, 6190 |
| `mediaInfoItem` | 5 | 2 | 1898–1941, 7165 |
| `overview-expand` | 5 | 2 | 3368–3392, 4870 |
| `scrollX` | 5 | 2 | 1799, 1837–1857 |
| `videoIndicator` | 5 | 2 | 3719–3747, 7642 |
| `visualLoginForm` | 5 | 2 | 6105–6149, 6190 |
| `withSectionTabs` | 5 | 2 | 2727–2744, 6504 |
| `alphaPickerButton` | 4 | 2 | 680, 5024–5036 |
| `backgroundProgress` | 4 | 2 | 2884–2896, 2926 |
| `emby-select` | 4 | 2 | 5517–5529, 7708 |
| `emby-tab-button-active` | 4 | 2 | 3974, 6730–6744 |
| `mediaSourceIndicator` | 4 | 2 | 810–833, 7642 |
| `play_arrow` | 4 | 2 | 3756–3772, 3941 |
| `playbackProgress` | 4 | 2 | 2884–2896, 2931 |
| `playlistIndexIndicatorImage` | 4 | 2 | 4598–4603, 6353–6359 |
| `programCell` | 4 | 2 | 5773, 5832–5841 |
| `cardOverlayButtonIcon` | 3 | 2 | 1063–1075, 1143 |
| `castCollapsible` | 3 | 2 | 872, 3614–3623 |
| `emby-scrollbuttons-button` | 3 | 2 | 1888, 7944–7951 |
| `emby-textarea` | 3 | 2 | 5508–5517, 5546 |
| `guestCastContent` | 3 | 2 | 872, 3614–3623 |
| `guide-channelHeaderCell` | 3 | 2 | 680, 5807–5823 |
| `guide-date-tab-button` | 3 | 2 | 680, 3974–3982 |
| `headerUserButton` | 3 | 2 | 600–613, 5102 |
| `noHeaderRight` | 3 | 2 | 1714, 6032–6036 |
| `overview` | 3 | 2 | 3388–3392, 4880 |
| `add` | 2 | 2 | 1799, 7165 |
| `alphaPicker-fixed-right` | 2 | 2 | 2768, 5036 |
| `backdropImageFadeIn` | 2 | 2 | 2823, 7682 |
| `book` | 2 | 2 | 2055, 2594 |
| `btnDeleteImage` | 2 | 2 | 3776, 3988 |
| `cardContent` | 2 | 2 | 872, 904 |
| `cardOverlayButton` | 2 | 2 | 1077, 1120 |
| `cardOverlayButton-hover` | 2 | 2 | 964, 1092 |
| `chevron_right` | 2 | 2 | 5197, 5241 |
| `classList` | 2 | 2 | 1799, 7165 |
| `collapseContent` | 2 | 2 | 3525, 3999 |
| `collectionItemsContainer` | 2 | 2 | 1826, 5013 |
| `content-primary` | 2 | 2 | 5077, 5133 |
| `editorsChoiceContainer` | 2 | 2 | 6838, 7862 |
| `editorsChoiceItemBanner` | 2 | 2 | 6838, 7590 |
| `editorsChoiceItemOverview` | 2 | 2 | 7862, 7955 |
| `endsAt` | 2 | 2 | 1919, 7165 |
| `f5f5f5` | 2 | 2 | 5351, 5381 |
| `fieldDescription` | 2 | 2 | 314, 7708 |
| `formDialogFooter-clear` | 2 | 2 | 3520, 4001 |
| `guide-programNameCaret` | 2 | 2 | 314, 5789 |
| `headroom` | 2 | 2 | 6492, 6529 |
| `indicator` | 2 | 2 | 840, 3707 |
| `mc-row` | 2 | 2 | 468, 7482 |
| `mediaInfoOfficialRating` | 2 | 2 | 1919, 7165 |
| `navMenuOption-selected` | 2 | 2 | 4780, 7299 |
| `nowPlayingInfoContainer` | 2 | 2 | 3162, 6290 |
| `org` | 2 | 2 | 3198, 3228 |
| `page` | 2 | 2 | 2768, 7069 |
| `paperList` | 2 | 2 | 881, 4012 |
| `playlist` | 2 | 2 | 4593, 6268 |
| `programSecondaryTitle` | 2 | 2 | 314, 5841 |
| `queue` | 2 | 2 | 2055, 2594 |
| `reactRoot` | 2 | 2 | 4469, 6888 |
| `recordingFields` | 2 | 2 | 4824, 4968 |
| `runtime` | 2 | 2 | 6202, 6230 |
| `sectionTitleContainer-cards` | 2 | 2 | 5162, 5227 |
| `sidebarHeader` | 2 | 2 | 4139, 7305 |
| `splide` | 2 | 2 | 6838, 7911 |
| `tagline` | 2 | 2 | 2668, 4880 |
| `upNextDialog-title` | 2 | 2 | 5281, 5315 |
| `vertical-list` | 2 | 2 | 1861, 7810 |
| `vertical-wrap` | 2 | 2 | 806, 1826 |
| `videoOsdBottom` | 2 | 2 | 3154, 6459 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 3154, 6459 |
| `userPreferencesPage` | 12 | 1 | 7693–7789 |
| `checkboxContainer` | 7 | 1 | 3602–3639 |
| `itemDetailsGroup` | 7 | 1 | 4887–4973 |
| `itemProgressBar` | 6 | 1 | 2873–2907 |
| `streaming-lookup-container` | 6 | 1 | 3256–3301 |
| `trackSelectionFieldContainer` | 6 | 1 | 4843–4866 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 7911–7951 |
| `innerCardFooter` | 5 | 1 | 3415–3444 |
| `chapterCardImageContainer` | 4 | 1 | 3415–3444 |
| `emby-select-withcolor` | 4 | 1 | 5517–5564 |
| `endTimeText` | 4 | 1 | 6202–6230 |
| `mainDetailButtons` | 4 | 1 | 3937–3951 |
| `overview-controls` | 4 | 1 | 3388–3400 |
| `startTimeText` | 4 | 1 | 6202–6224 |
| `button-flat` | 3 | 1 | 3135–3145 |
| `cardIndicators` | 3 | 1 | 3692–3702 |
| `cardOverlayFab-primary` | 3 | 1 | 1055–1077 |
| `com` | 3 | 1 | 3204–3222 |
| `content` | 3 | 1 | 4909–4940 |
| `fab` | 3 | 1 | 3797–3810 |
| `listChildrenCollapsible` | 3 | 1 | 4958–4973 |
| `mdl-slider-background-flex` | 3 | 1 | 2993–3006 |
| `mediaInfoCriticRating` | 3 | 1 | 1960–1969 |
| `nextUpSection` | 3 | 1 | 4953–4973 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 6254–6264 |
| `serverInfo` | 3 | 1 | 4016–4025 |
| `transcodingProgress` | 3 | 1 | 2884–2896 |
